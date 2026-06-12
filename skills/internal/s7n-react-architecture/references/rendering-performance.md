# Rendering Performance

Optimize React rendering by finding the actual source of work before adding memoization.

## Working Rules

- Identify what changed, which component re-rendered, and whether the render was expensive.
- Use memoization only when it removes real repeated work or stabilizes meaningful props.
- Use deferred rendering and transitions when user input needs to stay responsive.
- Avoid architecture that spreads high-churn state through broad context or global rerender paths.

## Source-Backed Guidance
### Understanding useMemo and useCallback

- Things ID(s): `RHnL73NybKR7CFZNWzPL4z`, `UqpfDAEKj8biMYQSZ6Fx4e`
- Source: <https://www.joshwcomeau.com/react/usememo-and-usecallback/>
- Decision: `secondary`
- Target: `rendering`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use useMemo/useCallback source to explain when memoization stabilizes real work and when it adds noise.
### Why React Re-Renders

- Things ID(s): `JE8s9BXuvL7hLwXSbaQAnh`, `KPYLd3VZiNWcYB6Wd1hCZQ`
- Source: <https://www.joshwcomeau.com/react/why-react-re-renders/>
- Decision: `primary`
- Target: `rendering`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use as primary React re-render mental-model source: identify state changes and render paths before optimizing.

