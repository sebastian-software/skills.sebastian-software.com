# Evolution and Operations

Use this reference for schema changes, backfills, index changes, data movement,
cutovers, retention, backup, restore, reconciliation, and production ownership.

## Evolve Compatibly

Prefer an expand-migrate-contract sequence:

1. **Expand:** introduce additive schema, tolerant readers, and compatible
   contracts without making old code invalid.
2. **Observe:** confirm the new path is deployed, reachable, and behaving as
   expected before migrating data or traffic.
3. **Migrate:** backfill or copy bounded slices with checkpoints, rate limits,
   retry safety, and progress visibility.
4. **Verify:** compare counts, invariants, checksums or samples, and
   user-visible behavior. Investigate discrepancies instead of hiding them in
   an aggregate success rate.
5. **Cut over:** change one reader, writer, tenant, or traffic slice at a time
   where the system permits it.
6. **Stabilize:** monitor correctness, lag, load, errors, and support signals
   for an explicit period.
7. **Contract:** remove old fields, code, indexes, and bridges only after all
   consumers are proven migrated and the recovery window has closed.

Do not assume a schema rollback repairs data written under the new behavior.
Choose rollback or roll-forward based on compatibility and the actual mutations
already committed.

## Plan Backfills as Production Work

Define:

- source snapshot or cursor semantics;
- chunk identity, ordering, and resumable checkpoints;
- idempotent writes and conflict handling;
- load budgets and automatic pause conditions;
- treatment of concurrent live writes;
- validation at record and aggregate levels;
- retry, quarantine, and manual repair paths; and
- completion and cleanup evidence.

Test the backfill on realistic data volume and skew when possible. A staging
dataset that lacks production cardinality, row size, hot tenants, or invalid
history does not establish production safety.

## Control Dual-Running and Cutover

When old and new paths coexist, document:

- the single authoritative writer at each phase;
- whether shadow output is observable but non-authoritative;
- comparison semantics and acceptable known differences;
- read routing and fallback behavior;
- conflict and drift detection;
- cutover approval, abort, and retry conditions; and
- the owner and date for deleting the temporary bridge.

Avoid indefinite bidirectional synchronization. It obscures ownership and makes
conflicts part of the steady state.

## Design Reconciliation

Reconciliation should answer:

1. Which records or time ranges were compared?
2. What equivalence rule applies?
3. Which differences are expected, known-wrong, or unexplained?
4. Can repair be replayed safely?
5. How is correction audited?
6. What closes the incident or migration gate?

Use invariant checks, source-to-projection counts, keyed hashes, targeted
samples, and user-flow probes as appropriate. Do not rely on one total count
when duplicates and omissions can cancel out.

## Own Runtime Safety

Assign explicit ownership and evidence for:

- saturation, latency, error, connection, lock, queue, and lag signals;
- slow queries, hot keys, long transactions, and storage growth;
- backup scope, encryption, retention, and restore drills;
- failover, replica rebuild, and corruption response;
- privacy deletion and retention propagation;
- capacity forecasts grounded in measured workload; and
- on-call actions, escalation, and vendor dependencies.

A successful backup job is not recovery evidence. Restore representative data
into an isolated environment, verify its usability, and record recovery time
and gaps.

## Gate the Change

Before each irreversible or high-risk step, require:

- compatible deployed code on all affected readers and writers;
- bounded, observable data movement;
- verified reconciliation;
- acceptable production load and user impact;
- a tested recovery action;
- an authorized decision owner; and
- a clear stop condition when evidence disagrees with the plan.
