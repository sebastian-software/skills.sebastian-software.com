# Cluster Brief: JS Tooling Queue 08

Reviewed: 2026-06-10

## Scope

This queue chunk mixes modern GitHub project inventory, old JavaScript package
notes, and one article source. GitHub projects were inspected through the
GitHub Project Matrix and are treated as deferred inventory or rejected package
churn. The Simon Willison article was reviewed as an article source.

## Access Notes

- GitHub repository links were checked through matrix metadata: canonical repo,
  description, stars, archived status, language, latest release, and last
  commit.
- `simonwillison.net/2025/Dec/15/porting-justhtml/` was reachable through web
  search. It is an article by Simon Willison, published 2025-12-15, about
  porting JustHTML from Python to JavaScript with Codex CLI and GPT-5.2, using
  html5lib-tests as a conformance suite.
- `mona-sans` and `Moonfin-Client` did not map to repository rows in the GitHub
  project matrix; both are treated as non-source inventory in this pass.

## Decision Summary

| Status | Count | Rationale |
| --- | ---: | --- |
| `candidate` | 1 | One article source with durable AI-assisted engineering/process value. |
| `deferred` | 28 | Active or potentially useful projects captured in the GitHub matrix. |
| `rejected` | 21 | Old package-shopping notes, stale build-tooling, private/macOS/media utilities, weak no-match org links, or narrow project-specific code links. |

## Candidate Source

- `simon-willison-justhtml-port` -- useful secondary source for an AI-assisted
  programming / coding-agent workflow reference. Durable ideas: set up a
  comprehensive conformance suite, let the agent work against tests, inspect
  the generated commits, and judge the result by proven behavior rather than
  vibes. This should be paired with other testing/conformance sources before
  changing a skill.

## Deferred Project Groups

- AI/document/scraping/content tools: `umami`, `insanely-fast-whisper`,
  `AI-Video-Transcriber`, `LEANN`, `yt-dlp`, `memsearch`, `marker`, `mem0`.
- Developer tooling: `fontaine`, `md4x`, `vite-task`, `tome`, `Lightning CSS`,
  `llm-gemini`, `debug`, `pino`/`bole`/`bunyan`, `luxon`, `markdown-rs`.
- External skill/agent repos: `wondelai/skills`, `wshobson/agents`,
  `oh-my-codex`.
- Platform/reference repos: W3C `IntersectionObserver` plus lazy-load example.

These are useful inventory, not direct skill sources.

## Rejected Themes

- Stale build and package-churn notes: `webpack-serve`, `backpack`, Webpack
  image loaders, PostCSS inline SVG, old CRA Jest config, `kyt`, old PWA
  tutorial, `mermaid-loader`.
- Old analytics/marketing package notes: duplicate `ganalytics`, exit-intent
  `gliojs`.
- Narrow or weak package picks: `polychrome`, `leva`, `postcss-font-magician`,
  `tipograf`, `modular-css`.
- Personal/macOS/media/non-skill inventory: `Locker`, Mona Sans org pages,
  `MonitorControl`, `Moonfin-Client`.

## Proposed Outcome

Decision: `existing skill update candidate` for the Simon Willison article only.

Potential target:

- AI-assisted coding workflow reference: conformance tests, long-running agent
  work, inspecting commits, and treating generated code as acceptable only when
  behavior is verified.

No skill changes should be made directly from this cluster.

## Things Actions

| Things ID | Decision | Final tag | Complete? | Reason |
| --- | --- | --- | --- | --- |
| `2RfSKroDnHmzYFsKHfrU6W` | deferred | `Skill Archive Deferred` | yes | Analytics platform project; matrix inventory only. |
| `NnYsEtJZJ32Kn1pAoDbu8M` | rejected | `Skill Archive Rejected` | yes | Old webpack dev-server source link from 2017; stale build-tooling source. |
| `DAaRsTuwiUSY8RRe3tnXa2` | deferred | `Skill Archive Deferred` | yes | Font fallback project; inventory only until paired with typography/performance docs. |
| `514qj3Sc9gzqkSZngd8HBe` | deferred | `Skill Archive Deferred` | yes | Markdown parser project; inventory only. |
| `4D4jkQ5K7rBW7cmkcvpLw3` | deferred | `Skill Archive Deferred` | yes | Speech transcription project; inventory only. |
| `8jzDvpsMwH1n2LLc3dVbox` | deferred | `Skill Archive Deferred` | yes | React Google Maps package; inventory only. |
| `Lhw6kDzGaA2qs53RoRaAbu` | deferred | `Skill Archive Deferred` | yes | Vite task runner project; inventory only. |
| `GiQhoUVyYqEDGWbfF8RvUH` | deferred | `Skill Archive Deferred` | yes | Documentation platform project; inventory only. |
| `MFHBdnroyx5GxFXfQoDrR2` | deferred | `Skill Archive Deferred` | yes | AI video transcription project; inventory only. |
| `oYj1AsFqrDb2afqk1zNxR` | deferred | `Skill Archive Deferred` | yes | External agent skills repo; inventory only. |
| `4Ncgja45Kn8FF8r73onGm5` | deferred | `Skill Archive Deferred` | yes | Agent marketplace repo; inventory only. |
| `S9gZW2dVxsAmaUAnmTVXWg` | deferred | `Skill Archive Deferred` | yes | Codex hooks/agent tooling project; inventory only. |
| `3R2UwqmbGuNdv3gSYhwdm3` | deferred | `Skill Archive Deferred` | yes | RAG/search project; inventory only. |
| `48BcA11KgKozvTbcdcTrP3` | deferred | `Skill Archive Deferred` | yes | Media download CLI project; inventory only. |
| `SsnhyEHBcvz8r7AF8fs3N3` | deferred | `Skill Archive Deferred` | yes | Model decoding research/project inventory. |
| `NUm7kJMVR1D2ubekzHb3kb` | deferred | `Skill Archive Deferred` | yes | AI memory/search project; inventory only. |
| `Erd8KfhyU355Wx9Rq8AcVo` | rejected | `Skill Archive Rejected` | yes | Low-signal project with no useful description; not source material. |
| `E3ynJnh998FzTD5APB21Mm` | deferred | `Skill Archive Deferred` | yes | Human-date parser project; inventory only. |
| `GjYkePJkcT2MnEyM5GdjN7` | deferred | `Skill Archive Deferred` | yes | Spellchecking library project; inventory only. |
| `sAwEiZrGos5tzJgodxYqH` | deferred | `Skill Archive Deferred` | yes | Hyphenation library project; inventory only. |
| `PGZDquw6VMTgtZmoUv7ChL` | candidate | `Skill Archive Candidate` | yes | Article source on AI-assisted porting with conformance tests and Codex workflow. |
| `MQBD235r6rGF7hrRXRGyy5` | rejected | `Skill Archive Rejected` | yes | Old Backpack build-system inspiration; stale project-specific note. |
| `JFepF8XE1ayveZb3ZrUTnt` | rejected | `Skill Archive Rejected` | yes | Old Webpack image placeholder loaders; stale package-shopping source. |
| `RdFWkauz6D7h4mETeDdj3H` | rejected | `Skill Archive Rejected` | yes | Narrow PostCSS inline-SVG package note; not durable source material. |
| `9DJa3xQK1tELPaJ8ZVNjVp` | deferred | `Skill Archive Deferred` | yes | Intersection Observer spec/repo plus lazy-load example; inventory until paired with current docs. |
| `FkKXwgYNX9RBdYAKSAd26` | rejected | `Skill Archive Rejected` | yes | Old color-manipulation package; package-shopping source. |
| `C93W39nmKp4fdcd4BnZg2u` | rejected | `Skill Archive Rejected` | yes | Old forked CRA Jest config source link; project-churn source. |
| `D33euun92b6aPEvSdsjUny` | rejected | `Skill Archive Rejected` | yes | Old Google Analytics helper package; duplicate stale package note. |
| `27nHcHys9ctNa4pd3NLdPu` | rejected | `Skill Archive Rejected` | yes | Old app build-system inspiration; not durable source material. |
| `GSDjz6Hz3592KDrHh4G1QP` | rejected | `Skill Archive Rejected` | yes | Duplicate `ganalytics` package note; stale implementation source. |
| `No56TvF47FT5zVvbGyiZMb` | rejected | `Skill Archive Rejected` | yes | Old PWA tutorial repo from 2016; use current official PWA docs instead. |
| `NkiZm3vShAyx7hdQy1zoDM` | rejected | `Skill Archive Rejected` | yes | React GUI/input package; package-shopping source. |
| `57QuWeJoVDWSJFTiznzwyu` | deferred | `Skill Archive Deferred` | yes | Lightning CSS project; inventory only. |
| `X4wrpX96pBSEHdV3aSfZoc` | deferred | `Skill Archive Deferred` | yes | Gemini plugin for Simon Willison's LLM CLI; inventory only. |
| `EutxmSNfMRWdapochaefoj` | deferred | `Skill Archive Deferred` | yes | Debug logging utility; inventory only. |
| `D95WbxBXwfBmcJNSSuUbjH` | deferred | `Skill Archive Deferred` | yes | Node logging package comparison bundle; inventory only. |
| `Fu8hVfGZVbHQvaKuPn1uWD` | deferred | `Skill Archive Deferred` | yes | Date/time library project; inventory only. |
| `JJyJF5BztZY7VvDmbJXMFw` | deferred | `Skill Archive Deferred` | yes | Markdown parser project; inventory only. |
| `EXBXdLyxrASNwSozM487Xb` | deferred | `Skill Archive Deferred` | yes | PDF-to-Markdown project; inventory only. |
| `UMYpmM3r9cXFfFZD9cBX23` | rejected | `Skill Archive Rejected` | yes | Old exit-intent marketing package; stale/non-skill source. |
| `Dgz7zZsNRTHr3EtprwNJ4z` | deferred | `Skill Archive Deferred` | yes | Marko framework project; inventory only. |
| `NAWyR7DYxfpExp7uTtaEVx` | rejected | `Skill Archive Rejected` | yes | Old Meteor-like framework repo from 2016; stale source. |
| `HadJYGLyd6zJgVSGQscBTM` | rejected | `Skill Archive Rejected` | yes | Archived CSS typography package; stale package-shopping source. |
| `8z7xAcjysYLC7JqD5GGJjU` | deferred | `Skill Archive Deferred` | yes | AI memory project subpath; inventory only. |
| `V4gCFCvskYTRVRaGqegcjo` | rejected | `Skill Archive Rejected` | yes | Old Mermaid Webpack loader from 2016; stale source. |
| `A98WiyNSALiLoarsxXZkR9` | rejected | `Skill Archive Rejected` | yes | CSS Modules successor package; package-shopping source without broader guidance. |
| `58b3ApG8XZfBwKCAvyuSEt` | rejected | `Skill Archive Rejected` | yes | Mona Sans org/page did not map to a repo; font inventory, not JS tooling source. |
| `WZjAiDMpCNi1cpz48m89zb` | rejected | `Skill Archive Rejected` | yes | Duplicate Mona Sans org/page; font inventory, not JS tooling source. |
| `GJYg3oqqjTdH3CLYdrZrWE` | rejected | `Skill Archive Rejected` | yes | macOS monitor-control utility; unrelated personal tooling. |
| `Q9aZRnJoMLh4SYTr4d2Jw8` | rejected | `Skill Archive Rejected` | yes | Moonfin org/page did not map to useful repo metadata; not source material. |
