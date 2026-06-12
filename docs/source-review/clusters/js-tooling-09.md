# Cluster Brief: JS Tooling Queue 09

Reviewed: 2026-06-10

## Scope

This queue chunk mixes old Webpack/PostCSS/polyfill package notes, a few active
tool projects, product/package pages, and two article/doc sources. GitHub
projects were inspected through the GitHub Project Matrix. Direct skill
candidates are limited to article/official documentation sources with durable
workflow value.

## Access Notes

- GitHub project links were checked through matrix metadata: canonical repo,
  description, stars, archived status, language, latest release, and last
  commit.
- Node.js Security Best Practices is official Node.js documentation and remains
  a strong candidate for a security/backend reference.
- The Priority Plus Navigation Things item includes both the old `okayNav`
  project and a CSS-Tricks article. The article is a valid UI/navigation pattern
  source; the legacy repo is not.
- Several PostCSS and Webpack links are old package-shopping notes tied to
  previous EdgeStack/boilerplate implementation ideas.

## Decision Summary

| Status | Count | Rationale |
| --- | ---: | --- |
| `candidate` | 2 | Official Node security docs and CSS-Tricks priority-navigation article. |
| `deferred` | 15 | Active or potentially useful project inventory captured in the GitHub matrix. |
| `rejected` | 33 | Stale Webpack/PostCSS/polyfill package notes, old boilerplate ideas, archived tools, weak package-shopping, or product/package pages. |

## Candidate Sources

- `node-security-best-practices` -- official Node.js guide for secure
  application patterns. Strong future source for backend/security hardening.
- `priority-navigation-pattern` -- CSS-Tricks article source for responsive
  priority-plus navigation. Use the article as source material; ignore the old
  `okayNav` project as implementation guidance.

## Deferred Project Inventory

- Current or broadly useful tooling projects: `node-fetch`/`unfetch`, `odiff`,
  `compression-webpack-plugin`, `overcommit`, `oxipng`, `puppeteer`, `pino`,
  `pnpm`, `postcss-load-config`, `postcss-font-magician`, `postcss-url`,
  `PostHog`, `rollup/plugins`, `SuperTinyIcons`.
- These are inventory only until paired with stronger article/docs sources.

## Rejected Themes

- Old/stale build tooling: `directory-named-webpack-plugin`, Angular CLI issue,
  Next v3 source paths, Webpack config utilities, `nwb`, `offline-plugin`,
  `parallel-webpack`, Webpack developer kit, legacy PWA/manifest/polyfill notes.
- Old PostCSS package-shopping: conditionals/loops/simple vars/functions/SVG
  packages, family/place/utilities/devtools, and similar one-off migration
  notes.
- Narrow UI/product packages: Motion Primitives product page, SnackbarLight,
  typefaces, Push.js, okayNav implementation, and other package-only sources.

## Proposed Outcome

Decision: `existing skill update candidates`

Potential future targets:

- Security/backend hardening reference from Node.js security docs.
- Responsive navigation pattern reference from CSS-Tricks priority navigation.

No skill changes should be made directly from this cluster.

## Things Actions

| Things ID | Decision | Final tag | Complete? | Reason |
| --- | --- | --- | --- | --- |
| `RAbsE6XESoZ4QG3HF99xSg` | rejected | `Skill Archive Rejected` | yes | Motion Primitives is a product/package page, not durable JS-tooling source material. |
| `Df6GV9cYkJpS7L4Pfe1cz5` | rejected | `Skill Archive Rejected` | yes | Narrow Webpack plugin package note; old package-shopping source. |
| `Ead6EFkuQC1sHQdQMq3NdP` | rejected | `Skill Archive Rejected` | yes | Old Angular CLI issue comment about vendor chunk size; project churn. |
| `Tr9MJgguG7T8iHCnTTPDdP` | rejected | `Skill Archive Rejected` | yes | Narrow PostCSS retina image package; package-shopping source. |
| `89ELuEC1iiXMLpemYmZS13` | rejected | `Skill Archive Rejected` | yes | Next/PWA boilerplate package idea; not durable source material. |
| `86TnkpzQcPiS4hm5q66wWD` | rejected | `Skill Archive Rejected` | yes | Old Next v3 package.json source path; stale project-internals note. |
| `KQSYaa1oXdriBkcjZCcpeP` | deferred | `Skill Archive Deferred` | yes | Fetch/polyfill projects; inventory only, use current platform docs before skill work. |
| `UyoZnTTA37RG1bGm4W26pv` | rejected | `Skill Archive Rejected` | yes | Tiny stale Server-Timing package; use current docs/articles instead. |
| `4t5jMvm6ttKsjk3SWN2AYv` | candidate | `Skill Archive Candidate` | yes | Official Node.js security best-practices documentation. |
| `3oX8v8JfZdkyr5nPSXMWZx` | rejected | `Skill Archive Rejected` | yes | Archived browser notification package; stale package-shopping source. |
| `DDgMV5UWyNPCBo1odDAd7m` | rejected | `Skill Archive Rejected` | yes | Old Webpack config utility package; stale build-tooling note. |
| `CU5PtczXq2ywiDe6vi44XF` | rejected | `Skill Archive Rejected` | yes | Low-signal snackbar package from 2016; package-shopping source. |
| `VvgTaTk3988vdGV7rhCG4T` | rejected | `Skill Archive Rejected` | yes | NPM typeface package collection; package inventory, not source material. |
| `MtYPmVH8DKTXokpaaLzbnS` | rejected | `Skill Archive Rejected` | yes | Archived `nwb` release note from Webpack v2 era. |
| `2Re1tmQrn58y4ZfgfNnvLL` | deferred | `Skill Archive Deferred` | yes | Active image-diff project; inventory only. |
| `7Tq3eQ9ATWMRGauP2ALyjh` | rejected | `Skill Archive Rejected` | yes | Old Webpack offline plugin; stale PWA build-tooling source. |
| `52W3xdyHh4N7NGyJbTD6oM` | deferred | `Skill Archive Deferred` | yes | Compression plugin and parallel uglify package bundle; inventory only. |
| `Jn1tg21wWsdshAjh46eLJq` | deferred | `Skill Archive Deferred` | yes | Git hook manager project; inventory only. |
| `QmzzksptHPZf3DVy1ndbh8` | deferred | `Skill Archive Deferred` | yes | PNG optimizer project; inventory only. |
| `2LwoKZqp4QTEfJoE8r5N62` | rejected | `Skill Archive Rejected` | yes | Archived parallel Webpack package; stale build-tooling source. |
| `H9WWkPnrpFG1GRrSZupNas` | deferred | `Skill Archive Deferred` | yes | Puppeteer project; inventory only. |
| `2Z7bR5sPD5tSDsZxe526PL` | deferred | `Skill Archive Deferred` | yes | Pino logging project; inventory only. |
| `RoySnhS6mbUdqqVSJNH3sn` | deferred | `Skill Archive Deferred` | yes | Pino plus formatter package bundle; inventory only. |
| `VPQHFdN8rF6NxN9oG1reFW` | rejected | `Skill Archive Rejected` | yes | Old Webpack developer-kit package; stale project-specific tooling. |
| `7ZT3YTd82jaaD76F1GXxnY` | deferred | `Skill Archive Deferred` | yes | pnpm release/project inventory; use current docs for skill material. |
| `AbVYfLnaBVxpktfeowTDMQ` | rejected | `Skill Archive Rejected` | yes | Old server-side polyfill bundle idea; stale package-shopping source. |
| `7TpsiH6e4JaDHccsZMaky1` | rejected | `Skill Archive Rejected` | yes | Old web app manifest polyfill from 2016; obsolete source. |
| `D68wcN6hcZYZJWs1nGSaZ1` | rejected | `Skill Archive Rejected` | yes | Polyfill.io alternative package note; not durable skill source. |
| `HVAfhKjCuygDYx2jkKyAr8` | rejected | `Skill Archive Rejected` | yes | Family.scss source path and porting idea; package-churn note. |
| `6BLLTfAdYgEHbk8Q7ujbDW` | rejected | `Skill Archive Rejected` | yes | Old JPEG quality tooling implementation note; package/project-specific. |
| `PxC4JAZZ6ujwvBM1XRgpcz` | rejected | `Skill Archive Rejected` | yes | Old PostCSS conditionals/loop package bundle; stale package-shopping. |
| `H3dmuU9Z6sbBT5NQknsHXW` | rejected | `Skill Archive Rejected` | yes | Old PostCSS devtools package from 2017; stale source. |
| `QbPx9iaFEN4F8qJ1qBbngz` | deferred | `Skill Archive Deferred` | yes | PostCSS config loader project; inventory only. |
| `JpySWBwfRiwRaWQSdoWEC6` | rejected | `Skill Archive Rejected` | yes | Duplicate PostCSS conditionals/loops/simple-vars package-shopping bundle. |
| `KkSYDfEJsmgg7efL235tGq` | rejected | `Skill Archive Rejected` | yes | Low-signal PostCSS family plugin; package-shopping source. |
| `J5Syk4N7o4PdCg2t7Vuzaa` | deferred | `Skill Archive Deferred` | yes | PostCSS font-face generator project; inventory only. |
| `9uuwherhsepdEzbQENAqno` | rejected | `Skill Archive Rejected` | yes | PostCSS functions migration/package note; not durable source material. |
| `DcGDY4aubHmib5Lsa8k2zc` | rejected | `Skill Archive Rejected` | yes | PostCSS inline SVG package; duplicate package-shopping source. |
| `L9TooaLgKLYrFJ7LWi8YVK` | rejected | `Skill Archive Rejected` | yes | Duplicate PostCSS inline SVG package note. |
| `WS88XrjLoJ2RzyRRukaxjW` | rejected | `Skill Archive Rejected` | yes | PostCSS simple variables package; package-shopping source. |
| `L5Qs6uUWUe2EE9wr7nx5yw` | rejected | `Skill Archive Rejected` | yes | PostCSS SVG package; stale package-shopping source. |
| `XzBzHfvJq3NZtF12GwYH3C` | rejected | `Skill Archive Rejected` | yes | Missing/inaccessible PostCSS SVG fragments repo; not usable. |
| `2b5cLsGaARbpvCzGmbPoB9` | rejected | `Skill Archive Rejected` | yes | Duplicate PostCSS inline SVG package note. |
| `KS2jwYvC3Gp6v1XJYH7AV3` | deferred | `Skill Archive Deferred` | yes | PostCSS URL project; inventory only. |
| `J8ssiARjpE2gBpSHQNTmw9` | rejected | `Skill Archive Rejected` | yes | Old PostCSS utilities package; package-shopping source. |
| `9NYbxwfvcSCyDR2vTu6iX8` | rejected | `Skill Archive Rejected` | yes | Archived PostCSS place shorthand plugin; stale source. |
| `TPeGqq7SumpBruqBYQqGj7` | deferred | `Skill Archive Deferred` | yes | PostHog `.cursorrules` source; inventory only, requires separate agent-rules review. |
| `SfnciSfXPnyCgkKbN6432u` | deferred | `Skill Archive Deferred` | yes | Rollup YAML plugin project; inventory only. |
| `9T5Yxa1wmSDZjbWp2VKgGX` | candidate | `Skill Archive Candidate` | yes | CSS-Tricks priority-navigation pattern article; ignore old okayNav implementation. |
| `HpXgAnDecqtSpdYTvKhS7u` | deferred | `Skill Archive Deferred` | yes | SVG product-icon project; visual asset inventory only. |
