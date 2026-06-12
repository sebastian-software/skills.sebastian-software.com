# Cluster Brief: JS Tooling Queue 04

Reviewed: 2026-06-10

## Scope

This queue chunk is mostly GitHub repository/project inventory with one
article-like React/Next.js source. GitHub projects are not direct skill sources
under the current policy, so project links were inspected through the GitHub
Project Matrix and classified as deferred or rejected. The non-GitHub article
was opened separately and reviewed as potential source material.

## Access Notes

- GitHub repository links were inspected through matrix metadata: description,
  stars, archived status, language, latest release, last commit, and Things
  back-references.
- `https://github.com/events/universe/recap` is a GitHub Universe product/event
  recap page, not a repository; it is marketing/news rather than durable source
  material.
- `https://ondrejvelisek.github.io/how-nextjs-breaks-react-fundamentals/`
  returned HTTP 200. Search/source snippets identify it as a 2024 article about
  how Next.js App Router/RSC can complicate React's conceptual model and DX.

## Decision Summary

| Status | Count | Rationale |
| --- | ---: | --- |
| `candidate` | 1 | One explanatory article with durable React/RSC mental-model value. |
| `deferred` | 32 | Active or potentially interesting projects captured in the GitHub matrix. |
| `rejected` | 17 | Stale/deprecated packages, narrow package-shopping, event/news pages, private-home-automation or otherwise weak sources. |

## Source Groups

### Candidate

- `how-nextjs-breaks-react-fundamentals` -- opinionated but substantive article
  on React Server Components, Next.js App Router, component composition, and
  where framework constraints can degrade the simple React mental model. Useful
  as a secondary source for a future React/RSC skill or reference. Pair with
  official React/Next.js docs before writing skill guidance.

### Deferred Project Inventory

- Runtime/concurrency/tooling projects: `piscina`, `tinypool`, `nrr`, `knip`,
  `es-toolkit`, `ohash`, `mutative`, `ink`, `nitrogql`, `resvg-js`.
- Type/data utility projects: `Fraction.js`, `typebox`, `ts-reset`,
  `validator.js`, `spacetime`.
- Frontend/platform projects: `capo.js`, `soketi`, `imaskjs`, `swr`,
  `multithreading`, `HEAD`.
- Content/asset and design-adjacent projects: `headless-qr`, `spectral.js`,
  `blazediff`.
- Reference or inventory projects: `awesome-regex`, `lla`,
  `claude-deep-research-skill`.

These may remain interesting, but they should not shape skills without stronger
article, official-doc, or guide sources.

### Rejected Themes

- Obsolete or deprecated tooling: `gzip-loader`, `happypack`, old `apex/up`
  hosting note.
- Narrow package-shopping or weak project metadata: `fontpie`, `logo-soup`,
  `copy-text-to-clipboard` alternatives where current platform guidance is
  better, `react-use-size`, `tokencss`, `trim-lines`,
  `hono-and-remix-on-vite`.
- Private/personal/home automation or unrelated inventory: `auto-identity-remove`,
  `homebridge-zp`, `homebridge-tedee`, `maple-font`.
- Old behavioral/analytics packages: `gliojs`, `ganalytics`.
- GitHub Universe recap is news/marketing, not source material.

## Proposed Outcome

Decision: `existing skill update candidate` for the article only.

Potential future target:

- React/RSC mental-model reference: capture framework constraints, server vs
  client component boundaries, composition caveats, and why opinion pieces need
  corroboration from official React/Next.js docs.

No skill changes should be made directly from this cluster. Convert the
candidate article into a source card or combine it with other React/RSC sources
first.

## Things Actions

| Things ID | Decision | Final tag | Complete? | Reason |
| --- | --- | --- | --- | --- |
| `HaP7BxuuZhWeaJt75UcrrV` | deferred | `Skill Archive Deferred` | yes | Active Node worker-thread pool project; matrix inventory only. |
| `3sjbgcYSwfjrXngmFTdBuJ` | rejected | `Skill Archive Rejected` | yes | Narrow font/layout-shift CLI package with stale metadata; weak source. |
| `DGyNFRjNhXMgrptDHhAAAv` | deferred | `Skill Archive Deferred` | yes | Rational-number library project; inventory only. |
| `NuNzDxBG85wmTrq4LNXqCV` | deferred | `Skill Archive Deferred` | yes | QR-code library project; inventory only. |
| `U7MMqXKeGoyDGPrtj3qgkA` | deferred | `Skill Archive Deferred` | yes | Paint-like color-mixing library; defer until paired with color articles/docs. |
| `VV8NyJU5BufsyEZ8XfJVq` | deferred | `Skill Archive Deferred` | yes | Duplicate `spectral.js` project; captured in matrix. |
| `B47gLrXdttFUBHV9G42JwW` | deferred | `Skill Archive Deferred` | yes | HTML head ordering project; useful inventory, but use official docs/articles before skill work. |
| `ByMTuUDzPpqeHnpTLPp1H2` | deferred | `Skill Archive Deferred` | yes | npm script runner project; matrix inventory only. |
| `2n6yq1bzQKiYS8bY4jXKwg` | rejected | `Skill Archive Rejected` | yes | Narrow logo-normalization UI package; package-shopping source. |
| `KBseZquNvCecfw7SgExRBS` | deferred | `Skill Archive Deferred` | yes | Runtime type-system project; inventory only. |
| `9sY69wvs6QSscNchqRg3KV` | deferred | `Skill Archive Deferred` | yes | Clipboard package project; defer to current platform/API docs before skill use. |
| `Q4QeZXFBvr331TPYa6HoFL` | rejected | `Skill Archive Rejected` | yes | Narrow random-string package note; prefer current Web Crypto/Nano ID guidance. |
| `WjtyUwJxd8EDhYezk7qLqd` | deferred | `Skill Archive Deferred` | yes | Regex resource list; potentially useful inventory, not direct skill source. |
| `6vjJrnqZ9J7bHmVEmcBy1T` | deferred | `Skill Archive Deferred` | yes | WebSocket server project; matrix inventory only. |
| `4saSijcH4VRXZ74Z3Xfg9j` | deferred | `Skill Archive Deferred` | yes | Timezone library project; inventory only. |
| `XJ7Uq4UsCWAHuQceeZAs7r` | rejected | `Skill Archive Rejected` | yes | Personal-info removal automation is outside the current software skill archive scope. |
| `RSEGhfWqsTmJySuZLxxtr3` | rejected | `Skill Archive Rejected` | yes | Font project misclassified as JS tooling; not skill-source material. |
| `8MxmFnTv8ZjBehxdjecLJd` | deferred | `Skill Archive Deferred` | yes | Pixel-diff project; testing inventory only. |
| `XBhsc4MFwaP6NHDe21gfXV` | rejected | `Skill Archive Rejected` | yes | Low-signal React measurement hook package; package-shopping source. |
| `REhXCM7qBgaRMpeKKKDrXR` | deferred | `Skill Archive Deferred` | yes | Active worker-thread pool project; inventory only. |
| `A7ybxCigs9wdrwRh4j6rvh` | rejected | `Skill Archive Rejected` | yes | Old token CSS project with weak metadata; not direct source material. |
| `8BKrXeJVWihFjqEWkQodoD` | deferred | `Skill Archive Deferred` | yes | Active utility-library project; inventory only. |
| `7xiBxcBNjCQMNP5EA8Vmyf` | deferred | `Skill Archive Deferred` | yes | TypeScript reset project; duplicate source group with next item. |
| `BK26HniZ5dHzdzE99dncf3` | deferred | `Skill Archive Deferred` | yes | Duplicate `ts-reset` project; captured in matrix. |
| `4Pp1kkjaH4Jkyis6ob5vRm` | deferred | `Skill Archive Deferred` | yes | CLI `ls` replacement project; inventory only. |
| `Ub9qse55S8y7YTNiUB7wbQ` | deferred | `Skill Archive Deferred` | yes | GraphQL/TypeScript toolchain project; inventory only. |
| `AXtfeAvcQogtr9u5iK3tbN` | deferred | `Skill Archive Deferred` | yes | Immutable update project; inventory only. |
| `7ML5wnwsHLSKKErmD4YieF` | deferred | `Skill Archive Deferred` | yes | Hashing/comparison utility project; inventory only. |
| `WUNCcXV9iCkUrvRh2tZpFr` | deferred | `Skill Archive Deferred` | yes | Input-mask project; defer to form UX/accessibility sources before skill use. |
| `NbnAFvNpSqiHX4epCRb5gZ` | deferred | `Skill Archive Deferred` | yes | React CLI app framework; inventory only. |
| `RwDdRCUPoAMd42ftMmgdV6` | deferred | `Skill Archive Deferred` | yes | String-validation project; inventory only. |
| `8zXruQmSaNp2zWHDXkBNcT` | deferred | `Skill Archive Deferred` | yes | SWR project/release note; use docs/articles for data-fetching skill material. |
| `9VwVxex7XVjXbQmk2Pb366` | deferred | `Skill Archive Deferred` | yes | Duplicate SWR project; captured in matrix. |
| `qiXRtudcpGP7ei4ETjPLP` | deferred | `Skill Archive Deferred` | yes | JavaScript multithreading project; inventory only. |
| `DhxpaAsb2zf3gUwXZWyWuS` | deferred | `Skill Archive Deferred` | yes | Knip project; duplicate source group with next item. |
| `Y22asofUN6rwbL3LhF65h2` | deferred | `Skill Archive Deferred` | yes | Duplicate Knip project; captured in matrix. |
| `6nozMzd9Bm5yH9tNpZvGsq` | rejected | `Skill Archive Rejected` | yes | Tiny whitespace utility with low/stale metadata; package-shopping source. |
| `TxhFv3bY6auSRX3DEXyDFz` | deferred | `Skill Archive Deferred` | yes | SVG renderer/toolkit project; inventory only. |
| `MECMpCnWcbjSxat5S9W19q` | rejected | `Skill Archive Rejected` | yes | Small example repo with weak metadata; not durable source material. |
| `Xo3aXpsfL4TzvutfddHCxz` | rejected | `Skill Archive Rejected` | yes | GitHub Universe recap is product/news marketing, not durable skill source. |
| `BiBCEnQhDKATtKNW2BRbDh` | rejected | `Skill Archive Rejected` | yes | Old exit-intent popup package; stale behavioral package-shopping source. |
| `VZ5QhiCrZ91oUj4yMGQNZn` | rejected | `Skill Archive Rejected` | yes | Old Google Analytics helper package; stale implementation note. |
| `SCJrkZgriEU5X9FjoHdwy9` | rejected | `Skill Archive Rejected` | yes | Archived/deprecated Webpack gzip loader. |
| `9zndEVFZpT77ePrBmpsphK` | rejected | `Skill Archive Rejected` | yes | Archived Webpack parallel-build tool; obsolete build-performance note. |
| `PPNTmWRb52dTCw7xti84TS` | deferred | `Skill Archive Deferred` | yes | HTML head guide repo; useful inventory, but pair with current MDN/web.dev before skill work. |
| `629pyC7g3UkWfHwX5fXTsW` | rejected | `Skill Archive Rejected` | yes | Homebridge/Sonos plugin is private home-automation inventory, not skill-source material. |
| `2QiM9wS529QB1amPTDPJcG` | rejected | `Skill Archive Rejected` | yes | Homebridge/Tedee smart-lock plugin is private home-automation inventory; repo is archived. |
| `Dv9pXHkoghEhB7kMWEXAS4` | rejected | `Skill Archive Rejected` | yes | Old hosting tool note with stale project metadata; not durable skill source. |
| `AFU1R3G9xzTNbnepRCd6Y3` | candidate | `Skill Archive Candidate` | yes | Explanatory React/Next.js article; useful secondary source for React/RSC mental-model guidance. |
| `2FTCdV4dLkndn7UhC9hWnu` | deferred | `Skill Archive Deferred` | yes | Claude deep-research skill repo; project inventory, not direct source material in this pass. |
