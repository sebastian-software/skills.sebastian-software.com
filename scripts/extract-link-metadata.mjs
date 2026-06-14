import fs from "node:fs";
import path from "node:path";

const URL_RE = /https?:\/\/[^\s)\]}>\"']+/gi;
const USER_AGENT =
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36";

function compact(value) {
  return String(value || "").replace(/\s+/g, " ").trim();
}

function cleanTitle(value) {
  return compact(value)
    .replace(/\s+[-|]\s+YouTube$/i, "")
    .replace(/\s+[-|]\s+X$/i, "")
    .replace(/\s+[-|]\s+Twitter$/i, "")
    .replace(/\s+[-|]\s+Instagram$/i, "");
}

function decodeEntities(value) {
  return String(value || "")
    .replace(/&amp;/g, "&")
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&nbsp;/g, " ")
    .replace(/&ouml;/g, "ö")
    .replace(/&Ouml;/g, "Ö")
    .replace(/&auml;/g, "ä")
    .replace(/&Auml;/g, "Ä")
    .replace(/&uuml;/g, "ü")
    .replace(/&Uuml;/g, "Ü")
    .replace(/&szlig;/g, "ß")
    .replace(/&ndash;/g, "–")
    .replace(/&mdash;/g, "—")
    .replace(/&rsquo;/g, "’")
    .replace(/&lsquo;/g, "‘")
    .replace(/&rdquo;/g, "”")
    .replace(/&ldquo;/g, "“")
    .replace(/&#x([0-9a-f]+);/gi, (_, hex) => String.fromCodePoint(Number.parseInt(hex, 16)))
    .replace(/&#([0-9]+);/g, (_, num) => String.fromCodePoint(Number.parseInt(num, 10)));
}

function extractUrls(item) {
  return [...`${item.name}\n${item.notes}`.matchAll(URL_RE)]
    .map((match) => match[0].replace(/[.,;]+$/, ""))
    .filter(Boolean);
}

function primaryUrl(item) {
  return extractUrls(item)[0] || "";
}

function domainOf(rawUrl) {
  try {
    return new URL(rawUrl).hostname.replace(/^www\./, "").replace(/^m\./, "");
  } catch {
    return "";
  }
}

function isYoutube(rawUrl) {
  return /(^|\.)youtube\.com$|(^|\.)youtu\.be$/i.test(domainOf(rawUrl));
}

function isTwitterStatus(rawUrl) {
  try {
    const url = new URL(rawUrl);
    const domain = url.hostname.replace(/^www\./, "").replace(/^mobile\./, "");
    return /^(x|twitter)\.com$/i.test(domain) && /\/status\/\d+/i.test(url.pathname);
  } catch {
    return false;
  }
}

function normalizeTwitterStatusUrl(rawUrl) {
  const url = new URL(rawUrl);
  const match = url.pathname.match(/\/([^/]+)\/status\/(\d+)/i);
  if (!match) {
    return rawUrl;
  }
  return `https://x.com/${match[1]}/status/${match[2]}`;
}

function isLikelyHtml(contentType) {
  return !contentType || /text\/html|application\/xhtml\+xml/i.test(contentType);
}

function metaContent(html, patterns) {
  for (const pattern of patterns) {
    const match = html.match(pattern);
    if (match?.[1]) {
      return cleanTitle(decodeEntities(match[1]));
    }
  }
  return "";
}

function parseHtmlMetadata(html) {
  const title =
    metaContent(html, [
      /<meta[^>]+property=["']og:title["'][^>]+content=["']([^"']+)["'][^>]*>/i,
      /<meta[^>]+content=["']([^"']+)["'][^>]+property=["']og:title["'][^>]*>/i,
      /<meta[^>]+name=["']twitter:title["'][^>]+content=["']([^"']+)["'][^>]*>/i,
      /<meta[^>]+content=["']([^"']+)["'][^>]+name=["']twitter:title["'][^>]*>/i,
      /<title[^>]*>([\s\S]*?)<\/title>/i,
    ]) || "";

  const description =
    metaContent(html, [
      /<meta[^>]+property=["']og:description["'][^>]+content=["']([^"']+)["'][^>]*>/i,
      /<meta[^>]+content=["']([^"']+)["'][^>]+property=["']og:description["'][^>]*>/i,
      /<meta[^>]+name=["']description["'][^>]+content=["']([^"']+)["'][^>]*>/i,
      /<meta[^>]+content=["']([^"']+)["'][^>]+name=["']description["'][^>]*>/i,
    ]) || "";

  return { title, description };
}

async function fetchWithTimeout(url, options = {}) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), options.timeoutMs || 12000);
  try {
    return await fetch(url, {
      redirect: "follow",
      signal: controller.signal,
      headers: {
        "user-agent": USER_AGENT,
        accept: "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        ...(options.headers || {}),
      },
    });
  } finally {
    clearTimeout(timeout);
  }
}

async function fetchYoutubeMetadata(rawUrl) {
  const oembedUrl = `https://www.youtube.com/oembed?format=json&url=${encodeURIComponent(rawUrl)}`;
  const response = await fetchWithTimeout(oembedUrl, { timeoutMs: 12000 });
  if (!response.ok) {
    throw new Error(`YouTube oEmbed HTTP ${response.status}`);
  }
  const data = await response.json();
  return {
    ok: true,
    source: "youtube-oembed",
    finalUrl: rawUrl,
    title: cleanTitle(data.title),
    description: "",
    author: compact(data.author_name || ""),
  };
}

function htmlToText(html) {
  return decodeEntities(
    String(html || "")
      .replace(/<br\s*\/?>/gi, "\n")
      .replace(/<\/p>/gi, "\n")
      .replace(/<[^>]+>/g, " ")
      .replace(/\s+/g, " ")
      .trim(),
  );
}

async function fetchTwitterMetadata(rawUrl) {
  const normalizedUrl = normalizeTwitterStatusUrl(rawUrl);
  const oembedUrl = `https://publish.twitter.com/oembed?omit_script=true&url=${encodeURIComponent(normalizedUrl)}`;
  const response = await fetchWithTimeout(oembedUrl, { timeoutMs: 12000 });
  if (!response.ok) {
    throw new Error(`Twitter oEmbed HTTP ${response.status}`);
  }

  const data = await response.json();
  const paragraphMatch = String(data.html || "").match(/<p[^>]*>([\s\S]*?)<\/p>/i);
  const tweetText = htmlToText(paragraphMatch?.[1] || data.html || "")
    .replace(/\bpic\.twitter\.com\/\S+/gi, "")
    .replace(/\s+/g, " ")
    .trim();
  const author = compact(data.author_name || "");
  const title = cleanTitle(`${author ? `${author}: ` : ""}${tweetText}`.slice(0, 220));

  return {
    ok: Boolean(tweetText),
    source: "twitter-oembed",
    finalUrl: normalizedUrl,
    title,
    description: "",
    author,
  };
}

async function fetchHtmlMetadata(rawUrl) {
  const response = await fetchWithTimeout(rawUrl, { timeoutMs: 12000 });
  const contentType = response.headers.get("content-type") || "";
  const finalUrl = response.url || rawUrl;

  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
  }

  if (!isLikelyHtml(contentType)) {
    return {
      ok: true,
      source: "non-html",
      finalUrl,
      title: "",
      description: "",
      contentType,
    };
  }

  const html = await response.text();
  const metadata = parseHtmlMetadata(html.slice(0, 800_000));
  return {
    ok: Boolean(metadata.title),
    source: "html",
    finalUrl,
    title: metadata.title,
    description: metadata.description,
    contentType,
  };
}

async function fetchMetadata(rawUrl) {
  try {
    if (isYoutube(rawUrl)) {
      return await fetchYoutubeMetadata(rawUrl);
    }
    if (isTwitterStatus(rawUrl)) {
      return await fetchTwitterMetadata(rawUrl);
    }
    return await fetchHtmlMetadata(rawUrl);
  } catch (error) {
    return {
      ok: false,
      source: isYoutube(rawUrl) ? "youtube-oembed" : isTwitterStatus(rawUrl) ? "twitter-oembed" : "html",
      finalUrl: rawUrl,
      title: "",
      description: "",
      error: error instanceof Error ? error.message : String(error),
    };
  }
}

function classifyByMetadata(item, metadata) {
  const text = `${metadata.title} ${metadata.description} ${metadata.finalUrl} ${item.name} ${item.notes}`.toLowerCase();
  if (/(react|next\.?js|typescript|javascript|node|vite|css|html|web platform|browser|frontend|tailwind|component|zod|tanstack|codex|github|api|developer|software|coding|programming|open source|ai model|agent|llm|ollama|claude|openai|gemini)/i.test(text)) {
    return { area: "Software & AI", project: "Metadata Review: Software & AI" };
  }
  if (/(design|typography|ui|ux|figma|motion|animation|icon|brand|visual|landing page)/i.test(text)) {
    return { area: "Design & Inspiration", project: "Metadata Review: Design" };
  }
  if (/(hotel|beach|travel|urlaub|reise|bahn|ticket|camping|resort|ferien)/i.test(text)) {
    return { area: "Travel & Places", project: "Metadata Review: Travel" };
  }
  if (/(finance|bank|steuer|tax|förder|foerder|bafa|budget|rechnung|invoice|private doctrine)/i.test(text)) {
    return { area: "Business & Admin", project: "Metadata Review: Finance & Admin" };
  }
  if (/(home|house|garten|garden|smart home|homekit|sonos|unifi|furniture|office|workspace|living)/i.test(text)) {
    return { area: "Home & Living", project: "Metadata Review: Home" };
  }
  if (/(fitness|health|medical|workout|life expectancy|länger leben|laenger leben)/i.test(text)) {
    return { area: "Health & Personal", project: "Metadata Review: Health" };
  }
  if (/(music|video|youtube|podcast|film|series|streaming|song|ottaviani)/i.test(text)) {
    return { area: "Media, Food & Culture", project: "Metadata Review: Media" };
  }
  return { area: item.area || "Review", project: "Metadata Review: Needs Human Review" };
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

function shouldRename(item, metadata) {
  if (!metadata.ok || !metadata.title) {
    return false;
  }
  const name = compact(item.name);
  if (/^https?:\/\//i.test(name)) {
    return true;
  }
  if (name.length < 8 && metadata.title.length > name.length + 8) {
    return true;
  }
  return false;
}

async function main() {
  const inputPath = process.argv[2];
  const outputPath = process.argv[3];
  const limit = Number(process.argv[4] || 0);
  if (!inputPath || !outputPath) {
    throw new Error("Usage: node scripts/extract-link-metadata.mjs <items.json> <output.json> [limit]");
  }

  const payload = JSON.parse(fs.readFileSync(inputPath, "utf8"));
  const items = payload.items || payload;
  const candidates = items
    .map((item) => ({ item, url: primaryUrl(item) }))
    .filter(({ url }) => url)
    .filter(({ item }) => /^https?:\/\//i.test(compact(item.name)) || /Videos & Channels|Social Links Review|Web Links Review|YouTube|X \/ Twitter/.test(item.project || ""));
  const selected = limit > 0 ? candidates.slice(0, limit) : candidates;

  let completed = 0;
  const results = await mapWithConcurrency(selected, 8, async ({ item, url }) => {
    const metadata = await fetchMetadata(url);
    completed += 1;
    if (completed % 25 === 0 || completed === selected.length) {
      console.error(`${completed}/${selected.length}`);
    }
    const target = classifyByMetadata(item, metadata);
    return {
      id: item.id,
      currentName: item.name,
      currentNotes: item.notes,
      currentProject: item.project || "",
      currentArea: item.area || "",
      url,
      domain: domainOf(url),
      metadata,
      proposedName: shouldRename(item, metadata) ? metadata.title : item.name,
      shouldRename: shouldRename(item, metadata),
      proposedArea: target.area,
      proposedProject: target.project,
      shouldReclassify: Boolean(metadata.ok && metadata.title && /Videos & Channels|Social Links Review|Web Links Review|YouTube|X \/ Twitter/.test(item.project || "")),
    };
  });

  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  fs.writeFileSync(
    outputPath,
    JSON.stringify(
      {
        generatedAt: new Date().toISOString(),
        source: inputPath,
        totalItems: items.length,
        candidates: candidates.length,
        fetched: results.length,
        ok: results.filter((result) => result.metadata.ok && result.metadata.title).length,
        renameCandidates: results.filter((result) => result.shouldRename).length,
        reclassifyCandidates: results.filter((result) => result.shouldReclassify).length,
        results,
      },
      null,
      2,
    ),
  );
}

main();
