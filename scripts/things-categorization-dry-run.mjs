import fs from "node:fs";
import path from "node:path";

const MAX_CATEGORY_SIZE = 30;
const URL_RE = /https?:\/\/[^\s)\]}>\"']+/gi;

function normalize(value) {
  return String(value || "")
    .toLowerCase()
    .replace(/ß/g, "ss")
    .normalize("NFKD")
    .replace(/\p{Diacritic}/gu, "");
}

function compact(value, maxLength = 140) {
  const text = String(value || "").replace(/\s+/g, " ").trim();
  if (text.length <= maxLength) {
    return text;
  }

  return `${text.slice(0, maxLength - 1)}…`;
}

function csvValue(value) {
  const text = String(value ?? "");
  if (!/[",\n\r]/.test(text)) {
    return text;
  }

  return `"${text.replace(/"/g, '""')}"`;
}

function extractUrls(item) {
  const text = `${item.name}\n${item.notes}`;
  return [...text.matchAll(URL_RE)]
    .map((match) => match[0].replace(/[.,;]+$/, ""))
    .filter(Boolean);
}

function extractDomains(item) {
  return extractUrls(item)
    .map((rawUrl) => {
      try {
        const url = new URL(rawUrl);
        return url.hostname.replace(/^www\./, "").replace(/^m\./, "");
      } catch {
        return "";
      }
    })
    .filter(Boolean);
}

function extractUrlSignalText(item) {
  return extractUrls(item)
    .map((rawUrl) => {
      try {
        const url = new URL(rawUrl);
        return `${url.hostname.replace(/^www\./, "").replace(/^m\./, "")} ${url.pathname.replace(/[^\p{Letter}\p{Number}]+/gu, " ")}`;
      } catch {
        return "";
      }
    })
    .join(" ");
}

function sourceLabel(domain) {
  if (!domain) {
    return "No Source";
  }

  const labels = [
    [/heise\.de$/, "heise"],
    [/stadt-bremerhaven\.de$/, "Stadt Bremerhaven"],
    [/ifun\.de$/, "ifun"],
    [/youtube\.com$|youtu\.be$/, "YouTube"],
    [/x\.com$|twitter\.com$|t\.co$/, "X / Twitter"],
    [/test\.de$/, "Stiftung Warentest"],
    [/oekotest\.de$/, "Oekotest"],
    [/techstage\.de$/, "TechStage"],
    [/amazon\.de$|amazon\.com$|amzn\.eu$/, "Amazon"],
    [/macstories\.net$/, "MacStories"],
    [/nytimes\.com$/, "NYTimes"],
    [/medium\.com$/, "Medium"],
    [/vercel\.com$/, "Vercel"],
    [/github\.com$/, "GitHub"],
    [/npmjs\.com$/, "npm"],
    [/figma\.com$/, "Figma"],
    [/dribbble\.com$/, "Dribbble"],
    [/seths\.blog$/, "Seth Godin"],
    [/herbertlui\.net$/, "Herbert Lui"],
    [/daringfireball\.net$/, "Daring Fireball"],
    [/smartapfel\.de$|homekitnews\.com$/, "Smart Home News"],
  ];

  for (const [pattern, label] of labels) {
    if (pattern.test(domain)) {
      return label;
    }
  }

  const parts = domain.split(".");
  if (parts.length >= 2) {
    return parts.at(-2)
      .replace(/[-_]+/g, " ")
      .replace(/\b\w/g, (char) => char.toUpperCase());
  }

  return domain;
}

function itemText(item) {
  const domains = extractDomains(item).join(" ");
  const contentWithoutRawUrls = `${item.name}\n${item.notes}`.replace(URL_RE, " ");
  const urlSignals = extractUrlSignalText(item);
  return normalize(`${contentWithoutRawUrls}\n${item.tags}\n${item.area}\n${item.project}\n${domains}\n${urlSignals}`);
}

function has(text, pattern) {
  return pattern.test(text);
}

function yearOf(item) {
  return String(item.created || item.modified || "unknown").slice(0, 4) || "unknown";
}

function existingProjectHint(item) {
  return item.project ? `Old Project ${item.project}` : "";
}

function classify(item) {
  const text = itemText(item);
  const domains = extractDomains(item);
  const primaryDomain = domains[0] || "";
  const source = sourceLabel(primaryDomain);
  const tags = normalize(item.tags);
  const oldProject = normalize(item.project);
  const hints = [source, yearOf(item), existingProjectHint(item)].filter(Boolean);

  function result(area, project, confidence, reason, extraHints = []) {
    const projectText = normalize(project);
    return {
      area,
      project,
      confidence,
      reason,
      primaryUrl: extractUrls(item)[0] || "",
      primaryDomain,
      source,
      hints: [...extraHints, ...hints].filter((hint, index, all) => {
        return hint && all.indexOf(hint) === index && !projectText.includes(normalize(hint));
      }),
    };
  }

  if (has(tags, /skill: ai agents|skill archive|skill: js tooling|skill: frontend ui|skill: performance|skill: testing|skill: backend cloud|skill: security|skill: visual assets|skill: marketing|skill: knowledge/)) {
    if (has(tags, /skill: ai agents/) || has(text, /\b(ai agents?|agentic|mcp|openai|claude|gpt|llm|cursor|copilot|qwen|gemini)\b/)) {
      return result("Software & AI", "AI Agents & Coding", "high", "skill tag or AI keyword", ["AI"]);
    }
    if (has(tags, /skill: frontend ui/)) {
      return result("Software & AI", "Frontend UI Skills", "high", "skill tag", ["Frontend"]);
    }
    if (has(tags, /skill: js tooling/)) {
      return result("Software & AI", "JavaScript Tooling Skills", "high", "skill tag", ["Tooling"]);
    }
    if (has(tags, /skill: performance/)) {
      return result("Software & AI", "Performance Skills", "high", "skill tag", ["Performance"]);
    }
    if (has(tags, /skill: testing/)) {
      return result("Software & AI", "Testing Skills", "high", "skill tag", ["Testing"]);
    }
    if (has(tags, /skill: security/)) {
      return result("Software & AI", "Security Skills", "high", "skill tag", ["Security"]);
    }
    if (has(tags, /skill: marketing/)) {
      return result("Business & Admin", "Marketing Skills", "high", "skill tag", ["Marketing"]);
    }
    if (has(tags, /skill: knowledge/)) {
      return result("Reading & Knowledge", "Knowledge Skills", "high", "skill tag", ["Knowledge"]);
    }
  }

  if (oldProject === "quotes" || has(text, /\bquote|zitat|seth godin|raymond joseph teller|vince ebert\b/)) {
    return result("Reading & Knowledge", "Quotes & Sayings", "high", "quote/project match", ["Quotes"]);
  }

  if (oldProject === "kochen" || has(text, /\brezept|kochen|cooking|essen|food|cocktail|verpoorten|bombardino|waldorf|fleisch|meatshop\b/)) {
    return result("Media, Food & Culture", "Recipes & Food", "high", "food keyword/project match", ["Food"]);
  }

  if (oldProject === "reise" || has(text, /\breise|urlaub|hotel|ferien|center parcs|landal|kempervennen|wirfttal|tel aviv|montabaur|trip|destination\b/)) {
    return result("Travel & Places", "Trips, Hotels & Destinations", "high", "travel keyword/project match", ["Travel"]);
  }

  if (oldProject === "fahrrad oscar 20\"" || oldProject === "kinder" || has(text, /\bfamilie|kinder|kindersitz|kinderfahrrad|oscar|baby|schule|bildschirmzeit|screen time|haidt|anxious generation|bafog\b/)) {
    if (has(text, /\bfahrrad|bike|kindersitz|sitz\b/)) {
      return result("Family & Kids", "Kids Mobility & Gear", "high", "family mobility keyword", ["Kids Gear"]);
    }
    if (has(text, /\bmedien|screen time|bildschirmzeit|fernseher|tablet|handy|anxious generation\b/)) {
      return result("Family & Kids", "Kids Media & Development", "high", "family media keyword", ["Kids Media"]);
    }
    return result("Family & Kids", "Family Admin & Ideas", "medium", "family keyword/project match", ["Family"]);
  }

  if (has(text, /\bgenossenschaft|steuer|steuern|holding|etf|fonds|vorabpauschale|finanz|bank|versicherung|recht|vertrag|ihk|gez|marke anmelden|kanzlei|buchhaltung|jahresabschluss\b/)) {
    return result("Business & Admin", "Finance, Tax & Legal", "high", "finance/admin keyword", ["Admin"]);
  }

  if (has(text, /\bmarketing|pricing|growth|sales|brand|agentur|agency|positioning|copywriting|seo|analytics|tracking|kunden|freelancer|firma|unternehmen|saas|product idea|produktidee|dropscan|fincompare|geckoboard|klipfolio\b/)) {
    if (has(text, /\bpricing|price|preis|kosten\b/)) {
      return result("Business & Admin", "Pricing & Offers", "high", "pricing keyword", ["Pricing"]);
    }
    if (has(text, /\banalytics|tracking|dashboard|geckoboard|klipfolio\b/)) {
      return result("Business & Admin", "Analytics & Dashboards", "high", "analytics keyword", ["Analytics"]);
    }
    return result("Business & Admin", "Marketing, SaaS & Company Ideas", "medium", "business keyword", ["Business Ideas"]);
  }

  if (has(text, /\bhomekit|smart home|smarthome|aqara|hue|eve |matter|thread|zigbee|tado|home assistant|smartapfel|homekitnews\b/)) {
    return result("Home & Living", "Smart Home & HomeKit", "high", "smart home keyword/source", ["Smart Home"]);
  }

  if (oldProject === "gartenbau" || has(text, /\b(?:garten|maehroboter|mahroboter|rasen|zaun|tor|pforte|outdoor|terrasse|pflanze)\b/)) {
    return result("Home & Living", "Garden & Outdoor", "high", "garden keyword/project match", ["Garden"]);
  }

  if (oldProject === "schallabsorber" || has(text, /\bschallabsorber|akustik|absorber|paneel|panel|sound\b/)) {
    return result("Home & Living", "Acoustics & Sound Panels", "high", "acoustics keyword/project match", ["Acoustics"]);
  }

  if (oldProject === "mobel" || has(text, /\bmobel|moebel|stuhl|tisch|regal|sofa|wandregal|lamellenwand|tylko|hovr|ikea\b/)) {
    return result("Home & Living", "Furniture & Shelving", "high", "furniture keyword/project match", ["Furniture"]);
  }

  if (oldProject === "dekoration" || has(text, /\bdeko|dekoration|poster|bild|bilder|stoff|wandbild|interior|lampe|leuchte|lighting|licht\b/)) {
    if (has(text, /\blampe|leuchte|lighting|licht|hue\b/)) {
      return result("Home & Living", "Lighting", "high", "lighting keyword", ["Lighting"]);
    }
    return result("Home & Living", "Decoration & Interior", "high", "decoration keyword/project match", ["Decoration"]);
  }

  if (oldProject === "office-ausstattung" || has(text, /\bburo|buero|office|desk|monitor|stuhl|meeting|podcast|mikrofon|rode|røde|displayport|switch|lan kabel\b/)) {
    return result("Home & Living", "Home Office & Workspace", "medium", "office/workspace keyword/project match", ["Office"]);
  }

  if (oldProject === "dielen-tur" || has(text, /\b(?:tur|tuer|diele|boden|renov|dusch|bad|kuche|kueche|elektroarbeiten|photovoltaik|solar|warmepumpe|waermepumpe)\b/)) {
    if (has(text, /\bphotovoltaik|solar|warmepumpe|waermepumpe|energie|strom\b/)) {
      return result("Home & Living", "Energy & Photovoltaics", "high", "energy keyword", ["Energy"]);
    }
    if (has(text, /\bdusch|bad|kuche|kueche\b/)) {
      return result("Home & Living", "Kitchen & Bath", "high", "kitchen/bath keyword", ["Kitchen Bath"]);
    }
    return result("Home & Living", "Renovation & House Work", "high", "house work keyword/project match", ["Renovation"]);
  }

  if (has(text, /\bopenai|claude|gpt|llm|qwen|gemini|mistral|anthropic|cursor|copilot|ai coding|prompt|agentic|mcp|ai agent|agents?|midjourney|elevenlabs|minimax|claw|openclaw\b/)) {
    if (has(text, /\bcursor|copilot|coding|code|developer|github|claw|openclaw\b/)) {
      return result("Software & AI", "AI Coding Tools", "high", "AI coding keyword", ["AI Coding"]);
    }
    if (has(text, /\bvoice|video|image|midjourney|elevenlabs|minimax|media\b/)) {
      return result("Software & AI", "AI Media & Generation", "high", "AI media keyword", ["AI Media"]);
    }
    return result("Software & AI", "AI Models, Agents & Research", "high", "AI keyword", ["AI Research"]);
  }

  if (has(text, /\breact|next\.?js|remix|jsx|tsx|server components|rsc|hooks?|react router\b/)) {
    return result("Software & AI", "Frontend: React & Next.js", "high", "React/frontend keyword", ["React"]);
  }

  if (has(text, /\bcss|sass|tailwind|oklch|typography|font|layout|grid|container query|animation|framer motion|gsap|web animation|drop-caps\b/)) {
    if (has(text, /\banimation|motion|gsap|transition\b/)) {
      return result("Software & AI", "Frontend: Animation & Motion", "high", "frontend animation keyword", ["Animation"]);
    }
    if (has(text, /\btypography|font|drop-caps|pimpmytype\b/)) {
      return result("Design & Inspiration", "Typography & Fonts", "high", "typography keyword", ["Typography"]);
    }
    return result("Software & AI", "Frontend: CSS & Styling", "high", "CSS/frontend keyword", ["CSS"]);
  }

  if (has(text, /\btypescript|javascript|node\.?js|npm|pnpm|vite|webpack|rspack|bun|deno|eslint|prettier|package|tooling|tinybase\b/)) {
    return result("Software & AI", "JavaScript Tooling & Libraries", "high", "JS/tooling keyword", ["Tooling"]);
  }

  if (has(text, /\bgraphql|api|backend|database|postgres|supabase|appwrite|server|cloudflare|worker|edge|vercel|netlify|deploy|hosting\b/)) {
    if (has(text, /\bvercel|netlify|cloudflare|deploy|hosting\b/)) {
      return result("Software & AI", "Deployment & Hosting", "high", "deployment keyword", ["Hosting"]);
    }
    return result("Software & AI", "Backend, APIs & Data", "high", "backend/data keyword", ["Backend"]);
  }

  if (has(text, /\bsecurity|auth|oauth|password|privacy|1password|webauthn|passkey|csp|xss|csrf\b/)) {
    return result("Software & AI", "Security & Privacy", "high", "security/privacy keyword", ["Security"]);
  }

  if (has(text, /\bperformance|perf|cache|render|web vitals|speed|slow|interaction times|prerendering\b/)) {
    return result("Software & AI", "Performance & Rendering", "high", "performance keyword", ["Performance"]);
  }

  if (has(text, /\btesting|test|playwright|vitest|jest|storybook|qa\b/)) {
    return result("Software & AI", "Testing & QA", "high", "testing keyword", ["Testing"]);
  }

  if (has(text, /\bhtml|web component|browser|webkit|safari|chrome|firefox|accessibility|aria|pwa\b/)) {
    return result("Software & AI", "Web Platform & Browsers", "medium", "web platform keyword", ["Web Platform"]);
  }

  if (oldProject === "homepage" || oldProject === "amiana" || oldProject === "tools" || oldProject === "technik kandidaten") {
    return result("Software & AI", "Old Software Projects Review", "medium", "legacy software project", [item.project]);
  }

  if (oldProject === "inspiration" || has(text, /\bfigma|design system|ui kit|icon|icons|illustration|dribbble|behance|landing page|webflow|framer|portfolio|website design|ui design|ux|brand guideline|logo\b/)) {
    if (has(text, /\bfigma|design system|ui kit|component\b/)) {
      return result("Design & Inspiration", "Design Systems & UI Kits", "high", "design systems keyword", ["Design Systems"]);
    }
    if (has(text, /\bicon|icons|illustration|asset|svg\b/)) {
      return result("Design & Inspiration", "Icons & Visual Assets", "high", "visual asset keyword", ["Assets"]);
    }
    if (has(text, /\blanding|website|portfolio|webflow|framer|dribbble|behance|inspiration\b/)) {
      return result("Design & Inspiration", "Web Design Inspiration", "high", "web design inspiration keyword", ["Inspiration"]);
    }
    return result("Design & Inspiration", "UI & UX Patterns", "medium", "design keyword", ["UI UX"]);
  }

  if (has(text, /\bapple|mac|iphone|ipad|imac|airpods|ios|macos|safari|ifun|macstories|daringfireball\b/)) {
    return result("Tech & Gadgets", "Apple, Mac & iOS", "high", "Apple/Mac keyword/source", ["Apple"]);
  }

  if (has(text, /\bhandytarif|vodafone|telekom|sim|5g|lte|smartphone|phone\b/)) {
    return result("Tech & Gadgets", "Phones, Plans & Mobile", "high", "mobile keyword", ["Mobile"]);
  }

  if (has(text, /\bauto|pkw|e-auto|elektroauto|leasing|mobile\.de|fahrrad|bike|e-bike|bahn\b/)) {
    return result("Mobility & Transport", "Cars, Bikes & Transport", "medium", "mobility keyword", ["Mobility"]);
  }

  if (oldProject === "unterhaltung" || has(text, /\bfilm|serie|streaming|netflix|prime video|apple tv|magenta tv|nebula|zdf|4kfilme|kino|youtube|youtu\.be|video\b/)) {
    if (has(text, /\byoutube|youtu\.be|video\b/)) {
      return result("Media, Food & Culture", "Videos & Channels", "medium", "video source/keyword", ["Videos"]);
    }
    return result("Media, Food & Culture", "Movies, TV & Streaming", "high", "entertainment keyword/project match", ["Streaming"]);
  }

  if (has(text, /\bbook|books|buch|buecher|lesen|reading|article|artikel|essay|newsletter|obsidian|second brain|knowledge|writing|schreiben|productivity|notizen|notes|zettelkasten\b/)) {
    if (has(text, /\bobsidian|second brain|zettelkasten|notizen|notes|knowledge\b/)) {
      return result("Reading & Knowledge", "Knowledge Management", "high", "knowledge management keyword", ["PKM"]);
    }
    if (has(text, /\bproductivity|produktiv|focus|brain|habits?\b/)) {
      return result("Reading & Knowledge", "Productivity & Thinking", "medium", "productivity keyword", ["Productivity"]);
    }
    if (has(text, /\bbook|books|buch|buecher|reading|lesen\b/)) {
      return result("Reading & Knowledge", "Books & Reading List", "medium", "book/reading keyword", ["Books"]);
    }
    return result("Reading & Knowledge", "Articles & Essays", "medium", "article/essay keyword", ["Articles"]);
  }

  if (has(text, /\bfitness|gesundheit|health|arzt|medical|psychology|mental|sport|train your brain\b/)) {
    return result("Health & Personal", "Health, Fitness & Mind", "medium", "health/personal keyword", ["Health"]);
  }

  if (has(text, /\bherbertlui\.net|seths\.blog|world\.hey\.com|timharford\.com|artofmanliness\.com|marco\.org|industrialempathy\.com|tinkerer\.club\b/)) {
    if (has(text, /\bbusiness|pricing|audience|case study|marketing|company|developers|technical debt|estimates?|software done well\b/)) {
      return result("Reading & Knowledge", "Business, Software & Work Essays", "medium", "essay source plus business/software keyword", ["Essays"]);
    }
    return result("Reading & Knowledge", "Essays & Personal Knowledge", "medium", "known essay source", ["Essays"]);
  }

  if (has(text, /\bthesweetsetup\.com|readwise\.io|sunsama\.com|brain\.fm|notion|planner|habit tracker|focus digest|do less\b/)) {
    return result("Reading & Knowledge", "Productivity Apps & Workflows", "medium", "productivity app/source keyword", ["Productivity"]);
  }

  if (has(text, /\bmagicpath\.ai|lovable\.dev|motionsites\.ai|v0\.dev\b/)) {
    return result("Software & AI", "AI App Builders & Design Tools", "high", "AI app/design builder source", ["AI Builders"]);
  }

  if (has(text, /\bollama\.com|lmstudio\.ai|openjarvis|local ai\b/)) {
    return result("Software & AI", "Local AI Tools", "high", "local AI source/keyword", ["Local AI"]);
  }

  if (has(text, /\bevilmartians\.com|engineering\.linecorp\.com|gitbutler\.com|tailscale\.com|zed\.dev|kagi\.com|che?zmoi\.io|chezmoi\.io|epicweb\.dev\b/)) {
    if (has(text, /\bai|vibe|agents?|developers use ai\b/)) {
      return result("Software & AI", "AI Coding Tools", "medium", "engineering source plus AI keyword", ["AI Coding"]);
    }
    return result("Software & AI", "Developer Tools & Engineering Articles", "medium", "developer tool/source", ["Dev Tools"]);
  }

  if (has(text, /\bmantine\.dev|ui\.shadcn\.com|radix-ui\.com|ark-ui\.com|component\.gallery\b/)) {
    return result("Software & AI", "UI Component Libraries", "high", "UI component library source", ["UI Libraries"]);
  }

  if (has(text, /\butopia\.fyi|matuzo\.at|bram\.us|oddbird\.net|zachleat\.com|nerdy\.dev|cloudfour\.com|thegoodlineheight\.com|leonardocolor\.io\b/)) {
    if (has(text, /\btypography|line height|fluid type|font|color\b/)) {
      return result("Design & Inspiration", "Typography, Color & Fluid Design", "high", "design/CSS source plus type/color keyword", ["Typography"]);
    }
    return result("Software & AI", "Frontend: CSS & Web Platform Sources", "high", "CSS/web platform source", ["CSS Sources"]);
  }

  if (has(text, /\bmintlify\.com|docusaurus\.io|ia\.net\/presenter|docs?|documentation\b/)) {
    return result("Software & AI", "Documentation & Developer Content", "medium", "documentation product/source", ["Docs"]);
  }

  if (has(text, /\bvalibot\.dev|rome\.tools|rolldown\.rs|voidzero\.dev|airbnb\.io|tkdodo\.eu|nodered\.org|gist\.github\.com|exceljs|uv\b/)) {
    return result("Software & AI", "JavaScript Tooling & Libraries", "medium", "developer library/tool source", ["Tooling"]);
  }

  if (has(text, /\boverreacted\.io|theburningmonk\.com|jeremydaly\.com|webdeveloper\.beehiiv\.com|better-upload\.js\.org|tremor\.so|parceljs\.org|tsev\.dev|wallabyjs\.com|merge\.dev|pavel-romanov\.com|solberg\.is|zod\.dev|nordcraft\.com|app\.quiver\.ai|kittygiraudel\.com|daverupert\.com|tpgi\.com|lingo\.dev|learn\.microsoft\.com|vulcanjs\.org|jamie\.build|starship\.rs|selfhosted\.show|bjornlu\.com|ladle\.dev|tempo\.formkit\.com|lexical\.dev|knip\.dev|dev\.to|addyosmani\.com|effect\.website|brew\.sh|stylexjs\.com|es-toolkit\.dev|localstack\.cloud|downshift-js\.com|pixijs\.com|formidable\.com|stackoverflow\.blog|lix\.dev|sugarcube\.sh|fusejs\.io|crawlee\.dev|kaleidawave\.github\.io|mathiasbynens\.github\.io|infrequently\.org|unraid\.net|scrypted\.app|caseyliss\.com\b/)) {
    if (has(text, /\bcolor|oklch|focus|scroll|ui|css|html|input|lcp|fetchpriority|font|typography\b/)) {
      return result("Software & AI", "Frontend: CSS & Web Platform Sources", "medium", "frontend/web platform source", ["CSS Sources"]);
    }
    if (has(text, /\bself-hosted|selfhosted|unraid|scrypted|tailscale|server|cloud|lambda|localstack\b/)) {
      return result("Software & AI", "Backend, APIs & Infrastructure", "medium", "backend/infrastructure source", ["Infrastructure"]);
    }
    return result("Software & AI", "Developer Tools & Engineering Articles", "medium", "developer source", ["Dev Tools"]);
  }

  if (has(text, /\bmonolisa\.dev|nickylaatz\.com|ia\.net\/topics|set\.studio\b/)) {
    return result("Design & Inspiration", "Typography & Visual Tools", "medium", "typography/design source", ["Typography"]);
  }

  if (has(text, /\beldoraui\.site|sketch\.com|colorjs\.io|br\.studio|primer\.style|berkeleygraphics\.com|minimum-design\.com|dontfuckwithscroll\.com|motion\.dev|colourcontrast\.cc|kumo-ui\.com|southleft\.com|furbo\.org|annebovelett\.eu|blog\.jim-nielsen\.com|dev\.aspect\.app|aspect\.app|rive\.app|ui\.sh|abduzeedo\.com|dgrees\.studio|plastic\.design|thesvg\.org|getdesign\.md|kargo\.studiovoila\.com|createwithplay\.com|emilkowal\.ski|time\.openstatus\.dev|piling\.js\.org|dev\.aspect\.app|supahero\.io\b/)) {
    if (has(text, /\btypeface|font|typography|mono|line length|readability\b/)) {
      return result("Design & Inspiration", "Typography & Visual Tools", "medium", "design typography source", ["Typography"]);
    }
    if (has(text, /\bmotion|animation|rive|clip path|interactive graphics|scroll\b/)) {
      return result("Design & Inspiration", "Interaction & Motion Inspiration", "medium", "motion/design source", ["Motion"]);
    }
    return result("Design & Inspiration", "Design Tools & Inspiration", "medium", "design source", ["Design"]);
  }

  if (has(text, /\bmydealz\.de|nubert\.de|de\.ooni\.com|ooni|parfum|ugreen|kabelkanal\b/)) {
    if (has(text, /\bnubert|subwoofer|center|audio|lautsprecher|speaker\b/)) {
      return result("Shopping & Product Research", "Audio & Entertainment Gear", "medium", "audio shopping source/keyword", ["Audio Gear"]);
    }
    if (has(text, /\booni|pizza|mehl|sauerteig|manitoba\b/)) {
      return result("Media, Food & Culture", "Pizza, Baking & Cooking Gear", "medium", "cooking gear keyword/source", ["Cooking"]);
    }
    return result("Shopping & Product Research", "Deals & Shopping Leads", "medium", "shopping/deals source", ["Deals"]);
  }

  if (has(text, /\bmiahdogtags\.com|teppichscheune\.de|i\.soreto\.com|melitta-momentum\.com|musikhaus-hochstein\.de|hamburgerlackprofi\.de|korodrogerie\.de|getyourgreen\.de|60beans\.com|support\.controme\.com|algenmax\.de|onkyo\.com|baristina\.com|m-de\.cupshe\.com|maanta\.de|sawade\.berlin|feey-pflanzen\.de|zarahome\.com|ersatzteile\.enders-germany\.com|mehlau\.net|marazzi\.de|miahdogtags\.com\b/)) {
    if (has(text, /\bkaffee|coffee|melitta|baristina|60beans|pralinen|koro|sawade\b/)) {
      return result("Media, Food & Culture", "Coffee, Sweets & Food Shopping", "medium", "food shopping source", ["Food Shopping"]);
    }
    if (has(text, /\bnubert|onkyo|dirac|subwoofer|preamplifier|audio|musikhaus\b/)) {
      return result("Shopping & Product Research", "Audio & Entertainment Gear", "medium", "audio product source", ["Audio Gear"]);
    }
    if (has(text, /\bteppich|flexispot|lufterfrischer|sonnensegel|pflanzen|marazzi|controme|fassaden|algenmax|enders\b/)) {
      return result("Home & Living", "Home Products & Maintenance", "medium", "home product/maintenance source", ["Home Products"]);
    }
    return result("Shopping & Product Research", "General Product Research", "medium", "product source", ["Shopping"]);
  }

  if (has(text, /\beurope\.huttopia\.com|huttopia|campingplatz|naturcamping\b/)) {
    return result("Travel & Places", "Camping & Nature Trips", "medium", "travel/camping source", ["Camping"]);
  }

  if (has(text, /\bmy\.schoolfox\.app|appcamps\.de|tinyhumans\.gitbook\.io\b/)) {
    return result("Family & Kids", "School, Kids Apps & Learning", "medium", "school/kids app source", ["Kids Learning"]);
  }

  if (has(text, /\bopenmed\.life|zahnprofis\.de|peptone\.io|muscle-booster\.io|myjuniper\.com|solution-talk\.de|tobias-beck\.com|momentleben\.de\b/)) {
    if (has(text, /\bopenmed|clinical|zahn|peptone|workout|gewichtsverlust|muscle\b/)) {
      return result("Health & Personal", "Health, Fitness & Medical", "medium", "health/medical source", ["Health"]);
    }
    return result("Health & Personal", "Coaching & Personal Development", "medium", "coaching/personal development source", ["Personal Development"]);
  }

  if (has(text, /\bgetrelatio\.me|personal-drive\.de|profitableskills\.com|skool\.com|edenred\.de|actualbudget\.org|lemonsqueezy\.com|legalmonster\.com|t\.sebastian-software\.de|rockstardevelopers\.de|mediatask\.de|vos9x\.com|dls\.co|bzgapps\.com|portal\.gitnation\.org|fitc\.ca\b/)) {
    if (has(text, /\bbudget|actualbudget|plausible|analytics|lemonsqueezy|zahlung|abo|edenred|legal|cookie consent\b/)) {
      return result("Business & Admin", "Business Tools, Billing & Analytics", "medium", "business tool/billing source", ["Business Tools"]);
    }
    if (has(text, /\bconference|talk|gitnation|fitc\b/)) {
      return result("Software & AI", "Developer Conferences & Talks", "medium", "developer conference source", ["Conferences"]);
    }
    return result("Business & Admin", "Company, Product & Positioning Notes", "medium", "business/product source", ["Company Notes"]);
  }

  if (has(text, /\bbgslabs\.org|mikekarnj\.com|reverse-dictionary\.virock\.org|techmeme\.com|mitpress\.mit\.edu|betterhumans\.pub|waitbutwhy\.com|insm-oekonomenblog\.de|adactio\.com|timkadlec\.com|theworst\.dev|mattruby\.substack\.com|substack\.com|medium\.com|nytimes\.com\b/)) {
    if (has(text, /\bdeveloper advocate|design tokens|software|markdown|blog|techmeme|web\b/)) {
      return result("Reading & Knowledge", "Software & Design Essays", "medium", "essay source plus software/design keyword", ["Essays"]);
    }
    return result("Reading & Knowledge", "Articles, Essays & Ideas", "medium", "article/essay source", ["Essays"]);
  }

  if (has(text, /\bsmartypants|webp|makeschema|cuid|bootstrap|icu message|git describe|frontend error logging|sentry|logrocket|posthog|adblocker|tailscale dns|mailfence|things 3|bot: skills|bot: things|install: uv\b/)) {
    if (has(text, /\bmailfence|privacy|dns|adblocker\b/)) {
      return result("Software & AI", "Security & Privacy", "medium", "software privacy/security keyword", ["Security"]);
    }
    return result("Software & AI", "Developer Notes & Snippets", "medium", "developer note/snippet keyword", ["Dev Notes"]);
  }

  if (has(text, /\bhomeassistent|home assistant|wallbox|nuki|sonos|wlan 160hz|unifi\b/)) {
    return result("Home & Living", "Smart Home & Network Setup", "medium", "smart home/network keyword", ["Smart Home"]);
  }

  if (has(text, /\bwohnflachen|wohnflaechen|wofiv|gemeindeblatt|forderverein|foerderverein|nabu kundigen|nabu kuendigen\b/)) {
    return result("Business & Admin", "Personal Admin & Forms", "medium", "admin/forms keyword", ["Admin"]);
  }

  if (has(text, /\bschuhe|nubuk|leder|pull-up-bar|koffer|farbe ammonite|schmuck|lantz\b/)) {
    return result("Shopping & Product Research", "Personal Products & Apparel", "medium", "personal product keyword", ["Personal Shopping"]);
  }

  if (has(text, /\bsauerteig|pizza|manitobamehl|fastenzeit\b/)) {
    return result("Media, Food & Culture", "Recipes & Food", "medium", "food keyword", ["Food"]);
  }

  if (has(text, /\btraders place|trading konto|inflationsausgleich|hans werner sinn\b/)) {
    return result("Business & Admin", "Finance, Tax & Legal", "medium", "finance/economics keyword", ["Finance"]);
  }

  if (has(text, /\bmediathekview|audible|fernseher|77 zoll|foto-bibliothek|fotos|re-import fotos\b/)) {
    return result("Media, Food & Culture", "Media Libraries & Devices", "medium", "media library/device keyword", ["Media Devices"]);
  }

  if (has(text, /\bcolayer|sebastian software|restaurant homepages|pull request|product|premium|reiche leute|geschafte|geschäfte\b/)) {
    return result("Business & Admin", "Company, Product & Positioning Notes", "medium", "company/product note keyword", ["Company Notes"]);
  }

  if (has(text, /\beinsicht oder erfahrung|konigsdisziplin|koenigsdisziplin|spuren hinterlassen|obvious is not obvious|klarheit begeisterung|build - teach - lead\b/)) {
    return result("Reading & Knowledge", "Quotes & Sayings", "medium", "quote-like note keyword", ["Quotes"]);
  }

  if (has(text, /\bfamilywall|whatsapp pin|einladen|paw patrol\b/)) {
    return result("Family & Kids", "Family Admin & Ideas", "medium", "family admin/media keyword", ["Family"]);
  }

  if (has(text, /\bamazon\.|amzn\.eu|angebot|angebote|kaufen|kosten|preis|review|vergleich|produkt|shop|ebay|etsy|test\.de|oekotest|techstage\b/)) {
    if (has(text, /\bburo|buero|office|monitor|desk|stuhl|mikrofon|displayport|lan kabel\b/)) {
      return result("Shopping & Product Research", "Office & Work Gear", "medium", "shopping/work gear keyword", ["Office Gear"]);
    }
    if (has(text, /\bmac|iphone|ipad|usb|kabel|displayport|lan|audio|kamera|microfon|mikrofon|router|computer|elektronik\b/)) {
      return result("Shopping & Product Research", "Tech Products", "medium", "shopping/tech keyword", ["Tech Products"]);
    }
    if (has(text, /\bbook|buch|books\b/)) {
      return result("Shopping & Product Research", "Books to Consider", "medium", "book shopping keyword", ["Books"]);
    }
    return result("Shopping & Product Research", "General Product Research", "low", "shopping/source keyword", ["Shopping"]);
  }

  if (primaryDomain) {
    if (has(text, /\bheise\.de|stadt-bremerhaven\.de|techstage\.de|ifun\.de|smartapfel\.de|homekitnews\.com/)) {
      return result("Tech & Gadgets", "Consumer Tech News Review", "low", "consumer tech source", ["Tech News"]);
    }
    if (has(text, /\bx\.com|twitter\.com|t\.co|threads\.com|instagram\.com|reddit\.com/)) {
      return result("Review", "Social Links Review", "low", "social link source", ["Social"]);
    }
    return result("Review", "Web Links Review", "low", "unclassified URL", ["Web Links"]);
  }

  return result("Review", "Manual Review", "low", "no strong signal", ["Manual"]);
}

function applySizeLimit(assignments, maxSize) {
  const mutable = assignments.map((assignment) => ({
    ...assignment,
    projectParts: [assignment.project],
  }));

  for (let pass = 0; pass < 5; pass += 1) {
    const groups = groupAssignments(mutable);
    const oversized = [...groups.values()].filter((group) => group.length > maxSize);
    if (!oversized.length) {
      break;
    }

    let changed = false;
    for (const group of oversized) {
      const hintCounts = new Map();
      for (const assignment of group) {
        for (const hint of assignment.hints) {
          if (!assignment.projectParts.includes(hint)) {
            hintCounts.set(hint, (hintCounts.get(hint) || 0) + 1);
          }
        }
      }

      const minHintSize = Math.min(maxSize, Math.max(4, Math.ceil(group.length * 0.04)));
      const eligibleHints = new Set(
        [...hintCounts.entries()]
          .filter(([, count]) => count >= minHintSize)
          .sort((a, b) => b[1] - a[1])
          .map(([hint]) => hint),
      );

      if (!eligibleHints.size) {
        continue;
      }

      for (const assignment of group) {
        const nextHint = assignment.hints.find((hint) => eligibleHints.has(hint) && !assignment.projectParts.includes(hint));
        const fallback = assignment.projectParts.includes("Mixed") ? "" : "Mixed";
        const nextPart = nextHint || fallback;
        if (nextPart) {
          assignment.projectParts.push(nextPart);
          changed = true;
        }
      }
    }

    if (!changed) {
      break;
    }
  }

  const finalGroups = groupAssignments(mutable);
  for (const group of finalGroups.values()) {
    if (group.length <= maxSize) {
      continue;
    }

    group
      .sort((a, b) => compact(a.item.name).localeCompare(compact(b.item.name), "de"))
      .forEach((assignment, index) => {
        assignment.projectParts.push(`Batch ${String(Math.floor(index / maxSize) + 1).padStart(2, "0")}`);
      });
  }

  return mutable.map((assignment) => ({
    ...assignment,
    project: assignment.projectParts.join(" - "),
  }));
}

function groupAssignments(assignments) {
  const groups = new Map();
  for (const assignment of assignments) {
    const key = `${assignment.area}\t${assignment.projectParts.join(" - ")}`;
    if (!groups.has(key)) {
      groups.set(key, []);
    }
    groups.get(key).push(assignment);
  }
  return groups;
}

function buildReports(payload, assignments, outputPrefix, maxSize) {
  const generatedAt = new Date().toISOString();
  const groups = new Map();
  const areas = new Map();

  for (const assignment of assignments) {
    const groupKey = `${assignment.area}\t${assignment.project}`;
    if (!groups.has(groupKey)) {
      groups.set(groupKey, []);
    }
    groups.get(groupKey).push(assignment);
    areas.set(assignment.area, (areas.get(assignment.area) || 0) + 1);
  }

  const sortedGroups = [...groups.entries()]
    .map(([key, group]) => {
      const [area, project] = key.split("\t");
      return { area, project, group };
    })
    .sort((a, b) => a.area.localeCompare(b.area, "de") || b.group.length - a.group.length || a.project.localeCompare(b.project, "de"));

  const oversize = sortedGroups.filter(({ group }) => group.length > maxSize);
  const lowConfidence = assignments.filter((assignment) => assignment.confidence === "low").length;
  const urlOnlyTitles = payload.items.filter((item) => /^https?:\/\//i.test(item.name.trim())).length;
  const withUrls = payload.items.filter((item) => extractUrls(item).length > 0).length;

  const markdown = [];
  markdown.push("# Things Categorization Dry Run");
  markdown.push("");
  markdown.push(`Generated: ${generatedAt}`);
  markdown.push(`Source export: ${payload.exportedAt || "unknown"}`);
  markdown.push(`Max category target: ${maxSize}`);
  markdown.push("");
  markdown.push("## Summary");
  markdown.push("");
  markdown.push(`- Open items analyzed: ${payload.items.length}`);
  markdown.push(`- Proposed Areas: ${areas.size}`);
  markdown.push(`- Proposed Projects/Categories: ${groups.size}`);
  markdown.push(`- Largest proposed category: ${Math.max(...sortedGroups.map(({ group }) => group.length))}`);
  markdown.push(`- Categories over target: ${oversize.length}`);
  markdown.push(`- Low-confidence assignments: ${lowConfidence}`);
  markdown.push(`- Items containing URLs: ${withUrls}`);
  markdown.push(`- URL-only titles: ${urlOnlyTitles}`);
  markdown.push("");
  markdown.push("## Proposed Areas");
  markdown.push("");
  for (const [area, count] of [...areas.entries()].sort((a, b) => b[1] - a[1])) {
    const projectCount = sortedGroups.filter((group) => group.area === area).length;
    markdown.push(`- ${area}: ${count} items, ${projectCount} categories`);
  }
  markdown.push("");
  markdown.push("## Categories");
  markdown.push("");
  for (const { area, project, group } of sortedGroups) {
    markdown.push(`### ${area} / ${project} (${group.length})`);
    const confidenceCounts = new Map();
    for (const assignment of group) {
      confidenceCounts.set(assignment.confidence, (confidenceCounts.get(assignment.confidence) || 0) + 1);
    }
    markdown.push("");
    markdown.push(`Confidence: ${[...confidenceCounts.entries()].map(([key, count]) => `${key} ${count}`).join(", ")}`);
    const reasons = [...new Set(group.map((assignment) => assignment.reason))].slice(0, 5);
    markdown.push(`Rules: ${reasons.join("; ")}`);
    markdown.push("");
    for (const assignment of group.slice(0, 8)) {
      const source = assignment.primaryDomain ? ` - ${assignment.primaryDomain}` : "";
      const oldLocation = [assignment.item.area, assignment.item.project].filter(Boolean).join(" / ");
      markdown.push(`- ${compact(assignment.item.name)}${source}${oldLocation ? ` (old: ${oldLocation})` : ""}`);
    }
    if (group.length > 8) {
      markdown.push(`- ... ${group.length - 8} more`);
    }
    markdown.push("");
  }

  if (oversize.length) {
    markdown.push("## Oversized Categories");
    markdown.push("");
    for (const { area, project, group } of oversize) {
      markdown.push(`- ${area} / ${project}: ${group.length}`);
    }
    markdown.push("");
  }

  const csvRows = [
    [
      "id",
      "name",
      "current_area",
      "current_project",
      "current_lists",
      "proposed_area",
      "proposed_project",
      "confidence",
      "reason",
      "primary_domain",
      "primary_url",
      "tags",
      "created",
      "modified",
    ],
  ];

  for (const assignment of assignments) {
    csvRows.push([
      assignment.item.id,
      assignment.item.name,
      assignment.item.area,
      assignment.item.project,
      assignment.item.lists.join("; "),
      assignment.area,
      assignment.project,
      assignment.confidence,
      assignment.reason,
      assignment.primaryDomain,
      assignment.primaryUrl,
      assignment.item.tags,
      assignment.item.created,
      assignment.item.modified,
    ]);
  }

  const csv = csvRows.map((row) => row.map(csvValue).join(",")).join("\n");
  const json = JSON.stringify(
    {
      generatedAt,
      sourceExportedAt: payload.exportedAt,
      maxCategorySize: maxSize,
      summary: {
        openItems: payload.items.length,
        proposedAreas: areas.size,
        proposedCategories: groups.size,
        largestCategory: Math.max(...sortedGroups.map(({ group }) => group.length)),
        oversizeCategories: oversize.length,
        lowConfidenceAssignments: lowConfidence,
        itemsContainingUrls: withUrls,
        urlOnlyTitles,
      },
      categories: sortedGroups.map(({ area, project, group }) => ({
        area,
        project,
        count: group.length,
        confidence: Object.fromEntries(
          [...group.reduce((counts, assignment) => {
            counts.set(assignment.confidence, (counts.get(assignment.confidence) || 0) + 1);
            return counts;
          }, new Map()).entries()],
        ),
        examples: group.slice(0, 10).map((assignment) => ({
          id: assignment.item.id,
          name: assignment.item.name,
          currentArea: assignment.item.area,
          currentProject: assignment.item.project,
          primaryDomain: assignment.primaryDomain,
          reason: assignment.reason,
        })),
      })),
      assignments: assignments.map((assignment) => ({
        id: assignment.item.id,
        name: assignment.item.name,
        currentArea: assignment.item.area,
        currentProject: assignment.item.project,
        currentLists: assignment.item.lists,
        proposedArea: assignment.area,
        proposedProject: assignment.project,
        confidence: assignment.confidence,
        reason: assignment.reason,
        primaryDomain: assignment.primaryDomain,
        primaryUrl: assignment.primaryUrl,
      })),
    },
    null,
    2,
  );

  fs.writeFileSync(`${outputPrefix}.md`, `${markdown.join("\n")}\n`);
  fs.writeFileSync(`${outputPrefix}.csv`, `${csv}\n`);
  fs.writeFileSync(`${outputPrefix}.json`, json);

  return {
    markdownPath: `${outputPrefix}.md`,
    csvPath: `${outputPrefix}.csv`,
    jsonPath: `${outputPrefix}.json`,
    summary: {
      openItems: payload.items.length,
      proposedAreas: areas.size,
      proposedCategories: groups.size,
      largestCategory: Math.max(...sortedGroups.map(({ group }) => group.length)),
      oversizeCategories: oversize.length,
      lowConfidenceAssignments: lowConfidence,
    },
    topAreas: [...areas.entries()].sort((a, b) => b[1] - a[1]).slice(0, 12),
  };
}

function main() {
  const inputPath = process.argv[2] || "/tmp/things-open-items.json";
  const outputDir = process.argv[3] || "reports";
  const maxSize = Number(process.argv[4] || MAX_CATEGORY_SIZE);
  const raw = JSON.parse(fs.readFileSync(inputPath, "utf8"));
  const payload = Array.isArray(raw) ? { exportedAt: "", items: raw } : raw;

  fs.mkdirSync(outputDir, { recursive: true });

  const initialAssignments = payload.items.map((item) => ({
    item,
    ...classify(item),
  }));
  const assignments = applySizeLimit(initialAssignments, maxSize);
  const outputPrefix = path.join(outputDir, `things-categorization-dry-run-${new Date().toISOString().slice(0, 10)}`);
  const result = buildReports(payload, assignments, outputPrefix, maxSize);

  console.log(JSON.stringify(result, null, 2));
}

main();
