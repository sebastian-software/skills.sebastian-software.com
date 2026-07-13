# Design and Review

Use this route as the broad web-design orchestrator. Evaluate the overall shape
of an experience: hierarchy, clarity, coherence, interaction cost, cognitive
load, and whether the result is good enough to ship.

Do not use this skill as a source archive. Article-derived input has already been distilled into rules, workflows, and references.

## Use First For

- Overall UI reviews, product surface critiques, redesign direction, and visual polish.
- Early design planning before choosing layout, component, motion, or copy details.
- Quality gates before shipping a frontend experience.
- Deciding which focused Effective Web route should handle a specific problem.

## Route Specific Work

- Layout, spacing, responsive CSS, grid/flex, safe areas: read [Layout and Spacing](route-layout.md).
- Typeface choice, readable measure, font loading, text hierarchy: read [Typography](route-typography.md).
- Color palettes, semantic tokens, dark mode, theming: read [Color and Theming](route-color.md).
- Buttons, dialogs, navigation, component primitives: read [Component Primitives](route-components.md).
- Inputs, validation, field grouping, form flows: read [Forms UX](route-forms.md).
- Tables, dense data, comparison views: read [Data Tables](route-tables.md).
- HTML semantics, focus, ARIA, keyboard access: read [Accessibility and HTML](route-accessibility.md).
- Motion, transitions, scroll interaction, reduced motion: read [Motion and Interaction](route-motion.md).
- Metadata, structured data, frontend SEO: read [Frontend SEO and AI Search](route-seo.md).
- CSS layers, custom properties, browser support, build tooling: read [CSS Architecture](route-css.md).
- Localization, RTL, text expansion, international UX: read [Internationalization UX](route-i18n.md).
- Interface copy, empty-state language, editorial UX: read [Interface Copy](route-copy.md).
- Loading, error, success, and not-found states: read [Error and Loading States](route-states.md).
- Auth UX and browser-security-sensitive flows: read [Auth and Security UX](route-auth.md).
- Print output and paged media: use `s7n-print-design`.
- Runtime speed and Core Web Vitals: read [Web Performance](route-performance.md).
- React architecture: read [React Architecture](route-react-architecture.md).
- React component implementation: read [React Components](route-react-components.md).
- Test strategy and Playwright/Vitest checks: read [Frontend Testing](route-testing.md).

## Review Workflow

1. Identify the job-to-be-done, primary user, primary action, and failure modes.
2. Check whether the current UI has one clear information hierarchy and one clear next action per state.
3. Remove visual or interaction elements that do not clarify, accelerate, reassure, or prevent mistakes.
4. Route narrow issues to the focused routes above instead of expanding this route.
5. Verify the result against the quality gates before considering the UI done.

## Baseline Rules

- Every visible element needs a job. Decoration is acceptable only when it improves recognition, trust, orientation, or comprehension.
- Optimize for scanning first, then reading. Users should understand state, next action, and risk without decoding the layout.
- Keep interaction cost low: related controls belong near the content they affect, destructive actions need recoverability, and repeated workflows need density.
- Do not make accessibility, responsive behavior, localization, or loading/error states late-stage patches.
- Prefer fewer stronger patterns over many local exceptions.

## References

- [fundamentals.md](fundamentals.md) - broad UI design principles and quality heuristics.
- [less-is-more.md](less-is-more.md) - reduction, clarity, and restraint.
- [design-registers.md](design-registers.md) - registers for design intent and decisions.
- [design-planning.md](design-planning.md) - planning workflow before implementation.
- [ui-quality-gates.md](ui-quality-gates.md) - final review gates before shipping.
