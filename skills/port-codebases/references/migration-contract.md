# Migration Contract

Create this contract before scaling a port. Keep it in the response for a small
task or in the repository's existing plan, issue, or ADR conventions when it
must survive sessions.

## Port Decision

- **Problem:** Name the recurring failure class, platform requirement,
  maintainability constraint, or strategic benefit.
- **Alternatives:** Record why hardening, an adapter, or a partial replacement is
  insufficient or preferable.
- **Delivery shape:** Choose mechanical big-bang, incremental slices, or a
  hybrid. Identify the temporary architecture and its removal condition.
- **Authority:** Distinguish assessment, pilot, implementation, merge, and
  release authorization.

## Equivalence Boundary

Record:

- public APIs, protocols, file formats, CLI behavior, exit codes, error classes,
  and diagnostics to preserve
- ordering, timing, retry, cancellation, cleanup, and concurrency semantics
- supported operating systems, architectures, runtimes, and configurations
- compatibility fixtures, language-independent tests, differential oracle, or
  production traces used for comparison
- performance, memory, startup, binary size, and throughput budgets where they
  matter
- explicitly approved behavior changes and who approved them
- exclusions such as generated code, third-party libraries, or separately
  migrated subsystems

Treat undocumented source behavior observed by real callers as evidence, not
automatically as a contract. Decide whether to preserve it before encoding it.

## Semantic Mapping

Write short, executable rules for differences likely to cause plausible ports
that compile but behave incorrectly:

| Concern | Questions to settle |
| --- | --- |
| Ownership and cleanup | Who owns each allocation, handle, callback, and GC root? When must cleanup run exactly once? |
| Errors and unwinding | Which errors return, throw, abort, retry, or clean up partially initialized state? |
| Numbers and time | How do overflow, truncation, negative values, precision, epochs, and duration units differ? |
| Strings and bytes | Which encoding, normalization, invalid sequences, terminators, and slice units apply? |
| Concurrency | What are the ordering, atomicity, wakeup, cancellation, and re-entrancy guarantees? |
| Compile-time features | Does the target preserve source-side specialization, macro evaluation, assertions, and side effects? |
| FFI and callbacks | Which side owns pointers, pins objects, controls callback lifetime, and crosses threads? |
| Platform behavior | Which filesystem, socket, path, signal, and ABI differences require dedicated fixtures? |

## Gate Ladder

Define concrete pass conditions rather than broad phrases such as "tests look
good":

1. representative pilot matches the oracle
2. dependency graph and target toolchain validate
3. target compiles without unapproved stubs or blanket suppressions
4. critical entry points start and complete smoke paths
5. focused and differential suites pass
6. complete suite passes without reduced test counts
7. all supported platforms and configurations pass
8. applicable sanitizer, leak, race, fuzz, and benchmark gates pass
9. rollout and rollback path is verified

Attach an owner and exception decision to any gate that cannot run. A missing
gate is residual risk, not a pass.
