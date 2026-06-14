# Baseline and Browser Support

Use current browser-support evidence before turning modern web-platform features into defaults. Baseline, official documentation, and project support policy should drive adoption, not novelty.

## Working Rules

- Prefer Baseline and official platform documentation over anecdotal support guesses.
- Separate feature-radar sources from implementation-rule sources.
- Add `@supports`, progressive enhancement, fallback behavior, or project-specific support constraints when using newly available features.
- Connect support policy to Browserslist, linting, CI, and design-system defaults where possible.
- Treat Baseline as compatibility evidence, not as proof of accessibility, usability, performance, security, assistive-technology behavior, or framework support.
- Resolve conflicts in favor of current Baseline/MDN/Web Platform Dashboard data over older articles, release notes, tweets, or single-browser demos.
- Before using a modern feature in reusable skill guidance, classify it as default-ready, progressive enhancement, project-gated, or radar only.

## Adoption Policy

| Feature status | Default decision | Required checks |
| --- | --- | --- |
| Baseline Widely available | Safe default for new code | Confirm project does not intentionally support older browsers, embedded webviews, or locked enterprise browsers. |
| Baseline Newly available | Use for enhancements and many production features, but do not assume every user has it yet | Check project Browserslist, analytics/RUM if available, fallback severity, and whether the missing feature breaks the task. |
| Limited availability | Do not make it a critical dependency unless the product is locked to supporting engines | Provide a fallback, hide behind `@supports`, or keep it as visual/performance enhancement only. |
| Single-browser or experimental radar | Do not codify as a rule | Mention only as radar or opt-in experimentation with explicit support caveats. |

Baseline answers "is this implemented across the core browser set?" It does not cover:

- older operating-system-tied browser versions,
- in-app browsers and WebViews,
- enterprise browser pinning,
- assistive technology support,
- polyfill fidelity,
- product-specific accessibility or performance risk.

Use product data when available. If no product data exists, prefer Widely available features for critical behavior, Newly available features for progressive enhancement, and Limited availability features only when unsupported users still get a coherent experience.

## Support Check Workflow

1. Identify whether the feature is critical, additive, or decorative.
2. Check the project's declared support policy: Browserslist, framework target, mobile OS support, WebView constraints, and CI browsers.
3. Check current Baseline/MDN/Web Platform Dashboard status.
4. For UI and interaction features, test keyboard, zoom, forced-colors/high-contrast, reduced motion, touch, and at least one screen-reader/browser combination when practical.
5. Decide the implementation path:
   - **Default:** no fallback needed beyond normal resilient CSS/HTML.
   - **Progressive enhancement:** add `@supports`, fallback markup/style, or optional enhancement behavior.
   - **Polyfill:** use only when the feature is critical and the polyfill preserves semantics, accessibility, and performance acceptably.
   - **Avoid:** choose a simpler established pattern.
6. Document the decision in the component or design-system rule when the feature becomes a shared default.

## 2026 Platform Radar

Use this as a currentness map, not as a replacement for live support checks.

### Strong Defaults

- Container size queries, `:has()`, subgrid, CSS nesting, `<search>`, `inert`, constraint validation, and `:user-valid` / `:user-invalid` have moved beyond novelty and can be treated as normal production tools unless a project has unusually old browser constraints.
- Popover is now a normal platform primitive for non-modal top-layer UI, but still pair it with correct trigger semantics, dismissal behavior, focus expectations, and touch/keyboard testing.

### Newly Available / Progressive Enhancement

- `@scope`, View Transitions, `view-transition-class`, `content-visibility`, `scrollend`, `dialog.requestClose()`, Event Timing, and LCP APIs are useful production tools, but should be introduced with project support checks and fallbacks where the missing feature affects core behavior.
- 2026 Baseline additions such as container style queries, `contrast-color()`, custom highlights, active view transitions, and the Navigation API are promising but should be treated as newly available until the project audience and fallback path are understood.

### Radar Only Unless Project-Gated

- Customizable native select (`appearance: base-select`, `::picker(select)`), interest-triggered popovers, CSS carousel primitives, CSS `@function`, CSS `if()`, advanced `attr()` typing, `field-sizing`, and reading-flow/order features need current support checks before becoming reusable rules.
- Masonry/layout proposals, `margin-trim`, and other active proposals should remain design radar, not implementation defaults.

## Polyfill Guidance

- Do not polyfill just because a polyfill exists. Polyfills add JavaScript, can affect INP, and may not reproduce browser semantics or accessibility tree behavior.
- Favor no polyfill for decorative or additive enhancements when the fallback is coherent.
- Conditionally load polyfills only for users who need them when the feature is critical.
- Avoid polyfilling complex platform semantics such as layout containment, top-layer behavior, form controls, or accessibility-sensitive widgets unless the tested polyfill is known to preserve behavior.
- Revisit polyfills periodically as features become Baseline Newly or Widely available.

## Additional Rules

- Practitioner default snippets around logical properties, reduced-motion guarded View Transitions, custom properties, OKLCH, focus-visible, text-wrap, hanging punctuation, low-specificity :where(), cascade layers, and line-height units; useful as habit/radar guidance, not a normative rule.
- Commentary on global CSS starters/resets, cascade layers, fluid root type, text wrapping, form/table defaults, motion preference guards, and team-specific foot-guns; not a normative starter to copy verbatim.
- Duplicate/tracking variant of the Coyier CSS starter commentary; decide together with 7ajo7EGH54gSpHF6dSemLW.
- Platform-radar guidance for Baseline, Web Platform Dashboard, support-policy tooling through Browserslist/ESLint/Stylelint/IDE integrations, and prioritization of newly available APIs such as Anchor Positioning, View Transitions, details enhancements, hidden=until-found, @scope, scrollend, and Core Web Vitals APIs; use as support-policy/radar guidance, not as detailed pattern guidance.
- Duplicate/supporting modern CSS radar guidance.
- Use Chrome CSS/UI I/O 2023 as platform radar, not concrete implementation rules.
- Use frontend handbook as broad background/radar guidance only.
- Use Baseline rule for browser feature availability policy.
- Use Modern CSS 2025 as platform radar and currentness guidance.
- Use Chrome Web UI I/O 2025 as platform radar for native UI capabilities.
