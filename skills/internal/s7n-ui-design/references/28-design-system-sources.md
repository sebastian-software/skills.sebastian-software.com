# Source-Backed Design System Notes

Use this reference for source-backed design-system decisions that cut across colour, tokens, SVG, visual effects, media, and component clarity. Keep durable rules here only when they affect reusable UI quality, not one-off decoration.

## Working Rules

- Prefer perceptual colour spaces and token derivation that preserve contrast and state clarity.
- Use modern theme primitives only when fallback and browser-support behavior are understood.
- Treat SVG, masks, clipping, filters, and backdrop effects as interface clarity tools, not default decoration.
- Check contrast, forced-colors behavior, reduced visual complexity, and performance before adopting visual effects.

## Source-Backed Guidance

### A Friendly Introduction to SVG • Josh W. Comeau

- Things ID(s): `4gsbJYcqimixCn8c1QFxtE`
- Source: <https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/>
- Decision: `primary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for design-system with svg-graphics/visual-assets cross-reference: strong current SVG fundamentals source covering inline SVG vs img, DOM/CSS addressability, shape primitives, presentational attributes, viewBox, scaling, and readable hand-authored SVG for icons/illustrations.

### Color Formats in CSS

- Things ID(s): `XBrTvm2kHgzbDZFPr696oZ`
- Source: <https://www.joshwcomeau.com/css/color-formats/>
- Decision: `primary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for design-system color foundations: color formats underpin token systems and UI color decisions. Source explains rationale; future skill should codify clear decisions/rules rather than retell the article.

### CSS color interpolation

- Things ID(s): `8sBvUvCRZqJQFAtVRMXbZy`
- Source: <https://css-tricks.com/what-you-need-to-know-about-css-color-interpolation/>
- Decision: `primary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for design-system colors: color interpolation affects gradients, transitions, color-mix behavior, OKLCH/perceptual smoothness, and token-derived visual quality; use for rules about choosing interpolation spaces and avoiding muddy/midpoint artifacts.

### CSS Masking - Ahmad Shadeed

- Things ID(s): `GJtP58SeVAjopqf64SJpgV`
- Source: <https://ishadeed.com/article/css-masking/>
- Decision: `primary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for design-system with visual-effects cross-reference: detailed CSS masking guide covering mask vs clip-path vs SVG masks, gradient masks, mask-size/position/repeat, mask-composite, text/image fades, avatar cutouts, tab rounding, and background-independent effects.

### CSS Relative Colors

- Things ID(s): `G6qpQjwaQ8wLy8hefcxBUM`
- Source: <https://ishadeed.com/article/css-relative-colors/>
- Decision: `primary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for design-system colors: relative color syntax and color-mix() enable derived tokens, alpha variants, hover shades, image-derived gradients, fallback layering with @supports, and reducing Sass/preprocessor-only color manipulation.

### CSS-Farbschema-abhängige Farben mit „light-dark()“ | Articles | web.

- Things ID(s): `8yJXAuViV4kkC3m37QWVwv`
- Source: <https://web.dev/articles/light-dark?hl=de>
- Decision: `primary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for design-system colors/theming: official web.dev light-dark()/color-scheme source for native light/dark token switching, system color behavior, Baseline status, reduced media-query complexity, and theme-aware color definitions.

### Fix Color Contrast - Web Accessibility for Text & UI Design - Pimp m

- Things ID(s): `KHCQBTAuZaX1wJEj3kworS`
- Source: <https://pimpmytype.com/color-contrast/>
- Decision: `primary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for design-system: color contrast as token, visual hierarchy, and component robustness topic; text contrast, non-text/component contrast, borders/icons/underlines as signifiers, button/input/filter state visibility, and WCAG minimums as floor rather than final design quality; cross-reference typography, component-development, and html-accessibility.

### How to have the browser pick a contrasting color in CSS | WebKit

- Things ID(s): `KEXm5g2iL2Vp78TV4tTmsh`
- Source: <https://webkit.org/blog/16929/contrast-color/>
- Decision: `primary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for design-system with tokens/colors cross-references: contrast-color() can simplify color token pairings for black/white foregrounds but does not guarantee accessibility; midtones need manual/perceptual checks, WCAG 2 contrast can diverge from perceived contrast, APCA/WCAG 3 context matters, text size/weight must be considered, and prefers-contrast plus light/dark mode alternatives should be planned.

### Amiana: Farb-Effekt für Fotos mit SVG-Filter

- Things ID(s): `2AbBRRK7CuNanifrxLhPk8`
- Source: <http://alistapart.com/article/finessing-fecolormatrix>
- Decision: `secondary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200, redirects to https://alistapart.com/article/finessing-fecolormatrix/
- Guidance: Secondary for design-system with svg-graphics/visual-effects cross-reference: useful explanatory SVG feColorMatrix source for image/color effects and filter math, but specialized and not a core token/design-system rule source.

### Come To The Light-dark() Side | CSS-Tricks

- Things ID(s): `JZiha4NLETyUWDeSmqz8oA`
- Source: <https://css-tricks.com/come-to-the-light-dark-side/>
- Decision: `secondary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for design-system: practical light-dark()/color-scheme theming article and examples, but the web.dev light-dark source should be the primary rule source; use this as implementation inspiration and caveat material.

### CSS Clipping Effekte

- Things ID(s): `JQWagG2ZKMtMfbmrkCdqCc`
- Source: <https://css-tricks.com/clipping-clipping-and-more-clipping/>
- Decision: `secondary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for design-system with visual-effects cross-reference: useful clipping/clip-path effect source, but older and mainly decorative; concrete rules should come from current clip-path/masking docs or newer shape sources.

### CSS color-mix()

- Things ID(s): `YMLiyWPuLrdMmQFUPSFZuF`
- Source: <https://developer.chrome.com/blog/whats-new-css-ui-2023/#color-mix>
- Decision: `secondary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for design-system with baseline cross-reference: official 2023 CSS UI roundup section for color-mix() awareness, but use focused color-mix/relative-color sources for concrete token and fallback rules.

### CSS P3 Farbraum mit Safari Dev Tools

- Things ID(s): `3dmG2U85tSdXyRmBpUTgLp`
- Source: <https://css-tricks.com/new-css-color-features-preview/>
- Decision: `secondary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200
- Related URLs: <https://twitter.com/jensimmons/status/1478858248677736454>, <https://twitter.com/ticky/status/1131775548516999168/photo/1>, <https://webkit.org/blog/6682/improving-color-on-the-web/>
- Guidance: Secondary for design-system colors: useful historical/currentness source cluster for P3/wide-gamut color and Safari tooling, but Twitter links should be ignored and concrete rules need newer color-space/Baseline documentation.

### CSS-Effekt: Blend-Mode + Isolation

- Things ID(s): `2uXBZWVyFU41XQ3zscGQGP`
- Source: <http://tympanus.net/codrops/css_reference/isolation/>
- Decision: `secondary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200, redirects to https://tympanus.net/codrops/css_reference/isolation/
- Related URLs: <https://css-tricks.com/almanac/properties/i/isolation/>
- Guidance: Secondary for design-system with visual-effects cross-reference: useful isolation/mix-blend-mode containment reference for preventing backdrop blending leaks and understanding stacking-context side effects, but narrow and older.

### Frosted Glass Effect

- Things ID(s): `DtZcmmnDyYCFnFn16kK8Qe`
- Source: <https://css-tricks.com/using-css-backdrop-filter-for-ui-effects/>
- Decision: `secondary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for design-system with visual-effects/component-development cross-references: practical backdrop-filter/frosted-glass UI effect source, useful for caveats around translucency, readability over unknown backgrounds, layering, fallbacks, and performance; not core visual language guidance.

### Grainy Gradients | CSS-Tricks - CSS-Tricks

- Things ID(s): `4W7PqhU6yWzhKBgKEyXER5`
- Source: <https://css-tricks.com/grainy-gradients/>
- Decision: `secondary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for design-system with visual-effects cross-reference: useful grain/noise gradient texture source for reducing banding and adding subtle texture, but specialized visual-effect material that should remain optional and constrained by readability/performance.

### Liquid Glass on the Web - Frontend Masters Blog

- Things ID(s): `NzVLBXdityhvxnVxSaNceA`
- Source: <https://frontendmasters.com/blog/liquid-glass-on-the-web/>
- Decision: `secondary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for design-system: current expressive-effects example for liquid glass/glassmorphism, backdrop-filter, SVG displacement/blur filters, refraction, highlights, and textured blur; use mainly as caveat material for contrast, readability over unknown backgrounds, UI hierarchy, reduced visual complexity, fallbacks, and performance; cross-reference html-accessibility, motion-interaction, and network-performance.
### What You Need to Know about Modern CSS (Spring 2024 Edition) - Front

- Things ID(s): `6D3SdBhegJu8XZ4g1kb8Vz`
- Source: <https://frontendmasters.com/blog/what-you-need-to-know-about-modern-css-spring-2024-edition/?ck_subscriber_id=1866528194&utm_source=convertkit&utm_medium=email&utm_campaign=%E2%9A%9B%EF%B8%8F%20This%20Week%20In%20React%20#180:%20Transitions,%20Drag%20&%20Drop,%20Metadata%20APIs,%20React%20name,%20Next.js%20Auth,%20useOptimistic,%20Cally,%20Docusaurus,%20New%20Architecture,%20Gesture%20Handler,%20Server%20Components,%20Privacy%20Manifest,%20Bun,%20xz,%20TypeScript,%20Signals...%20-%2013529181>
- Decision: `secondary`
- Target: `design`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Retarget to UI/design-system radar: modern CSS roundup is not React architecture.
### How we’re approaching theming with modern CSS

- Things ID(s): `QzrrbFs1PspCApNApzMHBg`
- Source: <https://piccalil.li/blog/how-were-approaching-theming-with-modern-css/>
- Decision: `secondary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use modern CSS theming source for token, cascade, and color-scheme architecture tradeoffs.
### Modern CSS Colors

- Things ID(s): `V7pLWJcxveP4kuoRU3LJkh`
- Source: <https://piccalil.li/blog/a-pragmatic-guide-to-modern-css-colours-part-two/?ref=main-rss-feed>
- Decision: `secondary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use modern CSS colors as design-token and color-space support source.
### PostCSS Plugin für ChromaJS

- Things ID(s): `GtPxGMm2QEVUHLgNpLfSw6`
- Source: <https://github.com/gka/chroma.js>
- Decision: `secondary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use Chroma/PostCSS source as tooling context for generated color tokens, not runtime design guidance.
### Redesign Case Study

- Things ID(s): `WkSeLg4zJ3iv4coHK7D6wb`
- Source: <https://ishadeed.com/article/redesign-2024/?ck_subscriber_id=1697729046>
- Decision: `secondary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use redesign case study as secondary design-system/process inspiration, not a normative source.
### SVG Inline

- Things ID(s): `RFLZcQheZd1Q6c2QTBHMQT`
- Source: <https://github.com/blog/2112-delivering-octicons-with-svg>
- Decision: `secondary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200, redirects to https://github.blog/engineering/delivering-octicons-with-svg/
- Guidance: Use SVG inline delivery source for icon-system and SVG-as-DOM tradeoffs.
### SVG Sprite Loading mit Webpack und React-Komponenten... evtl Ersatz

- Things ID(s): `3syzchS7pMkCg8ATjjBqtF`
- Source: <http://varun.ca/icon-component/>
- Decision: `secondary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200, redirects to https://varun.ca/icon-component/
- Guidance: Use SVG sprite/component workflow source as icon delivery context with current tooling caveats.
### What the heck is an SVG sprite sheet?

- Things ID(s): `2kzXeJ9mQBRqL9sSWaBADy`
- Source: <https://piccalil.li/links/what-the-heck-is-an-svg-sprite-sheet/?ref=main-rss-feed>
- Decision: `secondary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use SVG sprite sheet source for icon-system delivery tradeoffs and currentColor styling caveats.
### What You Need to Know About CSS Color Interpolation | CSS-Tricks

- Things ID(s): `TFQnKUZ6oe7QkRSA5kBEA8`
- Source: <https://css-tricks.com/what-you-need-to-know-about-css-color-interpolation/>
- Decision: `primary`
- Target: `design-system`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use color interpolation source as primary guidance for gradients, transitions, color-mix, and OKLCH behavior.

