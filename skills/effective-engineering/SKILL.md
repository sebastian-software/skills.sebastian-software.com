---
name: effective-engineering
description: >-
  Design software architecture, APIs, data models, transactions, and
  migrations; write or review Rust and server-side or shared-library
  TypeScript; design focused non-frontend tests and benchmarks. Use for system
  and code contracts. Browser implementation and frontend tests belong to
  effective-web; repository audits, ports, PR upkeep, dependency upgrades, and
  running existing checks belong to effective-delivery.
---

# Effective Engineering

Choose the route for the system or code decision, then read the references
needed to resolve it. Use repository contracts and observed requirements;
do not require a full architecture review for a local change.

Prefer the simplest design supported by evidence. Add abstractions, fallback
states, or tests for reachable, consequential behavior; weigh their maintenance
cost. Preserve security, privacy, authorization, money, and data-integrity
boundaries even when failures are rare. Do not invent scale or reliability
requirements.

Keep types, ownership, asynchronous work, and failure behavior explicit.
Validate changed contracts at a faithful boundary; performance claims need a
representative measurement. Continue through the authorized implementation and
report material uncertainty without expanding into speculative hardening.

## Route by Intent

| User intent | Read |
| --- | --- |
| Assess, design, review, or evolve system boundaries, responsibilities, quality attributes, operational readiness, or testing strategy | [Software Architecture](references/route-architecture.md) |
| Design or review a public HTTP, GraphQL, event, or library boundary: request and response shape, validation, error semantics, compatibility, retry safety, or consumer impact | [API and Interface Contracts](references/route-api-contracts.md) |
| Decide data models, datastores, transactions, consistency, replication, partitioning, streams, schema evolution, or migrations | [Data Systems](references/route-data.md) |
| Write or review server-side and shared-library TypeScript: types, narrowing, module and package API, async, cancellation, typed errors, tsconfig | [TypeScript Engineering](references/route-typescript.md) |
| Write or review Rust: ownership, borrowing, public API, naming, errors, panics, concurrency, cancellation | [Rust Engineering](references/route-rust.md) |
| Change Rust crate or module structure, public interfaces, domain types, persistence, or async boundaries | [Rust Architecture](references/route-rust-architecture.md) |
| Make a Rust runtime, build-time, binary-size, or profiling claim; choose collections, allocation, layout, boxing, or integer widths | [Rust Performance and Memory](references/route-rust-performance.md) |
| Write or review Rust unsafe blocks, raw pointers, FFI or ABI boundaries, SIMD, target features, atomics, Rayon, or thread pools | [Rust Unsafe and SIMD](references/route-rust-unsafe.md) |
| Protect a behavior, invariant, regression, failure path, retry, authorization rule, migration, or CLI contract; diagnose a flaky or undiscovered test | [Focused Testing](references/route-testing.md) |
| Design, repair, or interpret a microbenchmark, comparative benchmark, or bounded end-to-end performance workflow | [Benchmark Methodology](references/route-benchmarks.md) |

## Routing Boundaries

- `effective-web`: browser-facing TypeScript, React, frontend architecture,
  performance, and all frontend test design and diagnosis. Route by the outcome;
  pure logic inside a browser feature does not make it a backend task.
- `effective-delivery`: repository audits, implementation plans, ports, PR
  review and upkeep, dependency updates, running established checks, technical
  documentation, and team workflows. Supply language-depth findings as needed.
- `effective-product`: product direction and durable decisions recorded as ADRs.
- `effective-marketing`: positioning and public performance or reliability claims.
- `effective-writing`: articles and explainers about the engineering work.

New load, soak, and stress methodology is outside this collection. Escalate
specialist security, regulatory, infrastructure, or production-operations
choices when evidence and authority cannot establish a safe direction.
