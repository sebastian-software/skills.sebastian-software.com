# Rust Testing

Rust's native test organization gives useful placement choices. Select among
them from the claim and the crate's current conventions; property, snapshot,
and replay technique selection remains in [Select test evidence](select-test-evidence.md).

The implementation contracts under test — ownership, numeric, cancellation, and
unsafe — are owned by `rust-engineering`; this reference covers only how to place
and shape the Rust test evidence that protects them.

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

Select boundary evidence from the demonstrated risk:

- exercise minimum, maximum, sign, narrowing, and overflow behavior when
  arithmetic or conversion is part of the contract;
- exercise cancellation at meaningful await boundaries and verify owned state,
  cleanup, retry safety, and task shutdown;
- cover supported feature combinations and `cfg` branches that change public
  behavior rather than assuming the default feature set represents the crate;
- reach for property tests, fuzzing, Miri, sanitizers, or concurrency
  exploration only when the repository supports the tool and the risk justifies
  it; `rust-engineering` owns the unsafe and FFI proof discipline those tools
  verify.

Do not add a property, snapshot, mock, async, or unsafe-testing dependency by
default. A focused example or table-driven test is often the clearest evidence.
Do not split one coherent behavior across tests merely to enforce an assertion
count; keep failures diagnosable and the protected contract visible.

## Keep Live Smoke Tests Deliberately Opt-In

Credentialed, billable, remote, destructive, or flaky live checks are useful
smoke evidence only when clearly gated by the repository's existing mechanism:
an explicit environment flag, ignored test convention, dedicated CI job, or
separate command. Fail clearly when an opted-in environment is incomplete;
never make ordinary local or CI test runs depend on a secret or live account.

Report the deterministic local evidence separately from optional live evidence.
The normal test suite should still protect behavior through direct tests,
fixtures, local services, or replays.
