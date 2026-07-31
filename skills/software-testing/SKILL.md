---
name: software-testing
description: >-
  Design, implement, diagnose, and verify focused non-frontend software tests
  for services, APIs, databases, async work, CLIs, and Rust. Use when asked
  to protect a behavior, invariant, regression, failure path, retry,
  authorization rule, migration, command-line contract, or flaky test; to
  diagnose test discovery, collection, runner, or framework configuration; to
  make a rule or state transition directly testable; to add a focused
  performance-regression guard; or to design, repair, or interpret a
  repository-native microbenchmark, comparative benchmark, or bounded
  end-to-end workflow benchmark. Prefer repository-native test conventions and
  real behavior over mock choreography. For browser, component, or React tests
  use effective-web. Do not use for visual, accessibility, or browser E2E
  testing; repository-wide coverage audits; testing-strategy design (use
  software-architecture); or load, soak, stress, and capacity methodology.
---

# Software Testing (superseded)

This skill is superseded by `effective-engineering`. It remains installable for one
release window so existing selections keep resolving, and it carries no
guidance of its own.

Load `effective-engineering` and take the route that absorbed this work:

> Focused Testing (references/route-testing.md) and Benchmark Methodology
> (references/route-benchmarks.md)

Every reference that lived here moved with it, unchanged.

Install the successor:

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-engineering
```

## Routing Boundaries

- Route every request that previously landed here to `effective-engineering`.
- Do not answer from this stub. It states the handoff and nothing else.
