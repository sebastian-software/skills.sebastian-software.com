# Cluster Brief: Frontend UI Queue 05

## Metadata

| Field          | Value                                                |
| -------------- | ---------------------------------------------------- |
| Things cluster | `Skill: Frontend UI`                                 |
| Reviewed on    | 2026-06-10                                           |
| Reviewer       | Codex                                                |
| Write scope    | `docs/source-review/clusters/frontend-ui-05.md` only |

## Scope

This review covers 50 open Things intake items tagged as frontend UI. It is an
intermediate source-review artifact only: no Things tasks were changed and no
skill files were edited.

The filter used here is intentionally strict. Durable articles, official docs,
standards-facing explainers, and high-quality implementation guides can become
candidates. GitHub repos, package READMEs, product homepages, release/news
roundups, course sales pages, stale package ideas, and shallow link posts are
deferred or rejected unless the source itself is strong enough to guide a
repeatable agent workflow.

## Access Notes

- All provided URL groups were opened or checked over the network.
- Several tracking URLs were normalized while reviewing; tracking parameters did
  not affect the source decisions.
- Park UI's card URL redirects from `/react/docs/components/card` to
  `/docs/components/card`.
- `https://web-components.fluentui.dev/?path=/docs/concepts-introduction--page`
  loaded as a Storybook shell through the extractor. It was still identifiable
  as Fluent UI Web Components vendor documentation and treated as vendor/docs
  inventory rather than a direct source candidate.
- The Frontend Masters CSS Variables URL resolved as a course/product page
  rather than an article or open reference.
- Piccalilli's two `/links/` entries were checked through to their targets:
  `one-of-those-onboarding-uis-with-anchor-positioning` points to CSS-Tricks,
  while `opinions-for-writing-good-css` points to Andrew Walpole's personal
  article.
- `github.com/louisremi/memoize-immutable` redirects to
  `github.com/memoize-immutable/memoize-immutable`.
- GitHub project links already present in
  `docs/source-review/github-projects/github-project-matrix.csv` were treated
  as project inventory, not direct skill/reference source material.
- Exact duplicate article/product links were reviewed once and applied to all
  matching Things IDs.

## Dedupe Summary

- 50 Things tasks reviewed.
- 43 broad source groups after exact duplicate, redirect, and topic grouping.
- Exact duplicates:
  - `EQmx9Zw92dUPULMadKjBTR`, `Sz9LXzmqASdQXgfQ2K8na`: Ahmad Shadeed's
    `Learn CSS Subgrid` article with different newsletter parameters.
  - `2H1JnB15fxw9Kmu6y7C25e`, `Nhyw6TeAjQJu6QMw5miJb3`: Josh Comeau's
    `Making Sense of React Server Components`.
  - `TpWbaiDFmykq7Go5jTAPUJ`, `DHdEpa6PF7xxo28mJdw5s3`,
    `PmLpF9tgTLWZfQ9LP46WKg`: Piccalilli `Mindful Design` course page with
    different tracking parameters.
- Near duplicates or topic clusters:
  - Fluid sizing appears in the Piccalilli wrapper utility and Smashing's
    fluid typography guide; both are useful but should be deduped with earlier
    fluid typography sources before skill edits.
  - React Server Components appears as an Epic Web workshop repo and a Josh
    Comeau explanatory article. The article is the direct candidate; the GitHub
    workshop repo is deferred.
  - Component-library/vendor material appears in Park UI, Fluent UI Web
    Components, Mantine, React Spectrum release notes, React Aria migration
    notes, and React Helmet. Only the migration article was promoted because it
    contains reusable accessibility tradeoffs rather than just package docs.
  - Web-platform/news radar appears in Interop 2022, Interop 2023, and web.dev
    I/O 2024. The old Interop posts were rejected as stale; the 2024 roundup was
    deferred as standards radar.

## Decision Summary

| Status      | Count | Rationale                                                                                                                                                                                      |
| ----------- | ----: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `candidate` |    23 | Durable CSS, layout, typography, image-preview, web-components, animation, React architecture, menu UX, modal, color, component-architecture, tooltip, touch-input, and Storybook i18n guides. |
| `deferred`  |    12 | Potentially useful but better routed to React/RSC, browser automation, component-library/vendor, Storybook/tooling, email, JS/security, design-token, or standards-radar reviews.              |
| `rejected`  |    15 | Archived or narrow package links, stale browser/news roundups, product/course pages, old framework-specific tutorials, low-signal opinion pieces, and package-shopping items.                  |

## Per-Thing Decisions

|   # | Things ID                | URL group                                  | Decision    | Notes                                                                                                                    |
| --: | ------------------------ | ------------------------------------------ | ----------- | ------------------------------------------------------------------------------------------------------------------------ |
| 201 | `ASZDqLLAuYWZp37uS9tEnY` | `css-tricks-built-in-web-components`       | `candidate` | Practical custom-elements article on extending built-in elements with support caveats.                                   |
| 202 | `9H2vmqxQYvhkirmqGM8NY1` | `epicweb-react-server-components-github`   | `deferred`  | Workshop repo for RSC and Server Functions; useful inventory, but use explanatory articles and official docs as sources. |
| 203 | `CQT6f8wwHhj61yYWuiLzHz` | `lightpanda-browser-github`                | `deferred`  | Headless browser project for AI/automation; route to browser automation/tooling review.                                  |
| 204 | `8xoSvTZYFADUL2EZaDk2Jr` | `park-ui-card-docs`                        | `deferred`  | Component-library card docs; vendor/component inventory, not direct skill guidance.                                      |
| 205 | `HTeJHBycSFbE7hfZQ6uhs3` | `piccalilli-clamp-wrapper`                 | `candidate` | Concise CSS `clamp()` wrapper utility guide with progressive fallback.                                                   |
| 206 | `TuoM9pdAhh65cwH5sRyxeq` | `shud-bulletproof-react-components`        | `candidate` | Strong React component resilience guide covering async, server, composition, portals, and refs.                          |
| 207 | `2Gbiutt9Q6QC3bDmV9dHk8` | `fluent-ui-web-components-docs`            | `deferred`  | Fluent UI Web Components docs shell; useful only in a web-components/vendor review.                                      |
| 208 | `MgYtYmXmAoBUknE4HT95Z8` | `josh-full-bleed-layout`                   | `candidate` | Detailed CSS Grid full-bleed layout guide with line-length and grid-placement caveats.                                   |
| 209 | `7AwpfiLoDAXVKCCzF8WKoB` | `smashing-fluid-typography-clamp`          | `candidate` | Durable fluid typography guide covering `clamp()`, breakpoints, and accessibility concerns.                              |
| 210 | `EZeoRB2JKjAzHqREbUNFUy` | `storybook-i18n-components`                | `candidate` | Official Storybook article for locale switchers, decorators, i18next, and RTL direction testing.                         |
| 211 | `HcDFUdEhbqBJ8bbQi8ktux` | `in-view-github`                           | `rejected`  | Archived viewport utility repo; prefer current IntersectionObserver/platform guidance.                                   |
| 212 | `W6BxBkRUZG5s6iWde9X8ko` | `css-tricks-inline-image-previews`         | `candidate` | Practical image-placeholder workflow using Sharp, BlurHash, and generated inline previews.                               |
| 213 | `6LnfKPP6B21Hxjbhvuo3uv` | `webdev-interop-2022-wrapup`               | `rejected`  | Stale browser interoperability year-end roundup; superseded by current Baseline/support sources.                         |
| 214 | `JN2vqG3oR1jyM5XtFCtjuK` | `webdev-interop-2023`                      | `rejected`  | Old Interop news/radar post; not stable skill-reference material.                                                        |
| 215 | `PefC88bAi4AggCxR6R8tnR` | `chrome-scroll-driven-animations-course`   | `candidate` | Official Chrome scroll-driven animation course announcement with concepts, docs, and demo links.                         |
| 216 | `wUxqh3u27pKDAYMzS89bb`  | `piccalilli-complete-css-announcement`     | `rejected`  | Course/product announcement, not an open implementation source.                                                          |
| 217 | `Uffa21psQy4NT1mtDn3F69` | `css-tricks-too-much-css`                  | `rejected`  | Opinion essay about CSS feature growth; interesting but not actionable skill guidance.                                   |
| 218 | `Gs8E8rws97avGsAy4Kk4gw` | `react-spectrum-2024-07-22-release`        | `deferred`  | Official release note; prefer current React Aria/Spectrum docs in a vendor review.                                       |
| 219 | `NfnFHNaZT2dwzNTvqFDsdF` | `justice-github`                           | `rejected`  | Old performance-budget widget repo; use current Web Vitals/Lighthouse guidance instead.                                  |
| 220 | `BhWHdeFtav6sP2LN6FJjY4` | `frontendmasters-css-variables-course`     | `rejected`  | Course/catalog page, not durable source material.                                                                        |
| 221 | `Q7bSPJ5vAKYMM7HtTuC1Pg` | `devto-webpack2-lazy-react`                | `rejected`  | 2017 Webpack 2 lazy-loading tutorial; stale framework/tooling guidance.                                                  |
| 222 | `EQmx9Zw92dUPULMadKjBTR` | `ishadeed-css-subgrid`                     | `candidate` | Strong CSS Subgrid article with layout use cases and implementation details.                                             |
| 223 | `Sz9LXzmqASdQXgfQ2K8na`  | `ishadeed-css-subgrid`                     | `candidate` | Duplicate Ahmad Shadeed Subgrid article with different tracking parameters.                                              |
| 224 | `NzVLBXdityhvxnVxSaNceA` | `frontendmasters-liquid-glass`             | `candidate` | Current visual-effects article with `backdrop-filter`, SVG filter, and accessibility caveats.                            |
| 225 | `UPtnD1hpVsiB7VLFvyxma3` | `sinja-framer-motion-tooltip`              | `deferred`  | Detailed animated tooltip recipe, but library-specific and should be checked against accessibility guidance.             |
| 226 | `D345npubf7a86csT1rb61q` | `piccalilli-content-aware-components`      | `candidate` | Practical CSS `:has()`, grid, quantity-query, and container-query component guide.                                       |
| 227 | `2H1JnB15fxw9Kmu6y7C25e` | `josh-react-server-components`             | `candidate` | High-quality, updated React Server Components explainer with SSR, hydration, and boundary framing.                       |
| 228 | `Nhyw6TeAjQJu6QMw5miJb3` | `josh-react-server-components`             | `candidate` | Exact duplicate of item 227; same RSC explainer decision.                                                                |
| 229 | `CtjtXMkz2CxnCXXD7cEppB` | `mantine-homepage`                         | `deferred`  | Component-library homepage; vendor inventory only in this pass.                                                          |
| 230 | `9oaRN8SG1Hgu2a5brFDN6o` | `nng-menu-design-checklist`                | `candidate` | Research-backed menu UX checklist from NN/g; useful for navigation and IA references.                                    |
| 231 | `EWLPEibbrFkiZbw1RYjbG8` | `argos-react-aria-migration`               | `candidate` | Migration case study with reusable accessibility and UX tradeoffs between Radix and React Aria.                          |
| 232 | `TpWbaiDFmykq7Go5jTAPUJ` | `piccalilli-mindful-design-course`         | `rejected`  | Course sales page; broad design education outline but not direct source material.                                        |
| 233 | `DHdEpa6PF7xxo28mJdw5s3` | `piccalilli-mindful-design-course`         | `rejected`  | Duplicate Mindful Design course page with tracking parameters.                                                           |
| 234 | `PmLpF9tgTLWZfQ9LP46WKg` | `piccalilli-mindful-design-course`         | `rejected`  | Duplicate Mindful Design course page with tracking parameters.                                                           |
| 235 | `3QzcLphZTBT9z63RiEvdCG` | `css-tricks-modal-root-scrolling`          | `candidate` | Practical modal scroll-lock article; use with current dialog/inert/mobile viewport guidance.                             |
| 236 | `V7pLWJcxveP4kuoRU3LJkh` | `piccalilli-modern-css-colours-part-two`   | `candidate` | Strong modern CSS color guide covering color manipulation, surface levels, and schemes.                                  |
| 237 | `KedFFWf1rEpPGYsxhMXKDB` | `moderncss-component-architecture`         | `candidate` | Durable CSS architecture guide for resets, theming, layout, and component variants.                                      |
| 238 | `9uHi7h8Gqa9v41wbr9VvY3` | `smashing-modern-css-tooltips`             | `candidate` | Detailed modern CSS tooltip/speech-bubble implementation source.                                                         |
| 239 | `WmYYZAouQ23r3Dp9ji7jEn` | `memoize-immutable-github`                 | `rejected`  | Narrow memoization package for immutable data; JS/state tooling, not UI source material.                                 |
| 240 | `WpkvKEes6v6ibFvZXiKejY` | `josh-email-mjml-mdx`                      | `deferred`  | Strong responsive email workflow article, but belongs in an email/templating review, not this UI pass.                   |
| 241 | `FXhftGW5sZBSoRwEyWLQGZ` | `nanoid-github`                            | `deferred`  | Active ID-generation package already in matrix; route to JS/security/tooling review.                                     |
| 242 | `EeVfcVLSHC9Jvp91xwW7AY` | `postcss-momentum-scrolling-github`        | `rejected`  | Narrow PostCSS package for old iOS scrolling behavior; not durable UI guidance.                                          |
| 243 | `17HCnUvGaMKyxXZVkzLKWY` | `css-tricks-touch-devices-size`            | `candidate` | Durable responsive interaction article: do not infer touch capability from screen size.                                  |
| 244 | `MRCuox9ucqMbuzAuLmWkbN` | `webdev-new-in-web-io2024`                 | `deferred`  | Official web platform roundup; useful standards radar but too broad and high-churn.                                      |
| 245 | `DN27w44vkLQwURRnSR1Enz` | `storybook-framework-api`                  | `deferred`  | Storybook framework API/product evolution post; route to Storybook/tooling review with current docs.                     |
| 246 | `6bZgHBGRduxpokzmuXGNFS` | `react-helmet-github`                      | `rejected`  | Package README for document head management; stale package-shopping, not frontend UI source guidance.                    |
| 247 | `8ssGUJ4p7WstyFjgfNKtRE` | `css-tricks-onboarding-anchor-positioning` | `candidate` | Piccalilli linkpost points to a CSS-Tricks anchor-positioning onboarding UI guide.                                       |
| 248 | `24PemZbjce4oE42E9KAtxS` | `open-color-github`                        | `deferred`  | UI color palette asset/project; possible design-token inventory, not direct skill guidance.                              |
| 249 | `4dJATAY47d723e2gdFWvvN` | `andrew-walpole-good-css-opinions`         | `rejected`  | Piccalilli linkpost to a personal opinion article; too broad for archive use.                                            |
| 250 | `A9DpMbiBdeSz9AKXASeuBp` | `josh-partial-keyframes`                   | `candidate` | Practical animation article on partial CSS keyframes and composable motion changes.                                      |

## Source Groups

### Candidate: CSS Layout, Typography, And Responsive Interaction

- `piccalilli-clamp-wrapper`, `josh-full-bleed-layout`,
  `smashing-fluid-typography-clamp`, and `ishadeed-css-subgrid` are strong
  layout and fluid-sizing references. They should be deduped with prior fluid
  typography and layout candidates before updating a skill.
- `piccalilli-content-aware-components` and
  `css-tricks-onboarding-anchor-positioning` are modern CSS component/layout
  sources using `:has()`, quantity queries, container queries, and anchor
  positioning.
- `css-tricks-touch-devices-size` is useful responsive interaction guidance:
  agents should avoid equating small screens with touch or large screens with
  pointer-only interaction.

### Candidate: Components, Accessibility, And Product UI

- `shud-bulletproof-react-components` is a strong React component robustness
  source: async children, RSC/lazy boundaries, portals, refs, and composition
  pitfalls.
- `storybook-i18n-components` belongs with component-state and Storybook
  references for locale, RTL, and translation state coverage.
- `nng-menu-design-checklist`, `css-tricks-modal-root-scrolling`,
  `smashing-modern-css-tooltips`, and `argos-react-aria-migration` are useful
  accessibility and interaction references, but modal/tooltip rules should be
  paired with current platform and ARIA guidance.
- `josh-react-server-components` is the strongest React architecture source in
  this queue. The Epic Web workshop repo should remain secondary inventory.

### Candidate: Visual Effects, Images, Color, And Animation

- `css-tricks-inline-image-previews` is a practical image-loading/perceived
  performance source for inline placeholders.
- `chrome-scroll-driven-animations-course`, `frontendmasters-liquid-glass`, and
  `josh-partial-keyframes` are useful animation/effects references with
  progressive enhancement and accessibility caveats.
- `piccalilli-modern-css-colours-part-two` and
  `moderncss-component-architecture` are strong CSS architecture/color sources
  for themeable, component-based UI systems.
- `css-tricks-built-in-web-components` is useful for web-component enhancement
  work, but customized built-in support caveats need a current browser support
  check before any skill rule.

### Deferred: Vendor, Tooling, And Adjacent Reviews

- Vendor/component inventory: Park UI, Fluent UI Web Components, Mantine, React
  Spectrum release notes, and React Helmet should not be promoted from product
  or package pages alone.
- Tooling/project inventory: Epic Web RSC workshop, Lightpanda, Nano ID, Open
  Color, and Storybook framework API should be revisited only in more specific
  React, browser automation, JS/security, design-token, or Storybook reviews.
- Adjacent content: Josh Comeau's MJML/MDX email workflow deserves an
  email/templating review rather than a frontend UI source-card promotion here.
- Standards radar: web.dev I/O 2024 is useful context, but too broad and
  release-like for direct skill content.

### Rejected: Stale News, Product Pages, And Weak Package Shopping

- Stale browser/news material: Interop 2022 and Interop 2023 are superseded by
  current Baseline/browser-support references.
- Product or course pages: Complete CSS, Frontend Masters CSS Variables, and
  Mindful Design do not expose enough open reference material to become direct
  sources.
- Narrow or stale package links: `in-view`, `justice`, `memoize-immutable`,
  `postcss-momentum-scrolling`, and `react-helmet` are package-shopping links,
  not durable UI guidance.
- Low-signal opinion or stale tutorial material: `is-there-too-much-css-now`,
  `lazy-loaded-react-components-with-webpack-2`, and
  `opinions-for-writing-good-css`.

## Proposed Outcome

Decision: `existing skill update candidates` plus `defer` for project/vendor
inventory.

Target skills or references:

- Existing frontend/UI/CSS references can use the candidate sources for full
  bleed layouts, subgrid, fluid type, wrapper utilities, component-aware CSS,
  anchor positioning, modern color, component CSS architecture, modal scroll
  locking, tooltips, touch-input assumptions, image placeholders, scroll-driven
  animation, partial keyframes, and visual effects.
- React/component references can use the Josh Comeau RSC article and Shu Ding
  bulletproof component guide, with current React docs as the primary authority
  before any implementation rule.
- Storybook/testing references can absorb the i18n article for locale, RTL, and
  translation state coverage.
- Do not create a new skill from this queue alone.
- Do not promote package README links, course landing pages, release notes, or
  product homepages into skill sources without a later, more specific vendor or
  tooling review.

## Things Actions

| Things ID                | Decision  | Final tag                 | Complete? | Reason                                                                         |
| ------------------------ | --------- | ------------------------- | --------- | ------------------------------------------------------------------------------ |
| `ASZDqLLAuYWZp37uS9tEnY` | candidate | `Skill Archive Candidate` | yes       | Practical custom-elements article on extending built-in elements with caveats. |
| `9H2vmqxQYvhkirmqGM8NY1` | deferred  | `Skill Archive Deferred`  | yes       | RSC workshop repo; defer to React/RSC review with official docs and articles.  |
| `CQT6f8wwHhj61yYWuiLzHz` | deferred  | `Skill Archive Deferred`  | yes       | Headless browser project; browser automation/tooling inventory only.           |
| `8xoSvTZYFADUL2EZaDk2Jr` | deferred  | `Skill Archive Deferred`  | yes       | Park UI card docs are component-library vendor inventory.                      |
| `HTeJHBycSFbE7hfZQ6uhs3` | candidate | `Skill Archive Candidate` | yes       | CSS `clamp()` wrapper utility guide with progressive fallback.                 |
| `TuoM9pdAhh65cwH5sRyxeq` | candidate | `Skill Archive Candidate` | yes       | Strong React component resilience guide.                                       |
| `2Gbiutt9Q6QC3bDmV9dHk8` | deferred  | `Skill Archive Deferred`  | yes       | Fluent UI Web Components docs shell; vendor/web-components review only.        |
| `MgYtYmXmAoBUknE4HT95Z8` | candidate | `Skill Archive Candidate` | yes       | Detailed CSS Grid full-bleed layout source.                                    |
| `7AwpfiLoDAXVKCCzF8WKoB` | candidate | `Skill Archive Candidate` | yes       | Durable fluid typography and `clamp()` article.                                |
| `EZeoRB2JKjAzHqREbUNFUy` | candidate | `Skill Archive Candidate` | yes       | Storybook i18n, locale switcher, and RTL testing workflow.                     |
| `HcDFUdEhbqBJ8bbQi8ktux` | rejected  | `Skill Archive Rejected`  | yes       | Archived viewport utility repo; use current platform guidance instead.         |
| `W6BxBkRUZG5s6iWde9X8ko` | candidate | `Skill Archive Candidate` | yes       | Practical inline image-placeholder workflow.                                   |
| `6LnfKPP6B21Hxjbhvuo3uv` | rejected  | `Skill Archive Rejected`  | yes       | Stale Interop 2022 browser roundup.                                            |
| `JN2vqG3oR1jyM5XtFCtjuK` | rejected  | `Skill Archive Rejected`  | yes       | Old Interop 2023 news/radar post.                                              |
| `PefC88bAi4AggCxR6R8tnR` | candidate | `Skill Archive Candidate` | yes       | Official scroll-driven animation course/docs entry point.                      |
| `wUxqh3u27pKDAYMzS89bb`  | rejected  | `Skill Archive Rejected`  | yes       | Complete CSS course/product announcement.                                      |
| `Uffa21psQy4NT1mtDn3F69` | rejected  | `Skill Archive Rejected`  | yes       | CSS feature-growth opinion essay, not actionable guidance.                     |
| `Gs8E8rws97avGsAy4Kk4gw` | deferred  | `Skill Archive Deferred`  | yes       | React Spectrum release note; prefer current docs.                              |
| `NfnFHNaZT2dwzNTvqFDsdF` | rejected  | `Skill Archive Rejected`  | yes       | Old performance-budget widget repo; use Web Vitals/Lighthouse guidance.        |
| `BhWHdeFtav6sP2LN6FJjY4` | rejected  | `Skill Archive Rejected`  | yes       | Frontend Masters course/catalog page.                                          |
| `Q7bSPJ5vAKYMM7HtTuC1Pg` | rejected  | `Skill Archive Rejected`  | yes       | Stale 2017 Webpack 2 lazy-loading tutorial.                                    |
| `EQmx9Zw92dUPULMadKjBTR` | candidate | `Skill Archive Candidate` | yes       | Strong CSS Subgrid article.                                                    |
| `Sz9LXzmqASdQXgfQ2K8na`  | candidate | `Skill Archive Candidate` | yes       | Duplicate CSS Subgrid article with different tracking parameters.              |
| `NzVLBXdityhvxnVxSaNceA` | candidate | `Skill Archive Candidate` | yes       | Visual-effects article with glass, SVG filter, and accessibility caveats.      |
| `UPtnD1hpVsiB7VLFvyxma3` | deferred  | `Skill Archive Deferred`  | yes       | Framer Motion tooltip recipe; needs accessibility-focused review.              |
| `D345npubf7a86csT1rb61q` | candidate | `Skill Archive Candidate` | yes       | Content-aware CSS components using `:has()`, grid, and quantity queries.       |
| `2H1JnB15fxw9Kmu6y7C25e` | candidate | `Skill Archive Candidate` | yes       | High-quality React Server Components explainer.                                |
| `Nhyw6TeAjQJu6QMw5miJb3` | candidate | `Skill Archive Candidate` | yes       | Duplicate React Server Components explainer.                                   |
| `CtjtXMkz2CxnCXXD7cEppB` | deferred  | `Skill Archive Deferred`  | yes       | Mantine homepage; component-library vendor inventory.                          |
| `9oaRN8SG1Hgu2a5brFDN6o` | candidate | `Skill Archive Candidate` | yes       | NN/g menu design checklist.                                                    |
| `EWLPEibbrFkiZbw1RYjbG8` | candidate | `Skill Archive Candidate` | yes       | React Aria migration case study with accessibility tradeoffs.                  |
| `TpWbaiDFmykq7Go5jTAPUJ` | rejected  | `Skill Archive Rejected`  | yes       | Mindful Design course sales page.                                              |
| `DHdEpa6PF7xxo28mJdw5s3` | rejected  | `Skill Archive Rejected`  | yes       | Duplicate Mindful Design course page.                                          |
| `PmLpF9tgTLWZfQ9LP46WKg` | rejected  | `Skill Archive Rejected`  | yes       | Duplicate Mindful Design course page.                                          |
| `3QzcLphZTBT9z63RiEvdCG` | candidate | `Skill Archive Candidate` | yes       | Practical modal scroll-lock source with modern-docs caveat.                    |
| `V7pLWJcxveP4kuoRU3LJkh` | candidate | `Skill Archive Candidate` | yes       | Modern CSS color manipulation and scheme guide.                                |
| `KedFFWf1rEpPGYsxhMXKDB` | candidate | `Skill Archive Candidate` | yes       | Modern CSS component architecture and theming guide.                           |
| `9uHi7h8Gqa9v41wbr9VvY3` | candidate | `Skill Archive Candidate` | yes       | Detailed modern CSS tooltip/speech-bubble implementation.                      |
| `WmYYZAouQ23r3Dp9ji7jEn` | rejected  | `Skill Archive Rejected`  | yes       | Narrow immutable memoization package, not UI source material.                  |
| `WpkvKEes6v6ibFvZXiKejY` | deferred  | `Skill Archive Deferred`  | yes       | Responsive email workflow; route to email/templating review.                   |
| `FXhftGW5sZBSoRwEyWLQGZ` | deferred  | `Skill Archive Deferred`  | yes       | Nano ID package; JS/security/tooling inventory.                                |
| `EeVfcVLSHC9Jvp91xwW7AY` | rejected  | `Skill Archive Rejected`  | yes       | Narrow PostCSS plugin for old iOS scrolling behavior.                          |
| `17HCnUvGaMKyxXZVkzLKWY` | candidate | `Skill Archive Candidate` | yes       | Durable guidance on touch capability vs viewport size.                         |
| `MRCuox9ucqMbuzAuLmWkbN` | deferred  | `Skill Archive Deferred`  | yes       | Broad web.dev I/O 2024 platform roundup; standards radar only.                 |
| `DN27w44vkLQwURRnSR1Enz` | deferred  | `Skill Archive Deferred`  | yes       | Storybook framework API/product evolution post; use current docs later.        |
| `6bZgHBGRduxpokzmuXGNFS` | rejected  | `Skill Archive Rejected`  | yes       | React Helmet package README; stale package-shopping.                           |
| `8ssGUJ4p7WstyFjgfNKtRE` | candidate | `Skill Archive Candidate` | yes       | Target article covers onboarding UI with CSS anchor positioning.               |
| `24PemZbjce4oE42E9KAtxS` | deferred  | `Skill Archive Deferred`  | yes       | Open Color palette project; possible design-token inventory.                   |
| `4dJATAY47d723e2gdFWvvN` | rejected  | `Skill Archive Rejected`  | yes       | Personal CSS opinion article; too broad for archive use.                       |
| `A9DpMbiBdeSz9AKXASeuBp` | candidate | `Skill Archive Candidate` | yes       | Practical partial-keyframes animation article.                                 |
