# Rendering Performance

Find the actual source of rendering work before adding memoization. Most React
performance problems are state placed too high or unstable boundaries, not missing
`useMemo`. Diagnose with the Profiler, then fix the cause.

## What actually causes re-renders

- A component re-renders when its own state changes, when its parent re-renders, or
  when a context it consumes changes value. Props changing does not by itself trigger a
  render — the parent rendering does. Identify which of these three fired before
  reaching for a fix.
- A parent re-render re-renders all descendants by default, regardless of whether their
  props changed. `React.memo` stops that propagation only when the memoized component's
  props are referentially stable — so memo on a child that receives a fresh inline
  object or callback each render does nothing.
- New object, array, and function literals created in render are fresh references every
  time. They break `memo`, and they invalidate `useEffect`/`useMemo` dependency arrays.
  This — not raw render count — is what turns a cheap tree into wasted work.
- Measure with the React Profiler: record an interaction, find which components rendered
  and why ("Why did this render?"), and confirm a render is actually expensive before
  optimizing. A component that renders often but cheaply usually needs no change.
- First confirm the bottleneck is React render work at all. A slow interaction may be
  JavaScript outside React, layout/paint, network, hydration, or backend latency — check
  the browser Performance panel before assuming the fix lives in memoization.

## Move state and split components before memoizing

- The cheapest fix for over-rendering is to move state down to the smallest component
  that needs it, or lift the expensive subtree up as `children` so it is created once
  in the parent and passed through (a re-rendering parent does not re-render `children`
  it received as props). Restructure before memoizing.
- Colocate state with its consumers. State sitting higher than necessary re-renders
  unrelated siblings on every change; pushing it down often removes the need for any
  memoization at all.
- Derive values during render instead of storing them in state and syncing with effects.
  Redundant state plus a sync effect causes extra render passes and stale-value bugs.

## When to memoize, and when not to

- Use `useMemo` for a genuinely expensive computation, or to stabilize a reference that
  feeds a dependency array or a `memo`'d child. Use `useCallback` for the same
  stabilization reason for functions. Do not wrap trivial scalars or cheap expressions —
  the bookkeeping and dependency array cost more than the work saved and add noise.
- Memoization only pays off when the whole chain is stable: a `memo` child needs every
  prop stable, including callbacks (`useCallback`) and object props (`useMemo`). One
  unstable prop defeats the entire memo. Stabilize the chain or do not bother.
- Prefer the React Compiler (auto-memoization) over hand-written `useMemo`/`useCallback`
  where the project supports it; let it handle mechanical memoization so code stays
  readable. Treat it as an optimization aid, not a substitute for correct state
  ownership, stable boundaries, or measuring real work — and verify its current rules
  and assumptions against React docs before relying on them.

## Keeping input responsive

- When typing or another high-frequency input drives expensive derived UI (large filtered
  lists, charts), keep the input itself controlled and synchronous, and wrap the
  expensive derived render in `useDeferredValue` so the input stays responsive while the
  heavy view catches up. This is the first tool for "the search box lags while typing".
- Wrap non-urgent state updates triggered by an interaction in `useTransition` (or
  `startTransition`) so React can keep the UI interactive and show pending state instead
  of blocking on the update. Use it for tab switches, navigation, and filter applies.
- Reach for deferral and transitions before memoization when the complaint is input lag;
  they attack latency directly, whereas memoization only reduces wasted renders.
- Use `useOptimistic` for immediate UI feedback during a pending mutation only when the
  rollback and retry path on failure is clear; without defined failure handling it leaves
  the UI showing state that never committed.
- Read pending state with `useFormStatus` inside design-system submit controls rather than
  prop-drilling a `pending` flag from the parent form; the control subscribes to its
  enclosing `<form>` directly.
- When unwrapping a Promise with `use()` during render, read a framework- or cache-owned
  promise. Do not create a new uncached promise in render — it is recreated every render
  and re-suspends instead of resolving.

## Context and global state architecture

- Do not route high-churn state (cursor position, text input, scroll) through a wide
  context — every consumer re-renders on every change. Split contexts by update
  frequency: a stable "API"/dispatch context separate from a fast-changing "value"
  context, so components that only dispatch never re-render on value changes.
- Keep context values referentially stable with `useMemo`; an unmemoized object value
  re-renders all consumers whenever the provider renders, defeating the split above.
- For broad, frequently-updated shared state, prefer an external store with selector
  subscriptions (e.g. `useSyncExternalStore`-based) so each component re-renders only
  when its selected slice changes, instead of forcing a context-wide render. Fine-grained
  reactive/signal models are a valid tradeoff to understand here, not a mandate to
  abandon React state.

## List virtualization

- Virtualize long or unbounded lists (windowing) so only visible rows mount; rendering
  thousands of DOM nodes is a layout and memory cost that no memoization removes.
  Provide stable, accurate item `key`s and avoid index keys for reorderable data so
  React reuses DOM correctly. Defer to [Data Tables route](route-tables.md) for table-specific rendering.

## Review checklist

- Was the Profiler used to confirm which component re-rendered and that it is actually
  expensive — before any optimization?
- Can the problem be fixed by moving state down, colocating it, or passing the subtree as
  `children` instead of memoizing?
- Are `useMemo`/`useCallback` used only for expensive work or reference stability, with
  the whole prop chain stabilized rather than one link?
- Is input lag addressed with `useDeferredValue` / `useTransition` rather than blanket
  memoization?
- Are contexts split by update frequency, values memoized, and broad hot state moved to a
  selector-based store?
- Are long lists virtualized with stable keys?
