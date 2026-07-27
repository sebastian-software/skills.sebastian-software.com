# Transactions and Consistency

Use this reference when correctness depends on atomicity, isolation, concurrent
updates, ordering, retries, idempotency, or what a reader observes after writes.

## State the Guarantee per Flow

Replace broad labels such as “strong” or “eventual” with an observable contract:

- Which actor performs the write?
- Which subsequent read must observe it?
- Must operations from one actor remain ordered?
- May another actor observe stale state, and for how long?
- What happens during lag, failover, timeout, or partition?
- Is stale data visible, explicitly marked, retried, or unavailable?

Useful session-level guarantees include read-your-writes, monotonic reads, and
monotonic writes. Do not claim them from topology alone: trace every replica,
cache, projection, and failover path involved in the flow.

## Place Invariants at the Enforcement Boundary

Keep a multi-step business invariant inside one atomic boundary whenever the
store supports it. Prefer:

- unique or exclusion constraints for uniqueness;
- a transaction for facts that must commit together;
- a conditional update or compare-and-set for a versioned transition;
- a row or advisory lock when serialization is necessary and bounded;
- a ledger or immutable operation record where history is part of correctness.

A preflight read followed by an unconditional write is vulnerable to concurrent
change. Application validation can improve errors but does not replace the
atomic datastore guard.

## Choose Isolation from Anomalies

Select isolation from the anomalies the flow must prevent, not from a blanket
maximal setting:

- Identify dirty, non-repeatable, phantom, lost-update, write-skew, or ordering
  behavior that can violate a named invariant.
- Confirm the datastore's actual isolation semantics; names vary between
  products and configurations.
- Decide whether to serialize, lock, use a version precondition, redesign the
  invariant boundary, or accept and repair a documented anomaly.
- Bound contention and retry behavior under the expected conflict shape.

Test with real concurrent transactions at the closest faithful boundary. A
sequential unit test with mocked calls cannot demonstrate isolation.

## Make Retries Safe

Treat any timeout as an unknown outcome until the authoritative system can
confirm whether the operation committed. For retriable commands:

1. Give the logical operation a stable idempotency key.
2. Define its scope: actor, operation type, resource, or endpoint.
3. Store the result or state transition atomically with key consumption.
4. Retain deduplication state for at least the credible retry window.
5. Reject reuse with meaningfully different input.
6. Return the prior outcome or a well-defined status on replay.

“Set value to X” may be naturally repeatable but can still overwrite a newer
change. “Increment”, “send”, “charge”, and “append” require explicit duplicate
control.

## Coordinate Across Boundaries

Avoid assuming a transaction spans independent datastores or services. Prefer:

- one authoritative commit plus a transactional outbox;
- a durable log or change-data-capture stream from the source of truth;
- a state machine or saga with explicit compensation where business steps are
  genuinely distributed; or
- an idempotent consumer plus reconciliation and replay.

Do not describe compensation as rollback: an external side effect may be
irreversible, observable, or fail independently.

## Verify Correctness

Exercise cases that distinguish the claimed guarantee:

- two concurrent commands contend for the same invariant;
- the same operation is retried before and after completion;
- a timeout occurs after the server may have committed;
- a read follows a write through every routing and cache path;
- one distributed step commits while the next is unavailable;
- failover or replica lag changes the selected read source.

Record the observed result, configuration, environment, and remaining evidence
gap. Route focused test implementation to `software-testing`.
