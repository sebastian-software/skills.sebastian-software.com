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

