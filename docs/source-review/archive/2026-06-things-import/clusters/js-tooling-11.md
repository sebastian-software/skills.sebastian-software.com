# Cluster Brief: JS Tooling Queue 11

Reviewed: 2026-06-10

## Scope

This final JS tooling queue contains the remaining 35 open Things intake items
for `Skill: JS Tooling`. Most entries are GitHub projects, old Webpack-era
notes, changelogs, PRs, or package-shopping ideas. The review treats those as
project inventory rather than direct skill material. Only article-like guides
with durable, reusable guidance are promoted as candidates.

## Decision Summary

| Status | Count | Rationale |
| --- | ---: | --- |
| `candidate` | 3 | Durable guide/article sources for frontend-terminal basics, TypeScript export style, and vanilla-extract performance. |
| `deferred` | 17 | Active or potentially useful projects/resources for the GitHub Project Matrix or later focused reviews. |
| `rejected` | 15 | Stale Webpack-era tooling, release/changelog/discussion churn, old package alternatives, or archived/narrow plugins. |

## Candidate Sources

- Josh W. Comeau: `The Front-End Developer's Guide to the Terminal` is a
  current, beginner-friendly frontend terminal guide with npm scripts, Git,
  aliases, navigation, and safety basics.
- Basarat TypeScript Book: `defaultIsBad` is a focused TypeScript module/export
  style guide. It is GitHub-hosted but article-like documentation, not a project
  repo source.
- Lennart Jorgens: `Writing Performant CSS with vanilla-extract` is an
  article-style source on zero-runtime styling, CSS extraction, and build-time
  performance tradeoffs.

## Deferred Project Inventory

- Active or still-useful projects/resources: `fontfaceobserver`, `trash`,
  `pure`, `thread-loader`, `decaffeinate`, `trix`, `tsdown`, `UPNG.js`,
  `react-window`, `XState`, `thumbhash`, `vite/plugin-legacy`,
  TypeScript React Cheatsheets, and `postcss-simple-vars`.
- Adjacent inventory: `src2png` for code screenshots, `megatype` for responsive
  typography tooling, and Vitest Browser Mode discussion for testing review.
- These should not be used as direct skill sources unless later paired with
  current official docs or article-quality guidance.

## Rejected Themes

- Old Webpack-era experiments and plugins: `webpack-blocks` Webpack 2 branch,
  `webpack-common-shake`, `webpackmonitor`, `offline-plugin`, webpack i18n
  example note, and `chunk-splitting-plugin`.
- Release/changelog/discussion churn: Vite 4 discussion, Vite changelog, and
  Vite React plugin beta changelog.
- Old/narrow package ideas: `taskr`, `graphqlhub`, `tweezer.js`,
  `webfontloader`, and the old Create React App PR.

## Proposed Outcome

Decision: `candidate/defer/reject`

Use the three candidate sources only as source-review material. Do not edit
skills directly from this pass. Keep GitHub project links in project inventory
or future focused reviews.

## Things Actions

| Things ID | Decision | Final tag | Complete? | Reason |
| --- | --- | --- | --- | --- |
| `Li6tJhhj5mffxLnBvpRnpJ` | rejected | `Skill Archive Rejected` | yes | Old Gulp-alternative task runner; package-shopping source. |
| `5P3wwKyv7EoyFAzyABRdSf` | deferred | `Skill Archive Deferred` | yes | Active Zsh prompt project; interesting tooling inventory, not skill source. |
| `anBuCZZMBt9Bs8ZaMKrnz` | rejected | `Skill Archive Rejected` | yes | Stale GraphQLHub server project; not direct skill guidance. |
| `NvDUcqp5wmGRy37PqA5rsd` | candidate | `Skill Archive Candidate` | yes | Durable frontend terminal guide by Josh Comeau. |
| `Y5fyghAivhTkrLwTL9uqKd` | deferred | `Skill Archive Deferred` | yes | Webpack thread-loader project; defer to build-performance inventory. |
| `518qivGGDVNDYTw3Dy1671` | deferred | `Skill Archive Deferred` | yes | ThumbHash image-placeholder project; useful inventory, not direct article source. |
| `MGu8Uj4Y1MGqSUY5TKoST6` | deferred | `Skill Archive Deferred` | yes | Code screenshot tool project; presentation/tooling inventory only. |
| `FEjwCHWLobqXt9XRqarmBg` | deferred | `Skill Archive Deferred` | yes | CoffeeScript migration tool; project inventory only. |
| `3bfBNiRrmSodhc7RRHYh5B` | rejected | `Skill Archive Rejected` | yes | Old Create React App PR; project churn, not durable source. |
| `WgryvYrfuW6iAo4xmgUheP` | deferred | `Skill Archive Deferred` | yes | Active `trash` CLI/package; tooling inventory only. |
| `Ecgq2rhih5LAoqLvJ1pmZt` | deferred | `Skill Archive Deferred` | yes | Active Trix editor project; component/editor inventory only. |
| `J5UGLzCfsR27JPb8mugXQ3` | deferred | `Skill Archive Deferred` | yes | Active tsdown bundler project; JS tooling inventory. |
| `H4RJwSbtqvwJc6XDofoNeL` | rejected | `Skill Archive Rejected` | yes | Old small animation library; package-shopping source. |
| `E3bjrspNT7TktjFL1Wno4z` | deferred | `Skill Archive Deferred` | yes | TypeScript React Cheatsheets repo; useful resource inventory, not article source. |
| `AgTZ9C24HUv35RSDYxrEUZ` | deferred | `Skill Archive Deferred` | yes | Active PostCSS variables plugin; package inventory only. |
| `DpoQVUPkqudUCprdZcchAf` | deferred | `Skill Archive Deferred` | yes | UPNG.js image optimization project; image tooling inventory only. |
| `P4juwP4qTZws99yPEkNiLp` | deferred | `Skill Archive Deferred` | yes | React Window project; UI performance inventory, pair with docs/articles later. |
| `CF8SjxiRjR8sjcqQEydrfv` | rejected | `Skill Archive Rejected` | yes | Vite 4 GitHub discussion; release/planning churn. |
| `PtWJrKjoELjTYNGa7TS3PN` | rejected | `Skill Archive Rejected` | yes | Vite React plugin beta changelog; release churn. |
| `3BJSwxzQeLwQgBU23F9S52` | rejected | `Skill Archive Rejected` | yes | Vite changelog link; release churn rather than durable source. |
| `NfKNwNw7xuipZhKuucFDHs` | deferred | `Skill Archive Deferred` | yes | Vite legacy plugin package; tooling inventory only. |
| `LWxe95XNrip9XGfyJdRnhB` | deferred | `Skill Archive Deferred` | yes | Vitest Browser Mode discussion; defer to testing review with current docs. |
| `5mRUodfhNFhegZkdhUdn6B` | rejected | `Skill Archive Rejected` | yes | Old Web Font Loader project; stale direct source. |
| `JnGcdN4Jee3YQj9P55fDPD` | rejected | `Skill Archive Rejected` | yes | Old Webpack 2 branch of webpack-blocks; stale tooling source. |
| `4EFJ5sci7czWMbHJa4ZSJC` | rejected | `Skill Archive Rejected` | yes | Old CommonJS tree-shaking Webpack plugin. |
| `APyaHtcKdJA7cj7J35bDJp` | rejected | `Skill Archive Rejected` | yes | Duplicate old CommonJS tree-shaking Webpack plugin. |
| `9FhXQERK2onpZ9y9vGQAAz` | rejected | `Skill Archive Rejected` | yes | Old Webpack monitoring project; superseded by current bundle analyzers. |
| `Qttu2DHhGVWXNJSG82Qh93` | rejected | `Skill Archive Rejected` | yes | Old offline-plugin/AppCache-era Webpack project. |
| `VqHVszsG4Yqa6E5ZP1R7qK` | rejected | `Skill Archive Rejected` | yes | Narrow old Webpack i18n example note; not direct skill source. |
| `VghvVFQ5G5rHas5hnWkTE9` | rejected | `Skill Archive Rejected` | yes | Archived/narrow Webpack chunk-splitting plugin. |
| `ULWyCoeeMPauptUJiyoQYh` | candidate | `Skill Archive Candidate` | yes | Article-like TypeScript Book guidance on avoiding default exports. |
| `KGe4g1QciSLNCwL6LCH8eU` | candidate | `Skill Archive Candidate` | yes | Article on performant CSS with vanilla-extract. |
| `CLVc4SRPV2aM9jsCjMhNXB` | deferred | `Skill Archive Deferred` | yes | Active XState project; state-machine inventory, not direct article source. |
| `Xeu1vn38cns6qQECdJYGmN` | deferred | `Skill Archive Deferred` | yes | Responsive typography project; inventory only. |
| `YRuJ4sU2X3h5PWnanZNdog` | deferred | `Skill Archive Deferred` | yes | FontFaceObserver project; webfont-loading inventory only. |
