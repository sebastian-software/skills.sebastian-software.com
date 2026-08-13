---
name: software-architecture
description: >-
  Assess, design, review, and evolve general software architecture with
  explicit system boundaries, responsibilities, data and integration contracts,
  quality attributes, operational concerns, and migration paths. Use when a
  user asks for software or system architecture, architecture options or
  review, service or module boundaries, build-versus-buy or strategic-control
  decisions, monolith versus service decisions, scalability, reliability,
  deployability, operational readiness, performance objectives, load, soak, or
  stress objectives, workload scenarios, and capacity decisions, or
  non-frontend testing-strategy design such as the test pyramid, coverage
  goals, and which risks get which test types. Apply
  Twelve-Factor practices where they fit a long-running service; do not use for
  frontend-only architecture, codebase audit-only work, implementation plans,
  execution of an existing repository check, or recording an already-made
  decision when a narrower skill applies.
---

# Software Architecture (superseded)

This skill is superseded by `effective-engineering`. It remains installable for one
release window so existing selections keep resolving, and it carries no
guidance of its own.

Load `effective-engineering` and take the route that absorbed this work:

> Software Architecture (references/route-architecture.md)

Every reference that lived here moved with it, unchanged.

Install the successor:

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-engineering
```

## Routing Boundaries

- Route every request that previously landed here to `effective-engineering`.
- Do not answer from this stub. It states the handoff and nothing else.
