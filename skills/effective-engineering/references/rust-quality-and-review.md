# Rust Quality, Review, and Test Evidence

Use this reference for Rust-specific repository quality, review, test placement,
feature coverage, and readiness evidence. The Testing route still owns the
general choice among examples, properties, snapshots, replays, integration
boundaries, and doubles; use [Select test evidence](select-test-evidence.md)
when that choice is the task.

## Review the Repository Contract First

Use the repository's edition, MSRV, feature policy, formatting, lint groups,
deny/allow policy, target matrix, and validation commands. Do not add
`#![deny(warnings)]`, enable every Clippy group, migrate editions, or install a
tool as incidental cleanup.

Inspect the narrow changed crate and its downstream public surface:

- API and semver compatibility, feature-gated behavior, and auto traits;
- ownership, borrowing, cloning, allocation, and drop timing;
- expected errors, panic paths, error context, and partial state;
- overflow, casts, indexing, Unicode boundaries, and platform widths;
- cancellation, task lifetime, backpressure, locks, and ordering;
- unsafe invariants, FFI contracts, and cleanup;
- suppressions, TODO implementations, debug-only checks, and release behavior.

## Place Test Evidence at the Right Visibility

Select placement from the claim and the crate's current conventions:

- Put unit tests in the source module when they protect module-local behavior,
  private invariants, parsing, transformation, or state transitions. Keep them
  close to the code whose contract they explain.
- Put integration tests in the crate's `tests/` directory when the public API,
  crate wiring, feature combination, or externally observable behavior is the
  claim. Treat that directory as a consumer and use public APIs rather than
  reaching into private implementation details.
- Use doctests for concise public examples that are part of the API contract and
  should keep compiling. Keep setup small; do not force a doctest to exercise
  credentials, timing, or a multi-process environment.

Prefer the repository's existing layout, feature gates, test helpers, async
runtime setup, and commands. Rust does not require a particular test crate,
property library, snapshot library, or runner to make these distinctions useful.

## Protect Public Behavior and Failure Semantics

For a public client, protocol, parser, or library, protect the caller-visible
contract: returned values, errors, cancellation or timeout behavior, message
ordering, feature availability, and state after failure. Use deterministic
transport fixtures or replays when protocol sequencing is the risk. Keep an
irreducible mock at the outer transport boundary and document why a replay,
local implementation, or focused integration path cannot provide the evidence.

Use values and type-safe helpers that make identity, time, and expected state
obvious. Do not test borrow layout, private helper calls, or incidental
allocation choices unless they are explicitly part of the supported contract.

Select Rust-specific boundary evidence from the demonstrated risk:

- exercise minimum, maximum, sign, narrowing, and overflow behavior when
  arithmetic or conversion is part of the contract;
- exercise cancellation at meaningful await boundaries and verify owned state,
  cleanup, retry safety, and task shutdown;
- cover supported feature combinations and `cfg` branches that change public
  behavior rather than assuming the default feature set represents the crate;
- use property tests, fuzzing, Miri, sanitizers, or concurrency exploration only
  when the repository supports the tool and the risk justifies it; the Rust
  routes own the unsafe and FFI proof discipline those tools verify.

Do not add a property, snapshot, mock, async, or unsafe-testing dependency by
default. A focused example or table-driven test is often the clearest evidence.
Keep one coherent behavior together when several related assertions make the
protected contract more visible and failures remain diagnosable.

## Keep Live Smoke Tests Deliberately Opt-In

Credentialed, billable, remote, destructive, or flaky live checks are smoke
evidence only when clearly gated by the repository's existing mechanism: an
explicit environment flag, ignored-test convention, dedicated CI job, or
separate command. Fail clearly when an opted-in environment is incomplete;
never make ordinary local or CI test runs depend on a secret or live account.

Report deterministic local evidence separately from optional live evidence.
The normal suite should still protect behavior through direct tests, fixtures,
local services, or replays.

## Keep Suppressions Local

Fix a lint when it reveals unclear or unsafe code. When the lint does not fit,
scope `allow` or `expect` to the smallest item, state why the exception is
correct, and use the repository's preferred mechanism. Never silence a lint
group across a crate simply to make a changed line pass.

Treat Clippy as a reviewer, not an oracle. A suggestion that changes ownership,
precision, public compatibility, allocation, or readability needs the same
reasoning as a handwritten refactor.

## Optimize from Evidence

State the performance claim and measurement boundary before changing code.
Measure a representative workload using the repository's existing benchmark or
profiling setup. Check whether the cost is algorithmic, I/O, synchronization,
allocation, copying, cache behavior, or build configuration before selecting a
mechanism.

Do not use object size alone to mandate `Copy`, references, boxing, smaller
integers, `f32`, small-vector containers, LTO, codegen units, panic strategy, or
inlining. Include correctness, precision, compile time, binary size, platform,
and maintenance tradeoffs.

## Produce Decisive Evidence

Start with formatting or type/lint checks for the changed crate, then focused
tests at the visibility that matches the claim, and the nearest public consumer.
Expand to feature combinations, workspace checks, supported targets, release
mode, doctests, or specialized unsafe/concurrency tools when the claim requires
them.

Report exact commands and outcomes through `effective-delivery`. Do not claim a
feature matrix, target, MSRV, benchmark, Miri, sanitizer, or fuzz result that was
not actually exercised.
