---
name: issue-autopilot
description: >-
  Autonomously operate an unspecified GitHub or Linear issue queue: discover the
  authoritative tracker, rank open or unassigned work, select targets, delegate
  isolated implementations, reconcile queue-owned PRs, or monitor incoming issues.
  Use only when the user delegates issue selection, asks to process a backlog or
  monitor incoming work, or continues work already claimed by this autopilot. Do
  not use for a newly requested specific issue, finite list of issue identifiers,
  issue URL, exact issue title, or specific PR, even when the request says to fix,
  implement, investigate, review, or process it. Those are targeted workflows, not
  issue-autopilot.
---

# Issue Autopilot (superseded)

This skill is superseded by `effective-delivery`. It remains installable for one
release window so existing selections keep resolving, and it carries no guidance
of its own.

Load `effective-delivery` and take the route that absorbed this work:

> Issue Queue Autopilot (references/route-issue-autopilot.md)

Every reference and helper that lived here moved with it.

Install the successor:

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-delivery
```

## Routing Boundaries

- Route every request that previously landed here to `effective-delivery`.
- Do not answer from this stub. It states the handoff and nothing else.
