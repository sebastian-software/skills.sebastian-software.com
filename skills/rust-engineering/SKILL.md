---
name: rust-engineering
description: >-
  Implement, refactor, and review Rust crates and workspaces with explicit
  architecture, ownership, API, error, concurrency, unsafe, memory, and
  performance contracts. Use for Rust source changes, Cargo projects,
  lifetime or cloning decisions, public Rust APIs, crate/workspace boundaries,
  async Rust, unsafe code, FFI, allocation and data-layout choices, profiling,
  SIMD, atomics, parallelism, numeric conversions, or Rust-depth findings
  inside a code review that pr-review owns. Do not use for behavior-preserving
  ports, dependency-only updates, test-only work, documentation-only work, or
  merely running existing repository checks when a narrower skill owns the task.
---

# Rust Engineering (superseded)

This skill is superseded by `effective-engineering`. It remains installable for one
release window so existing selections keep resolving, and it carries no
guidance of its own.

Load `effective-engineering` and take the route that absorbed this work:

> Rust Engineering (references/route-rust.md) and its architecture,
> performance, and unsafe siblings

Every reference that lived here moved with it, unchanged.

Install the successor:

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-engineering
```

## Routing Boundaries

- Route every request that previously landed here to `effective-engineering`.
- Do not answer from this stub. It states the handoff and nothing else.
