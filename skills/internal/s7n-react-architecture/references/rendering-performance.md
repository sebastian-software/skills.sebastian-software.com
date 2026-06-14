# Rendering Performance

Optimize React rendering by finding the actual source of work before adding memoization.

## Working Rules

- Identify what changed, which component re-rendered, and whether the render was expensive.
- Use memoization only when it removes real repeated work or stabilizes meaningful props.
- Use deferred rendering and transitions when user input needs to stay responsive.
- Avoid architecture that spreads high-churn state through broad context or global rerender paths.
- Keep urgent input feedback separate from expensive derived UI.
- Use optimistic updates only when the failure/retry path is clear.
- Treat React Compiler as an optimization aid when available, not as a substitute for clean state ownership and measured performance.

## Diagnosis Order

1. Reproduce the slow interaction and record it with React DevTools Profiler, browser Performance panel, or production interaction attribution.
2. Identify whether the bottleneck is React render work, JavaScript outside React, layout/paint, network, hydration, or backend latency.
3. Find the state update that caused the work.
4. Narrow the subscribed/rendering subtree before adding memoization.
5. Memoize only when props are stable enough and the skipped work is meaningful.
6. Re-measure after the change.

## React 19 Tools

- Use Actions and async transitions to keep the current UI responsive during mutations.
- Use `useActionState` for form/action result state when it removes bespoke pending/error handling.
- Use `useFormStatus` inside design-system submit controls instead of prop drilling pending state from a parent form.
- Use `useOptimistic` for immediate feedback when rollback semantics are clear.
- Use `use` to read supported resources during render only when the promise/cache source is framework-compatible. Do not create uncached promises in render.
- Use improved hydration mismatch output to fix the root cause, not to suppress the warning.

## State Placement

- Keep high-churn local state close to the component that owns it.
- Use URL state for shareable navigation/filter/sort state.
- Use server/cache state for data fetched from the backend.
- Use context for low-churn cross-cutting values such as theme, auth shell, or design system settings; avoid broadcasting frequently changing list or form state through broad providers.
- Split contexts by update frequency when consumers do not need the same data.
- Use external stores only when subscription granularity or cross-tree coordination is a real need.

## Additional Rules

- Use useMemo/useCallback guidance to explain when memoization stabilizes real work and when it adds noise.
- Use as React re-render mental-model guidance: identify state changes and render paths before optimizing.
- Use deferred rendering for keeping input responsive when derived UI work is expensive.
- Use signals comparison as state-model tradeoff context, not a recommendation to replace React state.
- Duplicate/supporting useDeferredValue guidance for rendering responsiveness.
- Use as React Compiler mental-model and caveat material. Treat the compiler as a rendering optimization aid, not a substitute for clear state ownership, stable component boundaries, or measuring actual render work.
- Use as React Compiler roadmap/radar context only. Verify current React/compiler docs before changing lint rules, memoization policy, or build assumptions.
