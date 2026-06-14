# Framework Boundaries

Use framework features deliberately. Rendering mode, routing, data fetching, CSS delivery, Server-Timing, and build constraints shape React architecture.

## Working Rules

- Check what the framework does at build time, request time, stream time, and hydration time.
- Keep CSS and styling choices compatible with server/client boundaries.
- Use observability such as Server-Timing when architecture decisions need production feedback.
- Avoid treating one framework's RSC or routing behavior as universal React behavior.

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
