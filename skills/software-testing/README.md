[← Sebastian Software Skills](../../README.md)

# Software Testing

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Turn a concrete software risk into focused, trustworthy test evidence.**

Software Testing helps agents design and implement non-frontend tests for the
behavior that actually matters: service rules, API contracts, data boundaries,
async failure paths, command-line behavior, Rust public APIs, and regressions.
It starts from the repository's established test stack and makes important
logic directly testable before reaching for a mock.

## What It Can Deliver

- focused regression tests for authorization, validation, idempotency, and
  state-transition defects
- real-boundary evidence for databases, RLS, migrations, transactions, tenant
  isolation, service contracts, and integration behavior
- deterministic tests for timeouts, cancellation, retries, queues, callbacks,
  concurrency, and flaky tests
- CLI evidence for configuration precedence, stdout and stderr, exit status,
  working-directory and filesystem effects
- Rust unit, integration, public-API, doctest, replay, property, snapshot, and
  opt-in live-smoke test decisions that fit the crate's existing conventions
- small production-code extractions that make rules and state transitions
  directly testable without disguising a broad architectural rewrite
- focused performance-regression guards for a concrete function or service
  path against an explicit target
- reproducible microbenchmarks, semantically fair implementation comparisons,
  bounded end-to-end workflow benchmarks, and reviewable performance claims

## Use It When

Use this skill when a specific non-frontend behavior needs protection or a test
is unreliable: a service must not repeat a side effect after a timeout; a
migration must enforce a tenant boundary; a CLI must separate diagnostic output
from machine-readable output; a Rust client must replay protocol messages
deterministically; or a mock graph suggests that the code's decision mechanism
is inaccessible.

## Example Prompts

```text
Add a regression test for this API authorization bug using the repository's
real data and auth harness; do not replace the handler with mocks.

This retry sometimes duplicates an external side effect after a timeout.
Make the behavior deterministic and add the narrowest protective test.

Test this CLI's configuration precedence, stdout/stderr separation, exit
status, and filesystem behavior using the project-native test seam.

This Rust client test is flaky because callback ordering changes. Diagnose the
cause and make a deterministic replay-based test without requiring a live key.

Repair this comparative benchmark so both parsers perform the same semantics,
then retain enough repeated evidence and environment provenance for review.
```

See [SKILL.md](SKILL.md) for the workflow, evidence routes, double discipline,
and ownership boundaries.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill software-testing
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian software-testing
dalo approve skill sebastian:software-testing
dalo sync
```

## Related Skills

- [Effective Workflow](../effective-workflow/README.md) coordinates a wider
  change and hands focused non-frontend regression or invariant evidence to
  this skill.
- [Effective Web](../effective-web/README.md) owns browser, component, visual,
  accessibility, and browser E2E test depth, as well as frontend test strategy.
- [Software Validation](../software-validation/README.md) runs existing
  repository-native test and quality commands; this skill designs or repairs
  the test evidence itself.
- [Codebase Improvement](../codebase-improvement/README.md) investigates
  cross-cutting behavior and audits broad test risk; this skill owns focused
  test-suite diagnosis, test design, and implementation.
- [PR Review](../pr-review/README.md) judges whether a pull request has enough
  evidence to merge; this skill designs and implements the test evidence.
- [Software Architecture](../software-architecture/README.md) owns
  testing-strategy design, system contracts, quality scenarios, workload
  scenarios, performance targets, capacity, and broader redesign; this skill
  tests an agreed strategy or contract and owns repository-native benchmark
  methodology for a named question.
- [Port Codebases](../port-codebases/README.md) owns behavior parity and
  compatibility evidence across a port.

## Scope

This skill owns non-frontend test design, implementation, focused verification,
and the smallest production-code restructuring needed to expose a cohesive
mechanism. TypeScript and Rust are the primary ecosystems; other stacks get
standard-practice, convention-following depth rather than a prescribed
framework or toolchain. It does not prescribe Jest, Vitest, pytest,
cargo-nextest, rstest, proptest, mockall, Playwright, an assertion count, a
coverage percentage, or a strict TDD ritual. It does not own browser testing,
repository-wide audits, testing-strategy design and contract design (owned by
Software Architecture), load, soak, stress, and capacity methodology (no
first-party owner; benchmarks here are repository-native comparative
measurements), broad architectural change, or commits and delivery
orchestration. The evidence-led ownership split is recorded in
[ADR 0001](https://github.com/sebastian-software/skills.sebastian-software.com/blob/main/docs/adr/0001-performance-testing-ownership.md).

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
