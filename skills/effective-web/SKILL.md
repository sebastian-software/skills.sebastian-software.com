---
name: effective-web
description: >-
  Design, build, review, and improve user-facing web experiences including
  marketing sites, content pages, landing pages, web apps, dashboards, and
  React components. Use for UI/UX direction, layout, typography, color,
  components, forms, tables, accessibility, motion, internationalization,
  interface copy, loading and error states, auth UX, CSS architecture,
  frontend SEO and AI search, browser performance, frontend testing, React
  architecture, React component APIs, SVG textures, print stylesheets, paged
  media, or web-to-print output. Do not use for backend-only work,
  infrastructure or deployment, general-purpose writing, or print production
  that is unrelated to HTML and CSS.
---

# Effective Web

Treat the web experience as one system. Route each request to the smallest
relevant guidance set, then check the result across design, implementation,
accessibility, performance, and verification boundaries.

## Workflow

1. Inspect the product goal, primary users and actions, existing stack, local
   conventions, browser support, and available evidence.
2. Select one primary route from the table. Read that route before acting.
3. Load only the detailed references required by the route and current problem.
   Add another route only when the work genuinely crosses concerns.
4. Implement or review against the existing product language and architecture.
   Prefer measured evidence and repository conventions over generic defaults.
5. Verify the affected states, responsive behavior, keyboard and screen-reader
   use, loading cost, and relevant project checks before declaring the work done.

For a broad redesign or cross-cutting review, start with Design and Review, then
add the focused routes revealed by the review. For a narrow request, skip the
broad design route and load the matching focused route directly.

## Route by Intent

| User intent | Read |
| --- | --- |
| Plan, critique, redesign, polish, or quality-gate a whole experience | [Design and Review](references/route-design.md) |
| Fix hierarchy, grids, spacing, responsive layout, or safe areas | [Layout and Spacing](references/route-layout.md) |
| Improve type hierarchy, measure, rhythm, fallbacks, or font loading | [Typography](references/route-typography.md) |
| Build palettes, semantic tokens, contrast, dark mode, or themes | [Color and Theming](references/route-color.md) |
| Design buttons, navigation, dialogs, menus, or reusable primitives | [Component Primitives](references/route-components.md) |
| Build field layouts, validation, completion, or multi-step forms | [Forms UX](references/route-forms.md) |
| Design dense data, sorting, filtering, row actions, or responsive tables | [Data Tables](references/route-tables.md) |
| Review HTML semantics, accessible names, ARIA, focus, or keyboard use | [Accessibility and HTML](references/route-accessibility.md) |
| Add transitions, scrolling behavior, feedback, or reduced-motion support | [Motion and Interaction](references/route-motion.md) |
| Support localization, RTL, text expansion, or locale-aware formatting | [Internationalization UX](references/route-i18n.md) |
| Write labels, microcopy, empty states, errors, or product language | [Interface Copy](references/route-copy.md) |
| Design loading, empty, success, failure, retry, or not-found states | [Error and Loading States](references/route-states.md) |
| Build login, passkeys, recovery, sessions, permissions, or security UX | [Auth and Security UX](references/route-auth.md) |
| Organize cascade layers, tokens, scoping, browser support, or CSS tooling | [CSS Architecture](references/route-css.md) |
| Improve metadata, structured data, crawlability, previews, or AI search | [Frontend SEO and AI Search](references/route-seo.md) |
| Choose unit, component, visual, browser, or E2E coverage and CI strategy | [Frontend Testing](references/route-testing.md) |
| Diagnose Core Web Vitals, images, caching, resource loading, or perceived speed | [Web Performance](references/route-performance.md) |
| Decide React server/client boundaries, state placement, hydration, or rendering | [React Architecture](references/route-react-architecture.md) |
| Design reusable React APIs, composition, state ownership, refs, or interop | [React Components](references/route-react-components.md) |
| Create SVG noise, grain, paper, clouds, organic surfaces, or filter effects | [SVG Textures](references/route-textures.md) |
| Build print stylesheets, paged media, printable documents, or web-to-print output | [Print Design](references/route-print.md) |

## Detailed Reference Index

Read only the references needed for the selected route.

### Design and foundations

- [Design planning](references/design-planning.md)
- [Design registers](references/design-registers.md)
- [UI fundamentals](references/fundamentals.md)
- [Less is more](references/less-is-more.md)
- [UI quality gates](references/ui-quality-gates.md)

### Layout, type, and color

- [Layout and spacing](references/layout-spacing.md)
- [Responsive design](references/responsive-design.md)
- [Responsive CSS layout](references/css-layout-responsive.md)
- [Typography](references/typography.md)
- [Typography rules](references/typography-rules.md)
- [Webfonts](references/webfonts.md)
- [Color](references/colour.md)
- [Dark mode](references/dark-mode.md)
- [Design-system rules](references/design-system-rules.md)

### Components and interaction

- [Buttons](references/buttons.md)
- [Navigation](references/navigation.md)
- [Dialogs and modals](references/dialog-modal.md)
- [Component development](references/component-development.md)
- [UX patterns](references/ux-patterns.md)
- [Forms](references/forms.md)
- [Forms UX](references/forms-ux.md)
- [Data tables](references/tables-data.md)
- [Motion and interaction](references/motion-interaction.md)
- [Scroll patterns](references/scroll-patterns.md)

### Inclusive and resilient UX

- [HTML accessibility](references/html-accessibility.md)
- [Internationalization and RTL](references/i18n-rtl.md)
- [Internationalization UX](references/i18n-ux.md)
- [Copywriting](references/copywriting.md)
- [Editorial UX](references/editorial-ux.md)
- [Loading states](references/loading-states.md)
- [Error pages](references/error-pages.md)
- [Auth and web security](references/auth-web-security.md)

### Frontend engineering

- [CSS architecture](references/css-architecture.md)
- [Browser baseline support](references/baseline-support.md)
- [CSS build tooling](references/css-build-tooling.md)
- [SEO](references/seo.md)
- [AI search and entity distribution](references/ai-geo-distribution.md)
- [Browser performance](references/browser-performance.md)

### Testing

- [Testing-layer decisions](references/testing-layer-decision.md)
- [Storybook component testing](references/storybook-component-testing.md)
- [Visual-regression stability](references/visual-regression-stability.md)
- [Playwright E2E workflows](references/playwright-e2e-workflows.md)
- [CI and baseline review](references/ci-and-baseline-review.md)
- [Vendor tool notes](references/vendor-tool-notes.md)

### React

- [Server Components](references/server-components.md)
- [Rendering performance](references/rendering-performance.md)
- [Framework boundaries](references/framework-boundaries.md)
- [Component API design](references/component-api-design.md)
- [Forms and state](references/forms-and-state.md)
- [Interop and accessibility](references/interop-and-accessibility.md)

### SVG textures

- [Texture recipes](references/texture-recipes.md)
- [Filter primitives](references/filter-primitives.md)
- [CSS integration](references/css-integration.md)

### Print design

- [Print layout](references/print-layout.md)
- [Print typography](references/print-typography.md)
- [Web print styles](references/print-web-styles.md)
- [Paged-media features](references/print-page-features.md)
- [Print locale rules](references/print-locale.md)

## Boundaries

- Route Impressum, legal notices, privacy and cookie notice requirements,
  online-sales disclosures, and multi-jurisdiction compliance analysis to
  `web-legal-compliance`; return here for the resulting frontend implementation
  and verification work.
- Route locale-specific punctuation, quotation, spacing, and language-level
  typographic rules to `locale-typography`.
- Route general marketing copy and campaigns to external DALO catalog skills;
  use Interface Copy only for language embedded in a web experience.
- Keep backend-only architecture, infrastructure, deployment, load testing, and
  security audits, and non-web desktop publishing outside this skill unless
  they directly constrain the browser-facing result.
