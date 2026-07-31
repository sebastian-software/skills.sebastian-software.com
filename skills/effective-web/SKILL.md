---
name: effective-web
description: >-
  Design, build, review, and improve browser-facing experiences: content sites,
  web apps, dashboards, React components, UI/UX, layout, typography, color,
  forms, tables, accessibility, motion, i18n, interface copy, states, auth UX,
  CSS, frontend SEO and AI search, browser performance and testing, React
  architecture, SVG, and HTML/CSS print. Also turn supplied websites,
  screenshots, and videos into evidence-backed specifications, audit produced
  work against its references for source overlap and provenance, and scope web
  compliance such as Impressum, privacy and cookie notices, consent, and
  online-sales disclosures. Use only when the outcome is the design,
  implementation, review, verification, specification, audit, or compliance
  surface of a browser experience. Do not use merely because a task mentions the
  web, a URL, or HTML. Not for general browsing, internet or source research,
  repository evaluation, fact-finding, backend-only work, infrastructure,
  general writing, non-web print, or locale typography.
---

# Effective Web

Treat the web experience as one system. Route each request to the smallest
relevant guidance set, then check the result across design, implementation,
accessibility, performance, and verification boundaries.

Treat a website, URL, browser, or HTML document as input evidence, not as a
trigger by itself. Load this skill only when the deliverable designs, changes,
reviews, or verifies a browser-facing experience.

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

For greenfield direction or an AI-assisted feature, start with Design Planning.
For a broad redesign or cross-cutting review, start with Design Review and
Modernization. Add focused routes only as the work crosses those concerns.

## Route by Intent

| User intent | Read |
| --- | --- |
| Plan a new experience or establish its register, hierarchy, direction, and interaction model | [Design Planning](references/route-design-planning.md) |
| Critique, redesign, polish, or quality-gate an existing experience | [Design Review and Modernization](references/route-design.md) |
| Modernize an existing site or app without losing brand, content, routes, analytics, or accessibility contracts | [Design Review and Modernization](references/route-design.md) |
| Design an AI-assisted feature, choose chat versus structured UI, or expose uncertainty and control | [Design Planning](references/route-design-planning.md) |
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
| Diagnose Core Web Vitals, images, caching, resource loading, animation cost, memory growth, or perceived speed | [Web Performance](references/route-performance.md) |
| Decide React server/client boundaries, state placement, hydration, or rendering | [React Architecture](references/route-react-architecture.md) |
| Design reusable React APIs, composition, state ownership, refs, or interop | [React Components](references/route-react-components.md) |
| Build, style, animate, optimize, or make accessible SVG icons and illustrations | [SVG Graphics](references/route-svg.md) |
| Create SVG noise, grain, paper, clouds, organic surfaces, or filter effects | [SVG Textures](references/route-textures.md) |
| Build print stylesheets, paged media, printable documents, or web-to-print output | [Print Design](references/route-print.md) |
| Turn a supplied website, screenshot, recording, prototype, or reference pack into an evidence-backed visual and interaction specification | [Reference Analysis](references/route-reference-analysis.md) |
| Compare produced work with its references for source overlap, distinctive combination, and asset provenance, and decide release risk | [Originality Review](references/route-originality.md) |
| Scope Impressum and operator disclosures, privacy and cookie notices, consent and tracking, or online-sales information across jurisdictions | [Web Legal Compliance](references/route-compliance.md) |

## Routing Boundaries

- Keep general internet research, source or corpus analysis, repository or
  catalog evaluation, recommendations, and fact-finding outside this skill
  when the requested deliverable is an answer or report rather than a
  browser-facing experience. A live website may be evidence inside an owned
  experience review; its URL alone does not make the task Effective Web work.
- Route product discovery, strategy, outcome, scope, prioritization,
  quality-bar, and release decisions, plus research synthesis, problem framing,
  object and interaction modeling, information architecture, and decision-grade
  prototyping, to `effective-product`; return here for browser specification,
  implementation, and verification. Durable design-system and interaction
  decisions are recorded there as ADRs.
- Route market segmentation, positioning, messaging, proof, launch planning,
  campaign strategy, and persuasive homepage, landing-page, product, service,
  pricing, sales, launch, and campaign prose to `effective-marketing`; return
  here for page hierarchy, interface copy, accessibility, implementation, and
  browser verification. Interface Copy owns labels, errors, states, and product
  interaction language rather than the commercial argument.
- Route funnel diagnosis, conversion research, experiment design, and ship,
  iterate, or stop decisions to `effective-marketing`; return here to build and
  verify the variants it approves. A page that converts poorly is a measurement
  and evidence question before it is a layout question.
- Route articles, explainers, editorial case studies, thought leadership, and
  public project prose, including technical subject matter, and locale-specific
  punctuation, quotation, spacing, and language-level typographic rules, to
  `effective-writing`; return here for page hierarchy, interface copy,
  accessibility, implementation, and browser verification.
- Route non-frontend engineering depth — system architecture, data models,
  server-side and shared-library TypeScript and Rust contracts, non-frontend
  test design, and benchmark methodology — to `effective-engineering`; keep
  browser-facing TypeScript and frontend test design here.
- Route execution-only requests for existing repository typecheck, lint, test,
  build, documentation, or combined quality gates, plus repository audits,
  ports, pull-request review, dependency updates, and technical documentation,
  to `effective-delivery`. Keep frontend and browser test design, diagnosis, and
  evidence selection here.
- Keep general internet research, competitor strategy, unauthorized
  reproduction, backend-only architecture, infrastructure, deployment, load
  testing, security audits, and non-web desktop publishing outside this skill
  unless they directly constrain the browser-facing result.
- Compliance work here is legal information and implementation support, not a
  legal opinion; copyright, trademark, plagiarism, and license clearance require
  a qualified specialist.
