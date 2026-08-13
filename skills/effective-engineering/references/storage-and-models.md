# Storage and Models

Use this reference when defining authoritative facts, logical models, access
paths, constraints, or a datastore shortlist.

## Start with the Workload

Capture representative operations before naming a database:

- command or query and the user or system flow it supports
- lookup keys, predicates, joins, ordering, aggregation, and result size
- expected frequency, concurrency, latency sensitivity, and freshness
- write conflicts, invariant scope, retention, deletion, and audit needs
- observed values, forecasts, and unknowns

Do not compress all work into average requests per second. A low average can
hide hot keys, end-of-month batches, tenant skew, large scans, or one
latency-critical interaction. Measure the distribution that affects design.

## Model Authoritative Facts

1. Name each durable business fact in domain language.
2. Give it a stable identity and lifecycle.
3. State which component or process may author each mutation.
4. Express invariants independently of storage syntax.
5. Separate authoritative records from projections, caches, indexes, and
   analytical copies.
6. Mark personal, sensitive, regulated, retained, or deletable fields and route
   specialist policy questions when required.

Avoid storing the same mutable fact as equally authoritative in several places.
If consumers need different shapes, derive projections through an explicit
contract and provide a way to rebuild or reconcile them.

## Choose the Data Model

Choose a model whose native operations match the dominant invariants and access
paths:

- Prefer a relational model when transactions, constraints, joins, and
  evolving queries are central.
- Prefer a key-value or document shape when aggregate boundaries and
  key-directed access are stable and cross-aggregate invariants are limited.
- Prefer graph-oriented storage only when variable-depth relationship traversal
  is a central measured workload, not because the domain contains relationships.
- Prefer columnar analytical storage for large scans and aggregations separated
  from transactional command handling.
- Treat search engines as searchable projections unless the product and failure
  contract genuinely allow them to own the source fact.
- Treat object storage as durable blobs or immutable datasets with explicit
  metadata and indexing, not as an accidental transactional database.

These are candidate defaults, not categorical rules. Test actual query plans,
index behavior, limits, and operational properties in the target environment.

## Design Access Paths

For every important query:

1. Identify the authoritative or derived data source.
2. Specify keys, indexes, ordering, and bounded result shape.
3. Estimate or measure selectivity, fan-out, payload, and amplification.
4. Name the freshness and consistency requirement.
5. Define behavior when the index, projection, or cache is stale or unavailable.

Denormalize only for a demonstrated access or availability need. Record the
source field, propagation contract, acceptable lag, repair mechanism, and
rebuild path for every duplicated value.

## Evaluate a Datastore

Compare candidates against the same evidence:

| Concern | Question |
| --- | --- |
| Invariants | Can the store enforce the required uniqueness, atomicity, and conditional updates? |
| Access | Do primary reads and writes fit native keys, indexes, and query behavior? |
| Scale | Which measured bottleneck is relieved, and which new limit appears? |
| Failure | What becomes stale, unavailable, duplicated, or partially complete? |
| Evolution | Can schemas, indexes, projections, and records change compatibly? |
| Operations | Can the team observe, back up, restore, repair, and upgrade it? |
| Cost | What drives storage, compute, transfer, request, and operational cost? |
| Portability | Which useful features create lock-in, and what exit would be credible? |

Avoid scoring with arbitrary weights or universal thresholds. State decisive
requirements, meaningful tradeoffs, and evidence gaps directly.

## Stop Conditions

Stop and request evidence or specialist ownership when:

- the invariant cannot be stated clearly;
- capacity depends on an unmeasured hot-key or workload shape;
- privacy, residency, deletion, or regulatory obligations are unresolved;
- a vendor guarantee depends on an unverified tier or configuration; or
- operating, backup, restore, and incident ownership has no credible owner.
