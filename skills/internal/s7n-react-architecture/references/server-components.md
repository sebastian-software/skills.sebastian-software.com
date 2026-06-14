# Server Components

Use React Server Components to move data access and non-interactive rendering work to the server while keeping client components focused on interactivity.

## Working Rules

- Put data access and server-only dependencies behind server boundaries.
- Keep client components small and purposeful when interactivity is needed.
- Treat serialization, streaming, caching, and framework constraints as architecture inputs.
- Verify current framework support before copying examples across Next.js, React Router, Vite, or custom RSC setups.

## Additional Rules

- Use React Server Components mental-model for server/client split, data access, and interactivity boundaries.
- Use React WG RSC from-scratch discussion as mental-model for RSC protocol and boundaries.
- Use React 19 impossible-components as RSC capability/risk context, not as a blanket implementation rule.
- Use as React Router/Vite RSC implementation context; verify current framework support before copying APIs.
- Use frameworkless RSC as mental-model and caveat material, not default app architecture.
- Use as RSC explainer and caveat guidance; pair with React WG/framework docs.
