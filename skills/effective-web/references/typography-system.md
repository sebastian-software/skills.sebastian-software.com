# Typography System

Use this module to establish type roles, a readable scale, and resilient
fallback behavior for a digital product. Pick the reading task before tuning a
headline.

## Define Roles First

- Separate body, UI label, data, heading, and display roles. One well-supported
  sans-serif family with two or three clearly distinct weights is usually enough
  for product UI; add a second display face only when it earns its complexity.
- Choose body size, line height, and actual line length together. Labels and
  controls must remain readable at real device sizes; inputs generally need at
  least 16 CSS pixels on mobile to avoid unwanted browser zoom.
- Use a modest type scale and `clamp()` only with meaningful minimum and maximum
  sizes. Do not bind all text directly to viewport width.
- Set fallback families with compatible metrics where possible and use
  `font-size-adjust` when it reduces a damaging x-height mismatch. Test loading
  and layout shift rather than assuming a webfont always arrives.

## Keep the Hierarchy Calm

- Weight, size, spacing, and placement should reflect information hierarchy.
  Do not create emphasis by making every heading large, bold, or tightly packed.
- Left-align reading text by default. Reserve centered text for short labels and
  avoid justified narrow measures without a reviewed hyphenation strategy.

For typeface taxonomy, detailed scale examples, and display treatments, consult
the [deep typography appendix](typography.md).
