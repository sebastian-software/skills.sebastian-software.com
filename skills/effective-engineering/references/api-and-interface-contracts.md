# API and Interface Contracts

Make the consumer-visible promise explicit before choosing a transport,
framework, or storage mechanism. A public interface can be an HTTP or GraphQL
request, an event, a CLI-facing module, or a library API; its contract is the
behavior callers can rely on, not its syntax.

## Establish the Consumer Contract

For the affected flow, record only the distinctions consumers need:

- **Identity and authority:** who may initiate or observe the operation, and
  which stable resource, operation, or idempotency identity distinguishes one
  intent from another;
- **Input and validation:** required and optional fields, defaults, accepted
  ranges and states, and the boundary where untrusted input becomes a known
  value;
- **Outcome:** returned data or emitted event, observable state transition,
  completion model, and which fields or event order consumers may depend on;
- **Failure:** stable categories and safe details for invalid input, conflict,
  unavailable dependency, timeout, authorization failure, and an outcome whose
  completion is unknown; and
- **Compatibility:** supported consumers, extension points, removal or
  deprecation conditions, and the migration window when a change cannot remain
  compatible.

Do not expose internal storage shapes, framework exceptions, implementation
types, or provider payloads merely because they are convenient today. Conversely,
do not add a wrapper, version prefix, pagination scheme, or schema language when
no consumer, evolution, or interoperability need justifies it.

## Design for Uncertain Completion

A timeout or dropped acknowledgement says that a caller does not know whether
the effect occurred. When a repeated side effect is consequential, define:

1. a stable operation identity that is reused for the same intent but differs
   for a legitimately new one;
2. an atomic claim or deduplication boundary rather than a read-then-write
   check;
3. the response for an in-flight duplicate — reject, bounded wait, or pending
   state — and the recovery path for a stalled attempt;
4. request-mismatch behavior when the same identity carries a different
   payload; and
5. retention that outlives every retry, delayed delivery, and replay path.

Use this protocol only where a repeat can cause a consequential effect. A
read-only query, a naturally idempotent state set, or a local call does not need
an idempotency subsystem by default.

## Evolve Without Surprising Consumers

Prefer additive, opt-in, or parallel changes while existing consumers must
continue to work. Before removing or narrowing an observable field, event,
type, error, ordering guarantee, or capability, inspect representative
consumers and the stated compatibility promise. Decide whether a compatible
extension, explicit version boundary, bounded adapter, or coordinated cutover
is warranted by the actual consumer population and failure cost.

Keep one authoritative contract. Documentation, generated schema, type surface,
and transport fixtures are useful only when they agree with the implemented
behavior. If they disagree, identify the owner and repair path instead of
declaring the most convenient artifact canonical.

## Prove the Consequential Behavior

Choose evidence from the claim:

| Claim | Narrow evidence |
| --- | --- |
| Input is accepted, rejected, or normalized correctly | Boundary-level test with representative valid, invalid, and ambiguous values |
| Consumers receive a stable response, event, or error | Public-consumer, transport, or contract fixture that asserts the observable shape and meaning |
| A retry cannot duplicate a consequential effect | Deterministic sequence covering first effect, missing acknowledgement, repeat, duplicate claim, and final recovery state |
| A change remains compatible | Existing consumer compilation or interaction check plus an intentional migration case where relevant |
| A provider-specific behavior is assumed | Exact-version primary source plus a focused repository check, or an explicit uncertainty |

Avoid proving a contract only through handler internals, mock call order, a
generated schema, or a happy-path request. Use live systems only when the
repository can make them deliberate, safe, and opt-in; otherwise preserve the
failure boundary with a local implementation, fixture, or replay.
