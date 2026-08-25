# Route: API and Interface Contracts

Use this route when the decision is the contract a consumer crosses: an HTTP,
GraphQL, RPC, event, CLI-facing module, or public library boundary. Choose a
transport only when its properties solve a named consumer or operational need.
Do not turn a contract review into REST naming preferences, mandatory
pagination, a particular schema language, or a versioning ceremony.

## Workflow

1. Discover the producer, intended consumers, current public surface, supported
   versions, repository conventions, representative call sites, and the
   consequence when the boundary rejects, delays, duplicates, or partly applies
   a request. State unknown consumers, delivery guarantees, and authority
   limits before prescribing a shape.
2. Read [API and interface contracts](api-and-interface-contracts.md). Define
   the smallest stable inputs, outputs, events, validation boundary, error
   meaning, completion model, and compatibility promise the consumers need.
3. Read [Source-verified external contracts](source-verified-external-contracts.md)
   when framework, dependency, or vendor behavior materially affects the
   proposed contract.
4. Select the narrowest evidence that can disprove the consequential claim:
   consumer-facing integration coverage, a deterministic transport fixture or
   replay, a compatibility check, or a controlled failure-path test. Do not
   treat a schema file, mock, or endpoint naming convention as behavioral proof.
5. Report the contract, consumer impact, deliberate tradeoffs, migration or
   recovery conditions, and evidence gap. Keep unverified provider behavior
   explicitly provisional.

## Cross-links

- Overall service boundaries, ownership, deployment topology, quality
  attributes, and migration direction are the Architecture route. This route
  defines the contract within an agreed boundary.
- Data ownership, transactions, concurrency control, storage-backed
  idempotency, retention, reconciliation, and schema evolution are the Data
  route. This route names the caller-visible guarantee that those mechanisms
  must uphold.
- TypeScript and Rust routes implement language-specific public surfaces,
  ownership, types, errors, and runtime behavior after the contract is agreed.
- The Testing route designs and implements focused evidence. This route decides
  which external behavior needs protecting; it does not prescribe a test
  framework or make every boundary an end-to-end suite.
- Browser-facing APIs, frontend data contracts, component interfaces, and
  browser behavior belong to `effective-web` when the primary mission is a web
  surface.
- Escalate a threat-model, authorization, privacy, compliance, or security
  control decision to the responsible specialist when the available evidence
  cannot establish a safe contract. Naming an API boundary is not a security
  review.
- Repository-wide delivery planning, dependency updates, pull-request review,
  and external-facing technical documentation belong to `effective-delivery`.
