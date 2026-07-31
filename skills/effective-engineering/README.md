[← Sebastian Software Skills](../../README.md)

# Effective Engineering

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Design and write the software itself — boundaries, data, code, and the
evidence that proves it works.**

Effective Engineering is one of six disciplines in this collection. It turns a
product and delivery problem into a system direction, a data model that holds
its invariants, TypeScript and Rust whose contracts are honest to the next
maintainer, and the smallest tests and benchmarks that actually discriminate the
risk. It prefers repository evidence over named patterns, ambient strictness
fashions, and speculative optimization.

It replaces the former `software-architecture`, `data-systems`,
`typescript-engineering`, `rust-engineering`, and `software-testing` skills. See
[MIGRATION.md](../../MIGRATION.md) for the full mapping.

## Nine Routes

| Route | Owns |
| --- | --- |
| Software Architecture | boundaries, quality attributes, operability, testing strategy |
| Data Systems | models, transactions, consistency, replication, migrations |
| TypeScript Engineering | types, module APIs, async, typed errors, tsconfig |
| Rust Engineering | ownership, public API, naming, errors, concurrency |
| Rust Architecture | crate and module structure, domain types, async boundaries |
| Rust Performance and Memory | profiling, allocation, layout, binary size |
| Rust Unsafe and SIMD | unsafe, FFI, ABI, SIMD, atomics, Rayon |
| Focused Testing | invariants, failure paths, CLI contracts, flake diagnosis |
| Benchmark Methodology | microbenchmarks, comparisons, honest performance claims |

## What It Can Deliver

- architecture assessments, options with real tradeoffs, and migration sequences
- Twelve-Factor operability review that does not mandate a vendor or a container
- non-frontend testing strategy derived from quality scenarios, not a pyramid
  ratio
- data models with singular ownership and enforceable invariants
- consistency, idempotency, and failure contracts expressed per flow
- schema evolution, backfills, cutovers, reconciliation, and recovery plans
- TypeScript type, module, async, and error contracts, and reviews of them
- Rust ownership, API, concurrency, unsafe, and performance work with written
  safety and measurement arguments
- focused tests that prove they discriminate the failure they claim to catch
- benchmark designs that report their environment and their variance

## Use It When

Use this discipline when the deliverable is the system or the code: choosing a
boundary, deciding how data behaves under concurrency, writing or reviewing
TypeScript or Rust, protecting a behavior with a test, or designing a
measurement whose result someone will act on.

## Example Prompts

```text
Should this stay a modular monolith or split into services? Argue from our
actual load, ownership, and failure consequences, not from a pattern.

Two services write the same order status and customers see it move backwards.
Decide the ownership and consistency contract.

Review this crate's public API before 1.0. I care about lifetimes leaking
internals and about panic paths I have not documented.

This `as unknown as T` cast is holding a boundary together. Replace it with a
narrowing that actually proves the type, or tell me why it cannot be done.

Add a regression test for this fix and show me it fails against the old
behavior.

Design a benchmark that answers whether the new parser is faster in a way I
could publish without embarrassing myself.
```

See [SKILL.md](SKILL.md) for the workflow, route table, operating rules, and
routing boundaries.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-engineering
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian effective-engineering
dalo approve skill sebastian:effective-engineering
dalo sync
```

## Related Disciplines

- [Effective Delivery](../effective-delivery/README.md) owns repository
  lifecycle work: audits, implementation plans, ports, pull-request review,
  dependency updates, running the established checks, technical documentation,
  and the team system. This discipline supplies the language-depth findings
  inside a review.
- [Effective Web](../effective-web/README.md) owns everything browser-facing,
  including frontend TypeScript and frontend testing strategy.
- [Effective Product](../effective-product/README.md) owns the product decision
  a technical choice depends on, and the Architecture Decision Records that
  preserve durable rationale.
- [Effective Writing](../effective-writing/README.md) owns articles and
  explainers about the engineering work.

## Scope

This discipline designs and writes non-frontend software and the evidence for
it. It does not run the repository's established checks, manage pull requests,
update dependencies, execute ports, or write the product documentation — those
belong to Effective Delivery. It does not claim scale, failover, consistency,
recovery, safety, or performance properties from a product label, and no
first-party discipline currently claims load, soak, or stress execution
methodology.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
