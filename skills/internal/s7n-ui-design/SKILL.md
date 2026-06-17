---
name: s7n-ui-design
description: |
  Broad UI design planning and review for web apps, dashboards, forms, content pages, and design-system work. Use when the user asks for an overall UI critique, design direction, UX polish, interface quality gates, or a cross-cutting frontend design pass. For narrow implementation questions, prefer the focused S7N skills listed below.
license: MIT
metadata:
  author: sebastian-software
  version: "1.0"
---

# S7N UI Design

Use this skill as the broad UI design orchestrator. It is for the overall shape of an interface: hierarchy, clarity, coherence, interaction cost, cognitive load, and whether the design is good enough to ship.

Do not use this skill as a source archive. Article-derived input has already been distilled into rules, workflows, and references.

## Use First For

- Overall UI reviews, product surface critiques, redesign direction, and visual polish.
- Early design planning before choosing layout, component, motion, or copy details.
- Quality gates before shipping a frontend experience.
- Deciding which focused S7N skill should handle a specific design problem.

## Route Specific Work

- Layout, spacing, responsive CSS, grid/flex, safe areas: use `s7n-layout-spacing`.
- Typeface choice, readable measure, font loading, text hierarchy: use `s7n-typography`.
- Color palettes, semantic tokens, dark mode, theming: use `s7n-color-theming`.
- Buttons, dialogs, navigation, component primitives: use `s7n-component-primitives`.
- Inputs, validation, field grouping, form flows: use `s7n-forms-ux`.
- Tables, dense data, comparison views: use `s7n-data-tables`.
- HTML semantics, focus, ARIA, keyboard access: use `s7n-accessibility-html`.
- Motion, transitions, scroll interaction, reduced motion: use `s7n-motion-interaction`.
- Metadata, structured data, frontend SEO: use `s7n-frontend-seo`.
- CSS layers, custom properties, browser support, build tooling: use `s7n-css-architecture`.
- Localization, RTL, text expansion, international UX: use `s7n-i18n-ux`.
- Interface copy, empty-state language, editorial UX: use `s7n-editorial-ux`.
- Loading, error, success, and not-found states: use `s7n-error-loading-states`.
- Auth UX and browser-security-sensitive flows: use `s7n-auth-security-ux`.
- Print output and paged media: use `s7n-print-design`.
- Runtime speed and Core Web Vitals: use `s7n-web-performance`.
- React architecture or component implementation: use `s7n-react-architecture` or `s7n-react-component`.
- Test strategy and Playwright/Vitest frontend checks: use `s7n-frontend-testing`.

## Review Workflow

1. Identify the job-to-be-done, primary user, primary action, and failure modes.
2. Check whether the current UI has one clear information hierarchy and one clear next action per state.
3. Remove visual or interaction elements that do not clarify, accelerate, reassure, or prevent mistakes.
4. Route narrow issues to the focused skills above instead of expanding this skill.
5. Verify the result against the quality gates before considering the UI done.

## Baseline Rules

- Every visible element needs a job. Decoration is acceptable only when it improves recognition, trust, orientation, or comprehension.
- Optimize for scanning first, then reading. Users should understand state, next action, and risk without decoding the layout.
- Keep interaction cost low: related controls belong near the content they affect, destructive actions need recoverability, and repeated workflows need density.
- Do not make accessibility, responsive behavior, localization, or loading/error states late-stage patches.
- Prefer fewer stronger patterns over many local exceptions.

## References

- [references/fundamentals.md](references/fundamentals.md) - broad UI design principles and quality heuristics.
- [references/less-is-more.md](references/less-is-more.md) - reduction, clarity, and restraint.
- [references/design-registers.md](references/design-registers.md) - registers for design intent and decisions.
- [references/design-planning.md](references/design-planning.md) - planning workflow before implementation.
- [references/ui-quality-gates.md](references/ui-quality-gates.md) - final review gates before shipping.
