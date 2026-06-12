# Cluster Brief: Frontend UI Queue 04

## Metadata

| Field          | Value                                                |
| -------------- | ---------------------------------------------------- |
| Things cluster | `Skill: Frontend UI`                                 |
| Reviewed on    | 2026-06-10                                           |
| Reviewer       | Codex                                                |
| Write scope    | `docs/source-review/clusters/frontend-ui-04.md` only |

## Scope

This review covers 50 open Things intake items tagged as frontend UI. It is an
intermediate source-review artifact only: no Things tasks were changed and no
skill files were edited.

The filter used here is intentionally strict. Articles, official docs,
standards-facing explainers, and high-quality implementation guides can become
candidates. GitHub repos, package READMEs, product homepages, generators,
release/news material, dead links, and old package-shopping ideas are deferred
or rejected unless the source itself is durable guidance for a repeatable agent
workflow.

## Access Notes

- All provided URL groups were opened or checked over the network.
- GitHub project links were checked directly and cross-checked against
  `docs/source-review/github-projects/github-project-matrix.csv` where present.
- `https://github.com/morellodev/react-awesome-reveal` redirects to
  `https://github.com/awesome-reveal/react-awesome-reveal`.
- `https://github.com/jonathantneal/postcss-font-magician` redirects to
  `https://github.com/csstools/postcss-font-magician`.
- `https://github.com/signavio/react-mentions` returned 404. Search results
  show old issue pages and a maintained fork, but the queued source itself is
  not usable as archive material.
- `http://blog.invisionapp.com/5-ways-to-bridge-the-designer-developer-gap-on-responsive-web-projects/`
  failed DNS resolution and was treated as unavailable.
- The Medium landing-page article was reachable through browser extraction, but
  direct scripted fetches returned 403. It was still treated as marketing
  material rather than frontend UI source material.
- Ark UI and Learn UI Gradient Generator were reachable, but both are product or
  tool pages rather than durable skill-reference sources.
- Exact duplicate GitHub project links were reviewed once and applied to both
  Things IDs where relevant.

## Dedupe Summary

- 50 Things tasks reviewed.
- 44 broad source groups after exact duplicate and topic grouping.
- Exact duplicates:
  - `KKH1oagVwVHkUvf9eaYk5v`, `SohHo2sTVGpVckWwaJbj1n`: `recharts/recharts`.
  - `GyAT4hvuo3roJomWMo7UGH`, `XKjTg5ua72GedAUnNtHw8P`:
    `wellyshen/react-cool-dimensions`.
  - `EJt1GC7DwwV6z9bvd5aN4w`, `Voq3eXmGAuNXz7EX62L3Da`:
    `yocontra/react-responsive`.
- Topic duplicates or near-duplicates:
  - Virtualized list projects appear as `react-virtuoso` and
    `TanStack/virtual`; both are project inventory, not direct source material.
  - HTML-to-React rendering appears as `html-react-parser` and `interweave`;
    both need a future rich-text/security review with stronger sources.
  - Fluid/responsive typography appears as a package/tooling item
    (`postcss-font-magician` and old browser-support notes) and a better article
    candidate (`css-tricks-simplified-fluid-typography`).
  - Theming/color/gradient material appears across Learn UI, CSS-Tricks,
    WebKit, and Piccalilli; only explanatory articles or standards-facing
    sources were promoted.

## Decision Summary

| Status      | Count | Rationale                                                                                                                                                                                              |
| ----------- | ----: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `candidate` |     9 | Durable CSS, responsive design, layout stability, component, typography, theming, and standards-facing color guidance from articles or official browser-project sources.                               |
| `deferred`  |    23 | Potentially useful project inventory, vendor/component-library pages, data-viz or virtualization packages, analytics/tooling topics, or marketing/UX strategy sources better handled in later reviews. |
| `rejected`  |    18 | Dead links, stale shims, narrow package-shopping, product/tool generators, personal/profile material, old data-loading components, or domain-specific sources with little skill-archive value.         |

## Per-Thing Decisions

|   # | Things ID                | URL group                            | Decision    | Notes                                                                                                             |
| --: | ------------------------ | ------------------------------------ | ----------- | ----------------------------------------------------------------------------------------------------------------- |
| 151 | `LZRDpEYjeHhts6ZpwaLVcA` | `colorgrad-js-github`                | `rejected`  | Narrow gradient/color package README; not durable UI guidance.                                                    |
| 152 | `3scEfUM3ocFjSBFAgnDiPV` | `react-awesome-reveal-github`        | `rejected`  | Reveal animation package link; prefer Intersection Observer, animation, and accessibility guides.                 |
| 153 | `VMzSC6Z8rxQPsonLkwTjYE` | `lostgrid-github`                    | `rejected`  | PostCSS grid-system package; superseded by current CSS Grid/layout guidance.                                      |
| 154 | `FKNHDPCPYFDZkdT91uJ5P6` | `react-virtuoso-github`              | `deferred`  | Major virtualization component project; keep for list-performance/vendor review, not a direct source.             |
| 155 | `5bvYodeB9bwxBnvFMH9uoi` | `react-spring-github`                | `deferred`  | Major React animation library; defer to animation/vendor review with official docs.                               |
| 156 | `W3G3ZQg6ZNM79BUJnWNsjh` | `react-chrono-github`                | `rejected`  | Timeline component package; narrow package-shopping.                                                              |
| 157 | `KKH1oagVwVHkUvf9eaYk5v` | `recharts-github`                    | `deferred`  | Major React charting library; defer to data visualization/vendor review.                                          |
| 158 | `SohHo2sTVGpVckWwaJbj1n` | `recharts-github`                    | `deferred`  | Exact duplicate of item 157; same deferred data-viz inventory decision.                                           |
| 159 | `JRJvHuVJGuTPftcHmkFfg2` | `html-react-parser-github`           | `deferred`  | HTML-to-React parser package; revisit in rich-text/security review with stronger guidance.                        |
| 160 | `yHQ3DRMjY8BWw28tuZqRf`  | `beautify-github-profile-github`     | `rejected`  | GitHub profile README inspiration; not frontend UI skill material.                                                |
| 161 | `GGPQmRjmFD5NFPS3n5JWmh` | `react-number-format-github`         | `rejected`  | Number-format input package README; too narrow as source material.                                                |
| 162 | `Az7uAEKtQPN3uJJvgZkovu` | `react-i18nify-github`               | `rejected`  | Small React i18n package link; use current i18n docs/guides instead.                                              |
| 163 | `JZxVxfFVeeyVJErzr515ro` | `ha-component-kit-github`            | `rejected`  | Home Assistant-specific component kit; domain-specific package, not archive guidance.                             |
| 164 | `3EpJynuP5yP1pFKfCJfKfP` | `react-text-truncate-github`         | `rejected`  | Narrow multiline truncation component package.                                                                    |
| 165 | `6PapH8vdvuehpCa6JuLWKw` | `react-mentions-github`              | `rejected`  | Queued GitHub URL returns 404; old issue pages are not suitable source material.                                  |
| 166 | `ELpMe7AdVxnqT3kmwzNcUM` | `react-styleguidist-github`          | `deferred`  | Component documentation/styleguide tool; route to docs tooling review.                                            |
| 167 | `HGFSqGLwWWXu5na6H39uaW` | `react-table-library-github`         | `deferred`  | React data-table project; defer to data UI/vendor inventory.                                                      |
| 168 | `Jnrt2uBn6mT8n8P4zsio2E` | `tabler-icons-github`                | `deferred`  | Icon asset library; defer to asset/vendor inventory.                                                              |
| 169 | `BUYxFUWF4aMvizMKqVMU4T` | `tanstack-virtual-github`            | `deferred`  | Strong virtualization project; project inventory only in this pass.                                               |
| 170 | `U5XTsuGAr2uxJ3WwAU9oeD` | `react-modal-sheet-github`           | `deferred`  | Bottom-sheet component project; defer to component-library/accessibility review.                                  |
| 171 | `4AGKBdjeM296jZZWxQhWAH` | `react-intersection-observer-github` | `deferred`  | Useful Intersection Observer hook package; needs web-platform/performance sources before skill use.               |
| 172 | `Hd529bPNrMrax1E3GSaehh` | `react-youtube-github`               | `rejected`  | YouTube component package; narrow vendor wrapper.                                                                 |
| 173 | `TvjsCCALd2uX8PYUpaZ4xU` | `tokencss-github`                    | `deferred`  | Design-token/CSS tooling project; route to token/tooling review if still relevant.                                |
| 174 | `8tzLAzMFBYGbM1B2NzG9cj` | `tremor-github`                      | `deferred`  | Dashboard component library project; vendor inventory, not pattern guidance.                                      |
| 175 | `AZJWx2Kwq2VBbhCNDeTvA1` | `mutative-github`                    | `deferred`  | State-management/immutability package; JS tooling rather than frontend UI source.                                 |
| 176 | `GyAT4hvuo3roJomWMo7UGH` | `react-cool-dimensions-github`       | `rejected`  | Resize-measurement hook package; prefer ResizeObserver/container-query guidance.                                  |
| 177 | `XKjTg5ua72GedAUnNtHw8P` | `react-cool-dimensions-github`       | `rejected`  | Exact duplicate of item 176; same package-shopping decision.                                                      |
| 178 | `7G9YYoUQs33pDQU7gw9LK2` | `react-recoil-form-github`           | `rejected`  | Low-signal form package README; not durable form guidance.                                                        |
| 179 | `W7ESepiProEUjhtUqxed16` | `react-i13n-github`                  | `deferred`  | React instrumentation package; possible analytics/telemetry review, not UI source.                                |
| 180 | `EJt1GC7DwwV6z9bvd5aN4w` | `react-responsive-github`            | `deferred`  | React media-query package; defer to responsive tooling review with current CSS/media docs.                        |
| 181 | `Voq3eXmGAuNXz7EX62L3Da` | `react-responsive-github`            | `deferred`  | Exact duplicate of item 180; same deferred tooling decision.                                                      |
| 182 | `KVZ69EFRwbtDmfmgcQQ17`  | `learnui-gradient-generator`         | `rejected`  | Generator/product tool page with inspiration gallery; not durable skill source material.                          |
| 183 | `4W7PqhU6yWzhKBgKEyXER5` | `css-tricks-grainy-gradients`        | `candidate` | Practical CSS/SVG noise-gradient guide with use cases and browser-support notes.                                  |
| 184 | `UwB5V42Y9HiqNWqSvz4YBA` | `baymard-responsive-upscaling`       | `candidate` | Research-backed responsive upscaling article for large-screen ecommerce layouts.                                  |
| 185 | `XvSAQWoEpTXNRUX6RDcZhp` | `postcss-font-magician-github`       | `deferred`  | Font embedding PostCSS package; JS/CSS tooling inventory, not direct UI guidance.                                 |
| 186 | `Ue3NnJX9xPqT2kLVzF6kSg` | `invision-responsive-gap`            | `rejected`  | InVision blog URL failed DNS resolution; unavailable historical article.                                          |
| 187 | `KEuj9jCREMgQEfD2pYJ4rS` | `smashing-content-shift`             | `candidate` | Durable layout-stability article covering media, intrinsic ratios, widgets, ads, dynamic content, and fonts.      |
| 188 | `3rQzahG5KHnXKhJufrcC45` | `ishadeed-treeview-indent`           | `candidate` | Strong component-layout guide for treeview indentation across design-system examples.                             |
| 189 | `4CcKoLqkZJ8QHqagoSJ6BG` | `holen-github`                       | `rejected`  | Old declarative React fetch component; stale package pick, not UI source.                                         |
| 190 | `RsAg1sTf65Cn84fY7YZ9td` | `medium-landing-pages-convert`       | `deferred`  | Landing-page/social-proof article is marketing/conversion material, not frontend UI source.                       |
| 191 | `UgGCL5n8uGBDTqjtxt92bU` | `ark-ui-homepage`                    | `deferred`  | Headless component-library homepage; vendor review only, despite useful positioning.                              |
| 192 | `NizE9fkVjBwjeGJDD2Bs2c` | `sitepoint-font-size-adjust`         | `candidate` | CSS typography article on `font-size-adjust`; pair with current MDN/support data before skill edits.              |
| 193 | `HsELvKqw62yE9CcCiLEVFQ` | `mq4-hover-shim-github`              | `rejected`  | Archived 2015 hover media-query shim; stale polyfill source.                                                      |
| 194 | `9xPV5LuXs2FaoCAzNAKvsd` | `piccalilli-button-component`        | `candidate` | High-quality semantic button component guide covering HTML-first structure, CSS, states, and variants.            |
| 195 | `KEXm5g2iL2Vp78TV4tTmsh` | `webkit-contrast-color`              | `candidate` | Official WebKit standards-facing explainer for `contrast-color()` with accessibility caveats.                     |
| 196 | `WXP7Uf9XjHqD2FzfyCGkSL` | `smashing-storytelling-ux`           | `deferred`  | UX storytelling/product strategy article; useful but closer to content/marketing strategy than UI implementation. |
| 197 | `QzrrbFs1PspCApNApzMHBg` | `piccalilli-modern-css-theming`      | `candidate` | Practical modern CSS theming guide using layered foundations, skeletal CSS, and theme-specific flair.             |
| 198 | `8TB51Gz3em7HWtxBbKHSm1` | `interweave-github`                  | `deferred`  | React safe-HTML rendering package; defer to rich-text/security review with stronger docs.                         |
| 199 | `CocPynbWNrZpwkHg2GHF9`  | `html5validator-github`              | `deferred`  | Static HTML validation CLI; route to QA/static-site tooling review.                                               |
| 200 | `FSjG6W4nrS1FvNtvR4wb6i` | `css-tricks-fluid-typography`        | `candidate` | Practical fluid typography article; use with current CSS `clamp()` and accessibility guidance.                    |

## Source Groups

### Candidate: CSS Effects, Typography, And Theming

- `css-tricks-grainy-gradients` is a useful implementation source for adding
  texture to gradients with SVG noise and CSS gradients.
- `sitepoint-font-size-adjust` and `css-tricks-fluid-typography` are typography
  references. Both need current support and accessibility checks before becoming
  skill rules.
- `webkit-contrast-color` is an official, standards-facing color source. It is
  useful because it explains both the promise and the accessibility limits of
  automatic black/white contrast choices.
- `piccalilli-modern-css-theming` is a practical CSS architecture source for
  theme layering and progressive customization.

### Candidate: Responsive Layout And Component Craft

- `baymard-responsive-upscaling` provides research-backed large-screen layout
  guidance: reuse the same content, package it differently, and balance image
  detail against overview.
- `smashing-content-shift` is older but still useful for layout stability:
  reserve media space, handle dynamic widgets carefully, and account for web
  font shifts.
- `ishadeed-treeview-indent` is a strong component-level layout reference for
  hierarchical tree views.
- `piccalilli-button-component` is a strong semantic component guide for buttons
  and should be preferred over package examples.

### Deferred: Project, Vendor, And Adjacent Reviews

- Data visualization and dashboard inventory: `recharts`,
  `react-table-library`, and `tremor`.
- Virtualization and performance-adjacent inventory: `react-virtuoso`,
  `TanStack/virtual`, `react-intersection-observer`, and `react-responsive`.
- Component-library/vendor inventory: `react-spring`, `react-modal-sheet`,
  `styleguidist`, `tabler-icons`, `tokencss`, `Ark UI`, and `html5validator`.
- Rich-text/security inventory: `html-react-parser` and `interweave`; package
  README links are insufficient without current security and sanitization
  references.
- Adjacent content strategy: the Medium landing-page article and Smashing UX
  storytelling article are better routed to marketing/content strategy reviews.

### Rejected: Weak Package Shopping, Dead Links, And Irrelevant Sources

- Narrow or stale package links: `colorgrad-js`, `react-awesome-reveal`,
  `lostgrid`, `react-chrono`, `react-number-format`, `react-i18nify`,
  `react-text-truncate`, `react-youtube`, `react-cool-dimensions`,
  `react-recoil-form`, and `holen`.
- Unavailable or obsolete sources: `signavio/react-mentions`,
  the InVision responsive article, and the archived `mq4-hover-shim`.
- Irrelevant or too product/tool-centered sources:
  `beautify-github-profile`, `ha-component-kit`, and the Learn UI Gradient
  Generator.

## Proposed Outcome

Decision: `existing skill update candidates` plus `defer` for project/vendor
inventory.

Target skills or references:

- Existing frontend/UI/CSS design references can use the candidate sources for
  gradient texture, large-screen responsive layout, layout stability, treeview
  indentation, typography, semantic buttons, contrast-color caveats, theming,
  and fluid type.
- Future data visualization, component-library, animation, responsive tooling,
  rich-text/security, and static-site QA reviews can revisit the deferred
  projects with current official docs or stronger guides.
- Do not create a new skill from this queue alone.
- Do not promote package README links or product homepages into skill sources
  unless a later vendor review establishes a clear agent workflow and stronger
  reference set.

## Things Actions

| Things ID                | Decision  | Final tag                 | Complete? | Reason                                                                            |
| ------------------------ | --------- | ------------------------- | --------- | --------------------------------------------------------------------------------- |
| `LZRDpEYjeHhts6ZpwaLVcA` | rejected  | `Skill Archive Rejected`  | yes       | Narrow gradient/color package README; not durable UI guidance.                    |
| `3scEfUM3ocFjSBFAgnDiPV` | rejected  | `Skill Archive Rejected`  | yes       | Reveal animation package link; prefer platform and accessibility guidance.        |
| `VMzSC6Z8rxQPsonLkwTjYE` | rejected  | `Skill Archive Rejected`  | yes       | PostCSS grid-system package; superseded by current CSS layout guidance.           |
| `FKNHDPCPYFDZkdT91uJ5P6` | deferred  | `Skill Archive Deferred`  | yes       | Major virtualization component project; defer to list-performance/vendor review.  |
| `5bvYodeB9bwxBnvFMH9uoi` | deferred  | `Skill Archive Deferred`  | yes       | Major React animation library; defer to animation/vendor review.                  |
| `W3G3ZQg6ZNM79BUJnWNsjh` | rejected  | `Skill Archive Rejected`  | yes       | Timeline component package; narrow package-shopping.                              |
| `KKH1oagVwVHkUvf9eaYk5v` | deferred  | `Skill Archive Deferred`  | yes       | Major React charting library; defer to data visualization/vendor review.          |
| `SohHo2sTVGpVckWwaJbj1n` | deferred  | `Skill Archive Deferred`  | yes       | Duplicate Recharts link; same data-viz inventory decision.                        |
| `JRJvHuVJGuTPftcHmkFfg2` | deferred  | `Skill Archive Deferred`  | yes       | HTML-to-React parser package; revisit in rich-text/security review.               |
| `yHQ3DRMjY8BWw28tuZqRf`  | rejected  | `Skill Archive Rejected`  | yes       | GitHub profile README inspiration; not frontend UI skill material.                |
| `GGPQmRjmFD5NFPS3n5JWmh` | rejected  | `Skill Archive Rejected`  | yes       | Number-format input package README; too narrow as source material.                |
| `Az7uAEKtQPN3uJJvgZkovu` | rejected  | `Skill Archive Rejected`  | yes       | Small React i18n package link; use current i18n docs/guides instead.              |
| `JZxVxfFVeeyVJErzr515ro` | rejected  | `Skill Archive Rejected`  | yes       | Home Assistant-specific component kit; domain-specific package.                   |
| `3EpJynuP5yP1pFKfCJfKfP` | rejected  | `Skill Archive Rejected`  | yes       | Narrow multiline truncation component package.                                    |
| `6PapH8vdvuehpCa6JuLWKw` | rejected  | `Skill Archive Rejected`  | yes       | Queued GitHub URL returns 404.                                                    |
| `ELpMe7AdVxnqT3kmwzNcUM` | deferred  | `Skill Archive Deferred`  | yes       | Component documentation/styleguide tool; route to docs tooling review.            |
| `HGFSqGLwWWXu5na6H39uaW` | deferred  | `Skill Archive Deferred`  | yes       | React data-table project; defer to data UI/vendor inventory.                      |
| `Jnrt2uBn6mT8n8P4zsio2E` | deferred  | `Skill Archive Deferred`  | yes       | Icon asset library; defer to asset/vendor inventory.                              |
| `BUYxFUWF4aMvizMKqVMU4T` | deferred  | `Skill Archive Deferred`  | yes       | Strong virtualization project; project inventory only in this pass.               |
| `U5XTsuGAr2uxJ3WwAU9oeD` | deferred  | `Skill Archive Deferred`  | yes       | Bottom-sheet component project; defer to component-library/accessibility review.  |
| `4AGKBdjeM296jZZWxQhWAH` | deferred  | `Skill Archive Deferred`  | yes       | Intersection Observer hook package; needs platform/performance sources.           |
| `Hd529bPNrMrax1E3GSaehh` | rejected  | `Skill Archive Rejected`  | yes       | YouTube component package; narrow vendor wrapper.                                 |
| `TvjsCCALd2uX8PYUpaZ4xU` | deferred  | `Skill Archive Deferred`  | yes       | Design-token/CSS tooling project; route to token/tooling review.                  |
| `8tzLAzMFBYGbM1B2NzG9cj` | deferred  | `Skill Archive Deferred`  | yes       | Dashboard component library project; vendor inventory, not pattern guidance.      |
| `AZJWx2Kwq2VBbhCNDeTvA1` | deferred  | `Skill Archive Deferred`  | yes       | State-management/immutability package; JS tooling rather than frontend UI source. |
| `GyAT4hvuo3roJomWMo7UGH` | rejected  | `Skill Archive Rejected`  | yes       | Resize-measurement hook package; prefer ResizeObserver/container-query guidance.  |
| `XKjTg5ua72GedAUnNtHw8P` | rejected  | `Skill Archive Rejected`  | yes       | Duplicate react-cool-dimensions package link.                                     |
| `7G9YYoUQs33pDQU7gw9LK2` | rejected  | `Skill Archive Rejected`  | yes       | Low-signal form package README; not durable form guidance.                        |
| `W7ESepiProEUjhtUqxed16` | deferred  | `Skill Archive Deferred`  | yes       | React instrumentation package; possible analytics/telemetry review.               |
| `EJt1GC7DwwV6z9bvd5aN4w` | deferred  | `Skill Archive Deferred`  | yes       | React media-query package; defer to responsive tooling review.                    |
| `Voq3eXmGAuNXz7EX62L3Da` | deferred  | `Skill Archive Deferred`  | yes       | Duplicate react-responsive package link.                                          |
| `KVZ69EFRwbtDmfmgcQQ17`  | rejected  | `Skill Archive Rejected`  | yes       | Generator/product tool page, not durable skill source material.                   |
| `4W7PqhU6yWzhKBgKEyXER5` | candidate | `Skill Archive Candidate` | yes       | Practical CSS/SVG noise-gradient guide.                                           |
| `UwB5V42Y9HiqNWqSvz4YBA` | candidate | `Skill Archive Candidate` | yes       | Research-backed responsive upscaling article for large screens.                   |
| `XvSAQWoEpTXNRUX6RDcZhp` | deferred  | `Skill Archive Deferred`  | yes       | Font embedding PostCSS package; JS/CSS tooling inventory.                         |
| `Ue3NnJX9xPqT2kLVzF6kSg` | rejected  | `Skill Archive Rejected`  | yes       | InVision blog URL failed DNS resolution.                                          |
| `KEuj9jCREMgQEfD2pYJ4rS` | candidate | `Skill Archive Candidate` | yes       | Durable layout-stability article.                                                 |
| `3rQzahG5KHnXKhJufrcC45` | candidate | `Skill Archive Candidate` | yes       | Strong treeview indentation component-layout guide.                               |
| `4CcKoLqkZJ8QHqagoSJ6BG` | rejected  | `Skill Archive Rejected`  | yes       | Old declarative React fetch component; stale package pick.                        |
| `RsAg1sTf65Cn84fY7YZ9td` | deferred  | `Skill Archive Deferred`  | yes       | Landing-page/social-proof article belongs to marketing review.                    |
| `UgGCL5n8uGBDTqjtxt92bU` | deferred  | `Skill Archive Deferred`  | yes       | Headless component-library homepage; vendor review only.                          |
| `NizE9fkVjBwjeGJDD2Bs2c` | candidate | `Skill Archive Candidate` | yes       | CSS typography article on `font-size-adjust`; needs current support check.        |
| `HsELvKqw62yE9CcCiLEVFQ` | rejected  | `Skill Archive Rejected`  | yes       | Archived old hover media-query shim.                                              |
| `9xPV5LuXs2FaoCAzNAKvsd` | candidate | `Skill Archive Candidate` | yes       | High-quality semantic button component guide.                                     |
| `KEXm5g2iL2Vp78TV4tTmsh` | candidate | `Skill Archive Candidate` | yes       | Official WebKit `contrast-color()` explainer with accessibility caveats.          |
| `WXP7Uf9XjHqD2FzfyCGkSL` | deferred  | `Skill Archive Deferred`  | yes       | UX storytelling strategy source, not UI implementation guidance.                  |
| `QzrrbFs1PspCApNApzMHBg` | candidate | `Skill Archive Candidate` | yes       | Practical modern CSS theming guide.                                               |
| `8TB51Gz3em7HWtxBbKHSm1` | deferred  | `Skill Archive Deferred`  | yes       | React safe-HTML rendering package; defer to rich-text/security review.            |
| `CocPynbWNrZpwkHg2GHF9`  | deferred  | `Skill Archive Deferred`  | yes       | Static HTML validation CLI; route to QA/static-site tooling review.               |
| `FSjG6W4nrS1FvNtvR4wb6i` | candidate | `Skill Archive Candidate` | yes       | Practical fluid typography article.                                               |
