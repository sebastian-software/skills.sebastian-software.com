---
name: s7n-frontend-seo
description: |
  Frontend SEO, AI search/GEO, metadata, titles, descriptions, canonical URLs, structured data, Open Graph, Twitter cards, robots hints, favicons, indexability, content-rendering checks, entity clarity, business details, LLM crawler access, and content distribution. Use when building or reviewing public pages that need search/social previews, crawlable frontend output, AI Overview/AI Mode eligibility, ChatGPT/Claude search visibility, local/business profile consistency, or agent-readable content.
license: MIT
metadata:
  author: sebastian-software
  version: "1.0"
---

# S7N Frontend SEO

Use this skill for the frontend details that make public pages understandable to search engines, AI search systems, link previews, agents, and users before they click.

## Workflow

1. Identify page intent, canonical URL, primary entity, target audience, search surface, and target preview text.
2. Set title, description, canonical, robots behavior, social metadata, and discovery links.
3. Add structured data only when it accurately represents visible page content.
4. Verify crawlable rendered content, heading structure, image alt text, internal links, and entity consistency.
5. For AI/GEO work, separate Google Search requirements from broader LLM/agent discovery and crawler-control choices.
6. For local/business facts, define the source of truth and sync path across website, structured data, Google Business Profile, Merchant Center, feeds, APIs, and third-party citations.
7. Check previews, indexability, business profiles, and distribution channels after implementation.

## Rules

- Metadata must describe the actual page, not a generic product promise.
- Avoid duplicate titles and descriptions across important pages.
- Structured data must not invent claims or hidden content.
- Public pages need meaningful server-rendered or reliably rendered content.
- Performance, accessibility, and content clarity are SEO inputs.
- Google generative search does not require `llms.txt`, AI text files, special Markdown, or special schema.org markup; do not prescribe them as Google ranking requirements.
- AI/GEO work should improve extractable facts, entity clarity, source consistency, and crawl/access policy instead of chasing unverified prompt-injection or keyword-stuffing tactics.
- Use `llms.txt`, Markdown mirrors, feeds, APIs, or OpenAPI descriptions only when they serve real agent/developer retrieval needs outside Google Search, and label them as optional/radar where standards are not settled.
- Keep business facts consistent across visible page content, JSON-LD, Search Console, Google Business Profile, Merchant Center, social profiles, review sites, and local citations.

## References

- [references/09-seo.md](references/09-seo.md) - frontend SEO metadata, structured data, and implementation checks.
- [references/10-ai-geo-distribution.md](references/10-ai-geo-distribution.md) - AI search/GEO, entity authority, business data distribution, LLM crawler access, and agent-readable content.
