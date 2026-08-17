---
name: effective-engineering
description: >-
  Design and write software systems and focused non-frontend tests. Use for
  architecture and service or module boundaries; build-versus-buy, strategic
  control, quality attributes, and operational readiness; data models,
  datastores, transactions, consistency, replication, pipelines, schema
  evolution, and migrations; TypeScript type, module, async, and error
  contracts; Rust crates, ownership, APIs, unsafe code, concurrency, and
  performance; test strategy, regression tests, and benchmark design. Trigger
  when choosing system or data contracts, writing or reviewing TypeScript or
  Rust, or proving behavior with tests. Do not use for browser-facing work or
  repository lifecycle workflows such as audits, ports, PR reviews, dependency
  upgrades, and running existing checks.
---

# Effective Engineering

Design and write the software itself. Turn a product and delivery problem into
a system direction, a data model that holds its invariants, code whose contracts
are honest to the next maintainer, and the smallest evidence that proves the
behavior.

Prefer repository evidence over named patterns, ambient strictness fashions, and
speculative optimization. Choose the smallest design the evidence supports.

## Workflow

1. Discover before judging: scoped instructions, manifests, configuration, CI,
   lint and format policy, accepted ADRs, public entry points, nearby tests, and
   representative call sites. Discover the repository-native commands.
2. State the decision scope and evidence limits. Separate facts observed in the
   system from assumptions, forecasts, and open questions. Do not invent load,
   availability, recovery, regulatory, budget, ownership, MSRV, compiler-flag,
   runtime, or performance requirements.
3. Select one primary route from the table. Read that route before acting.
4. Load only the references the route names for this task.
5. Compare the smallest viable options against the same criteria, recommend one
   direction, and name the tradeoffs, deferred choices, and what would reopen
   the decision.
6. Verify the consequential claims at the narrowest faithful boundary
   available. Report what ran, what was skipped, and any remaining evidence gap
   honestly.

## Route by Intent

| User intent | Read |
| --- | --- |
| Assess, design, review, or evolve system boundaries, responsibilities, quality attributes, operational readiness, or testing strategy | [Software Architecture](references/route-architecture.md) |
| Decide data models, datastores, transactions, consistency, replication, partitioning, streams, schema evolution, or migrations | [Data Systems](references/route-data.md) |
| Write or review server-side and shared-library TypeScript: types, narrowing, module and package API, async, cancellation, typed errors, tsconfig | [TypeScript Engineering](references/route-typescript.md) |
| Write or review Rust: ownership, borrowing, public API, naming, errors, panics, concurrency, cancellation | [Rust Engineering](references/route-rust.md) |
| Change Rust crate or module structure, public interfaces, domain types, persistence, or async boundaries | [Rust Architecture](references/route-rust-architecture.md) |
| Make a Rust runtime, build-time, binary-size, or profiling claim; choose collections, allocation, layout, boxing, or integer widths | [Rust Performance and Memory](references/route-rust-performance.md) |
| Write or review Rust unsafe blocks, raw pointers, FFI or ABI boundaries, SIMD, target features, atomics, Rayon, or thread pools | [Rust Unsafe and SIMD](references/route-rust-unsafe.md) |
| Protect a behavior, invariant, regression, failure path, retry, authorization rule, migration, or CLI contract; diagnose a flaky or undiscovered test | [Focused Testing](references/route-testing.md) |
| Design, repair, or interpret a microbenchmark, comparative benchmark, or bounded end-to-end performance workflow | [Benchmark Methodology](references/route-benchmarks.md) |

## Operating Rules

- Start from the simplest deployable shape. Introduce a service boundary, a
  replica, a queue, an extra datastore, a trait, a generic, or an abstraction
  only for a concrete named driver.
- Make ownership singular. One component owns each mutable business fact; others
  get a contract, a projection, or an explicit write protocol.
- Design contracts for failure: timeouts, retries, idempotency, ordering,
  partial completion, degraded behavior, and compatibility are part of the
  design once a flow crosses a process or network boundary.
- Keep the type system and the compiler as contracts, not lints to silence.
  Justify every assertion, cast, suppression, and unsafe operation, and say when
  it can be removed.
- Own every asynchronous unit of work: await it, return it, or attach a
  deliberate handler, and propagate cancellation rather than orphaning it.
- Profile before optimizing. Treat a performance change as a measurement
  contract with workload, platform, toolchain, build profile, baseline, and
  metric recorded.
- Prefer a test of observable behavior over coverage percentage, assertion
  count, or mock choreography. A growing mock graph is a stop signal: improve
  the production seam instead.
- Never claim scale, failover, consistency, recovery, safety, or performance
  properties from a product label or a pattern name. Verify configured behavior
  and failure cases in the actual environment.
- Escalate specialist security, privacy, regulatory, infrastructure, or
  production-operations decisions when the available evidence and authority
  cannot establish a safe direction.

## Routing Boundaries

- Route repository lifecycle workflows to `effective-delivery`: repository-wide
  audits and prioritization, implementation-plan creation and review,
  behavior-preserving ports across languages, runtimes, frameworks, or major
  APIs, pull-request review and merge judgment, dependency selection and version
  updates, execution of established format, lint, typecheck, build, test, Miri,
  sanitizer, fuzz, benchmark, load, soak, or stress commands, technical
  documentation including TSDoc and rustdoc, and the team system around the
  work. This discipline supplies language-depth findings inside a review and a
  post-parity idiom pass on ported code.
- Route browser-facing work to `effective-web`: frontend CSS, React, rendering,
  component and interface architecture, browser-facing TypeScript, browser
  performance, and browser, component, visual, accessibility, and E2E testing
  including overall frontend testing strategy. Route by primary mission, not
  artifact type — a browser feature belongs there even when it contains pure
  logic; an independent shared library or a server-side domain contract belongs
  here.
- Route durable choices, ADR format, supersession, and drift control to
  `effective-product`, along with product strategy, scope, and prioritization
  that a technical decision depends on.
- Route positioning, messaging, and any market-facing claim about the system's
  performance or reliability to `effective-marketing`.
- Route articles, explainers, and public prose about the engineering work to
  `effective-writing`.
- No first-party discipline currently claims new load, soak, or stress execution
  methodology. State that boundary instead of inventing a tool or traffic model.
