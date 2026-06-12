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

