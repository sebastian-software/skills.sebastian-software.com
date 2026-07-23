---
name: effective-web
description: >-
  Diagnose, design, build, review, and improve user-facing web experiences:
  marketing sites, content pages, landing pages, web apps, dashboards, and
  React components. Covers UI/UX direction, layout, typography, color,
  components, forms, tables, accessibility, motion, internationalization
  (i18n) implementation, interface copy, loading and error states, auth UX,
  CSS architecture, frontend SEO and AI search, AI-assisted interface design,
  browser performance, frontend-only surprising behavior, frontend testing,
  React architecture and component APIs, SVG graphics (icons, paths,
  animation, textures), print stylesheets, paged media, and web-to-print
  output. Not for: backend-only work, infrastructure or deployment,
  general-purpose writing, print production unrelated to HTML and CSS, or
  locale-specific punctuation, quotation, spacing, and language-level
  typographic rules (locale-typography skill).
---

# Effective Web

Treat the web experience as one system. Route each request to the smallest
relevant guidance set, then check the result across design, implementation,
accessibility, performance, and verification boundaries.

## Workflow

1. Inspect the product goal, primary users and actions, accepted ADRs, existing
   stack, local conventions, browser support, and available evidence.
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
| Modernize an existing site or app without losing brand, content, routes, analytics, or accessibility contracts | [Design and Review](references/route-design.md) |
| Design an AI-assisted feature, choose chat versus structured UI, or expose uncertainty and control | [Design and Review](references/route-design.md) |
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
| Build, style, animate, optimize, or make accessible SVG icons and illustrations | [SVG Graphics](references/route-svg.md) |
| Create SVG noise, grain, paper, clouds, organic surfaces, or filter effects | [SVG Textures](references/route-textures.md) |
| Build print stylesheets, paged media, printable documents, or web-to-print output | [Print Design](references/route-print.md) |

## Routing Boundaries

- Route product discovery, strategy, outcome, scope, prioritization, quality-bar,
  and release decisions to `product-management`; return here to design,
  implement, and verify the resulting browser experience.
- Route research synthesis, problem framing, object and interaction modeling,
  information architecture, and decision-grade prototyping to `product-design`;
  return here for browser specification, implementation, and verification.
- Route Impressum, legal notices, privacy and cookie notice requirements,
  online-sales disclosures, and multi-jurisdiction compliance analysis to
  `web-legal-compliance`; return here for the resulting frontend implementation
  and verification work.
- Route locale-specific punctuation, quotation, spacing, and language-level
  typographic rules to `locale-typography`.
- Keep general marketing copy and campaign strategy outside this skill; use
  Interface Copy only for language embedded in a web experience.
- Keep backend-only architecture, infrastructure, deployment, load testing, and
  security audits, and non-web desktop publishing outside this skill unless
  they directly constrain the browser-facing result.
- Route execution-only requests for existing repository typecheck, lint, test,
  build, documentation, or combined quality gates to `software-validation`.
  Keep frontend and browser test design, diagnosis, and evidence selection here.
