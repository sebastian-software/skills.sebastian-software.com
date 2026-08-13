---
name: smart-dependency-updater
description: >-
  Research, select, introduce, group, implement, validate, and publish external
  dependency changes. Use when a user asks to add or choose a package, crate,
  action, image, SDK, or other versioned dependency; update or upgrade packages;
  replace Dependabot; make Renovate smarter; group dependency updates; create
  dependency PRs; assess changelog impact; modernize dependencies and related
  code; or adopt useful new APIs.
---

# Smart Dependency Updater (superseded)

This skill is superseded by `effective-delivery`. It remains installable for one
release window so existing selections keep resolving, and it carries no
guidance of its own.

Load `effective-delivery` and take the route that absorbed this work:

> Dependency Updates (references/route-dependencies.md)

Every reference that lived here moved with it, unchanged.

Install the successor:

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-delivery
```

## Routing Boundaries

- Route every request that previously landed here to `effective-delivery`.
- Do not answer from this stub. It states the handoff and nothing else.
