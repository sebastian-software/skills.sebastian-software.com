# Review and Verification

## Review Each Port Batch

Review against the source and contract, not against how confident the target
code appears.

1. Trace inputs, outputs, state transitions, cleanup, errors, and side effects in
   source and target.
2. Ask which target-language construct is only superficially equivalent. Check
   eager versus lazy evaluation, assertion behavior, overflow, rounding,
   iteration invalidation, destructor timing, aliasing, and callback ownership.
3. Trace early returns, partial initialization, exceptions, cancellation,
   re-entrancy, and asynchronous completion.
4. Inspect every unsafe or FFI boundary for pointer provenance, ownership,
   thread affinity, pinning, callback lifetime, and exactly-once cleanup.
5. Check platform and configuration branches, including release builds where
   debug assertions or instrumentation disappear.
6. Search for stubs, TODO implementations, dummy values, broad suppressions,
   disabled tests, modified fixtures, and newly unreachable paths.
7. Require a focused regression test for every discovered semantic mismatch
   when the behavior can be exercised deterministically.

Keep implementer and reviewer responsibilities distinct even when one agent
performs both sequentially. First identify and rank discrepancies; only then
apply fixes.

## Turn Failures into a Queue

Capture each failure with:

- exact command, platform, configuration, and source revision
- minimal diagnostic or failing fixture
- likely owning slice, without presenting the hypothesis as confirmed
- dependency on earlier failures
- verification command that will close the item

Cluster by root cause before assignment. Fixing one ownership rule or type
mapping may resolve hundreds of downstream errors; distributing every symptom
separately wastes resources and creates conflicting edits.

Regenerate the queue after structural changes. Never continue executing a stale
failure inventory merely because it is already partitioned.

## Verify in Increasing Scope

Use the narrowest decisive check first, then expand:

1. format, parse, or type check the changed slice
2. compile its package or dependency unit
3. run focused regression and differential fixtures
4. exercise the nearest public entry point
5. run dependent packages and integration tests
6. run the complete suite locally
7. run the supported CI matrix
8. run applicable release-mode, sanitizer, leak, race, fuzz, and benchmark gates

Do not repeatedly run the full suite while a narrow deterministic failure
remains. Do not declare parity from narrow checks once the queue is locally
green.

## Audit the Tests Themselves

Before merge, compare source and target branches for:

- test files, cases, assertion counts, fixtures, snapshots, and platform shards
- skip, ignore, quarantine, timeout, retry, and feature-gate changes
- code paths that return early or silently pass when infrastructure is missing
- CI jobs that were superseded, allowed to fail, or never scheduled
- sanitizers and coverage that appear enabled but do not instrument the new
  target code

Manually inspect enough CI output to prove that the suite ran. A green status is
evidence only after validating what produced it.

## Review the Process

Treat repeated defects as workflow feedback:

- Add a semantic mapping rule when multiple slices repeat the same translation
  mistake.
- Tighten task wording when agents optimize a proxy such as compilation by
  inserting stubs.
- Reduce batch size when reviews cannot reconstruct source behavior.
- Reduce parallelism when agents collide or integration dominates.
- Add isolation when tests exhaust shared memory, disk, sockets, or processes.
- Add a fixture or differential oracle when reviewers keep debating behavior.

Prefer repairing the process before generating more code with a known failure
mode.
