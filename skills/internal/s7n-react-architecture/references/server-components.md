# Server Components

Use React Server Components to move data access and non-interactive rendering work to the server while keeping client components focused on interactivity.

## Working Rules

- Put data access and server-only dependencies behind server boundaries.
- Keep client components small and purposeful when interactivity is needed.
- Treat serialization, streaming, caching, and framework constraints as architecture inputs.
- Verify current framework support before copying examples across Next.js, React Router, Vite, or custom RSC setups.

## Source-Backed Guidance
### Making Sense of React Server Components

- Things ID(s): `2H1JnB15fxw9Kmu6y7C25e`, `Nhyw6TeAjQJu6QMw5miJb3`
- Source: <https://www.joshwcomeau.com/react/server-components/>
- Decision: `primary`
- Target: `rsc`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use as React Server Components mental-model source for server/client split, data access, and interactivity boundaries.
### RSC From Scratch. Part 1: Server Components · reactwg/server-compone

- Things ID(s): `6snSQEt4cge8xb2J9H1Ho6`, `Caze5uUvVn4cBWdHq7H8c9`
- Source: <https://github.com/reactwg/server-components/discussions/5>
- Decision: `primary`
- Target: `rsc`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use React WG RSC from-scratch discussion as primary mental-model source for RSC protocol and boundaries.
### React 19 lets you write impossible components | Mux

- Things ID(s): `2A7kzYTTWgXACBGMnjjGbH`
- Source: <https://www.mux.com/blog/react-19-server-components-and-actions>
- Decision: `secondary`
- Target: `rsc`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use React 19 impossible-components article as RSC capability/risk context, not as a blanket implementation rule.

