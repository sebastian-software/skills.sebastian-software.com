# Route: Rust Engineering

Write Rust that makes architecture, ownership, failure, concurrency, safety,
and performance reasoning understandable to the next maintainer. Prefer
repository evidence and semantic types over universal thresholds, clever
compression, or speculative optimization.

This is the Rust entry route. Three sibling routes carry the deep material:
Rust Architecture, Rust Performance and Memory, and Rust Unsafe and SIMD. Start
here, then load only the one the task needs.

## Establish the Contract

1. Read scoped instructions and the affected code and tests. Check `Cargo.toml`,
   toolchain policy, features, targets, public consumers, or accepted decisions
   when they constrain the change. Use repository-native validation commands.
2. State the changed behavior and boundaries: inputs, outputs, ownership,
   mutation, expected errors, possible panics, cancellation, ordering,
   concurrency, resource limits, and any safety invariant. Do not invent a
   stronger MSRV, lint set, runtime, crate, or performance target.
3. Read [Ownership and API design](rust-ownership-and-api-design.md) when
   borrowing, domain types, parsing, trait boundaries, or abstraction changes.
4. Read [Naming and readability](rust-naming-and-readability.md) when deciding
   semantic names, Unicode handling, policy constants, or unclear control flow.
5. Read [Errors and concurrency](rust-errors-and-concurrency.md) when the change
   can fail, panic, spawn work, block, hold a lock, or be cancelled.
6. Read [Quality, review, and test evidence](rust-quality-and-review.md) when
   Rust-specific review or verification choices need guidance.

Then take the sibling route that matches the work:

- crate or module structure, public interfaces, services, domain types,
  persistence, async boundaries, or project organization → Rust Architecture
- runtime, build-time, binary-size, profiling, or benchmark claims; collections,
  allocation strategies, representations, alignment, cache layout, boxing, or
  integer widths → Rust Performance and Memory
- every unsafe block, unsafe trait implementation, raw pointer, foreign call, or
  ABI boundary; auto-vectorization, portable SIMD, intrinsics, target features,
  atomics, Rayon, or thread pools → Rust Unsafe and SIMD

## Review Output

For a review, report only findings that can affect correctness, safety,
compatibility, performance, or maintainability. Tie each finding to a concrete
path and contract, distinguish a verified defect from a risk or preference, and
propose the smallest correction consistent with repository conventions.

For an implementation, summarize the ownership and failure decisions, name the
focused evidence run, and state unverified feature, platform, unsafe, or
performance claims explicitly.

## Cross-links

- Rust-native test placement, public-API coverage, doctests, and opt-in live
  smoke evidence are the Testing route; this route owns the Rust contracts the
  tests must protect.
- Module and service boundary decisions for a Rust workspace are the
  Architecture route.
- Pull-request lifecycle, approval, CI recovery, merge judgment, ports, rustdoc
  and contributor documentation, crate selection and version updates,
  repository-wide audits and implementation plans, and execution of existing
  format, lint, build, test, Miri, sanitizer, fuzz, or benchmark commands belong
  to `effective-delivery`. This route supplies Rust-depth findings inside a
  review and a post-parity idiom pass on ported code.

Do not turn this route into a parallel test, documentation, dependency, or
delivery system.
