# Browser Performance

Use measured browser behavior to guide performance changes. Prioritize fixes that improve user-visible loading, rendering stability, and interaction latency without making the system harder to maintain.

## Working Rules

- Keep LCP resources discoverable in initial HTML whenever possible.
- Do not lazy-load above-the-fold or likely-LCP images.
- Use responsive images to match rendered size and DPR without exploding variant count.
- Reserve media and widget space to avoid avoidable CLS.
- Use cache freshness directives deliberately; stale content can improve perceived speed only when the product can tolerate the freshness model.
- Treat placeholder techniques as perceived-performance tools, not substitutes for correct image delivery.

## Source-Backed Guidance

### Don't fight the browser preload scanner

- Things ID(s): `A7EtoTHWwtpMvsCnmvKiug`
- Source: <https://web.dev/preload-scanner/?utm_source=CSS-Weekly&utm_campaign=Issue-507&utm_medium=email>
- Decision: `primary`
- Target: `network-performance`
- URL recheck: 2026-06-13, HTTP 200, redirects to https://web.dev/articles/preload-scanner?utm_source=CSS-Weekly&utm_campaign=Issue-507&utm_medium=email
- Guidance: Primary for network-performance: keep startup resources discoverable in HTML, avoid JS-injected startup scripts, do not lazy-load above-the-fold/LCP images through data-src, avoid hiding LCP images in CSS backgrounds unless preloaded intentionally, and avoid excessive inline/base64 resources that delay discovery and hurt caching; cross-reference component-development, editorial-ux, and media/design-system rules.

### Learn Images

- Things ID(s): `Ga7AGaG4XpqaaevALg1naW`
- Source: <https://web.dev/learn/images/>
- Decision: `primary`
- Target: `network-performance`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for network-performance with responsive-design cross-reference: broad official image course covering key performance issues, raster vs SVG, GIF/PNG/JPEG/WebP/AVIF, responsive images, srcset/sizes, picture/art direction, compression and encoding automation, CMS/framework integration, and image CDNs; use as umbrella reference for image delivery and responsive media rules.

