# Model-Tiered Orchestration

Separate roles by reasoning demand instead of assigning one model tier to the
entire port. Map current vendor-specific models onto these roles from measured
capability, price, latency, and tool reliability; do not hard-code brand names
or assume that a model's marketing tier predicts performance on this codebase.

## Default Role Ladder

| Role | Default capability | Responsibility |
| --- | --- | --- |
| Architect | Highest justified tier | Establish migration contract, semantic mappings, dependency boundaries, pilot, work packets, risk policy, and milestone audits. |
| Builder | Efficient middle tier | Implement one bounded slice from explicit source files, mapping rules, acceptance checks, and exclusions. |
| Evidence owner | Deterministic tools; normally the builder or integrator | Run specified checks, inspect diff hygiene, detect stubs or test weakening, classify failures, and assemble evidence. |
| Specialist reviewer | Highest justified tier for the risk | Review ownership, concurrency, FFI, security, parsers, numeric semantics, or cross-shard changes that exceed routine review. |

Do not assign a second model merely to repeat the builder's inspection. Prefer
scripts, compilers, tests, linters, sanitizers, and structural diff checks
whenever they can answer the question deterministically. Add one independent
model reviewer only when a fresh semantic judgment is proportionate to the
risk, deterministic evidence cannot close the question, or measured evaluations
show that the extra pass finds defects worth its cost.

Low price and availability are not evidence of review value. Reject a default
architect → builder → cheapest-reviewer loop for every batch; use the builder's
cold pass plus deterministic evidence until a named risk or measured result
justifies an independent reviewer.

## Architect Cadence

Use the architect:

1. before implementation to define the contract and pilot
2. after the pilot to correct mappings and choose delivery shape
3. at dependency-boundary or risk-weighted milestones
4. when repeated failures suggest a flawed shared rule
5. before integrating shards that changed cross-cutting behavior
6. before declaring parity, merging, or recommending release

Do not require the architect to reread every implementation transcript. Give it
a milestone packet containing:

- migration-contract revision and approved differences
- source and target revisions
- concise diff or changed-boundary inventory
- gates run, exact results, and test-count deltas
- new unsafe, FFI, concurrency, suppression, skip, or compatibility-shim changes
- unresolved failures, uncertainty, and builder, evidence, or reviewer disagreements
- baseline-versus-current performance and resource measurements when relevant

Trigger architect review by risk and boundary completion, not only by a fixed
number of files. A ten-line lifetime change may deserve review sooner than a
thousand lines of generated mappings.

## Builder Work Packet

Give the builder enough structure that implementation does not require
reconstructing architecture:

- one owned behavior slice and exact source files
- target files it may edit and files it must not touch
- relevant semantic mapping rules and approved exceptions
- expected inputs, outputs, errors, cleanup, and platform behavior
- one failing diagnostic or acceptance fixture
- narrow validation commands
- explicit prohibition on stubs, test weakening, blanket suppressions, unrelated
  redesign, and unapproved public behavior changes
- escalation conditions

If the packet cannot be made this concrete, keep the work with the architect or
split the slice further.

## Evidence Packet

Ask the evidence owner to return facts, not a broad quality opinion:

- commands executed and exact results
- changed tests, fixtures, skips, ignores, assertions, and suppressions
- new TODOs, placeholders, dummy paths, unsafe blocks, broad catches, or silent
  fallbacks
- source-to-target surface inventory for the owned slice
- likely failure cluster and the check that would close it
- items requiring semantic or specialist review

For an independent model review, use a cold diff view without the builder's
justification when possible. Keep that review focused on a concrete high-risk
question; it supplements deterministic evidence and must not waive contract
gates.

## Escalation Policy

Escalate from builder or evidence owner to the architect or specialist when:

- source behavior is ambiguous or conflicts with the migration contract
- the change crosses ownership, async callback, GC/native, FFI, security, parser,
  persistence, or concurrency boundaries
- a public API, protocol, error, timing, or ordering behavior may change
- the builder needs a new abstraction or cross-shard edit
- the same root cause survives two attempted fixes
- tests disagree across platforms or pass only with timing, retry, or fixture
  changes
- deterministic evidence is missing, contradictory, or suspiciously reduced

Do not escalate routine syntax and known-pattern translation merely because the
diff is large. Do not leave a high-risk change on a cheap path merely because
the diff is small.

## Cost and Quality Feedback Loop

Track by role and slice:

- accepted batches without rework
- defects found by deterministic gates, specialist review, architect, CI, and
  post-integration checks
- tokens or cost, latency, and human intervention
- recurring failure classes by model tier

Promote a task class to a stronger model when downstream rework costs more than
the savings. Demote stable, well-specified patterns after repeated clean batches.
Re-evaluate model assignments when models, prices, prompts, or repository
structure change.

The useful optimization target is verified behavior per total cost and elapsed
time, including review and rework.
