import fs from "node:fs";
import path from "node:path";

function compact(value) {
  return String(value || "").replace(/\s+/g, " ").trim();
}

function has(text, pattern) {
  return pattern.test(text);
}

function target(area, project, confidence = "medium", reason = "metadata-based global link project repair") {
  return { area, project, confidence, reason };
}

function classify(result, item) {
  const metadataTitle = compact(result.metadata?.title);
  const sourceText = [
    metadataTitle,
    result.metadata?.description,
    result.metadata?.author,
    result.metadata?.finalUrl,
    result.url,
    item.name,
    item.notes,
    item.project,
  ]
    .map(compact)
    .join(" ")
    .toLowerCase();
  const titleText = [metadataTitle, item.name].map(compact).join(" ").toLowerCase();

  const usefulMetadata =
    result.metadata?.ok &&
    metadataTitle &&
    !/^https:\/\/t\.co\//i.test(metadataTitle) &&
    !/^[^:]+:\s*https:\/\/t\.co\/\S+$/i.test(metadataTitle);
  const itemName = compact(item.name);
  const usefulCurrentName = itemName.length > 8 && !/^https?:\/\//i.test(itemName);

  if (!usefulMetadata && !usefulCurrentName) {
    if (has(sourceText, /youtube\.com\/@syntaxfm|syntaxfm/)) {
      return target("Software & AI", "Link Review: Developer Channels", "medium", "channel URL with recognizable developer channel");
    }
    if (has(sourceText, /youtube\.com\/@tailscale|tailscale/)) {
      return target("Home & Living", "Link Review: Smart Home & Homelab", "medium", "channel URL with recognizable networking channel");
    }
    return target("Review", "Link Review: Needs Human Review", "low", "no reliable link metadata");
  }

  if (has(sourceText, /porn|pornhat|adult|erotic|alix lynx|chad alva/)) {
    return target("Media, Food & Culture", "Link Review: Adult Media");
  }

  if (
    has(
      sourceText,
      /openclaw|clawdbot|nano.?claw|claude code|codex|ai coding|vibe code|coding assistant|workspace agents|agent that broke|ai agent|memory\.md|soul md|insecure agents|automating marketing tasks|build full websites/,
    )
  ) {
    return target("Software & AI", "Link Review: AI Coding Tools");
  }

  if (
    has(
      sourceText,
      /openai|anthropic|claude opus|claude\b|gemini|qwen|mistral|llm|ollama|glm|minimax|sam altman|dario amodei|ilya|ai safety|ai race|godfather of ai|multimodal ai|devday|wef.*ai|ai will|ai era|ai expert|ai model|qwen3|voxtral|moondream|analyze live video streams/,
    )
  ) {
    return target("Software & AI", "Link Review: AI Models & Research");
  }

  if (has(titleText, /redwood|solidjs|solidstart|svelte|astro/)) {
    return target("Software & AI", "Link Review: Frontend Frameworks - Other");
  }

  if (
    has(
      titleText,
      /react|next\.?js|remix|react router|react compiler|react query|tanstack|server actions|useeffect|concurrent react|turbopack|forwardref|zod/,
    )
  ) {
    return target("Software & AI", "Link Review: React & Next.js");
  }

  if (has(sourceText, /front.?end framework|framework better/)) {
    return target("Software & AI", "Link Review: Frontend Frameworks - Other");
  }

  if (
    has(
      sourceText,
      /css|web platform|declarative web push|form control styling|jen simmons|layout|margin-trim|slanted containers|details\s*&\s*summary|state of the web|web dev should know|fetch api|browser|html|imagekit|video api|digital asset management|web at google|google i\/o.*developer|developer keynote|dotjs|nordic\.js|bun|node\.js|vs code|creative coding|p5\.js|javascript|typescript|wasm|deploying .*github pages/,
    )
  ) {
    return target("Software & AI", "Link Review: Web Development");
  }

  if (has(sourceText, /design|ux|ui era|dieter rams|typography|frontend design|design trends|jenny wen|visual|prompt makes ai design/)) {
    return target("Design & Inspiration", "Link Review: Design & UX");
  }

  if (
    has(
      sourceText,
      /unifi|vlan|firewall|fiber gateway|home assistant|shelly|homelab|home server|paperless|scrypted|frigate|camera setup|tailscale|n8n|network settings|reolink|smart home/,
    )
  ) {
    return target("Home & Living", "Link Review: Smart Home & Homelab");
  }

  if (has(sourceText, /pizza|salmon|cooking|cook|vivaldi way|poached|neapolitanische|pizzateig/)) {
    return target("Media, Food & Culture", "Link Review: Food & Cooking");
  }

  if (has(sourceText, /protein|sugar doctor|diet|disease|cognitive decline|health|nutrition|80% of disease/)) {
    return target("Health & Personal", "Link Review: Health & Nutrition");
  }

  if (has(sourceText, /ottaviani|a state of trance|asot|gareth emery|andrew rayel|live in london|year mix|music festival|techtopia/)) {
    return target("Media, Food & Culture", "Link Review: Music & Live Sets");
  }

  if (has(sourceText, /prime video|amazon\.de.*ansehen|the boys|welt am draht|devil wears prada|trailer|film|series|continental|john wick|harald schmidt/)) {
    return target("Media, Food & Culture", "Link Review: Film & TV");
  }

  if (has(sourceText, /stiftung|steuern|tax|immocation|marktupdate|tariff|passive income|remote job|hubspot|business|startup|steven bartlett|diary of a ceo|ipo|finance/)) {
    return target("Business & Admin", "Link Review: Business, Finance & Startups");
  }

  if (has(sourceText, /xiaomi|electric car|kia pv5|elektro van|dyson|gameboy|apple at 50|pencilvac|global premiere|devices?/)) {
    return target("Tech & Gadgets", "Link Review: Devices & Vehicles");
  }

  if (has(sourceText, /yuval|simon sinek|trump|energy crisis|energiekrise|law and power|job markets|org charts|not prepared for 2027|being lied to about ai/)) {
    return target("Knowledge & Society", "Link Review: Society & Future");
  }

  if (has(sourceText, /all the things|things app|productivity|task management|focus course/)) {
    return target("Productivity & Workflows", "Link Review: Productivity Systems");
  }

  if (has(sourceText, /youtube|video|watch|live|playlist|prime video/)) {
    return target("Media, Food & Culture", "Link Review: Media to Inspect");
  }

  return target("Review", "Link Review: Needs Human Review", "low", "metadata did not match a clean category");
}

function parseArgs(argv) {
  const [metadataPath, itemsPath, outputPath] = argv.slice(2);
  if (!metadataPath || !itemsPath || !outputPath) {
    throw new Error("Usage: node scripts/build-link-project-repair.mjs <metadata.json> <current-items.json> <output.json>");
  }
  return { metadataPath, itemsPath, outputPath };
}

function main() {
  const { metadataPath, itemsPath, outputPath } = parseArgs(process.argv);
  const metadata = JSON.parse(fs.readFileSync(metadataPath, "utf8"));
  const itemsPayload = JSON.parse(fs.readFileSync(itemsPath, "utf8"));
  const currentItems = new Map((itemsPayload.items || itemsPayload).map((item) => [item.id, item]));

  const targetProjectPattern = /Videos & Channels|Social Links Review|Web Links Review|YouTube|X \/ Twitter/i;
  const assignments = [];
  const skipped = [];

  for (const result of metadata.results || []) {
    const item = currentItems.get(result.id);
    if (!item || !targetProjectPattern.test(item.project || "")) {
      continue;
    }

    const classification = classify(result, item);
    const assignment = {
      id: item.id,
      name: item.name,
      currentArea: item.area || "",
      currentProject: item.project || "",
      proposedArea: classification.area,
      proposedProject: classification.project,
      confidence: classification.confidence,
      reason: classification.reason,
      primaryDomain: result.domain || "",
      primaryUrl: result.url || "",
      metadataTitle: compact(result.metadata?.title),
      metadataSource: result.metadata?.source || "",
    };

    if (classification.confidence === "low") {
      skipped.push(assignment);
    } else if (assignment.currentProject !== assignment.proposedProject) {
      assignments.push(assignment);
    }
  }

  const countsByProject = {};
  for (const assignment of assignments) {
    countsByProject[assignment.proposedProject] = (countsByProject[assignment.proposedProject] || 0) + 1;
  }

  const payload = {
    generatedAt: new Date().toISOString(),
    metadataPath,
    itemsPath,
    targetProjectPattern: String(targetProjectPattern),
    assignments,
    skipped,
    countsByProject,
    sourceCandidates: assignments.length + skipped.length,
  };

  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  fs.writeFileSync(outputPath, JSON.stringify(payload, null, 2));

  console.log(
    JSON.stringify(
      {
        outputPath,
        assignments: assignments.length,
        skipped: skipped.length,
        countsByProject,
      },
      null,
      2,
    ),
  );
}

main();
