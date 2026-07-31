---
name: port-codebases
description: >-
  Plan, execute, review, and verify behavior-preserving codebase ports across
  programming languages, runtimes, frameworks, platforms, storage engines, or
  major APIs. Use when asked to rewrite or migrate an implementation while
  preserving semantics, mechanically translate a large body of code, replace a
  runtime or language, run a strangler or big-bang port, turn compiler and test
  failures into a migration queue, or organize AI-assisted porting with one or
  many agents. Scale the workflow to the available time, compute, and model
  budget without weakening correctness gates. Do not use for ordinary
  dependency bumps, small local refactors, or product redesigns disguised as a
  port.
---

# Port Codebases (superseded)

This skill is superseded by `effective-delivery`. It remains installable for one
release window so existing selections keep resolving, and it carries no
guidance of its own.

Load `effective-delivery` and take the route that absorbed this work:

> Behavior-Preserving Ports (references/route-porting.md)

Every reference that lived here moved with it, unchanged.

Install the successor:

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-delivery
```

## Routing Boundaries

- Route every request that previously landed here to `effective-delivery`.
- Do not answer from this stub. It states the handoff and nothing else.
