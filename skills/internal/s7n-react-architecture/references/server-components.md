# Server Components

Use React Server Components to move data access and non-interactive rendering work to the server while keeping client components focused on interactivity.

## Working Rules

- Put data access and server-only dependencies behind server boundaries.
- Keep client components small and purposeful when interactivity is needed.
- Treat serialization, streaming, caching, and framework constraints as architecture inputs.
- Verify current framework support before copying examples across Next.js, React Router, Vite, or custom RSC setups.
- Do not confuse Server Components with Server Actions. `"use server"` marks server-callable functions, not ordinary Server Components.
- Keep values passed from server to client serializable and stable enough to hydrate predictably.
- Treat framework cache, invalidation, routing, mutation, and deployment behavior as part of the RSC design, not an implementation detail.

## React 19 Baseline

React 19 makes the high-level Server Components model stable for libraries and apps that use frameworks with RSC support. The lower-level bundler/framework APIs remain framework-sensitive and may require version pinning or Canary coordination for framework authors.

Use these rules:

- Use Server Components for data access, server-only dependencies, non-interactive rendering, and reducing client bundle size.
- Use Client Components for event handlers, browser APIs, local interactive state, effects, refs, and client-only libraries.
- Keep Client Component boundaries as low as practical. Do not mark broad layout trees as client components because one leaf needs interactivity.
- Pass data down from Server Components into Client Components; do not pass non-serializable objects, database clients, class instances, or server-only functions unless the framework explicitly supports the pattern.
- Use Suspense and streaming deliberately around latency boundaries so loading states appear where users expect them.
- Audit hydration mismatches from unstable data, locale/date differences, invalid HTML nesting, random values, browser-only branches, and extensions modifying HTML.

## Server Actions and Forms

Server Actions can simplify mutation flows when the framework supports them, but they are not a reason to bypass form semantics.

- Preserve real `<form>` behavior where possible.
- Use `useActionState`, `useFormStatus`, and `useOptimistic` when they reduce custom pending/error/optimistic state code.
- Validate authorization and input on the server even when the client performs optimistic updates.
- Define redirect, cache invalidation, error boundary, retry, and progressive-enhancement behavior before adopting a Server Action pattern.
- Keep sensitive mutations idempotent or guarded against duplicate submit where appropriate.

## Additional Rules

- Use React Server Components mental-model for server/client split, data access, and interactivity boundaries.
- Use React WG RSC from-scratch discussion as mental-model for RSC protocol and boundaries.
- Use React 19 impossible-components as RSC capability/risk context, not as a blanket implementation rule.
- Use as React Router/Vite RSC implementation context; verify current framework support before copying APIs.
- Use frameworkless RSC as mental-model and caveat material, not default app architecture.
- Use as RSC explainer and caveat guidance; pair with React WG/framework docs.
