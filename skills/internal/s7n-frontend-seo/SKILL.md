---
name: s7n-frontend-seo
description: |
  Frontend SEO, metadata, titles, descriptions, canonical URLs, structured data, Open Graph, Twitter cards, robots hints, favicons, indexability, and content-rendering checks. Use when building or reviewing public pages that need search/social previews or crawlable frontend output.
license: MIT
metadata:
  author: sebastian-software
  version: "1.0"
---

# S7N Frontend SEO

Use this skill for the frontend details that make public pages understandable to search engines, link previews, and users before they click.

## Workflow

1. Identify page intent, canonical URL, primary entity, and target preview text.
2. Set title, description, canonical, robots behavior, and social metadata.
3. Add structured data only when it accurately represents visible page content.
4. Verify crawlable rendered content, heading structure, image alt text, and internal links.
5. Check previews and indexability after implementation.

## Rules

- Metadata must describe the actual page, not a generic product promise.
- Avoid duplicate titles and descriptions across important pages.
- Structured data must not invent claims or hidden content.
- Public pages need meaningful server-rendered or reliably rendered content.
- Performance, accessibility, and content clarity are SEO inputs.

## References

- [references/09-seo.md](references/09-seo.md) - frontend SEO metadata, structured data, and implementation checks.
