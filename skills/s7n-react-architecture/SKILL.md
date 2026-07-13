---
name: s7n-react-architecture
description: |
  This skill should be used when the user asks about "React Server Components", "server and client component boundaries", "React rendering performance", "hydration", "Suspense", "streaming", "useMemo", "useCallback", "React re-renders", "server actions", or "Next.js React architecture". It covers RSC mental models, rendering boundaries, data and state placement, hydration, memoization, and architecture tradeoffs.
license: MIT
metadata:
  author: sebastian-software
  version: "1.0"
---

# S7N React Architecture

Use this skill for React architecture decisions that affect rendering, server/client boundaries, data flow, hydration, streaming, or performance.

## Workflow

1. Identify the runtime and framework: React version, Next.js/Remix/React Router/Vite, server rendering mode, RSC support, and deployment target.
2. Separate architecture work from component craft. Use `s7n-react-component` when the task becomes reusable UI implementation.
3. Choose data and state placement deliberately: server, client, URL, cache, form, external store, or component local state.
4. Define server/client boundaries by data access, interactivity, serialization, bundle cost, and ownership.
5. Diagnose rendering work before optimizing: re-render source, expensive child, context churn, memoization cost, hydration mismatch, or network waterfall.
6. Prefer clear architecture over premature memoization or framework-specific cleverness.

## Reference Files

- [references/server-components.md](references/server-components.md) - RSC mental model, boundaries, and framework caveats.
- [references/rendering-performance.md](references/rendering-performance.md) - Re-renders, memoization, hooks, and UI responsiveness.
- [references/framework-boundaries.md](references/framework-boundaries.md) - Next.js, Vite, React Router, Server-Timing, and CSS/runtime boundaries.

## Boundaries

Do not use this skill for visual design or generic component APIs unless rendering architecture is the primary issue. Cross-reference `s7n-ui-design`, `s7n-react-component`, `s7n-web-performance`, and `s7n-frontend-testing` as needed.
