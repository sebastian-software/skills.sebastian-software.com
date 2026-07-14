# Design System Rules

Use this reference for reusable design-system decisions that cut across colour, tokens, SVG, visual effects, media, and component clarity. Keep durable rules here only when they affect reusable UI quality, not one-off decoration.

## Working Rules

### Color spaces and token derivation

- Author palettes and ramps in a perceptual color space (OKLCH or LCH) so equal numeric steps read as equal visual steps and lightness stays predictable across hues. Reduce chroma as colors approach white or black to avoid garish extremes.
- Define color pairs, not isolated colors. Every brand, surface, status, and accent token needs known foreground, border, focus, hover, active, disabled, and forced-colors behavior.
- Derive related tokens (hover, active, disabled, tints, alpha variants) with relative color syntax (`oklch(from …)`) and `color-mix()` instead of hand-tuned hex or preprocessor math, so one base change cascades. Treat these as Baseline-2024 features: ship a static fallback ahead of the derived value and gate non-baseline use behind `@supports`.
- Pick the interpolation color space deliberately for gradients, transitions, and `color-mix()`. Interpolate in OKLCH or another perceptual space to avoid muddy or desaturated midpoints; sRGB interpolation through gray is the common cause of dead-looking gradients.
- Treat the color format itself as a token decision. Define when the system uses `hex`, `rgb()`, `hsl()`, `oklch()`, `color-mix()`, and relative color syntax, and keep raw values out of components — reference semantic tokens only.
- Treat a color-format migration as a representation change, not an implicit
  redesign: preserve selectors, token roles, gradient structure, alpha, and
  formatting unless the task explicitly changes the palette. Leave CSS
  keywords and third-party configuration formats alone when they require hex or
  another specific syntax. Convert with a tested color implementation, inspect
  out-of-gamut results, and verify every foreground/background pair after the
  migration.

### Contrast and accessibility

- Treat WCAG 2 minimums (4.5:1 text, 3:1 large text and non-text/UI) as a floor, not a target; perceived contrast can still be weak at the minimum, especially for borders, icons, and underlines that carry meaning. Verify state visibility for buttons, inputs, and filters, not just static text.
- Use APCA as the primary design and review metric: its contrast value is
  polarity-aware, and its acceptance thresholds vary with text size and weight.
  Where a formal WCAG 2.x conformance claim, contract, or audit is in scope,
  also pass the applicable WCAG 2 ratios; those ratios are a separate
  compliance gate, not the design target.
- Treat `contrast-color()` as a Baseline-2026 convenience for picking black or
  white foregrounds, not an accessibility guarantee. Declare an explicit color
  before it when older targets matter, and verify the selected pair because
  mathematical preference between black and white can still leave mid-tone
  backgrounds perceptually weak. Plan `prefers-contrast` and light/dark
  alternatives rather than relying on automatic foreground selection.

### Theming architecture

- Use semantic tokens with explicit cascade ownership: define theme values at a single owning scope and let local overrides flow through custom properties, so component code never hard-codes a theme.
- Use `light-dark()` with `color-scheme` for simple per-property system-theme switching, but keep an explicit theme architecture (data attribute or class plus token sets) when products need user-selected themes, local theme overrides, or cross-brand variants.
- Gate wide-gamut/P3 colors and modern color functions on the product's browser
  baseline. Provide an intentional sRGB semantic token first, use `@supports`
  for colour-notation support, and combine it with `@media (color-gamut: p3)`
  before overriding the token with a P3 value. A successful feature query does
  not prove that the output device can render P3. Derive and gamut-map each
  variant for its target gamut, and verify contrast in both branches.

### Agent-readable system contracts

- Treat design decisions as maintained infrastructure. Record component purpose,
  allowed variants, token roles, states, accessibility constraints, examples,
  and anti-examples in versioned text next to the implementation.
- Give both engineers and agents a small closed vocabulary: semantic tokens,
  approved components, explicit usage rules, and migration mappings. Do not ask
  them to infer the system from screenshots or a large set of near-duplicates.
- Keep the executable component, its stories, and its guidance synchronized.
  When the system changes, identify stale rules and examples instead of leaving
  an old instruction file to drift silently.
- Audit for raw values, detached variants, competing icon/type/color systems,
  undefined tokens, and duplicate interaction patterns. Use deterministic
  inventory and linting before asking an LLM to interpret ambiguous findings.
- Preserve room for documented product-specific components. A closed token set
  should prevent accidental drift, not force every legitimate exception into a
  generic primitive.

### SVG, icons, and visual effects

- Prefer inline SVG, or a deliberate SVG delivery system (sprite or component), for icons that need `currentColor`, CSS state styling, accessibility control, or design-system theming. Author SVG with a correct `viewBox`, presentational attributes, and shape primitives so it scales cleanly and stays readable by hand.
- Treat masks, clipping, backdrop filters, glass, grain, and SVG filters as interface-clarity tools, not default decoration, and choose the right primitive: `clip-path` for hard geometric cutouts, CSS or SVG masks for soft/gradient fades (text and image fades, avatar cutouts, rounded tabs). Reserve `feColorMatrix` for specialized image/color math.
- Check contrast, forced-colors behavior, reduced visual complexity, and performance before adopting any effect. Keep effects optional layers with fallbacks; never let meaning depend on translucency, filtering, or an unknown backdrop, and never let an effect drop text contrast.
- Control stacking with `isolation: isolate` and explicit stacking contexts so blend modes, filters, and backdrop effects do not leak into unintended backgrounds.

## Token Review Checklist

- Does every semantic token have a role, not just a visual name?
- Does a format-only color migration preserve token meaning, CSS structure,
  third-party format contracts, and foreground/background relationships?
- Are derived colors checked in light mode, dark mode, hover/focus/active states, disabled states, and forced-colors mode?
- Do colors pass APCA as the design target, with WCAG 2 ratios added when a
  formal conformance requirement applies?
- Do gradients, transitions, and `color-mix()` operations use a color space that avoids muddy interpolation?
- Can the icon system inherit text color, align to type, expose labels, and avoid duplicated sprite/runtime complexity?
- Are visual effects optional layers with fallbacks, or does meaning depend on masking/filtering/translucency?
- Do wide-gamut/P3 tokens have intentional sRGB fallbacks, separate syntax and
  output-gamut gates, and verified foreground/background pairs in both branches?
- Can a contributor discover the approved component, variant, and token without
  reverse-engineering screenshots or copying a nearby implementation?
- Do deterministic checks catch raw values, undefined tokens, duplicates, and
  stale system guidance before generated code can amplify them?
