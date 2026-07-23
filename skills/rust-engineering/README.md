[← Sebastian Software Skills](../../README.md)

# Rust Engineering

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Write and review Rust whose ownership, failure, concurrency, and safety
contracts remain understandable under change.**

Rust Engineering gives agents a strict but evidence-led standard for Rust
implementation and review. It favors semantic types, explicit failure and
ownership, Unicode-safe text handling, bounded concurrency, written unsafe
proofs, repository-native linting, and measured optimization over universal
thresholds or borrow-checker workarounds.

## What It Can Deliver

- Rust implementations with deliberate borrowing, consumption, and cloning
- public APIs that encode useful domain distinctions without speculative traits
- readable naming, constants, comments, and control flow
- typed error and panic boundaries with actionable context
- cancellation-aware async work, backpressure, and owned task lifecycles
- focused unsafe, FFI, and manual `Send`/`Sync` reviews
- Rust-depth review findings, grounded in edition, MSRV, features, and CI
  policy, for a code review owned by PR Review

## Use It When

Use this skill while implementing, refactoring, or reviewing Rust crates and
workspaces, especially around ownership, lifetimes, public APIs, numeric
conversion, async execution, unsafe code, or FFI.

It does not replace the owner skills for pull-request lifecycle and merge
judgment, test design, rustdoc, dependency updates, repository-wide audits,
behavior-preserving ports, or execution of existing checks.

## Example Prompts

```text
Review this Rust parser for ownership, Unicode boundaries, numeric conversion,
and public error semantics.

Refactor this async worker so concurrency, cancellation, backpressure, and
shutdown ownership are explicit.

Design a safe Rust wrapper around this C API and document the invariants that
make each unsafe operation sound.

Implement this Rust API without adding speculative traits, clone-based lifetime
workarounds, or unexplained buffer and timeout values.
```

See [SKILL.md](SKILL.md) for the workflow, operating rules, and routing
boundaries.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill rust-engineering
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian rust-engineering
dalo approve skill sebastian:rust-engineering
dalo sync
```

## Related Skills

- [PR Review](../pr-review/README.md) owns pull-request lifecycle, approval, CI
  recovery, and merge judgment; this skill supplies the Rust-depth findings
  inside a review.
- [Software Testing](../software-testing/README.md) owns focused Rust test design
  and implementation against the contracts established here.
- [Tech Docs](../tech-docs/README.md) owns rustdoc, examples, and contributor
  documentation.
- [Software Validation](../software-validation/README.md) discovers and runs
  the repository's established Rust checks.
- [Smart Dependency Updater](../smart-dependency-updater/README.md) owns crate
  selection, feature changes, and version updates.
- [Port Codebases](../port-codebases/README.md) owns behavior-preserving moves
  into or out of Rust.

## Scope

This skill does not impose one async runtime, error crate, test library, lint
set, MSRV, edition, allocation strategy, or performance threshold. It does not
authorize unrelated cleanup, dependency additions, public API breaks, or unsafe
optimizations.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
