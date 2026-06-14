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
