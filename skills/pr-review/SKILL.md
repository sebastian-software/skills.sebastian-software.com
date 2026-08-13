---
name: pr-review
description: >-
  Review and maintain pull requests across GitHub, GitLab, Forgejo, Gitea, and
  other providers: inspect PRs, approve or request changes, handle feedback,
  fix valid findings, recover CI, keep branches current, or review
  caller-supplied context without taking provider action. Use when a user asks
  to review PRs, catch up on review work, maintain their own PRs, names a PR,
  requests a dry run, or delegates review analysis while retaining approval
  and delivery authority.
---

# PR Review (superseded)

This skill is superseded by `effective-delivery`. It remains installable for one
release window so existing selections keep resolving, and it carries no
guidance of its own.

Load `effective-delivery` and take the route that absorbed this work:

> PR Review and Upkeep (references/route-review.md)

Every reference that lived here moved with it, unchanged.

Install the successor:

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-delivery
```

## Routing Boundaries

- Route every request that previously landed here to `effective-delivery`.
- Do not answer from this stub. It states the handoff and nothing else.
