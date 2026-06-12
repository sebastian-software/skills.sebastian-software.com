# Cluster Brief: Frontend UI Queue 06

## Metadata

| Field          | Value                                                |
| -------------- | ---------------------------------------------------- |
| Things cluster | `Skill: Frontend UI`                                 |
| Reviewed on    | 2026-06-10                                           |
| Reviewer       | Codex                                                |
| Write scope    | `docs/source-review/clusters/frontend-ui-06.md` only |

## Scope

This review covers 50 open Things intake items tagged as frontend UI. It is an
intermediate source-review artifact only: no Things tasks were changed and no
skill files were edited.

The filter used here is intentionally strict. Durable articles, official docs,
standards-facing explainers, and high-quality implementation guides can become
candidates. GitHub repos, package READMEs, release notes, PRs/issues, product
pages, vendor homepages, and social posts are deferred or rejected unless the
linked source itself is article- or guide-like enough to support a repeatable
agent workflow.

## Access Notes

- All provided URL groups were opened or checked over the network.
- Tracking parameters were ignored for decisions, but title, URL, and notes
  links were all considered.
- `https://css-tricks.com/the-critical-request/` now redirects to the
  CSS-Tricks homepage, so the font-preload item was treated as source-unusable.
- `https://vis4.net/blog/posts/mastering-multi-hued-color-scales/` returned
  404, but the canonical current URL
  `https://www.vis4.net/blog/mastering-multi-hued-color-scales/` was found and
  reviewed alongside the linked Chroma.js project and palette helper.
- `https://redwoodjs.com/blog/rsc-now-in-redwoodjs` redirects to `rwsdk.com`
  and returns 404. Search results and surrounding Redwood references confirm the
  source was a framework-specific RSC announcement/walkthrough, not a durable
  direct frontend skill source.
- The Radix Twitter/X URL returned access restrictions, but the Things title
  and URL identify it as a release/social post; it was treated accordingly.
- GitHub project links already present in
  `docs/source-review/github-projects/github-project-matrix.csv` were treated
  as project inventory, not direct skill/reference source material.
- Exact duplicate article/video links were reviewed once and applied to all
  matching Things IDs.

## Dedupe Summary

- 50 Things tasks reviewed.
- 43 broad source groups after exact duplicate, broken-link, and topic grouping.
- Exact duplicates:
  - `3e46uPxTe8gvm8ehnyasKc`, `Lg2nNwUVYrP5tsbmHCTmFj`: `react-dom-stream`
    GitHub project with and without tracking parameters.
  - `49H4xjKuDFNZniFvH6v3yt`, `9jyDhDQy27UdXuhYMmL6uz`: same React Server
    Components, Suspense, and Actions YouTube roundtable.
  - `3XJAUQjYcWgpUKURQC6caV`, `VWJTy7jcv7sq1r1BXNtRE`,
    `X1Zu8htQT8puU3Jq847WSb`: Ahmad Shadeed's Vox featured-news rebuild
    article with and without newsletter parameters.
- Near duplicates or topic clusters:
  - React Server Components appears in Mux, Epic Web, Tim Tech, The New Stack,
    Redwood, Tom Preston-Werner, and YouTube sources. Only the practical
    explainer/implementation articles were promoted.
  - Tooltip/accessibility appears in Frontend Masters, Piccalilli, React Aria,
    and old React tooltip packages. Article/docs sources were promoted; package
    shopping was rejected.
  - PostCSS/tooling appears in flexbugs fixes, postcss-functions, Chroma.js,
    postcss-style-guide, doiuse, polished, and Razzle. Only the linked color
    scale article/tool group was promoted; package/tool projects were not.
  - CSS layout and interaction appears in print stylesheets, details/subgrid
    tabs, Shadeed's Vox rebuild, and Shadeed's redesign case study.

## Decision Summary

| Status      | Count | Rationale                                                                                                                                                                                                    |
| ----------- | ----: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `candidate` |    14 | Durable tooltip/anchor-positioning, accessibility, print CSS, CSS tabs/subgrid, React Aria docs, React hooks/RSC implementation, color-scale, modern CSS layout, and detailed design/CSS case-study sources. |
| `deferred`  |    14 | Potentially useful but better routed to component-library, PostCSS/tooling, router/dialog, responsive tooling, React/RSC media, select/color-picker, or framework-history reviews.                           |
| `rejected`  |    22 | Broken article URL, stale or archived packages, old boilerplates/SSR/PWA projects, package source files, release/social posts, framework announcements, and low-signal package-shopping items.               |

## Per-Thing Decisions

|   # | Things ID                | URL group                                   | Decision    | Notes                                                                                                        |
| --: | ------------------------ | ------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------ |
| 251 | `H2vSAorpXj9royWFZTMqfZ` | `frontendmasters-pointed-tooltips`          | `candidate` | Practical article on CSS Anchor Positioning through tooltip geometry.                                        |
| 252 | `8Xf7PX8wkRBkjRzPXaQ5UU` | `plyr-react-github`                         | `deferred`  | React media-player package; component/vendor inventory, not direct skill guidance.                           |
| 253 | `MGBuPLzGsamXEwCeHP44PS` | `postcss-flexbugs-fixes-github`             | `rejected`  | Archived PostCSS package; use current flexbox/browser-support guidance instead.                              |
| 254 | `AguDUCCtpqGUuCdPJPJg9v` | `postcss-functions-github`                  | `deferred`  | PostCSS utility package; route to CSS tooling review if needed.                                              |
| 255 | `TvJdZrKgpyeVNSaVxaFzDL` | `postcss-functions-transformer-source`      | `rejected`  | Package source file, not article/docs/reference material.                                                    |
| 256 | `GtPxGMm2QEVUHLgNpLfSw6` | `chroma-palettes-vis4-color-scales`         | `candidate` | Multi-URL group includes a durable color-scale article and palette helper; Chroma.js repo remains secondary. |
| 257 | `7WrHBhnXHPjkK1x1DAMpbv` | `polished-github`                           | `deferred`  | Styling utility package; possible CSS-in-JS/tooling inventory only.                                          |
| 258 | `WgV8JbhdMi2sPmCfWH2QwQ` | `postcss-style-guide-github`                | `rejected`  | Old/archived PostCSS style-guide generator; not durable UI guidance.                                         |
| 259 | `H1xDc6da6Nq3M97iYDf69A` | `doiuse-github`                             | `deferred`  | Active CSS browser-support lint package; route to CSS/tooling compatibility review.                          |
| 260 | `C8Z8ZDF6UyDgoymLZ5tnn6` | `piccalilli-practical-accessibility-tips`   | `candidate` | Practical accessibility snippets and component markup explainers.                                            |
| 261 | `XCCm5J3r1iqPDmJaMB6N1j` | `preact-redux-isomorphic-github`            | `rejected`  | Old example app/boilerplate; not direct frontend skill source material.                                      |
| 262 | `Hf4wSFYTygMz48u1mcTDUw` | `css-tricks-critical-request-redirect`      | `rejected`  | Provided article URL redirects to the CSS-Tricks homepage; source is unusable.                               |
| 263 | `5BipwdFDGsbY4ZXracY2rt` | `react-router-prompt-source`                | `deferred`  | Router prompt/dialog package code; possible pattern inventory, but not a guide.                              |
| 264 | `3zNQbsyz9k2bM4nzFdLggX` | `piccalilli-printing-the-web`               | `candidate` | Durable print stylesheet article with debugging and paper-layout guidance.                                   |
| 265 | `YazxJrDcieJVYmHyRDzrbe` | `css-tricks-pure-css-tabs-details-subgrid`  | `candidate` | Practical CSS tabs article using `details`, grid, and subgrid.                                               |
| 266 | `UTajjJPvdEba1VPwdTizUt` | `create-react-pwa-github`                   | `rejected`  | Stale create-react-app/PWA starter repo; use current PWA docs instead.                                       |
| 267 | `WkwLDNdcHCPPTzhy7xSeTM` | `radix-twitter-release`                     | `rejected`  | Social/release post about Radix fixes and CSS variables, not source guidance.                                |
| 268 | `Wjfp7pFbbdJJVyBehWNDju` | `razzle-github`                             | `deferred`  | Universal React build tool project; route to JS/SSR tooling review.                                          |
| 269 | `2A7kzYTTWgXACBGMnjjGbH` | `mux-react-19-rsc-actions`                  | `candidate` | Article explaining React 19 Server Components and Actions through concrete use cases.                        |
| 270 | `F4SxcNqNzc6eTRioiBpS1x` | `react-aria-components-docs`                | `candidate` | Official React Aria Components documentation for accessible custom-styled components.                        |
| 271 | `4WzLVR39bEB3arthAczwBb` | `react-aria-tooltip-github`                 | `rejected`  | Narrow tooltip package repo; use current ARIA/platform tooltip guidance instead.                             |
| 272 | `3WYkF1zSWRxCqPsqU7wh4p` | `reactbits-homepage`                        | `deferred`  | Animated component gallery/product homepage; vendor/component inventory only.                                |
| 273 | `NPWD11eWu3murnKuyHcuGa` | `react-boilerplate-github`                  | `rejected`  | Old boilerplate repo; not durable workflow guidance.                                                         |
| 274 | `9AeXUcJL1CTMamyowMog9M` | `react-component-queries-github`            | `rejected`  | Old component-query package superseded by modern CSS container-query guidance.                               |
| 275 | `3e46uPxTe8gvm8ehnyasKc` | `react-dom-stream-github`                   | `rejected`  | Old React streaming SSR package; use current React/framework docs instead.                                   |
| 276 | `Lg2nNwUVYrP5tsbmHCTmFj` | `react-dom-stream-github`                   | `rejected`  | Duplicate old React streaming SSR package with tracking parameter.                                           |
| 277 | `bjSgb8q93XCZg6yU6BGtg`  | `css-tricks-react-hooks-deep-cuts`          | `candidate` | Article-style React hooks guide; use as secondary source behind current React docs.                          |
| 278 | `UjHjZQ7TBA3S8UeqtxHsir` | `react-imgpro-github`                       | `rejected`  | Old React image-processing component package; not durable effects guidance.                                  |
| 279 | `JwjayStuekujB2jkURq68P` | `react-loadable-github`                     | `rejected`  | Legacy code-splitting package; prefer current React lazy/Suspense docs.                                      |
| 280 | `RHX3KcmXehHKSH8nnHmDT2` | `thenewstack-react-panel-rsc`               | `rejected`  | News/panel summary about RSC adoption; interesting but not actionable skill guidance.                        |
| 281 | `4v3oGRw8ckhsmt6rAMYdxp` | `react-path-menu-github`                    | `rejected`  | Animated menu demo package; not a reusable source guide.                                                     |
| 282 | `H2dk9oNy8aqPvq6YnsB3Ui` | `react-prepare-github`                      | `rejected`  | Old async SSR package; superseded by current React/framework data-loading patterns.                          |
| 283 | `6Nnu5sxtprHnnwpkYz12xz` | `react-responsive-github`                   | `deferred`  | React media-query package; already better suited to responsive tooling review.                               |
| 284 | `49H4xjKuDFNZniFvH6v3yt` | `youtube-react-roundtable-rsc`              | `deferred`  | RSC roundtable video; possible background material, not direct source-card content.                          |
| 285 | `9jyDhDQy27UdXuhYMmL6uz` | `youtube-react-roundtable-rsc`              | `deferred`  | Exact duplicate of the RSC roundtable video.                                                                 |
| 286 | `N9vSFkk6XUZVhCRNZDEHVe` | `react-select-virtualized-select-github`    | `deferred`  | Select and virtualized-select package inventory; component-library review only.                              |
| 287 | `Awvp1FVpZjBViqwdTDb1Wp` | `redwood-rsc-now-404`                       | `rejected`  | Provided RedwoodJS blog URL now 404 and was framework-specific announcement material.                        |
| 288 | `M8jjLUR6CSSvPXyM9UDhbd` | `youtube-rsc-under-7-minutes`               | `deferred`  | RSC explainer video; route to React/RSC media review if videos are accepted.                                 |
| 289 | `W1VjtM8cD41zRdCJtXKXuJ` | `epicweb-rsc-vite-react-router`             | `candidate` | Practical RSC implementation tip using Vite and React Router.                                                |
| 290 | `XpjwajaJmjFSymT8XA2rx6` | `timtech-rsc-without-framework`             | `candidate` | Detailed no-framework RSC experiment with clear caveats.                                                     |
| 291 | `5z3QUJD3kTdKmckn5j5Wkd` | `react-sortable-hoc-github`                 | `rejected`  | Legacy drag/sort package; package shopping, not direct UI guidance.                                          |
| 292 | `6sQSLwmgR2aFmvazfMCPa1` | `react-accessible-tabs-github`              | `rejected`  | Old accessible-tabs package; use ARIA APG/current component docs instead.                                    |
| 293 | `5BEtWpALnkDv6LFZL1Tibf` | `react-toolbox-github`                      | `rejected`  | Old component library package; not direct skill source material.                                             |
| 294 | `3W8zeFHc4AVXWZ4urZr49T` | `react-color-github`                        | `deferred`  | Color picker package; possible component/design-tool inventory only.                                         |
| 295 | `3SnoNraGQa25Lza6zkhsx1` | `react-poop-github`                         | `rejected`  | Old React error-handler package; not frontend UI guidance.                                                   |
| 296 | `3XJAUQjYcWgpUKURQC6caV` | `ishadeed-rebuild-featured-news-modern-css` | `candidate` | Strong modern CSS layout rebuild article with concrete implementation details.                               |
| 297 | `VWJTy7jcv7sq1r1BXNtREp` | `ishadeed-rebuild-featured-news-modern-css` | `candidate` | Duplicate modern CSS rebuild article with newsletter parameters.                                             |
| 298 | `X1Zu8htQT8puU3Jq847WSb` | `ishadeed-rebuild-featured-news-modern-css` | `candidate` | Duplicate modern CSS rebuild article.                                                                        |
| 299 | `WkSeLg4zJ3iv4coHK7D6wb` | `ishadeed-redesign-2024`                    | `candidate` | Detailed redesign case study with CSS highlights, responsive layout, and interaction notes.                  |
| 300 | `3VLwRbZZGzA5w3cSuFP4hL` | `tom-preston-werner-redwood-next-epoch-rsc` | `deferred`  | Framework strategy article about Redwood/RSC; useful context only for RSC history.                           |

## Source Groups

### Candidate: CSS Layout, Interaction, And Accessibility

- `frontendmasters-pointed-tooltips` is useful for tooltip positioning and CSS
  Anchor Positioning, but should be paired with current browser support and ARIA
  guidance before any skill rule.
- `piccalilli-practical-accessibility-tips`, `react-aria-components-docs`, and
  `css-tricks-pure-css-tabs-details-subgrid` provide practical accessibility
  and component markup guidance. React Aria should remain a vendor/library
  reference, not a mandate to use that library.
- `piccalilli-printing-the-web` is a solid source for print stylesheets and
  print debugging.
- `ishadeed-rebuild-featured-news-modern-css` and `ishadeed-redesign-2024`
  contain concrete modern CSS layout, container query, scroll animation, and
  responsive implementation examples.

### Candidate: React Architecture And RSC

- `mux-react-19-rsc-actions`, `epicweb-rsc-vite-react-router`, and
  `timtech-rsc-without-framework` are the strongest RSC sources in this queue:
  they explain boundaries, server/client behavior, and practical caveats.
- `css-tricks-react-hooks-deep-cuts` can be a secondary hooks reference, but any
  skill edits should privilege current React documentation.
- The New Stack panel, Tom Preston-Werner's Redwood article, the RedwoodJS 404
  blog link, and YouTube videos should not be direct source cards from this
  queue. They are context or historical/vendor material.

### Candidate: Color And Visual Systems

- `chroma-palettes-vis4-color-scales` is promoted because the URL group includes
  a guide-like article about multi-hued color scales and a palette helper. The
  Chroma.js GitHub repo itself remains project inventory.
- `react-color-github` is only component inventory; do not promote package pages
  into color guidance without stronger design-system or accessibility sources.

### Deferred: Component, Package, And Tooling Inventory

- Component-library/vendor inventory: `plyr-react-github`, `reactbits-homepage`,
  `react-select-virtualized-select-github`, and `react-color-github`.
- Tooling/project inventory: `postcss-functions-github`, `doiuse-github`,
  `polished-github`, `razzle-github`, and `react-responsive-github`.
- Pattern inventory that needs better sources: `react-router-prompt-source` for
  navigation blocking/dialogs and the RSC YouTube videos for explanatory media.

### Rejected: Broken URLs, Stale Projects, And Package Shopping

- Broken/unusable sources: `css-tricks-critical-request-redirect` and
  `redwood-rsc-now-404`.
- Release/social material: `radix-twitter-release`.
- Stale or superseded projects: `postcss-flexbugs-fixes-github`,
  `postcss-style-guide-github`, `create-react-pwa-github`,
  `preact-redux-isomorphic-github`, `react-dom-stream-github`,
  `react-loadable-github`, `react-prepare-github`, `react-component-queries`,
  `react-boilerplate`, and `react-toolbox`.
- Narrow package/demo links: `react-aria-tooltip-github`,
  `react-imgpro-github`, `react-path-menu-github`,
  `react-sortable-hoc-github`, `react-accessible-tabs-github`, and
  `react-poop-github`.
- Low-actionability context: `thenewstack-react-panel-rsc` is a news/panel
  summary rather than implementation guidance.

## Proposed Outcome

Decision: `existing skill update candidates` plus `defer` for project/vendor
inventory.

Target skills or references:

- Existing frontend/UI/CSS references can use the candidate sources for anchor
  positioning, tooltips, print stylesheets, accessibility snippets, tabs,
  subgrid, modern CSS layout, responsive redesign implementation, and color
  scales.
- React references can use the RSC and hooks candidates only after checking
  current React documentation as the primary authority.
- Component package links should remain inventory and should not be promoted
  from package README/homepage material alone.
- Do not create a new skill from this queue alone.
- Do not promote GitHub package links, social posts, release notes, broken URLs,
  or framework strategy announcements into skill sources without a later, more
  specific review.

## Things Actions

| Things ID                | Decision  | Final tag                 | Complete? | Reason                                                                          |
| ------------------------ | --------- | ------------------------- | --------- | ------------------------------------------------------------------------------- |
| `H2vSAorpXj9royWFZTMqfZ` | candidate | `Skill Archive Candidate` | yes       | Practical CSS Anchor Positioning tooltip article.                               |
| `8Xf7PX8wkRBkjRzPXaQ5UU` | deferred  | `Skill Archive Deferred`  | yes       | React media-player package; component inventory only.                           |
| `MGBuPLzGsamXEwCeHP44PS` | rejected  | `Skill Archive Rejected`  | yes       | Archived PostCSS flexbug package; use current platform guidance.                |
| `AguDUCCtpqGUuCdPJPJg9v` | deferred  | `Skill Archive Deferred`  | yes       | PostCSS utility package; route to CSS tooling review.                           |
| `TvJdZrKgpyeVNSaVxaFzDL` | rejected  | `Skill Archive Rejected`  | yes       | Package source file, not guide/reference material.                              |
| `GtPxGMm2QEVUHLgNpLfSw6` | candidate | `Skill Archive Candidate` | yes       | URL group includes a durable multi-hued color-scale article and palette helper. |
| `7WrHBhnXHPjkK1x1DAMpbv` | deferred  | `Skill Archive Deferred`  | yes       | Styling utility package; CSS-in-JS/tooling inventory.                           |
| `WgV8JbhdMi2sPmCfWH2QwQ` | rejected  | `Skill Archive Rejected`  | yes       | Old/archived PostCSS style-guide generator.                                     |
| `H1xDc6da6Nq3M97iYDf69A` | deferred  | `Skill Archive Deferred`  | yes       | CSS browser-support lint package; tooling review material.                      |
| `C8Z8ZDF6UyDgoymLZ5tnn6` | candidate | `Skill Archive Candidate` | yes       | Practical accessibility snippets and component markup explainers.               |
| `XCCm5J3r1iqPDmJaMB6N1j` | rejected  | `Skill Archive Rejected`  | yes       | Old Preact/Redux example app and boilerplate.                                   |
| `Hf4wSFYTygMz48u1mcTDUw` | rejected  | `Skill Archive Rejected`  | yes       | Provided CSS-Tricks article URL redirects to homepage.                          |
| `5BipwdFDGsbY4ZXracY2rt` | deferred  | `Skill Archive Deferred`  | yes       | Router prompt/dialog package code; needs better pattern sources.                |
| `3zNQbsyz9k2bM4nzFdLggX` | candidate | `Skill Archive Candidate` | yes       | Durable print stylesheet and print debugging article.                           |
| `YazxJrDcieJVYmHyRDzrbe` | candidate | `Skill Archive Candidate` | yes       | CSS tabs article using `details`, grid, and subgrid.                            |
| `UTajjJPvdEba1VPwdTizUt` | rejected  | `Skill Archive Rejected`  | yes       | Stale create-react-app/PWA starter repo.                                        |
| `WkwLDNdcHCPPTzhy7xSeTM` | rejected  | `Skill Archive Rejected`  | yes       | Radix release/social post, not source guidance.                                 |
| `Wjfp7pFbbdJJVyBehWNDju` | deferred  | `Skill Archive Deferred`  | yes       | Universal React build tool project; JS/SSR tooling review.                      |
| `2A7kzYTTWgXACBGMnjjGbH` | candidate | `Skill Archive Candidate` | yes       | React 19 Server Components and Actions article with concrete use cases.         |
| `F4SxcNqNzc6eTRioiBpS1x` | candidate | `Skill Archive Candidate` | yes       | Official React Aria Components docs for accessible custom components.           |
| `4WzLVR39bEB3arthAczwBb` | rejected  | `Skill Archive Rejected`  | yes       | Narrow tooltip package repo; prefer current ARIA/platform guidance.             |
| `3WYkF1zSWRxCqPsqU7wh4p` | deferred  | `Skill Archive Deferred`  | yes       | Animated component gallery/product homepage.                                    |
| `NPWD11eWu3murnKuyHcuGa` | rejected  | `Skill Archive Rejected`  | yes       | Old React boilerplate repo.                                                     |
| `9AeXUcJL1CTMamyowMog9M` | rejected  | `Skill Archive Rejected`  | yes       | Old component-query package superseded by container queries.                    |
| `3e46uPxTe8gvm8ehnyasKc` | rejected  | `Skill Archive Rejected`  | yes       | Old React streaming SSR package.                                                |
| `Lg2nNwUVYrP5tsbmHCTmFj` | rejected  | `Skill Archive Rejected`  | yes       | Duplicate old React streaming SSR package.                                      |
| `bjSgb8q93XCZg6yU6BGtg`  | candidate | `Skill Archive Candidate` | yes       | Article-style React hooks guide; secondary to current React docs.               |
| `UjHjZQ7TBA3S8UeqtxHsir` | rejected  | `Skill Archive Rejected`  | yes       | Old React image-processing package.                                             |
| `JwjayStuekujB2jkURq68P` | rejected  | `Skill Archive Rejected`  | yes       | Legacy code-splitting package; prefer lazy/Suspense docs.                       |
| `RHX3KcmXehHKSH8nnHmDT2` | rejected  | `Skill Archive Rejected`  | yes       | RSC news/panel summary, not actionable guidance.                                |
| `4v3oGRw8ckhsmt6rAMYdxp` | rejected  | `Skill Archive Rejected`  | yes       | Animated menu demo package, not source guidance.                                |
| `H2dk9oNy8aqPvq6YnsB3Ui` | rejected  | `Skill Archive Rejected`  | yes       | Old async SSR package.                                                          |
| `6Nnu5sxtprHnnwpkYz12xz` | deferred  | `Skill Archive Deferred`  | yes       | React media-query package; responsive tooling inventory.                        |
| `49H4xjKuDFNZniFvH6v3yt` | deferred  | `Skill Archive Deferred`  | yes       | RSC roundtable video; background/media review only.                             |
| `9jyDhDQy27UdXuhYMmL6uz` | deferred  | `Skill Archive Deferred`  | yes       | Duplicate RSC roundtable video.                                                 |
| `N9vSFkk6XUZVhCRNZDEHVe` | deferred  | `Skill Archive Deferred`  | yes       | Select and virtualized-select packages; component inventory.                    |
| `Awvp1FVpZjBViqwdTDb1Wp` | rejected  | `Skill Archive Rejected`  | yes       | RedwoodJS blog URL now 404 and framework-specific.                              |
| `M8jjLUR6CSSvPXyM9UDhbd` | deferred  | `Skill Archive Deferred`  | yes       | RSC explainer video; defer to React/RSC media review.                           |
| `W1VjtM8cD41zRdCJtXKXuJ` | candidate | `Skill Archive Candidate` | yes       | Practical RSC implementation tip for Vite and React Router.                     |
| `XpjwajaJmjFSymT8XA2rx6` | candidate | `Skill Archive Candidate` | yes       | No-framework RSC experiment with clear caveats.                                 |
| `5z3QUJD3kTdKmckn5j5Wkd` | rejected  | `Skill Archive Rejected`  | yes       | Legacy drag/sort package.                                                       |
| `6sQSLwmgR2aFmvazfMCPa1` | rejected  | `Skill Archive Rejected`  | yes       | Old accessible-tabs package; prefer ARIA APG/current docs.                      |
| `5BEtWpALnkDv6LFZL1Tibf` | rejected  | `Skill Archive Rejected`  | yes       | Old React component library package.                                            |
| `3W8zeFHc4AVXWZ4urZr49T` | deferred  | `Skill Archive Deferred`  | yes       | Color picker package; component/design-tool inventory.                          |
| `3SnoNraGQa25Lza6zkhsx1` | rejected  | `Skill Archive Rejected`  | yes       | Old React error-handler package.                                                |
| `3XJAUQjYcWgpUKURQC6caV` | candidate | `Skill Archive Candidate` | yes       | Strong modern CSS layout rebuild article.                                       |
| `VWJTy7jcv7sq1r1BXNtREp` | candidate | `Skill Archive Candidate` | yes       | Duplicate modern CSS layout rebuild article.                                    |
| `X1Zu8htQT8puU3Jq847WSb` | candidate | `Skill Archive Candidate` | yes       | Duplicate modern CSS layout rebuild article.                                    |
| `WkSeLg4zJ3iv4coHK7D6wb` | candidate | `Skill Archive Candidate` | yes       | Detailed redesign case study with CSS implementation highlights.                |
| `3VLwRbZZGzA5w3cSuFP4hL` | deferred  | `Skill Archive Deferred`  | yes       | Redwood/RSC framework strategy article; context only.                           |
