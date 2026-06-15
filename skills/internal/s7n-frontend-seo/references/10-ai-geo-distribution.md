# AI Search, GEO, and Content Distribution

Use this reference when public content must be discoverable, understandable, citable, or actionable across classic search, Google AI features, LLM search, browser agents, local/business surfaces, and partner feeds.

## Working Rules

- Treat classic SEO and AI/GEO as overlapping disciplines. The durable base is still crawlable, useful, accurate, well-linked content with clear entities and trustworthy sources.
- Do not prescribe `llms.txt`, AI text files, Markdown mirrors, chunking, or special schema.org markup as requirements for Google AI Overviews or AI Mode. Google says these are not required.
- Use structured data to clarify real visible entities and qualify for rich results. Do not add hidden facts, fake reviews, unsupported services, or speculative claims.
- Keep important facts available in visible text, not only in images, PDFs, JavaScript state, JSON-LD, or third-party widgets.
- Make the page's primary entity explicit: organization, local business, product, service, person, article, event, place, or dataset.
- Align facts across the visible page, JSON-LD, canonical URL, sitemap, Google Business Profile, Merchant Center, social profiles, review platforms, partner directories, and feeds.
- Separate crawler access for search, training, and user-triggered retrieval. Different AI companies expose different user agents and opt-out semantics.
- Treat industry GEO tactics as hypotheses until measured. Favor entity clarity, citation consistency, original information gain, and answer usefulness over manipulative AI recommendation poisoning.

## Source Classification

Use this hierarchy when turning research into skill rules:

| Source class | Examples | How to use |
| --- | --- | --- |
| Official requirements | Google Search Central, Google Business Profile API, schema.org, IndexNow, OpenAI crawler docs, Anthropic crawler docs | May change rules and checklists. |
| Official product guidance | Search Console docs, Merchant Center docs, Business Profile help, Bing Webmaster Guidelines | Use for surface-specific workflows and distribution paths. |
| Practitioner research | Aleyda Solis, Mike King/iPullRank, Lily Ray, Kevin Indig, Cindy Krum, Jason Barnard/Kalicube, Brodie Clark, Glenn Gabe, Marie Haynes, Crystal Carter, Jono Alderson | Use as review questions, experiments, and heuristics. Do not turn into ranking guarantees. |
| News/vendor commentary | GEO tool vendors, agency posts, media coverage, tool surveys | Use as market radar only. Watch for incentives and overclaiming. |

## Google AI Features

For Google AI Overviews and AI Mode, follow the normal Google Search technical requirements:

- Make pages indexable and eligible for snippets.
- Keep content helpful, reliable, and people-first.
- Keep important content in text form, with high-quality images/video where useful.
- Make structured data match visible text.
- Keep Merchant Center and Google Business Profile data current where relevant.
- Use Search Console to diagnose indexability and traffic. AI feature traffic is reported in the normal Web search type rather than as a clean standalone GEO metric.

Do not add:

- `llms.txt` as a Google AI ranking requirement,
- special "AI schema",
- hidden JSON-LD facts,
- artificial content chunking solely for Google AI,
- pages rewritten only for machines instead of users.

Use Google-Extended and preview controls only when the product goal is to limit use or display. For Search appearance, use supported controls such as `noindex`, `nosnippet`, `data-nosnippet`, and `max-snippet`; understand that recrawling can take time.

## Entity Authority

AI search and classic search both need to understand "who/what is this about?" and "why should this source be trusted?"

For organizations and local businesses:

- Create one canonical entity page for the organization and one canonical page per physical location when locations differ.
- Add visible name, legal/trading name where useful, address, phone, service area, opening hours, contact methods, leadership/authors where relevant, credentials, policies, and unique differentiators.
- Use `Organization`, `LocalBusiness`, more specific local subtypes, `WebSite`, `BreadcrumbList`, `Product`, `Service`, `Article`, `FAQPage`, `Event`, or other schema types only when they match visible content and Google eligibility.
- Use stable `@id` values in JSON-LD to connect entity references across pages.
- Use `sameAs` sparingly for profiles that unambiguously identify the same entity: Google Business Profile/Maps URL, LinkedIn, Wikidata, Crunchbase, GitHub, YouTube, or official social profiles.
- Keep entity facts consistent across citations. Mismatched names, addresses, phone numbers, service lists, categories, and opening hours reduce confidence.

Practitioner heuristic: think in entities and passages, not just keywords. Pages should make it easy to extract the answer, the source entity, the evidence, and the next action.

## Business Data Distribution

The website is the best editorial source of truth, but not automatically the operational source of truth for every surface.

For local businesses:

- Claim and verify the Google Business Profile. Google explicitly uses this for Maps, local results, and knowledge panel business facts.
- Verify the official website in Search Console.
- Show business details visibly on the site and mark them up with `LocalBusiness` structured data.
- Keep `openingHoursSpecification`, address, phone, `url`, `geo`, departments, menus, reservations, service areas, and special hours accurate.
- Update Google Business Profile directly when Maps/Knowledge Panel facts must change. Use manual updates for small operations and the Business Profile API for multi-location or CMS-driven workflows.
- For products/ecommerce, use Merchant Center feeds in addition to product pages and `Product` structured data.
- For bookings/orders, use official platform integrations where applicable, such as Reserve with Google / Maps Booking APIs, instead of assuming website markup alone creates an action surface.

Source-of-truth model:

| Data type | Preferred source of truth | Distribution |
| --- | --- | --- |
| Editorial pages | CMS/website | Sitemap, internal links, Search Console, canonical URLs, social previews. |
| Organization identity | Website entity page | Organization JSON-LD, Search Console, knowledge panel claim, sameAs profiles. |
| Local hours/address | Business profile/location data system | Website visible content, LocalBusiness JSON-LD, Google Business Profile/API, local citations. |
| Product availability/prices | Commerce/PIM | Product pages, Product JSON-LD, Merchant Center feed, partner marketplaces. |
| Documentation/API facts | Docs source repo | HTML docs, Markdown mirrors, sitemap, OpenAPI, changelog/RSS, optional llms.txt. |

## Crawling, Recrawling, and Push

- Use XML sitemaps for canonical URLs and meaningful `lastmod` values. Do not update `lastmod` when the visible content did not materially change.
- Use Search Console URL Inspection for a few important Google recrawl requests. It is not a bulk indexing API and does not guarantee instant indexing.
- Use IndexNow for participating engines such as Bing when URLs are added, updated, or deleted. IndexNow accepts single URL GET-style submissions and JSON POST batches.
- Use RSS/Atom/changelog feeds when humans, agents, or downstream systems need to monitor new content.
- For high-change data, provide APIs or feeds rather than expecting crawlers to infer every update from rendered pages.
- Use `Last-Modified`, `ETag`, and cache headers coherently so crawlers and agents can avoid unnecessary fetches.

## LLM and Agent Access

Robots and AI crawlers now have separate purposes:

- Googlebot controls Google Search crawling.
- Google-Extended can limit use in some Google AI training/grounding systems without being the same as Search indexing controls.
- OpenAI separates `OAI-SearchBot` for ChatGPT search visibility, `GPTBot` for training, and `ChatGPT-User` for user-triggered retrieval. `robots.txt` handling differs by purpose.
- Anthropic separates `ClaudeBot` for training, `Claude-SearchBot` for search, and `Claude-User` for user-triggered retrieval.

Decide crawler policy intentionally:

| Goal | Policy direction |
| --- | --- |
| Appear in AI search answers | Allow search crawlers such as Googlebot, OAI-SearchBot, Claude-SearchBot, and other desired search agents. |
| Avoid training use | Disallow training crawlers where supported, such as GPTBot or ClaudeBot, without necessarily blocking search crawlers. |
| Support user-directed agents | Avoid blocking user-triggered agents if users need agents to retrieve docs, product details, booking flows, or support content. |
| Protect private/paid content | Use authentication, noindex where appropriate, server-side access control, and clear robots policy; do not rely on `robots.txt` as security. |

## Agent-Readable Content

Agents may inspect rendered pages, DOM structure, accessibility tree, screenshots, structured data, feeds, and APIs.

Make content agent-readable by making it user-readable:

- Use semantic HTML, headings, tables, lists, labels, captions, and accessible names.
- Keep critical facts in text, not only in images, canvas, carousels, videos, or collapsed widgets.
- Put answer-ready summaries near the relevant detail, not in a disconnected FAQ dump.
- Use comparison tables when users compare options.
- Use stable IDs, canonical URLs, breadcrumbs, and internal links.
- Expose machine interfaces when the task is operational: OpenAPI specs, product feeds, event feeds, booking APIs, downloadable docs, or changelogs.
- Provide Markdown mirrors only when they help real documentation/API consumers. Treat `llms.txt` as optional discovery/radar, not as a settled search standard.

Practitioner heuristic: answer engines often need concise passages with enough context to cite. Write sections that can stand alone: claim, scope, evidence, date, entity, and action.

## Industry Heuristics Worth Testing

Use these as experiments and review questions:

- **Relevance engineering:** cover the user task, related entities, alternatives, constraints, evidence, and next steps rather than repeating one keyword.
- **Information gain:** add original data, examples, benchmarks, screenshots, prices, policies, expert commentary, or process details that competitors do not have.
- **Citation consistency:** make the same core facts appear consistently across website, profiles, feeds, PR, docs, reviews, and third-party directories.
- **Passage quality:** create sections that answer specific questions directly while linking to deeper detail.
- **Topical authority:** maintain a coherent cluster of pages that demonstrates experience in the domain, not isolated one-off posts.
- **Reputation surfaces:** monitor reviews, forums, Reddit, YouTube, industry directories, partner pages, and press mentions because LLM answers may synthesize from off-site evidence.
- **Measurement reality:** track branded AI answers manually or with tools, but expect incomplete attribution. Avoid promising clean ROI from GEO dashboards.

Avoid:

- fake third-party listicles,
- self-serving "best X" pages pretending to be neutral,
- spammed Q&A pages,
- prompt-injection text for crawlers,
- hidden entity stuffing,
- auto-generated doorway pages,
- off-site review manipulation.

These may create short-lived AI visibility but increase brand, legal, and spam risk.

## AI/GEO Review Checklist

- Is the page indexable, canonical, snippet-eligible, and internally linked?
- Is the primary entity obvious in visible content and structured data?
- Are important facts visible in text and consistent with JSON-LD?
- Are Google Business Profile, Merchant Center, Search Console, and local citations up to date where relevant?
- Does each page answer a real user task better than competing generic pages?
- Does the page include original facts or evidence worth citing?
- Are sitemaps, `lastmod`, feeds, and push mechanisms aligned with real content changes?
- Are AI/search/training/user-agent crawler policies intentional?
- Is `llms.txt` or Markdown included only because a real audience/tool uses it?
- Are measurement expectations honest: classic rankings, impressions, Search Console traffic, AI citations/mentions, referral logs, and brand accuracy checks?
