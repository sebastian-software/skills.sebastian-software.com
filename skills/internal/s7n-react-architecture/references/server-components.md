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

