import fs from "node:fs";
import path from "node:path";

const USER_AGENT =
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36";

function compact(value) {
  return String(value || "").replace(/\s+/g, " ").trim();
}

function decodeEntities(value) {
  return String(value || "")
    .replace(/&amp;/g, "&")
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&nbsp;/g, " ")
    .replace(/&#x([0-9a-f]+);/gi, (_, hex) => String.fromCodePoint(Number.parseInt(hex, 16)))
    .replace(/&#([0-9]+);/g, (_, num) => String.fromCodePoint(Number.parseInt(num, 10)));
}

async function fetchWithTimeout(url, options = {}) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), options.timeoutMs || 15000);
  try {
    return await fetch(url, {
      redirect: "follow",
      signal: controller.signal,
      headers: {
        "user-agent": USER_AGENT,
        "accept-language": "en-US,en;q=0.9,de;q=0.7",
        accept: "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        ...(options.headers || {}),
      },
    });
  } finally {
    clearTimeout(timeout);
  }
}

function parseHtmlText(html) {
  const withoutNoise = String(html || "")
    .replace(/<script[\s\S]*?<\/script>/gi, " ")
    .replace(/<style[\s\S]*?<\/style>/gi, " ")
    .replace(/<noscript[\s\S]*?<\/noscript>/gi, " ");

  const title =
    compact(decodeEntities(withoutNoise.match(/<meta[^>]+property=["']og:title["'][^>]+content=["']([^"']+)["']/i)?.[1])) ||
    compact(decodeEntities(withoutNoise.match(/<title[^>]*>([\s\S]*?)<\/title>/i)?.[1]));

  const paragraphs = [...withoutNoise.matchAll(/<(?:p|li|h[1-3]|blockquote)[^>]*>([\s\S]*?)<\/(?:p|li|h[1-3]|blockquote)>/gi)]
    .map((match) =>
      compact(
        decodeEntities(
          match[1]
            .replace(/<br\s*\/?>/gi, "\n")
            .replace(/<[^>]+>/g, " "),
        ),
      ),
    )
    .filter((text) => text.length > 40)
    .filter((text, index, arr) => arr.indexOf(text) === index);

  const text = paragraphs.join("\n\n");
  return {
    title,
    text,
    wordCount: text ? text.split(/\s+/).length : 0,
    excerpt: text.slice(0, 2500),
  };
}

function extractCaptionTracks(html) {
  const match = String(html).match(/"captionTracks":(\[.*?\]),"audioTracks"/s);
  if (!match?.[1]) return [];
  try {
    return JSON.parse(match[1]);
  } catch {
    return [];
  }
}

async function extractYoutube(candidate) {
  const watchUrl = `https://www.youtube.com/watch?v=${candidate.youtubeId}`;
  const response = await fetchWithTimeout(watchUrl, { timeoutMs: 15000 });
  if (!response.ok) throw new Error(`YouTube watch HTTP ${response.status}`);
  const html = await response.text();
  const tracks = extractCaptionTracks(html);
  if (!tracks.length) {
    return { ok: false, kind: "youtube", error: "no caption tracks", transcript: "", wordCount: 0, tracks: [] };
  }

  const track =
    tracks.find((item) => item.languageCode?.startsWith("en") && item.kind !== "asr") ||
    tracks.find((item) => item.languageCode?.startsWith("en")) ||
    tracks.find((item) => item.kind !== "asr") ||
    tracks[0];
  const url = new URL(track.baseUrl);
  url.searchParams.set("fmt", "json3");
  const transcriptResponse = await fetchWithTimeout(url.toString(), { timeoutMs: 15000 });
  if (!transcriptResponse.ok) throw new Error(`timedtext HTTP ${transcriptResponse.status}`);

  const data = await transcriptResponse.json();
  const transcript = compact(
    (data.events || [])
      .flatMap((event) => event.segs || [])
      .map((seg) => seg.utf8 || "")
      .join(" "),
  );

  return {
    ok: Boolean(transcript),
    kind: "youtube",
    track: {
      languageCode: track.languageCode || "",
      name: track.name?.simpleText || "",
      kind: track.kind || "",
    },
    transcript,
    wordCount: transcript ? transcript.split(/\s+/).length : 0,
    excerpt: transcript.slice(0, 2500),
  };
}

async function extractArticle(candidate) {
  const response = await fetchWithTimeout(candidate.url, { timeoutMs: 15000 });
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  const contentType = response.headers.get("content-type") || "";
  if (!/text\/html|application\/xhtml\+xml/i.test(contentType)) {
    return { ok: false, kind: "article", error: `non-html ${contentType}`, text: "", wordCount: 0 };
  }
  const html = await response.text();
  return { ok: true, kind: "article", finalUrl: response.url, ...parseHtmlText(html.slice(0, 1_200_000)) };
}

async function mapWithConcurrency(items, concurrency, mapper) {
  const results = new Array(items.length);
  let nextIndex = 0;
  async function worker() {
    while (nextIndex < items.length) {
      const index = nextIndex++;
      results[index] = await mapper(items[index], index);
    }
  }
  await Promise.all(Array.from({ length: concurrency }, worker));
  return results;
}

function parseArgs(argv) {
  const args = {
    inputPath: argv[2] || "reports/things-skill-source-discovery-2026-06-14.json",
    outputPath: argv[3] || "reports/things-skill-source-content-2026-06-14.json",
    targets: new Set(["ui-design", "react", "web-performance", "frontend-testing"]),
    limit: 0,
  };
  for (const arg of argv.slice(4)) {
    if (arg.startsWith("--targets=")) {
      args.targets = new Set(arg.slice("--targets=".length).split(",").filter(Boolean));
    } else if (arg.startsWith("--limit=")) {
      args.limit = Number(arg.slice("--limit=".length));
    }
  }
  return args;
}

async function main() {
  const args = parseArgs(process.argv);
  const discovery = JSON.parse(fs.readFileSync(args.inputPath, "utf8"));
  let candidates = discovery.candidates.filter((candidate) => args.targets.has(candidate.target));
  if (args.limit > 0) candidates = candidates.slice(0, args.limit);

  let completed = 0;
  const results = await mapWithConcurrency(candidates, 4, async (candidate) => {
    try {
      const content = candidate.kind === "youtube" ? await extractYoutube(candidate) : await extractArticle(candidate);
      completed += 1;
      if (completed % 10 === 0 || completed === candidates.length) {
        console.error(`${completed}/${candidates.length}`);
      }
      return { ...candidate, content };
    } catch (error) {
      completed += 1;
      if (completed % 10 === 0 || completed === candidates.length) {
        console.error(`${completed}/${candidates.length}`);
      }
      return {
        ...candidate,
        content: {
          ok: false,
          kind: candidate.kind,
          error: error instanceof Error ? error.message : String(error),
          wordCount: 0,
        },
      };
    }
  });

  const payload = {
    generatedAt: new Date().toISOString(),
    inputPath: args.inputPath,
    targets: [...args.targets],
    candidates: candidates.length,
    ok: results.filter((result) => result.content.ok && result.content.wordCount > 0).length,
    youtubeOk: results.filter((result) => result.kind === "youtube" && result.content.ok && result.content.wordCount > 0).length,
    articleOk: results.filter((result) => result.kind === "article" && result.content.ok && result.content.wordCount > 0).length,
    results,
  };

  fs.mkdirSync(path.dirname(args.outputPath), { recursive: true });
  fs.writeFileSync(args.outputPath, JSON.stringify(payload, null, 2));
  console.log(JSON.stringify({ outputPath: args.outputPath, candidates: payload.candidates, ok: payload.ok, youtubeOk: payload.youtubeOk, articleOk: payload.articleOk }, null, 2));
}

main();
