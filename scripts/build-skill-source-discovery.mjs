import fs from "node:fs";
import path from "node:path";

function compact(value) {
  return String(value || "").replace(/\s+/g, " ").trim();
}

function domainOf(rawUrl) {
  try {
    return new URL(rawUrl).hostname.replace(/^www\./, "").replace(/^m\./, "");
  } catch {
    return "";
  }
}

function youtubeId(rawUrl) {
  try {
    const url = new URL(rawUrl);
    const host = url.hostname.replace(/^www\./, "").replace(/^m\./, "");
    if (host === "youtu.be") {
      return url.pathname.split("/").filter(Boolean)[0] || "";
    }
    if (host.endsWith("youtube.com")) {
      return (
        url.searchParams.get("v") ||
        url.pathname.match(/\/shorts\/([^/?#]+)/)?.[1] ||
        url.pathname.match(/\/live\/([^/?#]+)/)?.[1] ||
        ""
      );
    }
  } catch {
    return "";
  }
  return "";
}

function classify(text) {
  const t = text.toLowerCase();
  if (/(css|layout|grid|flexbox|subgrid|container quer|anchor position|:has|style quer|responsive|viewport|design system|typography|color|svg|accessib|a11y|forms?|button|select|dialog|tooltip|popover|web platform|html)/i.test(t)) {
    return "ui-design";
  }
  if (/(react|next\.?js|remix|react router|tanstack|server actions|react compiler|react query|hook form|zod|solidjs|svelte|astro)/i.test(t)) {
    return "react";
  }
  if (/(playwright|storybook|vitest|visual regression|frontend testing|e2e|screenshot test)/i.test(t)) {
    return "frontend-testing";
  }
  if (/(lcp|cls|inp|core web vitals|performance|preload|cache|image delivery|server timing)/i.test(t)) {
    return "web-performance";
  }
  if (/(claude code|codex|openclaw|clawdbot|ai coding|coding assistant|agent|llm|ollama|qwen|gemini|openai|anthropic)/i.test(t)) {
    return "ai-workflows";
  }
  return "review";
}

function scoreCandidate(candidate) {
  const text = `${candidate.title} ${candidate.project} ${candidate.url}`.toLowerCase();
  let score = 0;
  if (candidate.kind === "youtube") score += 2;
  if (/(css|layout|:has|subgrid|container|anchor|html|accessib|forms?|tooltip|popover|select|dialog|design|typography)/i.test(text)) score += 8;
  if (/(react|next|remix|tanstack|server actions|react compiler|hook form)/i.test(text)) score += 6;
  if (/(performance|lcp|preload|image|cache|testing|playwright|storybook|vitest)/i.test(text)) score += 5;
  if (/(tutorial|guide|explained|state of|what'?s next|conference|keynote|documentary)/i.test(text)) score += 1;
  return score;
}

function main() {
  const metadataPath = process.argv[2] || "reports/things-all-open-link-metadata-2026-06-13.json";
  const completedPath = process.argv[3] || "reports/things-skill-source-completion-ids-2026-06-14.json";
  const outputPath = process.argv[4] || "reports/things-skill-source-discovery-2026-06-14.json";

  const metadata = JSON.parse(fs.readFileSync(metadataPath, "utf8"));
  const completed = new Set(JSON.parse(fs.readFileSync(completedPath, "utf8")).ids || []);
  const projectRepair = fs.existsSync("reports/things-global-link-project-repair-2026-06-13.json")
    ? JSON.parse(fs.readFileSync("reports/things-global-link-project-repair-2026-06-13.json", "utf8"))
    : { assignments: [] };
  const repairedProject = new Map(projectRepair.assignments.map((assignment) => [assignment.id, assignment.proposedProject]));

  const candidates = [];
  for (const result of metadata.results || []) {
    if (completed.has(result.id)) continue;
    const url = result.url || "";
    const title = compact(result.metadata?.title || result.proposedName || result.currentName);
    const project = repairedProject.get(result.id) || result.proposedProject || result.currentProject || "";
    const domain = domainOf(url);
    const videoId = youtubeId(url);
    const text = `${title} ${project} ${domain} ${url}`;
    const target = classify(text);
    if (target === "review") continue;

    const candidate = {
      id: result.id,
      title,
      url,
      domain,
      kind: videoId ? "youtube" : "article",
      youtubeId: videoId,
      currentProject: result.currentProject || "",
      proposedProject: project,
      target,
      metadataSource: result.metadata?.source || "",
    };
    candidate.priority = scoreCandidate(candidate);
    candidates.push(candidate);
  }

  candidates.sort((a, b) => b.priority - a.priority || a.target.localeCompare(b.target) || a.title.localeCompare(b.title));

  const counts = {};
  for (const candidate of candidates) {
    const key = `${candidate.target}/${candidate.kind}`;
    counts[key] = (counts[key] || 0) + 1;
  }

  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  fs.writeFileSync(
    outputPath,
    JSON.stringify(
      {
        generatedAt: new Date().toISOString(),
        metadataPath,
        completedPath,
        totalCandidates: candidates.length,
        counts,
        candidates,
      },
      null,
      2,
    ),
  );
  console.log(JSON.stringify({ outputPath, totalCandidates: candidates.length, counts }, null, 2));
}

main();
