---
name: decision-records
description: >-
  Create, review, update, supersede, and audit Architecture Decision Records
  (ADRs) for durable project decisions. Use when a user asks for an ADR,
  decision log, architecture decision, design decision, communication or brand
  voice decision, or recorded rationale; when a cross-cutting technical,
  product, design, content, marketing, security, operational, or process choice
  must remain understandable across people, tools, and agent sessions; or when
  experienced judgment and explicit analysis conflict in a durable decision; or
  when another skill identifies a decision whose undocumented rationale would
  otherwise drift. Preserve existing repository conventions and do not create
  skill-specific dot folders or private memory formats.
---

# Decision Records (superseded)

This skill is superseded by `effective-product`. It remains installable for one
release window so existing selections keep resolving, and it carries no guidance
of its own.

Load `effective-product` and take the route that absorbed this work:

> Decision Records (references/route-decisions.md)

Every reference that lived here moved with it, unchanged.

Install the successor:

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-product
```

## Routing Boundaries

- Route every request that previously landed here to `effective-product`.
- Do not answer from this stub. It states the handoff and nothing else.
