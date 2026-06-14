# Design System Rules

Use this reference for reusable design-system decisions that cut across colour, tokens, SVG, visual effects, media, and component clarity. Keep durable rules here only when they affect reusable UI quality, not one-off decoration.

## Working Rules

- Prefer perceptual colour spaces and token derivation that preserve contrast and state clarity.
- Use modern theme primitives only when fallback and browser-support behavior are understood.
- Treat SVG, masks, clipping, filters, and backdrop effects as interface clarity tools, not default decoration.
- Check contrast, forced-colors behavior, reduced visual complexity, and performance before adopting visual effects.
- Define color pairs, not isolated colors. Every brand, surface, status, and accent token needs known foreground, border, focus, hover, active, disabled, and forced-colors behavior.
- Use OKLCH, relative color syntax, and `color-mix()` for token derivation when they improve consistency; guard support and manually verify contrast for midtones and state colors.
- Use `light-dark()` with `color-scheme` for simple system-theme tokens, but keep explicit theme architecture when products need user-selected themes or cross-brand variants.
- Treat `contrast-color()` as a convenience for simple black/white foreground choices, not an accessibility guarantee.
- Prefer inline SVG or a deliberate SVG delivery system for icons that need `currentColor`, CSS state styling, accessibility control, or design-system theming.
- Use masks, clipping, backdrop filters, glass, grain, and SVG filters only when the effect improves hierarchy or media integration. Do not let effects reduce text contrast or make controls depend on unknown backgrounds.

## Token Review Checklist

- Does every semantic token have a role, not just a visual name?
- Are derived colors checked in light mode, dark mode, hover/focus/active states, disabled states, and forced-colors mode?
- Do gradients, transitions, and `color-mix()` operations use a color space that avoids muddy interpolation?
- Can the icon system inherit text color, align to type, expose labels, and avoid duplicated sprite/runtime complexity?
- Are visual effects optional layers with fallbacks, or does meaning depend on masking/filtering/translucency?
- Are wide-gamut/P3 colors and modern color functions support-gated for the product's browser baseline?

## Additional Rules

- Use SVG fundamentals when designing icon and illustration systems: inline SVG vs img, DOM/CSS addressability, shape primitives, presentational attributes, viewBox, scaling, and readable hand-authored SVG.
- Treat color formats as design-token decisions; define clear rules for when to use hex, rgb(), hsl(), oklch(), color-mix(), and relative color syntax.
- Color interpolation affects gradients, transitions, color-mix behavior, OKLCH/perceptual smoothness, and token-derived visual quality; use for rules about choosing interpolation spaces and avoiding muddy/midpoint artifacts.
- Use CSS masking deliberately: distinguish mask vs clip-path vs SVG masks, and account for gradient masks, mask-size/position/repeat, mask-composite, text/image fades, avatar cutouts, tab rounding, and background-independent effects.
- Relative color syntax and color-mix() enable derived tokens, alpha variants, hover shades, image-derived gradients, fallback layering with @supports, and reducing Sass/preprocessor-only color manipulation.
- Use `light-dark()` and `color-scheme` for native light/dark token switching when support, system color behavior, and theme ownership are clear.
- Color contrast as token, visual hierarchy, and component robustness topic; text contrast, non-text/component contrast, borders/icons/underlines as signifiers, button/input/filter state visibility, and WCAG minimums as floor rather than final design quality; connect to typography, component-development, and html-accessibility.
- Contrast-color() can simplify color token pairings for black/white foregrounds but does not guarantee accessibility; midtones need manual/perceptual checks, WCAG 2 contrast can diverge from perceived contrast, APCA/WCAG 3 context matters, text size/weight must be considered, and prefers-contrast plus light/dark mode alternatives should be planned.
- Use SVG `feColorMatrix` only for specialized image/color effects where filter math is justified.
- Keep clipping, clip-path, backdrop-filter, glass, grain, noise, SVG displacement, blur filters, refraction, highlights, and textured blur optional. Verify contrast, readability over unknown backgrounds, hierarchy, fallbacks, reduced visual complexity, and performance before shipping.
- Use `isolation` and stacking-context control to prevent blend-mode effects from leaking into unintended backdrops.
- Use modern CSS theming for token, cascade, and color-scheme architecture tradeoffs.
- Use modern CSS colors as design-token and color-space support.
- Use Chroma/PostCSS as tooling context for generated color tokens, not runtime design guidance.
- Treat redesign examples as process inspiration, not normative design-system rules.
- Use SVG inline delivery for icon-system and SVG-as-DOM tradeoffs.
- Use SVG sprite/component workflow as icon delivery context with current tooling caveats.
- Use SVG sprite sheet for icon-system delivery tradeoffs and currentColor styling caveats.
- Use color interpolation rules for gradients, transitions, color-mix, and OKLCH behavior.
- SVG icon systems belong with visual assets.
- Keep detailed token rules grounded in color-function behavior and contrast checks.
- Prefer semantic tokens, explicit cascade ownership, and support-aware use of `color-scheme` / `light-dark()` for CSS custom properties, light/dark mode, and local theme overrides.
