# Replication, Partitioning, and Streams

Use this reference only when measured availability, locality, integration,
asynchronous work, or scale creates a distribution requirement.

## Replicate for a Named Purpose

Name whether replication serves availability, recovery, read scale, geographic
latency, analytics, or integration. Then define:

- write authority and failover authority;
- synchronous or asynchronous acknowledgement;
- expected and worst credible lag;
- read routing and session guarantees;
- conflict behavior and resolution ownership;
- recovery-point and recovery-time expectations; and
- how failover and restoration are tested.

Replicas add failure modes. They do not automatically improve availability when
failover is manual, untested, or unable to meet the product's consistency need.

## Partition Only with Evidence

Before partitioning, establish:

1. the current capacity or locality limit;
2. the workload and growth evidence that will reach it;
3. the keys used by dominant reads and writes;
4. tenant, time, geography, and popularity skew;
5. cross-partition queries and invariant scope; and
6. rebalance, reshard, backup, and recovery behavior.

Choose a partition key that distributes the actual workload and keeps critical
operations local. A high-cardinality key can still produce hot partitions when
activity is skewed. Time-based keys can concentrate current writes. Tenant keys
can isolate customers but leave very large tenants as hotspots.

Do not pre-shard because a forecast sounds large. Prefer a single logical store,
appropriate indexes, vertical headroom, read replicas, archival, or workload
changes when those address the measured constraint with less operational cost.
Define the evidence that would justify revisiting partitioning.

## Treat Streams as Data Contracts

For every event or record, state:

- the authoritative source and event identity;
- the meaning and schema, including version evolution;
- partitioning and the actual ordering scope;
- delivery semantics as implemented, not marketed;
- consumer idempotency and deduplication scope;
- retry, backoff, poison-message, and dead-letter behavior;
- retention, replay, checkpointing, and reset behavior; and
- ownership of lag, reconciliation, and privacy obligations.

Assume messages can be delayed, duplicated, reordered across partitions, or
reprocessed after recovery unless the complete system proves otherwise.
“Exactly once” at one layer does not make external side effects exactly once.

## Separate Batch and Streaming Decisions

Prefer batch when bounded staleness is acceptable and replayable snapshots make
the workflow simpler. Prefer streaming when the decision or user experience
requires continuous low-latency propagation and the team can operate lag,
replay, schema evolution, and out-of-order data.

Compare:

- freshness requirement versus processing latency;
- source completeness and watermark behavior;
- late and corrected records;
- deterministic replay and backfill;
- state size and checkpoint recovery;
- observability, on-call burden, and cost.

A scheduled incremental job can be the correct middle ground. Do not make
streaming a default merely because events exist.

## Avoid Hidden Dual Writes

Writing a database and a queue, cache, index, analytics store, or second
database from one request creates two independent outcomes unless one commit
atomically governs both. Prefer an outbox, source log, or change stream from the
authoritative write. Make consumers idempotent and retain:

- source position or event identity;
- propagation lag and failure metrics;
- replay and reconciliation commands;
- a rebuild path for derived state; and
- an explicit response to poison or permanently invalid records.

If a temporary migration must write two systems, define which is authoritative,
how conflicts are detected, how every record is reconciled, and when the second
write will be removed.
