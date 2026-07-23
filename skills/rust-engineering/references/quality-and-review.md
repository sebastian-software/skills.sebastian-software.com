# Quality and Review

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
tests and the nearest public consumer. Expand to feature combinations,
workspace checks, supported targets, release mode, doctests, or specialized
unsafe/concurrency tools when the claim requires them.

Report exact commands and outcomes through `software-validation`. Do not claim a
feature matrix, target, MSRV, benchmark, Miri, sanitizer, or fuzz result that was
not actually exercised.
