# Rendering Performance

Optimize React rendering by finding the actual source of work before adding memoization.

## Working Rules

- Identify what changed, which component re-rendered, and whether the render was expensive.
- Use memoization only when it removes real repeated work or stabilizes meaningful props.
- Use deferred rendering and transitions when user input needs to stay responsive.
- Avoid architecture that spreads high-churn state through broad context or global rerender paths.

## Additional Rules

- Use useMemo/useCallback guidance to explain when memoization stabilizes real work and when it adds noise.
- Use as React re-render mental-model guidance: identify state changes and render paths before optimizing.
- Use deferred rendering for keeping input responsive when derived UI work is expensive.
- Use signals comparison as state-model tradeoff context, not a recommendation to replace React state.
- Duplicate/supporting useDeferredValue guidance for rendering responsiveness.
- Use as React Compiler mental-model and caveat material. Treat the compiler as a rendering optimization aid, not a substitute for clear state ownership, stable component boundaries, or measuring actual render work.
- Use as React Compiler roadmap/radar context only. Verify current React/compiler docs before changing lint rules, memoization policy, or build assumptions.
