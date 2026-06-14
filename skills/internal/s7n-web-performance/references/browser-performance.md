# Browser Performance

Use measured browser behavior to guide performance changes. Prioritize fixes that improve user-visible loading, rendering stability, and interaction latency without making the system harder to maintain.

## Working Rules

- Keep LCP resources discoverable in initial HTML whenever possible.
- Do not lazy-load above-the-fold or likely-LCP images.
- Use responsive images to match rendered size and DPR without exploding variant count.
- Reserve media and widget space to avoid avoidable CLS.
- Use cache freshness directives deliberately; stale content can improve perceived speed only when the product can tolerate the freshness model.
- Treat placeholder techniques as perceived-performance tools, not substitutes for correct image delivery.
- Do not hide startup resources behind JavaScript, `data-src`, client-only rendering, or CSS backgrounds unless there is a deliberate preload/discovery plan.
- Use `fetchpriority="high"` narrowly for the actual likely LCP image; avoid broad preload/fetchpriority use that competes with CSS, fonts, or scripts.
- Keep responsive image variants pragmatic. Too few waste bytes; too many increase storage, generation work, and CDN cache fragmentation.
- Choose placeholder techniques such as blur-up, BlurHash, LQIP, or traced previews only after image sizing, compression, cache behavior, and LCP discovery are correct.
- Use Server-Timing or equivalent instrumentation when frontend symptoms may be caused by backend/rendering latency.
- For interaction-heavy tools, reduce perceived latency with local reads, optimistic writes, durable retry queues, and narrowly subscribed UI updates before chasing micro-optimizations.
- Keep high-frequency workflows keyboard-accessible and command-driven where appropriate; path length is part of perceived performance.
- Animate only when motion clarifies state or spatial origin. Prefer `transform` and `opacity`, keep durations short, and avoid layout-triggering properties in dense task surfaces.

## Performance Review Checklist

- Is the LCP element known from measurement, not guessed?
- Is the LCP image or text discoverable in initial HTML, correctly sized, and not lazy-loaded?
- Do `srcset` and `sizes` match rendered layout across viewport/container states?
- Are media dimensions, aspect ratios, and skeletons reserving stable space before content arrives?
- Are cache headers, `stale-while-revalidate`, and CDN behavior aligned with product freshness expectations?
- Are placeholders smaller than the problem they solve, cacheable where appropriate, and not delaying real image discovery?
- Do interaction-heavy flows show immediate local feedback without waiting for network confirmation?
- Are live updates scoped to the components and fields that changed rather than causing broad list or page re-renders?
- Do keyboard shortcuts, command palettes, or focused interaction paths reduce repeated task cost without hiding mouse/touch alternatives?
- Are state transitions limited to composited or paint-only properties, with layout-property animation avoided in long lists and dense work surfaces?
- Is the optimization verified with before/after evidence from browser tooling or production metrics?

## Measurement Policy

Measure before optimizing unless the problem is an obvious correctness issue such as a lazy-loaded LCP image.

- Use field data for user-impact decisions: RUM, CrUX, Search Console Core Web Vitals, or product analytics that report LCP, INP, and CLS.
- Use lab tools to debug and prevent regressions: Chrome DevTools Performance panel, Lighthouse, WebPageTest, Playwright traces, and framework profilers.
- Treat Lighthouse as a diagnostic tool, not the full truth. Lighthouse can measure LCP and CLS in lab conditions, but it cannot directly measure real INP because there is no real user input; use TBT as a lab proxy only.
- Prefer Chrome DevTools Performance panel for local Core Web Vitals debugging. The standalone Web Vitals extension ended support in 2025 after its core workflow moved into DevTools.
- Segment field data by page type, device class, geography, connection, and logged-in/out state when possible. A single aggregate score can hide the failing cohort.
- Verify changes with before/after evidence and include the metric, test conditions, and remaining uncertainty.

## Core Web Vitals Targets

Use the current stable Core Web Vitals set:

- **LCP:** good at 2.5s or less.
- **INP:** good at 200ms or less.
- **CLS:** good at 0.1 or less.

Evaluate at the 75th percentile, segmented across mobile and desktop where data is available. Do not treat one fast local run as proof that users are passing.

## LCP Debug Order

1. Confirm the actual LCP element in field/lab tooling.
2. Check server and document timing: TTFB, redirects, HTML streaming, and render-blocking resources.
3. Ensure the LCP resource is discoverable in initial HTML, not injected by JavaScript or hidden in a CSS background without a preload.
4. Ensure the LCP image is not lazy-loaded and has correct `srcset`, `sizes`, dimensions, and compression.
5. Use `fetchpriority="high"` only for the likely LCP resource, and avoid broad preloads that compete with CSS, fonts, or scripts.
6. Check font loading when the LCP is text.

## INP Debug Order

1. Identify the slow interaction from field attribution or manual reproduction.
2. Separate input delay, processing duration, and presentation delay.
3. Reduce long tasks, hydration cost, broad re-renders, expensive event handlers, layout thrash, and synchronous third-party work.
4. Keep urgent visual feedback local and immediate.
5. Move non-urgent work into transitions, idle periods, workers, or server boundaries when the stack supports it.

## CLS Debug Order

1. Identify which element shifted and what inserted, resized, or restyled it.
2. Reserve space for images, embeds, ads, banners, skeletons, and late-loaded widgets.
3. Avoid inserting content above existing content unless the action is user-initiated.
4. Match fallback and final font metrics with `font-size-adjust`, size-adjusted font faces, or restrained font loading.
5. Keep animations on transform/opacity rather than layout properties.

## Additional Rules

- Keep startup resources discoverable in HTML, avoid JS-injected startup scripts, do not lazy-load above-the-fold/LCP images through data-src, avoid hiding LCP images in CSS backgrounds unless preloaded intentionally, and avoid excessive inline/base64 resources that delay discovery and hurt caching; connect to component-development, editorial-ux, and media/design-system rules.
- Cover image performance across raster vs SVG, GIF/PNG/JPEG/WebP/AVIF, responsive images, srcset/sizes, picture art direction, compression, encoding automation, CMS/framework integration, and image CDNs.
- Optimize LCP images through correct img/srcset/sizes, rendered size and DPR-aware variants, avoid lazy-loading LCP images, keep LCP image discoverable in initial HTML, use fetchpriority=high intentionally, understand preload scanner behavior, and avoid blind preload overuse.
- Use stale-while-revalidate only where the product can tolerate the freshness model; treat it as perceived speed and caching behavior, not a security or forms concern.
- Treat blur-up, base64/LQIP, special encodings, and calmer loading states as placeholder patterns, not as substitutes for correct real-resource discovery.
- Frame layout stability around media, widgets, fonts, and late layout CSS; pair historical CLS examples with current Core Web Vitals behavior.
- Balance responsive image breakpoint count: too few variants waste bandwidth, while too many increase storage, processing complexity, and CDN cache fragmentation.
- Server-Timing belongs to production performance observability.
- Inline previews, BlurHash, Sharp, and Lambda concern image loading UX.
- For product-app performance, consider local-first data, IndexedDB-backed initial loads, optimistic mutations, durable retry queues, granular observable updates, keyboard-first workflows, command palettes, and restrained animation. Do not treat MobX or any single app architecture as mandatory.
