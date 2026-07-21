# Rust Testing

Rust's native test organization gives useful placement choices. Select among
them from the claim and the crate's current conventions; property, snapshot,
and replay technique selection remains in [Select test evidence](select-test-evidence.md).

## Place Evidence at the Right Visibility

- Put unit tests in the source module when they protect module-local behavior,
  private invariants, parsing, transformation, or state transitions. Keep them
  close to the code whose contract they explain.
- Put integration tests in the crate's `tests/` directory when the public API,
  crate wiring, feature combination, or externally observable behavior is the
  claim. Treat that directory as a consumer: use public APIs rather than
  reaching into private implementation details.
- Use doctests for concise public examples that are part of the API contract
  and should keep compiling. Keep their setup small and do not force a doctest
  to exercise credentials, timing, or a multi-process environment.

Prefer existing crate layout, feature-gating, test helpers, async runtime
setup, and commands. Rust does not require a particular test crate, property
library, snapshot library, or test runner to make this distinction useful.

## Test Public Behavior and Failure Semantics

For a public client, protocol, parser, or library, define the caller-visible
contract: returned values, errors, cancellation or timeout behavior, message
ordering, feature availability, and state after failure. Use a deterministic
transport fixture or replay when protocol sequencing is the risk. Keep an
irreducible mock at the outer transport boundary and document why a replay,
local implementation, or focused integration path cannot provide the evidence.

Use values and type-safe helpers that make identity, time, and expected state
obvious. Do not test borrow layout, private helper calls, or incidental
allocation choices unless those are explicitly part of the supported contract.

## Keep Live Smoke Tests Deliberately Opt-In

Credentialed, billable, remote, destructive, or flaky live checks are useful
smoke evidence only when clearly gated by the repository's existing mechanism:
an explicit environment flag, ignored test convention, dedicated CI job, or
separate command. Fail clearly when an opted-in environment is incomplete;
never make ordinary local or CI test runs depend on a secret or live account.

Report the deterministic local evidence separately from optional live evidence.
The normal test suite should still protect behavior through direct tests,
fixtures, local services, or replays.
