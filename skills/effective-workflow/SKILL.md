---
name: effective-workflow
description: >-
  Coordinate multi-stage or mixed-domain software work from an unclear request
  through an authorized change, focused verification, and a review-ready
  handoff. Use when a task spans diagnosis, implementation, validation, review,
  or delivery and needs sequencing across repository-native workflows and
  first-party specialist skills. Prefer the matching specialist directly for
  an already narrow documentation, dependency, test, review, architecture,
  port, or frontend request.
---

# Effective Workflow (superseded)

This skill is superseded by `effective-delivery`. It remains installable for one
release window so existing selections keep resolving, and it carries no
guidance of its own.

Load `effective-delivery` and take the route that absorbed this work:

> Workflow Orchestration (references/route-orchestration.md)

Every reference that lived here moved with it, unchanged.

Install the successor:

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-delivery
```

## Routing Boundaries

- Route every request that previously landed here to `effective-delivery`.
- Do not answer from this stub. It states the handoff and nothing else.
