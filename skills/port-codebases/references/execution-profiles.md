# Execution Profiles

Choose a profile from the real bottleneck: reasoning, editing, compilation,
tests, integration, or review. Increase concurrency only when isolated work is
waiting and the verifier can absorb more output.

Choose concurrency here, then assign model tiers separately through
[Model-tiered orchestration](model-tiering.md). A Solo run can still alternate
architect, builder, and verifier models sequentially; a Parallel run need not
use the highest tier for every worker.

## Solo Profile

Use for constrained subscriptions, local models, expensive repositories, or
ports that cannot be safely partitioned.

- Work in one vertical slice at a time.
- Keep batches small enough to review source and target side by side.
- Run a cold review after implementation: inspect only the diff, source slice,
  migration contract, and failing evidence; disregard the implementation
  narrative.
- Alternate modes explicitly: implement, compact the evidence, review, fix,
  verify. A fresh context is helpful but not mandatory.
- Run narrow deterministic checks after every batch and the expensive full
  suite at scheduled checkpoints or before dependency-boundary integration.
- Cache builds and fixtures, reuse failure logs, and stop rerunning unchanged
  expensive checks.
- Prioritize high-risk seams and representative behavior over maximizing files
  translated per session.

Use the same correctness gates as larger profiles. Reduce batch size and
frequency of full checks before reducing validation depth.

## Paired Profile

Use when two contexts, agents, or alternating sessions are affordable.

- Assign one implementer and one adversarial reviewer. If possible, give the
  reviewer no implementation rationale.
- Let the reviewer compare source, target, contract, and tests; do not have it
  rewrite the code during the first review pass.
- Rotate roles between slices to reduce systematic blind spots.
- Share concise mapping rules and verified failures, not complete chat histories.
- Use one fixer after findings are triaged. Reject contradictory or speculative
  findings before editing.

For high-risk ownership, concurrency, crypto, parser, or FFI slices, add a
second focused review pass instead of increasing implementation parallelism.

## Parallel Profile

Use only when the dependency graph exposes independent ownership boundaries.

- Allocate one shard per crate, package, directory, platform, or test group.
- Give every shard exclusive file ownership or an isolated worktree. Maintain a
  single integration owner and queue.
- Prevent workers from using destructive shared-state commands, broad repository
  rewrites, or uncoordinated dependency changes.
- Bound CPU, memory, disk, process, and network-heavy tests. Do not let agent
  concurrency overwhelm the validation environment.
- Commit or checkpoint coherent batches with source-slice identity and exact
  validation evidence.
- Integrate in dependency order. Regenerate compiler and test failure queues
  after integration rather than distributing stale failures.

Parallelize review and test classification as well as writing. If review or CI
becomes the bottleneck, adding implementers decreases confidence and increases
rework.

## Budget Controls Shared by All Profiles

- Serialize stable rules into a concise migration contract instead of repeating
  the full repository context.
- Feed agents one owned slice and one failure class at a time.
- Prefer compiler diagnostics, focused diffs, stack traces, fixtures, and failing
  tests over broad prose.
- Deduplicate failures by root cause before assigning work.
- Use deterministic tools for inventories, formatting, code generation, and
  repeated comparisons where available.
- Escalate a slice to a stronger model or human specialist based on risk and
  repeated failure, not merely size.
- Measure useful throughput as verified behavior per cost and integration time,
  not generated lines or number of agents.

## Changing Profiles

Start Solo or Paired during contract creation and the pilot. Scale out only
after the pilot proves that slices are independent and the mapping rules work.
Scale down when failures cross shard boundaries, integration queues grow,
reviewers find repeated systematic mistakes, or resource contention makes tests
unreliable.
