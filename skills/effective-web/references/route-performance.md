# Web Performance

Use this skill for browser-facing performance work where implementation choices affect loading, rendering, network discovery, perceived speed, or Core Web Vitals.

## Workflow

1. Identify the measured problem first: LCP, CLS, INP, blocking resources, image bytes, caching, resource discovery, or perceived loading state.
2. Inspect the app stack, rendering mode, image pipeline, CDN/cache behavior, framework defaults, and current measurement tools.
3. Apply the narrowest useful fix: image markup, preload/resource discovery, cache freshness, layout reservation, dynamic import boundaries, font loading, or interaction work.
4. Verify with local browser tools and project checks. Prefer measured before/after evidence over theoretical optimization.
5. Explain tradeoffs: freshness vs cache reuse, bytes vs variants, above-the-fold priority vs preload overuse, visual polish vs rendering stability.

## Reference Files

- [browser-performance.md](browser-performance.md) - Browser performance rules for images, LCP, preload behavior, caching, and perceived loading.

## Boundaries

Do not use this skill as a marketing SEO audit. Cross-reference SEO only when performance affects crawlable content, Core Web Vitals, metadata delivery, or social/media assets.

Do not treat security headers as performance work unless transport, caching, or policy choices directly affect loading behavior.
