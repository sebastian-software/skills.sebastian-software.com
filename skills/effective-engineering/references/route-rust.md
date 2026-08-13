# Route: Rust Engineering

Write Rust that makes architecture, ownership, failure, concurrency, safety,
and performance reasoning understandable to the next maintainer. Prefer
repository evidence and semantic types over universal thresholds, clever
compression, or speculative optimization.

This is the Rust entry route. Three sibling routes carry the deep material:
Rust Architecture, Rust Performance and Memory, and Rust Unsafe and SIMD. Start
here, then load only the one the task needs.

## Establish the Contract

1. Read scoped instructions, `Cargo.toml`, workspace configuration, CI, lint
   policy, formatting configuration, relevant ADRs, public APIs, nearby tests,
   and representative call sites. Discover the edition, MSRV, supported targets,
   feature combinations, async runtime, and repository-native commands.
2. State the changed behavior and boundaries: inputs, outputs, ownership,
   mutation, expected errors, possible panics, cancellation, ordering,
   concurrency, resource limits, and any safety invariant. Do not invent a
   stronger MSRV, lint set, runtime, crate, or performance target.
3. Read [Ownership and API design](rust-ownership-and-api-design.md) for
   borrowing, newtypes, parsing, trait boundaries, and abstraction choices.
4. Read [Naming and readability](rust-naming-and-readability.md) for semantic
   names, Unicode-safe text handling, constants, comments, and maintainable
   control flow.
5. Read [Errors and concurrency](rust-errors-and-concurrency.md) when the change
   can fail, panic, spawn work, block, hold a lock, or be cancelled.
6. Read [Quality and review](rust-quality-and-review.md) before declaring the
   change ready.

Then take the sibling route that matches the work:

- crate or module structure, public interfaces, services, domain types,
  persistence, async boundaries, or project organization → Rust Architecture
- runtime, build-time, binary-size, profiling, or benchmark claims; collections,
  allocation strategies, representations, alignment, cache layout, boxing, or
  integer widths → Rust Performance and Memory
- every unsafe block, unsafe trait implementation, raw pointer, foreign call, or
  ABI boundary; auto-vectorization, portable SIMD, intrinsics, target features,
  atomics, Rayon, or thread pools → Rust Unsafe and SIMD

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
- Make crate and module boundaries carry dependency direction, stability
  promises, and explicit negative invariants; keep I/O and serialization at
  the boundary when a pure core improves testing or incremental computation.
- Preserve readable control flow. Prefer explicit matches and small helpers when
  combinator chains obscure error, ownership, or early-return behavior.
- Profile before optimizing. Do not choose integer widths, collection layouts,
  boxing, inlining, LTO, allocation strategies, or copying thresholds from a
  generic size rule.
- Treat a performance change as a measurement contract: record workload,
  platform, toolchain, build profile, baseline, metric, and the evidence that
  identified the bottleneck. Keep specialized SIMD or target-feature paths
  behind a safe fallback and a documented dispatch contract.
- Derive atomic ordering from a happens-before argument. Treat Rayon chunking,
  async blocking work, queue bounds, and shutdown as resource and lifecycle
  contracts rather than throughput folklore.
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
