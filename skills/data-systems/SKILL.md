---
name: data-systems
description: >-
  Design, review, and evolve reliable data models, datastores, transactions,
  consistency contracts, replication, partitioning, batch or streaming flows,
  and data migrations. Use for database or event-model decisions, read and
  write guarantees, concurrent updates, dual-write risks, replication lag,
  sharding or partition-key choices, data-pipeline semantics, schema evolution,
  backfills, cutovers, and recovery planning. Start from observed access
  patterns, invariants, load, failure consequences, and operational capability;
  do not introduce distribution, polyglot persistence, or event sourcing
  without a concrete driver.
---

# Data Systems

Turn a data requirement into explicit ownership, invariants, access paths,
consistency guarantees, failure behavior, and an operable evolution path.
Choose the smallest data system that satisfies the evidence; named technologies
and patterns are candidates, not conclusions.

## Workflow

1. Establish the decision and evidence boundary:
   - business facts and invariants that must remain true
   - commands, reads, queries, scans, and retention needs
   - observed or forecast load, growth, latency, and availability needs
   - failure consequences, recovery objectives, privacy, and compliance limits
   - current systems, team skills, operational ownership, and migration limits
2. Mark every input as observed, required, forecast, or unknown. Do not invent
   traffic, cardinality, growth, correctness, locality, or durability needs.
   When a missing fact can change the design, identify the measurement or
   decision needed before commitment.
3. Model the authoritative facts, identities, relationships, lifecycle, and
   ownership before selecting storage. Read [Storage and models](references/storage-and-models.md)
   for model and datastore choices driven by access patterns and invariants.
4. Define correctness per user or system flow. Read [Transactions and consistency](references/transactions-and-consistency.md)
   when work involves atomicity, isolation, concurrent updates, idempotency,
   read-your-writes, stale reads, or coordination across boundaries.
5. Read [Replication, partitioning, and streams](references/replication-partitioning-and-streams.md)
   only when measured scale, availability, locality, integration, or
   asynchronous processing creates a concrete need. Make lag, ordering,
   duplicate delivery, hot partitions, and partial failure visible.
6. Read [Evolution and operations](references/evolution-and-operations.md) for
   schema changes, backfills, dual-running, cutovers, reconciliation, recovery,
   retention, and operability. Prefer compatible, observable steps over a
   one-shot migration.
7. Compare the smallest viable options against the same decision criteria:
   invariant support, access-path fit, failure semantics, operational burden,
   cost shape, reversibility, and migration risk. Reject sophistication that
   addresses an unobserved problem while creating a current one.
8. Recommend one direction and state deferred choices, assumptions, failure
   behavior, migration gates, rollback or roll-forward conditions, and the
   evidence that would reopen the decision.
9. Verify the consequential claims. Exercise representative reads and writes,
   concurrent conflicts, retries, partial failures, recovery, and migration
   reconciliation at the narrowest faithful boundary available.

## Operating Rules

- Give each mutable business fact one authoritative writer or an explicit
  coordination protocol. Shared storage and duplicate writers do not create
  shared ownership.
- Express consistency as a flow-level guarantee. Name who must observe which
  write, in what order, within what bound, and what stale or unavailable state
  the product can expose.
- Preserve invariants in the layer that can enforce them under concurrency.
  A read-then-write check without a transaction, version precondition, or
  equivalent atomic guard is not proof.
- Treat retries and duplicate delivery as normal distributed behavior.
  Idempotency requires a stable operation identity, a defined deduplication
  scope, and retention long enough for the retry window.
- Avoid uncoordinated dual writes. Prefer one committed write followed by a
  durable outbox, log, change stream, or reconciled migration path; document
  what repairs partial completion.
- Introduce replicas, caches, partitions, queues, streams, or additional
  datastores only for a named requirement that simpler storage cannot meet.
- Separate a logical data model from a vendor or product. Preserve the
  invariants and access contract when comparing implementations.
- Treat schema, retention, deletion, backup, restore, and observability as
  runtime behavior, not cleanup after implementation.
- Never claim scale, failover, consistency, or recovery properties from a
  product label. Verify configured behavior and failure cases in the actual
  environment.

## Default Deliverable

Return a decision-ready data-system proposal containing:

1. facts, access patterns, invariants, evidence, assumptions, and unknowns;
2. authoritative ownership and the proposed logical model;
3. required consistency, concurrency, durability, and failure semantics by flow;
4. the smallest viable storage and processing shape with rejected alternatives;
5. evolution, compatibility, reconciliation, cutover, and recovery steps;
6. operational signals, capacity assumptions, and escalation conditions; and
7. verification scenarios that discriminate the important guarantees.

## Routing Boundaries

- Use `software-architecture` for overall system boundaries, service ownership,
  quality attributes, deployment topology, and cross-system migration
  direction. Use this skill for the data model and data-behavior decisions
  inside or between those agreed boundaries.
- Hand focused database, transaction, migration, async, retry, and failure-path
  test design or implementation to `software-testing`; this skill defines the
  data guarantee and failure scenario that the test must preserve.
- Use `decision-records` when a durable datastore, consistency, ownership, or
  migration choice needs an ADR and the user authorizes that artifact.
- Use `codebase-improvement` for repository-wide diagnosis, prioritization, and
  executable change planning when the data concern is one part of a broader
  legacy or maintainability problem.
- Use `port-codebases` when the primary goal is behavior-preserving migration
  across languages, runtimes, frameworks, platforms, or major APIs; keep data
  compatibility and cutover guarantees here.
- Escalate specialist security, privacy, regulatory, infrastructure, or
  production-operations decisions when the available evidence and authority
  cannot establish a safe direction.

Do not turn a data-system decision into a broad architecture redesign. Return
system-boundary findings to the architecture owner and keep this skill focused
on facts, access, correctness, distribution, evolution, and operability.
