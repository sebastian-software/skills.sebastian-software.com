# Framework Boundaries

The framework decides when code runs (build, request, stream, hydration) and where
modules land (server bundle vs client bundle). Treat those phases and that split as
explicit architecture inputs, and never assume one framework's RSC, routing, or
caching behavior is universal React behavior.

## Execution phases

- Map every module to the phase where it runs: build time (static generation,
  config), request time (server render, data loading, server actions), stream time
  (progressive flushing of HTML and RSC payload), and hydration time (client attaches
  event handlers). Code that reads a database belongs in request time; code that
  measures the DOM belongs in hydration time. Misplacing it is the root cause of most
  "works locally, breaks in prod" rendering bugs.
- Keep server-only modules out of the client graph. Import `server-only` in modules
  that must never ship to the browser so an accidental client import fails the build
  instead of leaking secrets or bloating the bundle. Use `client-only` for the inverse.
- Do not rely on request-time globals (headers, cookies, `searchParams`) inside code
  that the framework may statically prerender. Reading them forces dynamic rendering;
  decide that tradeoff deliberately rather than discovering it as an opt-out.

## App code vs reusable library code

- Point dependencies inward: reusable UI and domain libraries must not import from app
  routes, route loaders, or framework request context. Application code wires framework
  features to library components, not the reverse.
- Keep framework-coupled concerns (file-system routing, `next/*` or React Router
  loaders, server actions, env access) in the app layer. A component that imports
  `next/navigation` is app code, not a library primitive — extract the framework call
  to a prop or context so the component stays portable.
- Pass data and callbacks into shared components as props; do not let them reach into
  router or request state. This keeps them testable without a framework harness and
  reusable across Next.js, React Router, and Vite setups.

## Routing and data loading

- Treat routing, data loading, and server rendering as one coherent architecture, not
  three isolated library choices. Evaluate a router by how it co-locates data with
  routes, parallelizes loaders, handles pending/error UI, and revalidates — not by API
  surface alone.
- Load data at the route boundary (loader, server component, or route segment) so the
  framework can fetch in parallel and avoid client request waterfalls. Push fetches
  down into leaf components only when the data is genuinely leaf-local.
- Verify current React Router / Next.js loader and revalidation APIs against their docs
  before encoding version-specific behavior into rules; these surfaces change between
  majors.

## Server Actions and mutations

- Treat a server action as a server-side mutation endpoint, not just an `onSubmit`
  shortcut. Validate and authorize every input inside the action — the client cannot be
  trusted, and the action is independently reachable.
- After a mutation, invalidate the affected cache (e.g. `revalidatePath` /
  `revalidateTag` in Next.js) so the UI reflects new state; do not rely on client-side
  refetch alone.
- Make actions progressively enhanceable: bind them to a `<form action={...}>` so the
  flow works before hydration, and layer `useActionState` / `useFormStatus` for pending
  and error feedback on top. Return serializable results and field-level errors rather
  than throwing for expected validation failures.
- Confirm the framework's current behavior for redirects, error propagation, and
  closures-over-server-values before relying on them; action semantics are
  framework-version-specific.
- Guard sensitive mutations against duplicate execution: make them idempotent, or dedupe
  by request key, so a double submit, retry, or replayed action does not charge, send, or
  create twice.

## CSS and asset delivery

- Choose styling that survives the server/client boundary. Build-time CSS (CSS Modules,
  compiled/zero-runtime CSS, Tailwind) works in server components; runtime
  CSS-in-JS that needs a client context or React hooks generally cannot render inside a
  server component without a client wrapper. Decide this before picking a styling lib.
- Code-split heavy or below-the-fold client components with the framework's dynamic
  import so their JS and CSS load on demand. Gate browser-only widgets (maps, editors)
  behind a client boundary and, where supported, disable SSR for them rather than
  fighting hydration.
- Coordinate asset priority with render timing instead of treating assets as a pure
  component concern: preload fonts and LCP images, set `fetchpriority`/`rel=preload`
  for critical resources, and let the framework hoist and dedupe `<link>`/`<script>`
  so discovery is not blocked by hydration. Defer to `s7n-web-performance` for budgets.

## Observability

- When an architecture decision needs production evidence (is this slow at request time
  or hydration time?), emit `Server-Timing` headers from loaders/actions and read them
  in browser devtools or RUM. Measure before changing rendering strategy.

## Review checklist

- Is each module placed in the correct phase (build / request / stream / hydration),
  and are server-only modules fenced off from the client graph?
- Do dependencies point inward — does any reusable component import app routes, loaders,
  or framework request context?
- Is data loaded at the route boundary in parallel, without client waterfalls?
- Do server actions validate, authorize, invalidate cache, and work without JS?
- Is the styling approach compatible with server components, and are heavy client
  widgets code-split behind a boundary?
- Are framework-specific loader/action/cache APIs verified against current docs rather
  than assumed universal?
