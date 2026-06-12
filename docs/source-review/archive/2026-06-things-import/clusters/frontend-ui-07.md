# Cluster Brief: Frontend UI Queue 07

## Metadata

| Field | Value |
| --- | --- |
| Things cluster | `Skill: Frontend UI` |
| Reviewed on | 2026-06-10 |
| Reviewer | Codex |
| Write scope | `docs/source-review/clusters/frontend-ui-07.md` only |

## Scope

This review covers 50 open Things intake items tagged as frontend UI. It is an
intermediate source-review artifact only: no Things tasks were changed and no
skill files were edited.

The filter used here is intentionally strict. Durable articles, official docs,
standards-facing explainers, and high-quality implementation guides can become
candidates. GitHub repos, package READMEs, release notes, PRs/issues, product
pages, vendor homepages, and social posts are deferred or rejected unless the
linked source itself is article- or guide-like enough to support a repeatable
agent workflow. Interesting background material was not promoted when it was
not directly relevant to frontend UI skill guidance.

## Access Notes

- All provided URL groups were opened or checked over the network.
- Tracking parameters were ignored for decisions, but title, URL, and notes
  links were all considered.
- Piccalilli `/links/` entries were checked as linkposts and, where visible,
  through to their original linked targets. Linkposts were promoted only when
  the original target/commentary was clearly guide-like and frontend-relevant.
- X/Twitter and some `t.co` URLs were access-restricted or malformed by smart
  quote characters in the captured URL. Their Things titles and URL/notes
  context were still considered, but social posts were not treated as durable
  source-card material.
- GitHub project links already present in
  `docs/source-review/github-projects/github-project-matrix.csv` were treated
  as project inventory, not direct skill/reference source material.
- Exact duplicate links were reviewed once and applied to all matching Things
  IDs.

## Dedupe Summary

- 50 Things tasks reviewed.
- 45 broad source groups after exact duplicate and topic grouping.
- Exact duplicates:
  - `6snSQEt4cge8xb2J9H1Ho6`, `Caze5uUvVn4cBWdHq7H8c9`: same ReactWG
    "RSC From Scratch" GitHub discussion.
  - `MgrWB7C25KjVb5JSZiDzEQ`, `TaJ1j2aeDUqyMPcpXwJLwz`: same Josh W. Comeau
    `useDeferredValue` article with different tracking parameters.
  - `3Yiw2X5Df8N3SW6c2rbGjD`, `BUcVr8BFyK5GE9jZy33PUv`: same CSS-Tricks
    Tailwind `@apply` article.
  - `7ajo7EGH54gSpHF6dSemLW`, `C3jrBjqmfgTRorm6wJX8hk`: same Piccalilli link
    and commentary for "The Coyier CSS starter".
- Near duplicates or topic clusters:
  - View transitions and scroll-driven animation appear in Chrome docs,
    Piccalilli/CSS-Tricks links, WebKit, and CSS-Tricks. Standards-facing docs
    and practical implementation articles were promoted.
  - CSS layout and component styling appears in section layout, `:has()`
    spacing, subgrid, focus styles, tables, scoped CSS, viewport units, and CSS
    starter sources.
  - Component-library and package inventory appears in shadcn/ui, NLUX,
    sass-loader, responsive-loader, preload-webpack-plugin, Freactal, and other
    GitHub links. These were not promoted as direct frontend UI sources.
  - React architecture/performance appears in ReactWG RSC discussions,
    React Router release/video material, SWR social material, and
    `useDeferredValue`. Only the guide-like RSC and performance article sources
    were promoted.

## Decision Summary

| Status | Count | Rationale |
| --- | ---: | --- |
| `candidate` | 29 | Durable View Transition, scroll animation, React RSC/performance, CSS layout, accessibility/focus, subgrid, table styling, responsive design, viewport unit, SVG icon, Tailwind, and native select articles/docs/guides. |
| `deferred` | 7 | Potentially useful typography, responsive image tooling, Sass/tooling, SWR/RSC, shadcn/component-library, and CSS survey trend material that needs a more specific review or stronger primary sources. |
| `rejected` | 14 | Release notes, old/stale GitHub packages, GitHub PRs, social launch posts, broad videos/opinion pieces, vendor/product pages, and out-of-scope security/API-key material. |

## Per-Thing Decisions

| # | Things ID | URL group | Decision | Notes |
| ---: | --- | --- | --- | --- |
| 301 | `WnRXZj2vu69LuHodEyqL8n` | `chrome-view-transitions-docs` | `candidate` | Official Chrome documentation for same-document and cross-document View Transitions. |
| 302 | `Brpay29VsTtSmzM8ioPNzy` | `react-router-6-5-release` | `rejected` | GitHub release note; route changes may be interesting, but this is not durable guide material. |
| 303 | `Nfp8MhDC2L7KyuiQekiJe` | `preload-webpack-plugin-github` | `rejected` | Archived/predecessor webpack plugin repo; use current preload/modulepreload guidance instead. |
| 304 | `KoF6PZDfx7xeawmRwA74uT` | `piccalilli-replacing-gsap-scroll-animations` | `candidate` | Piccalilli linkpost points to a practical CSS scroll animation rework article. |
| 305 | `9rBi5gx8HpxytMwL9tf5Vt` | `responsive-loader-github` | `deferred` | Webpack responsive-image loader; useful tooling inventory, not direct UI guidance. |
| 306 | `QTWZi7TT3jgS6ZFkA6LMYH` | `youtube-rich-harris-frameworks-edge` | `rejected` | Broad interview/video about frameworks and the edge; interesting context, not source guidance. |
| 307 | `KcLeJfdFPuPs4NENh1WhcH` | `youtube-rip-react-router` | `rejected` | Opinion/video material about routing; not durable frontend UI source material. |
| 308 | `QthEWMSCQoDAPdVpo6JC6A` | `twitter-font-vertical-metrics-thread` | `deferred` | Typography thread may inform font metric review, but social posts are not stable source cards. |
| 309 | `6snSQEt4cge8xb2J9H1Ho6` | `reactwg-rsc-from-scratch-part-1` | `candidate` | Guide-like ReactWG discussion explaining Server Components from first principles. |
| 310 | `Caze5uUvVn4cBWdHq7H8c9` | `reactwg-rsc-from-scratch-part-1` | `candidate` | Duplicate guide-like ReactWG Server Components discussion. |
| 311 | `7TckixMfGeP4xdgYLrUFbc` | `sass-loader-github` | `deferred` | Official webpack loader project; CSS tooling inventory rather than frontend UI guidance. |
| 312 | `7r2qZhdMLgApZ1wHyeP4tD` | `redux-synapse-github` | `rejected` | Old low-signal Redux binding package; not durable React state guidance. |
| 313 | `8V4jYWhNUxGdgiTCsWQC46` | `webkit-scroll-driven-animations-css` | `candidate` | WebKit guide explaining CSS scroll-driven animations and timelines. |
| 314 | `7K37zAPaThhaEaymwjFFNk` | `spin-that-shit-github` | `rejected` | SCSS spinner package/demo; package shopping, not source guidance. |
| 315 | `4uH41CNdZ14cPfBnDSU6gb` | `shadcn-twitter-launch` | `rejected` | Social launch post for a component collection; not guide/reference material. |
| 316 | `BYt4BzcciE2NRk9cWWpDJ9` | `shadcn-ui-homepage` | `deferred` | Component-library/vendor homepage; route to component inventory, not direct skill source. |
| 317 | `Fz8Nyyk5Z2z4z8rT96dvoj` | `swr-beta-rsc-twitter` | `deferred` | Social beta note about SWR/RSC data fetching; useful only as context after official docs. |
| 318 | `2eM9FbRLgafx3ULFGUZf9s` | `css-tricks-scroll-timelines-unlimited-dimensions` | `candidate` | Practical CSS Scroll Timelines article with implementation pattern. |
| 319 | `MgrWB7C25KjVb5JSZiDzEQ` | `joshwcomeau-use-deferred-value` | `candidate` | Detailed React `useDeferredValue` article for UI responsiveness. |
| 320 | `TaJ1j2aeDUqyMPcpXwJLwz` | `joshwcomeau-use-deferred-value` | `candidate` | Duplicate React `useDeferredValue` performance article. |
| 321 | `CjKv1LaVS2UR3dECZpj82f` | `joshwcomeau-header-blockers` | `candidate` | Practical CSS article for sticky-header collision/scroll target polish. |
| 322 | `XMJfCxTrF3tjRU6wiLTNb9` | `css-tricks-donut-scopes` | `candidate` | Article-style explainer for CSS scoping/donut scope patterns. |
| 323 | `JD5mWxmHNyBPhviZWeLCBG` | `ishadeed-modern-css-section-layout` | `candidate` | Strong modern CSS section layout guide with concrete implementation details. |
| 324 | `Jny4ki2K9mpmHFq9VEJiMv` | `css-tricks-has-vertical-spacing` | `candidate` | Practical `:has()` article for vertical spacing in long-form content. |
| 325 | `SBC11yteQ19ob6PX9re3S5` | `joshwcomeau-modern-spacer-gif` | `candidate` | Detailed component-spacing article; use as pattern discussion, not blanket rule. |
| 326 | `9FdqY58HR6Cs8szghQTjVP` | `css-tricks-spas-shared-element-transitions` | `candidate` | Article connects SPA tradeoffs, focus/scroll behavior, and shared element transitions. |
| 327 | `PnctxHQnx7iW6p4LZBQixJ` | `css-tricks-focus-styles-custom-properties` | `candidate` | Practical focus-style standardization article using CSS custom properties. |
| 328 | `RiaEW3itKwtGR2GCnMwyhT` | `piccalilli-view-transitions-today` | `candidate` | Practical Piccalilli article for implementing View Transitions progressively. |
| 329 | `JcYgiUeFNZaQHmNm8w1iym` | `piccalilli-state-of-css-2025` | `deferred` | CSS survey/trend linkpost; useful radar, not implementation guidance. |
| 330 | `TK8vRkphoXMwXQLkCurP53` | `web-dev-state-of-css-2022` | `deferred` | Older CSS survey summary; context only, superseded for skill guidance. |
| 331 | `ALPLCSgfiksps2DTp2QU1R` | `freactal-github` | `rejected` | Archived React state-management package; not current UI guidance. |
| 332 | `D8RHkqvhUFYNUdYB5iKKKt` | `piccalilli-modern-css-tables` | `candidate` | Practical modern CSS table styling guide. |
| 333 | `ECUyfiaFbse2Wa8JtX6ZgK` | `piccalilli-subgrid-simple-layout` | `candidate` | Practical subgrid article enhancing a simple layout. |
| 334 | `GeEhJHNGGvhjeJuMrZajg8` | `joshwcomeau-subgrid` | `candidate` | Detailed CSS subgrid guide with component layout examples. |
| 335 | `3syzchS7pMkCg8ATjjBqtF` | `varun-component-svg-icon-system` | `candidate` | Article-style SVG icon component workflow; use with current SVG and bundler caveats. |
| 336 | `3Yiw2X5Df8N3SW6c2rbGjD` | `css-tricks-tailwind-apply` | `candidate` | Article-style Tailwind `@apply` discussion; Tailwind-specific but guide-like. |
| 337 | `BUcVr8BFyK5GE9jZy33PUv` | `css-tricks-tailwind-apply` | `candidate` | Duplicate Tailwind `@apply` article. |
| 338 | `N5Nr66BdyFks2L75tH4SDz` | `css-tricks-telephone-links` | `candidate` | Practical semantic HTML article for `tel:` links and mobile behavior. |
| 339 | `K4NkLodB3oSeSSCos4KKVW` | `postcss-import-pr-204` | `rejected` | GitHub PR/testing detail for PostCSS import extensions; not source guidance. |
| 340 | `XcR1W92yAwH9XJoRB3YjJk` | `beautify-text-github` | `rejected` | Old typographic text-formatting package repo; package inventory only. |
| 341 | `D9emEr2Fjvivbx2h95e2Pp` | `css-tricks-explaining-html-css-niece` | `rejected` | Personal/lightweight explainer; not actionable skill guidance. |
| 342 | `YPjE7QDNrmiqjNwqKMzcKX` | `frontendmasters-frontend-handbook-2024` | `candidate` | Broad but guide-like frontend handbook; useful as secondary orientation source. |
| 343 | `WMo2RNEEwqdKHFQaSvzz38` | `chrome-customizable-select` | `candidate` | Official Chrome article on CSS-customizable native `<select>` and related standards work. |
| 344 | `7ajo7EGH54gSpHF6dSemLW` | `piccalilli-coyier-css-starter` | `candidate` | Article/commentary reviewing a global CSS starter with concrete CSS caveats. |
| 345 | `C3jrBjqmfgTRorm6wJX8hk` | `piccalilli-coyier-css-starter` | `candidate` | Duplicate CSS starter article/commentary. |
| 346 | `S54LBxHMvsF4kiEtapzv5H` | `piccalilli-future-web-dev-ai` | `rejected` | Broad AI/web-dev opinion linkpost; not frontend UI source guidance. |
| 347 | `3un8g64C5Lurw8yoHFARJX` | `ishadeed-responsive-design-2023` | `candidate` | Detailed responsive design guide with modern layout considerations. |
| 348 | `sawtsQjn1r5XtVkh28FqG` | `web-dev-large-small-dynamic-viewport-units` | `candidate` | web.dev guide to `svh`, `lvh`, `dvh`, and viewport unit behavior. |
| 349 | `CztbLZiwsyh5fMHvZCSXbD` | `nlux-docs-homepage` | `rejected` | Vendor/product docs for an AI chat UI library; not frontend UI skill source material. |
| 350 | `JQgBHYtCaLgzHL61bsMNYL` | `smashing-react-api-keys` | `rejected` | React/API-key security article is out of scope for frontend UI source review. |

## Source Groups

### Candidate: View Transitions And Scroll Animation

- `chrome-view-transitions-docs` is the strongest primary source for View
  Transitions, covering same-document and cross-document use with browser
  support caveats.
- `piccalilli-view-transitions-today`,
  `piccalilli-replacing-gsap-scroll-animations`,
  `webkit-scroll-driven-animations-css`, and
  `css-tricks-scroll-timelines-unlimited-dimensions` are practical companion
  sources for progressive enhancement, scroll timelines, and CSS-native
  animation patterns.
- `css-tricks-spas-shared-element-transitions` is older and more architectural,
  but useful for the UX tradeoffs around SPA navigation, focus management,
  scroll restoration, and page-transition expectations.

### Candidate: CSS Layout, Styling, And Accessibility

- `ishadeed-modern-css-section-layout`,
  `ishadeed-responsive-design-2023`,
  `piccalilli-subgrid-simple-layout`, and `joshwcomeau-subgrid` are strong
  layout sources for modern responsive CSS.
- `css-tricks-has-vertical-spacing`, `joshwcomeau-header-blockers`,
  `piccalilli-modern-css-tables`, `css-tricks-donut-scopes`,
  `piccalilli-coyier-css-starter`, and
  `web-dev-large-small-dynamic-viewport-units` are practical implementation
  sources for common page and component problems.
- `css-tricks-focus-styles-custom-properties`,
  `css-tricks-telephone-links`, and `chrome-customizable-select` are useful for
  accessible/semantic UI controls and interaction details.

### Candidate: React, Components, And Design System Patterns

- `reactwg-rsc-from-scratch-part-1` is promoted despite being a GitHub
  discussion because it is guide-like and comes from the React working group.
  It should be paired with current React docs before any skill edits.
- `joshwcomeau-use-deferred-value` is a practical React UI performance source
  for keeping interactions responsive.
- `joshwcomeau-modern-spacer-gif` and `varun-component-svg-icon-system` are
  article-style component pattern sources. Both should be used with caveats:
  spacers are not a blanket spacing rule, and the SVG icon workflow predates
  current bundler/SVG conventions.
- `css-tricks-tailwind-apply` is Tailwind-specific but article-like enough to
  retain as secondary guidance for utility CSS organization tradeoffs.
- `frontendmasters-frontend-handbook-2024` is broad orientation material, not a
  narrow rule source.

### Deferred: Trends, Social Context, And Tooling Inventory

- `twitter-font-vertical-metrics-thread` and `swr-beta-rsc-twitter` may contain
  useful ideas, but they are social posts and need durable primary or article
  sources before promotion.
- `responsive-loader-github`, `sass-loader-github`, and `shadcn-ui-homepage`
  are tooling or component-library inventory. They can inform future package or
  design-system reviews, but they should not become frontend UI source cards
  from README/homepage material alone.
- `piccalilli-state-of-css-2025` and `web-dev-state-of-css-2022` are trend
  radar sources. They are useful for prioritization context, not implementation
  instructions.

### Rejected: Releases, Packages, PRs, Vendor Pages, And Out-Of-Scope Items

- Release/social/video material rejected here: `react-router-6-5-release`,
  `youtube-rich-harris-frameworks-edge`, `youtube-rip-react-router`,
  `shadcn-twitter-launch`, and `piccalilli-future-web-dev-ai`.
- GitHub package or PR sources rejected here: `preload-webpack-plugin-github`,
  `redux-synapse-github`, `spin-that-shit-github`, `freactal-github`,
  `postcss-import-pr-204`, and `beautify-text-github`.
- Low-actionability or out-of-scope article/vendor material rejected here:
  `css-tricks-explaining-html-css-niece`, `nlux-docs-homepage`, and
  `smashing-react-api-keys`.

## Proposed Outcome

Decision: `existing skill update candidates` plus `defer` for trend, tooling,
social, and component-library inventory.

Target skills or references:

- Existing frontend/UI/CSS references can use the candidate sources for View
  Transitions, scroll timelines, subgrid, responsive design, viewport units,
  focus styles, native select styling, long-form spacing, tables, scoped CSS,
  and SVG icon component patterns.
- React references can use the RSC and `useDeferredValue` candidates only after
  checking current React documentation as the primary authority.
- Component package links should remain inventory and should not be promoted
  from package README/homepage material alone.
- Do not create a new skill from this queue alone.
- Do not promote GitHub releases, PRs/issues, package READMEs, social posts,
  vendor/product pages, videos, or unrelated security articles into frontend UI
  skill sources without a later, more specific review.

## Things Actions

| Things ID | Decision | Final tag | Complete? | Reason |
| --- | --- | --- | --- | --- |
| `WnRXZj2vu69LuHodEyqL8n` | candidate | `Skill Archive Candidate` | yes | Official View Transition API documentation. |
| `Brpay29VsTtSmzM8ioPNzy` | rejected | `Skill Archive Rejected` | yes | GitHub release note, not durable guide material. |
| `Nfp8MhDC2L7KyuiQekiJe` | rejected | `Skill Archive Rejected` | yes | Archived preload webpack plugin repo. |
| `KoF6PZDfx7xeawmRwA74uT` | candidate | `Skill Archive Candidate` | yes | Practical CSS scroll animation rework article. |
| `9rBi5gx8HpxytMwL9tf5Vt` | deferred | `Skill Archive Deferred` | yes | Responsive-image webpack loader inventory. |
| `QTWZi7TT3jgS6ZFkA6LMYH` | rejected | `Skill Archive Rejected` | yes | Broad framework interview video, not source guidance. |
| `KcLeJfdFPuPs4NENh1WhcH` | rejected | `Skill Archive Rejected` | yes | Router opinion video, not durable guidance. |
| `QthEWMSCQoDAPdVpo6JC6A` | deferred | `Skill Archive Deferred` | yes | Typography social thread needs durable sources. |
| `6snSQEt4cge8xb2J9H1Ho6` | candidate | `Skill Archive Candidate` | yes | Guide-like ReactWG Server Components discussion. |
| `Caze5uUvVn4cBWdHq7H8c9` | candidate | `Skill Archive Candidate` | yes | Duplicate ReactWG Server Components guide discussion. |
| `7TckixMfGeP4xdgYLrUFbc` | deferred | `Skill Archive Deferred` | yes | Sass webpack loader tooling inventory. |
| `7r2qZhdMLgApZ1wHyeP4tD` | rejected | `Skill Archive Rejected` | yes | Old Redux binding package. |
| `8V4jYWhNUxGdgiTCsWQC46` | candidate | `Skill Archive Candidate` | yes | WebKit CSS scroll-driven animations guide. |
| `7K37zAPaThhaEaymwjFFNk` | rejected | `Skill Archive Rejected` | yes | SCSS spinner package/demo. |
| `4uH41CNdZ14cPfBnDSU6gb` | rejected | `Skill Archive Rejected` | yes | shadcn social launch post. |
| `BYt4BzcciE2NRk9cWWpDJ9` | deferred | `Skill Archive Deferred` | yes | shadcn/ui component-library homepage. |
| `Fz8Nyyk5Z2z4z8rT96dvoj` | deferred | `Skill Archive Deferred` | yes | SWR/RSC beta social note. |
| `2eM9FbRLgafx3ULFGUZf9s` | candidate | `Skill Archive Candidate` | yes | Practical CSS Scroll Timelines article. |
| `MgrWB7C25KjVb5JSZiDzEQ` | candidate | `Skill Archive Candidate` | yes | React `useDeferredValue` UI performance article. |
| `TaJ1j2aeDUqyMPcpXwJLwz` | candidate | `Skill Archive Candidate` | yes | Duplicate React `useDeferredValue` article. |
| `CjKv1LaVS2UR3dECZpj82f` | candidate | `Skill Archive Candidate` | yes | Sticky-header collision CSS article. |
| `XMJfCxTrF3tjRU6wiLTNb9` | candidate | `Skill Archive Candidate` | yes | CSS scoping/donut scope explainer. |
| `JD5mWxmHNyBPhviZWeLCBG` | candidate | `Skill Archive Candidate` | yes | Modern CSS section layout guide. |
| `Jny4ki2K9mpmHFq9VEJiMv` | candidate | `Skill Archive Candidate` | yes | `:has()` vertical spacing article. |
| `SBC11yteQ19ob6PX9re3S5` | candidate | `Skill Archive Candidate` | yes | Component spacing pattern article. |
| `9FdqY58HR6Cs8szghQTjVP` | candidate | `Skill Archive Candidate` | yes | SPA tradeoffs and shared transitions article. |
| `PnctxHQnx7iW6p4LZBQixJ` | candidate | `Skill Archive Candidate` | yes | Focus styles with CSS custom properties. |
| `RiaEW3itKwtGR2GCnMwyhT` | candidate | `Skill Archive Candidate` | yes | Practical View Transitions implementation article. |
| `JcYgiUeFNZaQHmNm8w1iym` | deferred | `Skill Archive Deferred` | yes | CSS survey/trend radar, not implementation guidance. |
| `TK8vRkphoXMwXQLkCurP53` | deferred | `Skill Archive Deferred` | yes | Older CSS survey summary; context only. |
| `ALPLCSgfiksps2DTp2QU1R` | rejected | `Skill Archive Rejected` | yes | Archived React state package. |
| `D8RHkqvhUFYNUdYB5iKKKt` | candidate | `Skill Archive Candidate` | yes | Modern CSS table styling guide. |
| `ECUyfiaFbse2Wa8JtX6ZgK` | candidate | `Skill Archive Candidate` | yes | Practical subgrid layout article. |
| `GeEhJHNGGvhjeJuMrZajg8` | candidate | `Skill Archive Candidate` | yes | Detailed CSS subgrid guide. |
| `3syzchS7pMkCg8ATjjBqtF` | candidate | `Skill Archive Candidate` | yes | SVG icon component workflow article. |
| `3Yiw2X5Df8N3SW6c2rbGjD` | candidate | `Skill Archive Candidate` | yes | Tailwind `@apply` guide-like article. |
| `BUcVr8BFyK5GE9jZy33PUv` | candidate | `Skill Archive Candidate` | yes | Duplicate Tailwind `@apply` article. |
| `N5Nr66BdyFks2L75tH4SDz` | candidate | `Skill Archive Candidate` | yes | Semantic `tel:` link article. |
| `K4NkLodB3oSeSSCos4KKVW` | rejected | `Skill Archive Rejected` | yes | GitHub PR/testing detail. |
| `XcR1W92yAwH9XJoRB3YjJk` | rejected | `Skill Archive Rejected` | yes | Old text-formatting package repo. |
| `D9emEr2Fjvivbx2h95e2Pp` | rejected | `Skill Archive Rejected` | yes | Lightweight personal explainer. |
| `YPjE7QDNrmiqjNwqKMzcKX` | candidate | `Skill Archive Candidate` | yes | Broad frontend handbook guide. |
| `WMo2RNEEwqdKHFQaSvzz38` | candidate | `Skill Archive Candidate` | yes | Official customizable native select article. |
| `7ajo7EGH54gSpHF6dSemLW` | candidate | `Skill Archive Candidate` | yes | CSS starter article/commentary. |
| `C3jrBjqmfgTRorm6wJX8hk` | candidate | `Skill Archive Candidate` | yes | Duplicate CSS starter article/commentary. |
| `S54LBxHMvsF4kiEtapzv5H` | rejected | `Skill Archive Rejected` | yes | Broad AI/web-dev opinion linkpost. |
| `3un8g64C5Lurw8yoHFARJX` | candidate | `Skill Archive Candidate` | yes | Detailed responsive design guide. |
| `sawtsQjn1r5XtVkh28FqG` | candidate | `Skill Archive Candidate` | yes | web.dev viewport units guide. |
| `CztbLZiwsyh5fMHvZCSXbD` | rejected | `Skill Archive Rejected` | yes | Vendor docs for AI chat UI library. |
| `JQgBHYtCaLgzHL61bsMNYL` | rejected | `Skill Archive Rejected` | yes | Out-of-scope React API-key security article. |

## Counts

- `candidate`: 29
- `deferred`: 7
- `rejected`: 14
- Total Things actions rows: 50

No Things actions were executed. No skill files were edited.
