[← Sebastian Software Skills](../../README.md)

# Data Systems

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Design data around the facts that must remain true, then add distribution
only when real access, scale, or failure evidence demands it.**

Data Systems helps agents turn database, consistency, pipeline, and migration
questions into explicit guarantees and operable change paths. It starts with
access patterns, invariants, load, failure consequences, and team capability
instead of recommending a fashionable datastore or architecture by default.

## What It Can Deliver

- logical data models and authoritative ownership boundaries
- datastore comparisons tied to real reads, writes, and constraints
- transaction, isolation, concurrency, and read-consistency contracts
- replication, partitioning, batch, and streaming tradeoffs
- safe schema evolution, backfills, cutovers, and reconciliation
- failure scenarios and verification criteria for consequential guarantees

## Use It When

Use this skill to choose or review a datastore, prevent lost updates, define
read-your-writes behavior, assess replication lag, remove risky dual writes,
design an event or batch flow, evaluate partitioning, or evolve production data
without an unsafe flag day.

## Example Prompts

```text
Model subscriptions and entitlements for these access patterns and invariants.
Compare the smallest viable storage options without assuming microservices.

Users sometimes see their old settings immediately after saving. Define the
read-your-writes contract and diagnose which replica and cache paths violate it.

Two workers can approve the same claim at once. Show how to prevent the
concurrent update from breaking the invariant and how we should verify it.

Plan a compatible migration from this legacy schema. Avoid uncoordinated dual
writes, include reconciliation, and state the cutover and rollback gates.
```

See [SKILL.md](SKILL.md) for the complete data-model, consistency, distribution,
and evolution workflow.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill data-systems
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian data-systems
dalo approve skill sebastian:data-systems
dalo sync
```

## Related Skills

- [Software Architecture](../software-architecture/README.md) owns overall
  system and service boundaries, quality attributes, and deployment direction;
  Data Systems owns the model and data semantics within them.
- [Software Testing](../software-testing/README.md) turns an agreed transaction,
  migration, retry, or consistency guarantee into focused executable evidence.
- [Decision Records](../decision-records/README.md) preserves a durable
  datastore, ownership, consistency, or migration decision.
- [Codebase Improvement](../codebase-improvement/README.md) diagnoses and plans
  broader repository change when data risk is only one part of the problem.

## Scope

This skill covers data modeling, storage and processing tradeoffs, consistency,
distribution, evolution, and operating evidence. It does not replace overall
software architecture, infrastructure ownership, security or privacy review,
regulatory advice, vendor-specific production expertise, or focused test
implementation.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
