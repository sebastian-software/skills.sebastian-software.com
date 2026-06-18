# AI Search, GEO, and Content Distribution

Use this reference when public content must be discoverable, understandable, citable, or actionable across classic search, Google AI features, LLM search, browser agents, local/business surfaces, and partner feeds.

The durable base is the same as classic SEO: crawlable, useful, accurate, well-linked content with clear entities and trustworthy sources. AI/GEO adds entity clarity, source consistency, extractable passages, and intentional crawler policy on top of that base — it does not replace it. Weight official guidance from search and AI providers over vendor or agency claims; treat evolving AI-search tactics as hypotheses to measure, not settled ranking rules.

## Working Rules

- Treat classic SEO and AI/GEO as overlapping disciplines built on the same crawlable, useful, accurate, well-linked content.
- Do not prescribe `llms.txt`, AI text files, Markdown mirrors, content chunking, or special schema.org markup as requirements for Google AI Overviews or AI Mode. Google says these are not required.
- Use structured data to clarify real visible entities and qualify for rich results. Do not add hidden facts, fake reviews, unsupported services, or speculative claims.
- Keep important facts in visible text, not only in images, PDFs, JavaScript state, JSON-LD, or third-party widgets.
- Make the page's primary entity explicit: organization, local business, product, service, person, article, event, place, or dataset.
- Align facts across the visible page, JSON-LD, canonical URL, sitemap, Google Business Profile, Merchant Center, social profiles, review platforms, partner directories, and feeds.
- Separate crawler access for search, training, and user-triggered retrieval. Different AI providers expose different user agents and opt-out semantics.
- Favor entity clarity, citation consistency, original information gain, and answer usefulness over manipulative AI recommendation tactics. Measure GEO claims before trusting them.

## Google AI Features

For Google AI Overviews and AI Mode, follow the normal Google Search technical requirements:

- Make pages indexable and eligible for snippets.
- Keep content helpful, reliable, and people-first.
- Keep important content in text form, with high-quality images and video where useful.
- Make structured data match visible text.
- Keep Merchant Center and Google Business Profile data current where relevant.
- Use Search Console to diagnose indexability and traffic. AI feature traffic is reported under the normal Web search type, not as a standalone GEO metric.

Do not add the following as Google AI ranking requirements:

- `llms.txt`,
- special "AI schema",
- hidden JSON-LD facts,
- content chunking solely for Google AI,
- pages rewritten only for machines instead of users.

Use Google-Extended and preview controls only when the goal is to limit AI use or display. For search appearance, use supported controls such as `noindex`, `nosnippet`, `data-nosnippet`, and `max-snippet`, and expect recrawling to take time.

## Entity Authority

AI search and classic search both need to answer "who or what is this about?" and "why should this source be trusted?"

For organizations and local businesses:

- Create one canonical entity page for the organization, and one canonical page per physical location when locations differ.
- Show visible name, legal or trading name where useful, address, phone, service area, opening hours, contact methods, authors or leadership where relevant, credentials, policies, and unique differentiators.
- Use `Organization`, `LocalBusiness`, more specific local subtypes, `WebSite`, `BreadcrumbList`, `Product`, `Service`, `Article`, `FAQPage`, `Event`, or other schema types only when they match visible content and Google eligibility.
- Use stable `@id` values in JSON-LD to connect entity references across pages.
- Use `sameAs` only for profiles that unambiguously identify the same entity, such as the Google Business Profile or Maps URL, LinkedIn, Wikidata, Crunchbase, GitHub, YouTube, or official social profiles.
- Keep entity facts consistent across citations. Mismatched names, addresses, phone numbers, service lists, categories, and opening hours reduce confidence.

Think in entities and passages, not only keywords. Pages should make it easy to extract the answer, the source entity, the supporting evidence, and the next action.

## Business Data Distribution

The website is the best editorial source of truth, but not automatically the operational source of truth for every surface.

For local businesses:

- Claim and verify the Google Business Profile. Google uses it directly for Maps, local results, and knowledge panel business facts.
- Verify the official website in Search Console.
- Show business details visibly on the site and mark them up with `LocalBusiness` structured data.
- Keep `openingHoursSpecification`, address, phone, `url`, `geo`, departments, menus, reservations, service areas, and special hours accurate.
- Update the Google Business Profile directly when Maps or knowledge panel facts must change. Use manual updates for small operations and the Business Profile API for multi-location or CMS-driven workflows.
- For products and ecommerce, use Merchant Center feeds in addition to product pages and `Product` structured data.
- For bookings and orders, use official platform integrations such as Reserve with Google or Maps Booking APIs rather than assuming page markup alone creates an action surface.

Source-of-truth model:

| Data type | Preferred source of truth | Distribution |
| --- | --- | --- |
| Editorial pages | CMS/website | Sitemap, internal links, Search Console, canonical URLs, social previews |
| Organization identity | Website entity page | Organization JSON-LD, Search Console, knowledge panel claim, `sameAs` profiles |
| Local hours/address | Business profile/location data system | Website visible content, LocalBusiness JSON-LD, Google Business Profile/API, local citations |
| Product availability/prices | Commerce/PIM | Product pages, Product JSON-LD, Merchant Center feed, partner marketplaces |
| Documentation/API facts | Docs source repo | HTML docs, sitemap, OpenAPI, changelog/RSS, optional Markdown mirrors |

## Crawling, Recrawling, and Push

- Use XML sitemaps for canonical URLs with meaningful `lastmod` values. Do not bump `lastmod` when the visible content did not materially change.
- Use Search Console URL Inspection for a few important Google recrawl requests. It is not a bulk indexing API and does not guarantee instant indexing.
- Use IndexNow for participating engines such as Bing when URLs are added, updated, or deleted. IndexNow accepts single-URL submissions and JSON POST batches.
- Use RSS, Atom, or changelog feeds when humans, agents, or downstream systems need to monitor new content.
- For high-change data, provide APIs or feeds rather than expecting crawlers to infer every update from rendered pages.
- Set `Last-Modified`, `ETag`, and cache headers coherently so crawlers and agents can avoid unnecessary fetches.

## LLM and Agent Access

Search and AI crawlers now serve separate purposes, and policy should be set per purpose:

- Googlebot controls Google Search crawling.
- Google-Extended can limit use in some Google AI training and grounding systems without being the same as Search indexing controls.
- OpenAI separates `OAI-SearchBot` for ChatGPT search visibility, `GPTBot` for training, and `ChatGPT-User` for user-triggered retrieval, with `robots.txt` handling that differs by purpose.
- Anthropic separates `ClaudeBot` for training, `Claude-SearchBot` for search, and `Claude-User` for user-triggered retrieval.

Decide crawler policy intentionally:

| Goal | Policy direction |
| --- | --- |
| Appear in AI search answers | Allow search crawlers such as Googlebot, `OAI-SearchBot`, and `Claude-SearchBot` |
| Avoid training use | Disallow training crawlers where supported, such as `GPTBot` or `ClaudeBot`, without necessarily blocking search crawlers |
| Support user-directed agents | Avoid blocking user-triggered agents when users need them to retrieve docs, product details, booking flows, or support content |
| Protect private or paid content | Use authentication, `noindex` where appropriate, and server-side access control; do not rely on `robots.txt` as security |

## Agent-Readable Content

Agents may inspect rendered pages, DOM structure, the accessibility tree, screenshots, structured data, feeds, and APIs. The most reliable way to make content agent-readable is to make it user-readable.

- Use semantic HTML, headings, tables, lists, labels, captions, and accessible names.
- Keep critical facts in text, not only in images, canvas, carousels, videos, or collapsed widgets.
- Put answer-ready summaries near the relevant detail, not in a disconnected FAQ dump.
- Use comparison tables when users compare options.
- Use stable IDs, canonical URLs, breadcrumbs, and internal links.
- Expose machine interfaces when the task is operational: OpenAPI specs, product feeds, event feeds, booking APIs, downloadable docs, or changelogs.
- Provide Markdown mirrors only when real documentation or API consumers use them. Treat `llms.txt` as optional discovery, not a settled search standard.

Answer engines often need concise passages with enough context to cite. Write sections that can stand alone: claim, scope, evidence, date, entity, and action.

## Tactics Worth Testing

Treat these as experiments and review questions rather than ranking guarantees:

- Relevance coverage: address the user task, related entities, alternatives, constraints, evidence, and next steps instead of repeating one keyword.
- Information gain: add original data, examples, benchmarks, screenshots, prices, policies, expert commentary, or process detail that competitors lack.
- Citation consistency: make the same core facts appear consistently across website, profiles, feeds, PR, docs, reviews, and third-party directories.
- Passage quality: write sections that answer specific questions directly while linking to deeper detail.
- Topical authority: maintain a coherent cluster of pages that demonstrates real experience, not isolated one-off posts.
- Reputation surfaces: monitor reviews, forums, video, industry directories, partner pages, and press mentions, because AI answers may synthesize from off-site evidence.
- Measurement reality: track branded AI answers manually or with tools, but expect incomplete attribution. Do not promise clean ROI from GEO dashboards.

Avoid tactics that create short-lived AI visibility but increase brand, legal, and spam risk:

- fake third-party listicles,
- self-serving "best X" pages posing as neutral,
- spammed Q&A pages,
- prompt-injection text aimed at crawlers,
- hidden entity stuffing,
- auto-generated doorway pages,
- off-site review manipulation.

## AI/GEO Review Checklist

- Is the page indexable, canonical, snippet-eligible, and internally linked?
- Is the primary entity obvious in visible content and structured data?
- Are important facts visible in text and consistent with JSON-LD?
- Are Google Business Profile, Merchant Center, Search Console, and local citations up to date where relevant?
- Does each page answer a real user task better than competing generic pages?
- Does the page include original facts or evidence worth citing?
- Are sitemaps, `lastmod`, feeds, and push mechanisms aligned with real content changes?
- Are search, training, and user-agent crawler policies intentional?
- Is `llms.txt` or a Markdown mirror included only because a real audience or tool uses it?
- Are measurement expectations honest across classic rankings, impressions, Search Console traffic, AI citations and mentions, referral logs, and brand accuracy checks?
