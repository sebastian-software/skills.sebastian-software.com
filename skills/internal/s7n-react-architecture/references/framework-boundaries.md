# Framework Boundaries

Use framework features deliberately. Rendering mode, routing, data fetching, CSS delivery, Server-Timing, and build constraints shape React architecture.

## Working Rules

- Check what the framework does at build time, request time, stream time, and hydration time.
- Keep CSS and styling choices compatible with server/client boundaries.
- Use observability such as Server-Timing when architecture decisions need production feedback.
- Avoid treating one framework's RSC or routing behavior as universal React behavior.
- Verify exact framework versions before copying examples for Server Actions, RSC, streaming, asset loading, cache invalidation, or route loaders.
- Keep browser resource discovery coordinated with framework abstractions; framework image/script/font helpers still need LCP, preload, and cache review.

## Framework Decision Checklist

- Which React version is installed, and which framework features are stable in this version?
- Does the route render at build time, request time, stream time, or only on the client?
- Where does data load: server component, route loader, client query, action, cache, or edge function?
- How are mutations validated, authorized, retried, and reflected in cached UI?
- How are errors represented: thrown responses, error boundaries, not-found boundaries, form state, or toast state?
- How are CSS, fonts, images, scripts, and metadata discovered by the browser?
- Can the chosen pattern be observed in production with Server-Timing, logs, traces, RUM, or framework analytics?

## React vs Framework APIs

React provides primitives such as Server Components, Suspense, Actions, transitions, `use`, and form-related hooks. Frameworks decide how those primitives connect to routing, bundling, server execution, caching, redirects, deployment, and invalidation.

Do not write skill guidance that assumes:

- Next.js Server Actions work the same way as React Router, Remix, Vite, or custom RSC setups.
- A framework's cache invalidation model is part of React itself.
- A route loader, server function, edge runtime, or server action has the same security and deployment constraints across frameworks.
- A framework image/font/script helper automatically solves LCP or preload discovery.

## Additional Rules

- Use as framework-site architecture example, not as universal Next.js guidance.
- Use CSS-in-RSC for styling constraints across server/client boundaries.
- Use as dynamic component/CSS architecture guidance, with framework and browser-support caveats.
- Use framework-boundary caveat for Next.js vs React fundamentals.
- Use as React asset-loading radar/context. Keep asset priority, preload, discovery, and render timing coordinated with browser-performance rules rather than treating asset loading as only a component concern.
- Use as Next.js Server Actions capability context. Before adopting patterns, verify current framework behavior around validation, auth, redirects, cache invalidation, error handling, progressive enhancement, and form semantics.
- Use as Server Actions update/radar guidance. Treat API changes as framework-version-specific and pair with Next.js docs before encoding rules.
- Use as React Router architecture tradeoff context: routing, data loading, server rendering, and framework features should be evaluated as a coherent app architecture, not as isolated library preferences.
- Use as React Router feature-radar context. Verify current React Router docs before relying on specific APIs in skill guidance.
- Use as framework comparison context. Capture tradeoffs around routing, data loading, server rendering, deployment model, ecosystem maturity, and team familiarity instead of turning one framework into a default.
