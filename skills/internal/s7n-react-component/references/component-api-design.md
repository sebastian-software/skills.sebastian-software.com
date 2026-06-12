# Component API Design

Design React component APIs so composition, state, styling, and semantics remain predictable as components are reused.

## Working Rules

- Prefer clear composition over prop surfaces that encode every possible layout.
- Use polymorphic `as` APIs only when the semantic element truly must vary.
- Keep accessible names, roles, focus behavior, and disabled behavior explicit.
- Expose styling hooks without forcing consumers to know private DOM structure.

## Source-Backed Guidance
### Advanced React component composition

- Things ID(s): `ESpokt4xw8RoDmGhedyQer`
- Source: <https://frontendmastery.com/posts/advanced-react-component-composition-guide/>
- Decision: `secondary`
- Target: `react-api`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Advanced composition source for separating layout, behavior, and extension points in reusable React component APIs.

