# Async and Errors

## Own Every Promise

A promise represents work in flight; leaving it unowned drops errors and hides
ordering. Every promise must be awaited, returned to a caller who owns it, or
given a deliberate `.catch`/`.then` handler. The rules that change decisions:

- a floating promise is a defect — an unhandled rejection can crash a Node
  process under `unhandledRejection`, and its error is invisible to callers;
- do not fire an `async` function for its side effect without handling failure;
  if the work is intentionally detached, give it an explicit error sink and say
  why the result is not awaited;
- use `Promise.all` when independent work should proceed concurrently, but know
  it rejects on the first failure and leaves siblings running — use
  `Promise.allSettled` when every result matters, and bound concurrency instead
  of launching an unbounded fan-out over a large input.

## Propagate Cancellation, Do Not Orphan Work

Model cancellation with `AbortSignal` rather than letting a timed-out or
superseded operation continue. Accept an optional `signal`, pass it into
`fetch`, timers, and downstream calls, and check `signal.aborted` or listen for
`abort` at await points that can leave partial state. Treat the resulting
`AbortError` as an expected outcome, not a failure to log as an error. A timeout
implemented by ignoring a late result still consumes the resource; cancel it.

## Prefer Typed Failure to Thrown Anything

`throw` accepts any value, and a caught value is `unknown` — it may not be an
`Error`. Decide how a given failure is represented:

- for expected, handleable outcomes (validation, not-found, conflict), prefer a
  typed result (a discriminated union of success and failure) or a typed error
  the caller can branch on, over a bare string or a generic thrown `Error`;
- reserve `throw` for genuinely exceptional conditions and programmer errors;
- when wrapping a lower-level failure, preserve the original with the `Error`
  `cause` option instead of flattening it into a string, so the chain survives
  for diagnostics;
- in a `catch`, narrow `unknown` before use (`instanceof Error`, a type guard);
  do not assume `err.message` exists.

## Keep Errors Useful at Boundaries

At a service, CLI, queue, or FFI boundary, translate internal errors once into
the stable external contract. Preserve the actionable cause, the affected
operation, and safe recovery information without leaking secrets, stack detail,
or unstable internal shapes to an external caller. Do not log-and-rethrow the
same error at every layer; choose the layer that owns the operational event and
preserve the source chain for the rest.

## Handle Backpressure and Blocking Honestly

For streaming or high-volume work, respect backpressure: await a stream's drain
or use the async-iterator protocol rather than buffering an unbounded queue in
memory. Do not block the event loop with synchronous CPU-heavy work on a request
path; move it to a worker, a queue, or a bounded batch using the repository's
established mechanism. Bound queues, retries, and concurrency from an actual
resource constraint, and define overload behavior rather than assuming infinite
capacity.
