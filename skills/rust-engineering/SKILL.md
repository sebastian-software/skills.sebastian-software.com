---
name: rust-engineering
description: >-
  Implement, refactor, and review Rust crates and workspaces with explicit
  ownership, API, error, concurrency, unsafe, and maintainability contracts.
  Use for Rust source changes, Cargo projects, lifetime or cloning decisions,
  public Rust APIs, async Rust, unsafe code, FFI, numeric conversions, or a
  Rust-specific code review. Do not use for behavior-preserving ports,
  dependency-only updates, test-only work, documentation-only work, or merely
  running existing repository checks when a narrower skill owns the task.
---

# Rust Engineering

Write Rust that makes ownership, failure, concurrency, and safety understandable
to the next maintainer. Prefer repository evidence and semantic types over
universal thresholds, clever compression, or speculative optimization.

## Establish the Contract

1. Read scoped instructions, `Cargo.toml`, workspace configuration, CI, lint
   policy, formatting configuration, relevant ADRs, public APIs, nearby tests,
   and representative call sites. Discover the edition, MSRV, supported targets,
   feature combinations, async runtime, and repository-native commands.
2. State the changed behavior and boundaries: inputs, outputs, ownership,
   mutation, expected errors, possible panics, cancellation, ordering,
   concurrency, resource limits, and any safety invariant. Do not invent a
   stronger MSRV, lint set, runtime, crate, or performance target.
3. Read [Ownership and API design](references/ownership-and-api-design.md) for
   borrowing, newtypes, parsing, trait boundaries, and abstraction choices.
4. Read [Naming and readability](references/naming-and-readability.md) for
   semantic names, Unicode-safe text handling, constants, comments, and
   maintainable control flow.
5. Read [Errors and concurrency](references/errors-and-concurrency.md) when the
   change can fail, panic, spawn work, block, hold a lock, or be cancelled.
6. Read [Unsafe and FFI](references/unsafe-and-ffi.md) for every unsafe block,
   unsafe trait implementation, raw pointer, foreign call, or ABI boundary.
7. Read [Quality and review](references/quality-and-review.md) before declaring
   the change ready. Route focused test design to `software-testing`, technical
   documentation to `tech-docs`, and execution of established checks to
   `software-validation`.

## Implementation Rules

- Make invalid states difficult to represent when the domain distinction is
  stable and valuable. Do not replace every primitive with a wrapper.
- Borrow when the callee only observes data, consume when ownership transfer is
  meaningful, and clone only when the duplicate ownership is intentional.
- Use types and names to carry units, identity, state, and ownership. Replace a
  repeated or policy-bearing literal with a named constant or configuration;
  keep an obvious local literal local when naming it adds no meaning.
- Return `Result` for expected failure. Panic only for a programmer error or a
  locally proven invariant, and make that proof recoverable from code,
  documentation, or a focused assertion message.
- Keep public interfaces smaller than their implementation burden, but add a
  trait, generic, macro, or adapter only for demonstrated variation or reuse.
- Preserve readable control flow. Prefer explicit matches and small helpers when
  combinator chains obscure error, ownership, or early-return behavior.
- Profile before optimizing. Do not choose integer widths, collection layouts,
  boxing, inlining, LTO, allocation strategies, or copying thresholds from a
  generic size rule.
- Scope suppressions narrowly. Explain why a local `allow`, `expect`, unsafe
  operation, or manual `Send`/`Sync` is sound and when it can be removed.

## Review Output

For a review, report only findings that can affect correctness, safety,
compatibility, performance, or maintainability. Tie each finding to a concrete
path and contract, distinguish a verified defect from a risk or preference, and
propose the smallest correction consistent with repository conventions.

For an implementation, summarize the ownership and failure decisions, name the
focused evidence run, and state unverified feature, platform, unsafe, or
performance claims explicitly.

## Routing Boundaries

- Route language, runtime, framework, or API ports to `port-codebases`; use this
  skill for Rust quality inside an already selected Rust implementation.
- Route test selection and implementation to `software-testing`; this skill owns
  the Rust contracts the tests must protect.
- Route rustdoc and contributor documentation to `tech-docs`.
- Route crate selection and version updates to `smart-dependency-updater`.
- Route existing format, lint, build, test, Miri, sanitizer, fuzz, or benchmark
  command execution to `software-validation`.
- Route repository-wide audits and implementation plans to
  `codebase-improvement`.

Do not turn this skill into a parallel test, documentation, dependency, or
delivery system.
