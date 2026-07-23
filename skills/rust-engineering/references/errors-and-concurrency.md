# Errors and Concurrency

## Separate Expected Failure from Defects

`Result` for handleable failure and `Option` for genuine absence is baseline;
the rules that change decisions are to not erase a meaningful failure into
`None`, to preserve a typed error when callers must branch, and to add context
at boundaries that identify the failed operation or resource. Do not log and
return the same error at every layer — choose the layer that owns the
operational event and preserve the source chain for diagnostics.

Use `unwrap` or `expect` only when failure would prove a programmer error or a
locally established invariant, with an assertion or `expect` message that states
the invariant rather than a generic claim that the value "should exist". Do not
ban these methods mechanically in tests, prototypes, generated code, or proven
invariant boundaries; review whether the proof remains valid instead.

## Make Numeric Failure Explicit

Choose checked, saturating, wrapping, or overflowing arithmetic from the domain
contract. Do not rely on debug-versus-release overflow differences. Use fallible
conversions when range or sign can change, and test the boundary values that
justify the chosen behavior.

## Design Async Work for Cancellation

Treat every `.await` as a possible cancellation and interleaving point. Identify
which state may already have changed, which resource must be released, and
whether retrying is safe. Keep guards and partially initialized state owned so
drop behavior leaves a valid result.

- Do not hold a synchronous mutex guard across any `.await` point.
- Use an async-aware lock only when the protected operation genuinely spans an
  await; otherwise shorten the critical section or move awaited work outside.
- Bound queues, tasks, retries, and concurrency from an actual resource or
  workload constraint. Define backpressure and overload behavior.
- Give spawned work an owner, completion path, error path, and shutdown policy.
  Do not detach important tasks merely to satisfy a lifetime.
- Make blocking or CPU-heavy work explicit and use the repository's established
  runtime mechanism; do not assume Tokio or another executor.

Avoid task-local or global mutable state when a parameter or owned context makes
the dependency visible. If synchronization is required, document the protected
invariant rather than only naming the lock.

## Keep Errors Useful at Boundaries

At CLI, service, FFI, and task boundaries, translate internal errors once into
the stable external contract. Preserve actionable cause, affected operation,
and safe recovery information without leaking secrets or unstable internal
types. Do not use error strings as an internal branching protocol.
