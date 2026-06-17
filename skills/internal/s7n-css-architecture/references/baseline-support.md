# Baseline and Browser Support

Use current browser-support evidence before turning modern web-platform features into defaults. Baseline, official documentation, and project support policy should drive adoption, not novelty.

## Working Rules

- Prefer Baseline and official platform documentation (MDN, the Web Platform Dashboard) over anecdotal support guesses or copy-pasted "can I use this yet" snippets.
- Adopt a feature as a default only once Baseline confirms it meets the project's support target. Treat "Baseline Widely available" as a safe default and "Baseline Newly available" as something to gate or enhance progressively.
- Gate newer APIs behind `@supports`, with a defined fallback for the unsupported path, whenever absent support would break layout or function rather than degrade gracefully.
- Encode the support target once in Browserslist and let Stylelint, autoprefixing, and CI read from it, so support policy is enforced mechanically instead of by memory.
- Wire the same support target into design-system defaults, so shared components ship only features the target browsers honor.
- Prefer logical properties (`margin-block`, `inset-inline`, `padding-block`) over physical ones so layouts adapt to writing mode and direction.
- Use `oklch()` for color so lightness and chroma stay perceptually even across a palette; provide an `rgb()`/`hex` fallback only when the support target predates Baseline OKLCH.
- Define theme and spacing values as custom properties rather than hard-coded literals, so theming and overrides resolve through the cascade.
- Use `:focus-visible` (not `:focus`) for focus rings, and never remove a focus indicator without supplying a visible replacement.
- Keep shared selectors at low specificity with `:where()` so downstream styles can override without specificity escalation.
- Use cascade layers (`@layer`) to control source-order precedence instead of reaching for `!important`.
- Guard motion behind `@media (prefers-reduced-motion: reduce)`; ship animation and View Transitions as an enhancement that a reduced-motion preference disables.
- Improve text with `text-wrap: balance` for headings and `text-wrap: pretty` for body copy where Baseline support allows, treating both as progressive enhancements.
- Size root and fluid type with `clamp()` and viewport-relative units so typography scales without per-breakpoint overrides.
- Start from a modern reset (`box-sizing: border-box`, sensible `line-height`, removed default margins, accessible form and media defaults) rather than copying a dated reset verbatim.
