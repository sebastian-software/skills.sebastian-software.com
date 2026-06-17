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
- Treat Baseline as compatibility evidence only, not as proof of accessibility, usability, performance, security, assistive-technology behavior, or framework support; verify those separately.
- When sources disagree, trust current Baseline/MDN/Web Platform Dashboard data over older articles, release notes, social posts, or single-browser demos.
- Before relying on a modern feature, classify it as a safe default, a progressive enhancement, or project-gated (allowed only once the project's support policy confirms it), and implement accordingly.

## Adoption Policy

| Feature status | Default decision | Required checks |
| --- | --- | --- |
| Baseline Widely available | Safe default for new code | Confirm the project does not intentionally support older browsers, embedded webviews, or locked enterprise browsers. |
| Baseline Newly available | Use for enhancements and many production features, but do not assume every user has it yet | Check Browserslist, analytics/RUM where available, fallback severity, and whether the missing feature breaks the task. |
| Limited availability | Do not make it a critical dependency unless the product is locked to supporting engines | Provide a fallback, hide it behind `@supports`, or keep it as a visual/performance enhancement only. |
| Single-browser or experimental | Do not codify as a rule | Keep it as opt-in experimentation with explicit support caveats. |

Baseline answers whether a feature is implemented across the core browser set. It does not cover older OS-tied browser versions, in-app browsers and WebViews, enterprise browser pinning, assistive-technology support, polyfill fidelity, or product-specific accessibility and performance risk.

Use product data when available. Without it, prefer Widely available features for critical behavior, Newly available features for progressive enhancement, and Limited availability features only when unsupported users still get a coherent experience.

## Support Check Workflow

1. Decide whether the feature is critical, additive, or decorative.
2. Check the project's declared support policy: Browserslist, framework target, mobile OS support, WebView constraints, and CI browsers.
3. Check current Baseline/MDN/Web Platform Dashboard status.
4. For UI and interaction features, test keyboard, zoom, forced-colors/high-contrast, reduced motion, touch, and at least one screen-reader/browser combination when practical.
5. Choose the implementation path:
   - **Default:** no fallback beyond normal resilient CSS/HTML.
   - **Progressive enhancement:** add `@supports`, fallback markup/style, or optional enhancement behavior.
   - **Polyfill:** only when the feature is critical and the polyfill preserves semantics, accessibility, and performance acceptably.
   - **Avoid:** choose a simpler established pattern.
6. Record the decision in the component or design-system rule once the feature becomes a shared default.

## Polyfill Guidance

- Do not polyfill just because a polyfill exists; polyfills add JavaScript, can hurt INP, and may not reproduce browser semantics or accessibility-tree behavior.
- Skip the polyfill for decorative or additive enhancements when the fallback is coherent.
- Load polyfills conditionally, only for users who need them, and only when the feature is critical.
- Avoid polyfilling complex platform semantics such as layout containment, top-layer behavior, form controls, or accessibility-sensitive widgets unless a tested polyfill is known to preserve behavior.
- Revisit polyfills as features reach Baseline Newly or Widely available and remove them once unneeded.
