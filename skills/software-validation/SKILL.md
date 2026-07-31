---
name: software-validation
description: >-
  Discover, execute, and report existing repository-native software checks.
  Use when asked to validate a change, run the repository's established checks
  against a change or package, run
  the applicable typecheck, static analysis, lint, format, test, benchmark,
  load, soak, stress, build, package, documentation, doctest, link,
  generated-reference, or example checks, or
  explain what validation evidence is still missing. Do not use to invent or
  install tooling, design new tests, choose architecture quality targets,
  prioritize repository improvements, or orchestrate delivery.
---

# Software Validation (superseded)

This skill is superseded by `effective-delivery`. It remains installable for one
release window so existing selections keep resolving, and it carries no
guidance of its own.

Load `effective-delivery` and take the route that absorbed this work:

> Repository Validation (references/route-validation.md)

Every reference that lived here moved with it, unchanged.

Install the successor:

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-delivery
```

## Routing Boundaries

- Route every request that previously landed here to `effective-delivery`.
- Do not answer from this stub. It states the handoff and nothing else.
