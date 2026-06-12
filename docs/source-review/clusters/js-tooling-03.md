# Cluster Brief: JS Tooling Queue 03

Reviewed: 2026-06-10

## Scope

This queue chunk contains 50 GitHub repository/project links. Under the current
archive policy, GitHub projects are not direct skill sources. They are tracked
in the GitHub Project Matrix and only become skill material later if paired with
stronger article, official-doc, specification, or implementation-guide sources.

All links were inspected through the GitHub Project Matrix metadata generated
from GitHub's API: description, stars, archive status, language, latest release,
last commit, and Things back-references.

## Decision Summary

| Status | Count | Rationale |
| --- | ---: | --- |
| `candidate` | 0 | No direct skill sources in this chunk. |
| `deferred` | 41 | Active or potentially interesting technical projects now captured in the GitHub matrix. |
| `rejected` | 9 | Misclassified, very narrow decorative/package-shopping links, stale/weak entries, or non-skill inventory. |

## Deferred Project Groups

- Accessibility/UI primitives: `focus-trap`, `dark-mode-toggle`,
  `glide-data-grid`, `frimousse`, `Hyphenopoly`, `wouter`.
- Tooling/runtime/framework projects: `turbowatch`, `hono`, `html-minifier-next`,
  `graphql-request`/`graffle`, `linkinator`, `middy`, `vinxi`, `partykit`.
- Content extraction/conversion/search projects: `zerox`, `SingleFile`,
  `quarkdown`, `image-js`, `defuddle`, `uFuzzy`, `minisearch`,
  `fuzzy-search`, `feedsmith`, `turndown`, `readability`, `tesseract.js`,
  `jsPDF`.
- Reference/framework inventory: `typescript-book`, `hotscript`,
  `js-framework-benchmark`, `next-saas-starter`, `luxon`, `react-tracking`,
  `superpowers`.
- AI/agent or macOS-adjacent tools: `llama-fs`, `mud` is rejected separately,
  while `superpowers` remains deferred because it is agent-workflow related.

These are useful as project inventory, but should not drive skill edits by
themselves.

## Rejected Themes

- Narrow visual/decorative package picks without broader explanatory guidance:
  `corner-smoothing`, `hamburger-react`, `atropos`.
- Misclassified or weak non-JS tooling inventory: `instrument-serif`,
  `awesome-mac`, `mud`.
- Deprecated/outdated package clue: `clipboard-polyfill` explicitly says most
  projects probably do not need it anymore.
- Low-signal package-shopping entries with weak metadata: `dev-error-boundary`,
  `ultramatter`.

## Proposed Outcome

Decision: `defer/reject only`

No skill changes and no source cards should be created from this queue chunk
alone. If one of these tools becomes relevant later, use the GitHub matrix row
as inventory and find stronger current sources before editing a skill.

## Things Actions

| Things ID | Decision | Final tag | Complete? | Reason |
| --- | --- | --- | --- | --- |
| `FG787SY88vGbgFnky1skUP` | deferred | `Skill Archive Deferred` | yes | Active focus-management project; captured in GitHub matrix, not direct skill source. |
| `WHVLNo8cyeLTMKwr5Lr1XU` | deferred | `Skill Archive Deferred` | yes | Active Node file-watch/task project; matrix inventory only. |
| `XAAyxY9nynJ2hErmnQwvWw` | deferred | `Skill Archive Deferred` | yes | OCR/document-extraction project; interesting inventory, needs stronger docs/articles before skill use. |
| `4dG1kWTv8RDVx3ahWEkkhN` | deferred | `Skill Archive Deferred` | yes | TypeScript book repo; potentially useful but still GitHub-hosted source requiring a separate content review. |
| `T3YHDJLD34D9LaQepctVBV` | deferred | `Skill Archive Deferred` | yes | Single-file web capture project; project inventory, not skill source. |
| `LQVs8oChZb7kLXswg9kocR` | deferred | `Skill Archive Deferred` | yes | Active React data-grid project; package inventory rather than article/guide source. |
| `RsKrYrhmKqSuZdD1n4QbNt` | deferred | `Skill Archive Deferred` | yes | Dark-mode custom-element project; use broader dark-mode docs/guides for skill work. |
| `UN1gGTh84uAbFBynRnMKcL` | rejected | `Skill Archive Rejected` | yes | Narrow corner-smoothing Tailwind package; decorative package-shopping source. |
| `RLR4VkRf4CHoiZhLgh2sZ5` | deferred | `Skill Archive Deferred` | yes | Advanced TypeScript type-level library; interesting inventory, not direct skill source. |
| `6oEzY2k4QfA87VnZKaehHx` | deferred | `Skill Archive Deferred` | yes | Active web-standard framework project; matrix inventory only. |
| `55MhReB6HdezzVY2fjA2ff` | deferred | `Skill Archive Deferred` | yes | Markdown/publishing tool project; interesting inventory, not skill source. |
| `E97xvbhSXp8u7iVdoiEXDj` | deferred | `Skill Archive Deferred` | yes | JavaScript image-processing project; matrix inventory only. |
| `8Q6q3W9z15TsLjq4uRuDKL` | rejected | `Skill Archive Rejected` | yes | Font repository misclassified as JS tooling and not skill source material. |
| `WdeKkh9BXtu4UtVoZsDhCE` | deferred | `Skill Archive Deferred` | yes | AI file-organization project; project inventory, not direct skill material. |
| `B3mNPgNNw4b9m31Vjq9isA` | deferred | `Skill Archive Deferred` | yes | Active HTML minifier project; package inventory only. |
| `FjUzSVXkrhLoSxZsLtZnnZ` | deferred | `Skill Archive Deferred` | yes | GraphQL client project now canonicalized to `graffle`; inventory only. |
| `F6sCC8DBUoTFbCA8AFF6oX` | rejected | `Skill Archive Rejected` | yes | Broad macOS software list, not relevant to skill-source review. |
| `7hsRWkuk1oXhkyM9DxRSgn` | deferred | `Skill Archive Deferred` | yes | Browser-tab synchronization project; project inventory only. |
| `G9vwH8bQ4jRMBrEwUzFR5T` | deferred | `Skill Archive Deferred` | yes | Jest matcher project; testing-package inventory, not source guidance. |
| `G4fhva9TuFMdyjJZQCKTo8` | rejected | `Skill Archive Rejected` | yes | macOS markdown viewer, not JS-tooling skill material. |
| `S1nDWHGYfsoZkE7LsNqMaA` | deferred | `Skill Archive Deferred` | yes | Broken-link checker project; matrix inventory only. |
| `62hwJS5AJk1a4ZQsfRbeMe` | deferred | `Skill Archive Deferred` | yes | React schedule/grid project; package inventory only. |
| `G75GrrthG4jkyaNqn9Xo62` | deferred | `Skill Archive Deferred` | yes | Web-page content extraction project; project inventory only. |
| `SzjmjHjuwBz2Ba6cW1bWgm` | deferred | `Skill Archive Deferred` | yes | Framework benchmark project; useful inventory, not skill source by itself. |
| `138ML66gWLH6X7piw7ioKk` | deferred | `Skill Archive Deferred` | yes | Fuzzy-search project; duplicate source group with the next item. |
| `RT38jhwK1kU9LknFKp7dhm` | deferred | `Skill Archive Deferred` | yes | Duplicate `uFuzzy` project; captured in matrix. |
| `FNrJcsc6yZy9zWcx6tm6pr` | deferred | `Skill Archive Deferred` | yes | Next SaaS starter kit; project inventory, not source guidance. |
| `EDVua3kT91ULTgBoFXuVzE` | rejected | `Skill Archive Rejected` | yes | Clipboard polyfill says most projects probably do not need it anymore; outdated package clue. |
| `TENzZTtHr3gqKm2hqzy3uP` | deferred | `Skill Archive Deferred` | yes | Emoji-picker package; inventory only. |
| `n1qT7KH7MECHu7HyuDFw5` | deferred | `Skill Archive Deferred` | yes | Client/full-text search project; inventory only. |
| `JVAeBeztZPEhKHm6cNGrzp` | rejected | `Skill Archive Rejected` | yes | Narrow hamburger-icon package; no durable skill-source value. |
| `527FgufibtBWPUy19quhb9` | deferred | `Skill Archive Deferred` | yes | Fuzzy-search package; inventory only. |
| `Xo4GBZzJxDo4nnCcPjCqfB` | deferred | `Skill Archive Deferred` | yes | Feed parser/generator project; inventory only. |
| `Hc1XcQHEyKmu733oQrEXam` | rejected | `Skill Archive Rejected` | yes | Low-signal Remix error-boundary package; weak package-shopping source. |
| `5rDvjjtwcJsKSjmuMAzCrz` | deferred | `Skill Archive Deferred` | yes | Page-transition package; inventory only, use articles/docs for view-transition skills. |
| `9wG7XNtJATar7FWHp9a1v` | deferred | `Skill Archive Deferred` | yes | AWS Lambda middleware project; inventory only. |
| `2MhM9VAq4b3KpMasLRQCCU` | deferred | `Skill Archive Deferred` | yes | HTML-to-Markdown converter project; inventory only. |
| `W7HyKbwnkyvJRjXsfubCHv` | deferred | `Skill Archive Deferred` | yes | Hyphenation project; inventory only. |
| `Y62Bv8QcBtDGpWtctorJAG` | deferred | `Skill Archive Deferred` | yes | React/Preact router project; inventory only. |
| `TbRBFY6FPWh4AzGzgMvveL` | deferred | `Skill Archive Deferred` | yes | Date/time library project; inventory only. |
| `5VvkkmN5FtPZFa7mvnLc74` | deferred | `Skill Archive Deferred` | yes | Readability extraction project; inventory only. |
| `SS1tQvL7ho18NCYSqwLq1R` | deferred | `Skill Archive Deferred` | yes | OCR project; inventory only. |
| `SrUpbwiw6X9xJoPtNytX42` | rejected | `Skill Archive Rejected` | yes | Tiny frontmatter parser with weak/stale metadata; package-shopping source. |
| `T92bM4bEawq9rUyZnbDNks` | deferred | `Skill Archive Deferred` | yes | Full-stack JavaScript SDK project; inventory only. |
| `Y4NV4PuaZtHpPYunm4pE7L` | deferred | `Skill Archive Deferred` | yes | CSS view-transition pattern project; defer until paired with article/docs. |
| `M6XjMwQ9wUw3dgJGqkEL8a` | rejected | `Skill Archive Rejected` | yes | Decorative 3D parallax package; not skill-source material. |
| `Jo47xBB1JcU9YAbBHM5GJ2` | deferred | `Skill Archive Deferred` | yes | React tracking project; inventory only. |
| `Q9RATFZpAhhYaF3zEc49Vs` | deferred | `Skill Archive Deferred` | yes | Client-side PDF project; inventory only. |
| `VdfQShFeq1pZTPTPj5XAh5` | deferred | `Skill Archive Deferred` | yes | Multiplayer app platform project; inventory only. |
| `FjV4hmBGunUbcU7dQMwBwi` | deferred | `Skill Archive Deferred` | yes | Agentic skills framework project; interesting inventory, not direct skill-source material in this pass. |
