# React Performance Priorities

Optimize React and framework code in impact order. Do not start with memoization
or JavaScript micro-optimizations when the page still has network waterfalls,
unnecessary client code, or unsafe server state.

## Priority Order

1. Eliminate network and async waterfalls.
2. Reduce initial and route-level JavaScript and CSS.
3. Fix server rendering, serialization, cache, and request-isolation problems.
4. Deduplicate client fetching, subscriptions, and persistent browser state.
5. Diagnose and reduce expensive React renders.
6. Improve browser rendering and long-list cost.
7. Apply measured JavaScript micro-optimizations last.

Measure before and after. A lower-priority change may still matter when evidence
shows it is the actual bottleneck, but the priority order prevents polishing
cheap loops while critical-path work remains serial.

## Async Dependency Graph

- Start independent work early and await it as late as correctness permits.
  Move `await` into the branch that consumes the result instead of blocking
  return paths that do not need it.
- Use `Promise.all` for independent operations. For partial dependencies, chain
  each dependent operation from its own prerequisite so one slow item does not
  delay unrelated work.
- Restructure server-component siblings and route loaders so independent data
  starts concurrently. Add scoped Suspense boundaries when streaming a stable
  shell improves the experience.
- Do not introduce a dependency solely to express a small dependency graph that
  native promises can state clearly.

## Bundle and Discovery

- Prefer direct, statically analyzable imports and explicit maps of allowed
  dynamic modules. Paths assembled too dynamically widen bundles, file tracing,
  cold starts, and build work.
- Split heavy editors, maps, charts, and below-the-fold interactive features at
  route or interaction boundaries. Load optional modules only when activated.
- Preload optional code on meaningful intent such as pointer hover or keyboard
  focus only when the likely benefit exceeds bandwidth and memory cost.
- Defer non-critical analytics and support widgets so they do not compete with
  the primary interaction. Verify framework-specific import optimization before
  replacing every barrel import mechanically.

## Server State and Caches

- Treat module scope on a server as process-wide. Never put request-scoped
  mutable user, tenant, permission, locale, or transaction state in a module
  variable; concurrent requests can leak data across users.
- Distinguish per-request deduplication from cross-request caching. Define cache
  lifetime, key, tenant and authorization boundaries, invalidation, maximum
  size, and failure behavior before adopting a shared cache.
- Authenticate and authorize server actions inside the action. A page, layout,
  or middleware guard does not make a directly callable mutation safe.
- Minimize data crossing server-to-client boundaries. Send the fields the client
  uses and keep non-interactive transformation or rendering on the server unless
  moving work prevents materially duplicated serialization.
- Treat framework cache, background-work, and post-response APIs as
  version-specific. Verify current official documentation before encoding them.

## Client Ownership

- Deduplicate global event listeners and network subscriptions at their owning
  boundary instead of registering one listener per component instance.
- Version persistent browser-storage keys, store only the required non-sensitive
  fields, validate parsed data, and handle unavailable storage, quota, and schema
  migration failures.
- Use passive touch and wheel listeners only when the handler never calls
  `preventDefault`; semantic correctness comes before the scrolling hint.
- Prefer URL, server, form, or cache ownership over copying the same state into
  component state and synchronizing it with effects.

## Review Checklist

- What measured user-visible cost is being reduced?
- Does any independent work still wait for an unrelated `await`?
- Is heavy or optional code discoverable and loaded only when needed?
- Can request data cross users through module-level mutable state or a cache key?
- Are cache scope, invalidation, authorization, and failure behavior explicit?
- Is browser persistence minimal, versioned, validated, and recoverable?
- Did the proposal jump to memoization or loop tuning before higher-impact work?
