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
### Snappy UI Optimization with useDeferredValue

- Things ID(s): `TaJ1j2aeDUqyMPcpXwJLwz`
- Source: <https://www.joshwcomeau.com/react/use-deferred-value/?from=newsletter>
- Decision: `secondary`
- Target: `rendering`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use deferred rendering source for keeping input responsive when derived UI work is expensive.
### Why You Don't Need Signals in React · Daishi Kato's blog

- Things ID(s): `V3w1qcYsno3Hum2irvYBsQ`
- Source: <https://blog.axlight.com/posts/why-you-dont-need-signals-in-react/?ck_subscriber_id=1866528194&utm_source=convertkit&utm_medium=email&utm_campaign=%E2%9A%9B%EF%B8%8F+This+Week+In+React+%23143%3A+RSC+Quiz%2C+useFormStatus%2C+Next.js+Website%2C+Panda+CSS%2C+useLayoutEffect%2C+Million.js%2C+Immer%2C+Super+Apps%2C+React-Three-Fiber%2C+Vite...%20-%2010625518>
- Decision: `secondary`
- Target: `rendering`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use signals comparison as state-model tradeoff context, not a recommendation to replace React state.
### Snappy UI Optimization with useDeferredValue

- Things ID(s): `MgrWB7C25KjVb5JSZiDzEQ`
- Source: <https://www.joshwcomeau.com/react/use-deferred-value/?ck_subscriber_id=1866528194&utm_source=convertkit&utm_medium=email&utm_campaign=%E2%9A%9B%EF%B8%8F%20This%20Week%20In%20React%20#185:%20React%20Conf,%20useDeferredValue,%20React%20Query,%20refs,%20Next.js%20after,%20mini-react,%20Astro,%20MDXTS,%20Radix,%20Solid,%20Redwood,%20Pigment,%20Apollo,%20Playwright,%20Re.Pack,%20RN-Model3D,%20RN%20perf,%20RN%20Video,%20VisionOS,%20LiveView,%20Anchor%20Positioning%20...%20-%2013902810>
- Decision: `secondary`
- Target: `react-architecture`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Duplicate/supporting useDeferredValue source for rendering responsiveness.

### React Compiler: It's Stranger Than You Think

- Things ID(s): `57vJhjeocJ8yQmaYmaFntU`
- Source: <https://m.youtube.com/watch?v=wnXGSwrOw80>
- Decision: `secondary`
- Target: `rendering`
- Transcript extraction: 2026-06-14, 6,289 words
- Guidance: Use as React Compiler mental-model and caveat material. Treat the compiler as a rendering optimization aid, not a substitute for clear state ownership, stable component boundaries, or measuring actual render work.

### What's next for the React Compiler?

- Things ID(s): `LZS2D9BTTAWTfcQ1sKc4PY`
- Source: <https://m.youtube.com/watch?v=qd5yk2gxbtg>
- Decision: `secondary`
- Target: `rendering`
- Transcript extraction: 2026-06-14, 2,800 words
- Guidance: Use as React Compiler roadmap/radar context only. Verify current React/compiler docs before changing lint rules, memoization policy, or build assumptions.
