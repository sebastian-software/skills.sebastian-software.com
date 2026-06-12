# Cluster Brief: JS Tooling Queue 06

Reviewed: 2026-06-10

## Scope

This queue chunk contains 50 GitHub project links. Most are AI-agent tooling,
external skill repos, scraping/OCR/content tools, CLI tools, terminal apps, or
personal utility projects. Under the current source-review policy, GitHub
projects are tracked in the GitHub Project Matrix and are not direct skill
sources.

All links were inspected through the matrix metadata: canonical repository,
description, stars, archived status, language, latest release, and last commit.

## Decision Summary

| Status      | Count | Rationale                                                                                                            |
| ----------- | ----: | -------------------------------------------------------------------------------------------------------------------- |
| `candidate` |     0 | No article/doc/spec source in this chunk strong enough for direct skill use.                                         |
| `deferred`  |    44 | Interesting active projects captured in the GitHub matrix.                                                           |
| `rejected`  |     6 | Private/personal utility, weak low-signal project, Home Assistant/macOS app inventory, or stale task-runner project. |

## Deferred Project Groups

- AI agents, skills, and agent infrastructure: `andrej-karpathy-skills`,
  `gbrain`, `gstack`, `spec-kit`, `My-Brain-Is-Full-Crew`, `openclaw-studio`,
  `awesome-openclaw-usecases`, `nanobot`, `local-client-prospector-skill`,
  `autoresearch`, `awesome-claws`, `37signals-skills`, `lossless-claw`,
  `mattpocock/skills`, `mempalace`, `agent-lightning`,
  `ralph-orchestrator`, `agency-agents`, `last30days-skill`.
- Web scraping, content extraction, and document tools: `firecrawl`,
  `langextract`, `obscura`, `deepcrawl`, `markitdown`.
- Developer and CLI tools: `gt`, `ghostty`, `lazygit`, `fzf`,
  `streamable-mcp-server-template`, `md4w`, `up-fetch`, `uptime-kuma`,
  `eza`.
- AI/media/model projects: `voicebox`, `mlx-vlm-falcon`,
  Liquid AI cookbook example, `gemma-tuner-multimodal`, `lossless-cut`,
  `MisoTTS`.
- Product/tool inventory: `FormBee`, `karakeep`, `react-doctor`.

These projects may be useful later as tool inventory. They should not drive
skill edits until paired with stronger explanatory sources.

## Rejected Themes

- Personal-health/anxiety or life-ops project: `My-Brain-Is-Full-Crew` would be
  interesting as personal tooling, but it is not relevant source material for
  the software skill archive; it remains deferred above because it is agent
  infrastructure adjacent. The clearly private/home-specific entries are
  rejected below.
- Low-signal repos without enough description/context:
  `local-client-prospector-skill` is kept deferred as external-skill inventory,
  but should not be promoted without content review; `ha-sankey-chart` and
  macOS window management are rejected as unrelated personal tooling.
- Old/stale tool: `lukeed/taskr` last committed in 2020 and is only a package
  idea.

## Proposed Outcome

Decision: `defer/reject only`

No source cards and no skill changes should be made from this chunk. Use the
GitHub Project Matrix if these projects become relevant in a future tool or
external-skill review.

## Things Actions

| Things ID                | Decision | Final tag                | Complete? | Reason                                                                                    |
| ------------------------ | -------- | ------------------------ | --------- | ----------------------------------------------------------------------------------------- |
| `PHhbgMDSaC4ySaXYLSjexD` | deferred | `Skill Archive Deferred` | yes       | Active web scraping/API project; matrix inventory only.                                   |
| `JaB3JoHurgiGaXfKj5CGJ6` | deferred | `Skill Archive Deferred` | yes       | Form backend project; inventory only.                                                     |
| `Bh5convz5J1MQo1mTZRyJQ` | deferred | `Skill Archive Deferred` | yes       | External Claude skill/prompt repo; defer to external-skill review.                        |
| `KfoPGKoNREKBiTUCRz1y7d` | deferred | `Skill Archive Deferred` | yes       | Agent brain project; duplicate source group with next item.                               |
| `Uoa8QUEwGPGUW45AVfPSWE` | deferred | `Skill Archive Deferred` | yes       | Duplicate `gbrain`; captured in matrix.                                                   |
| `BGjVGN8G5N3yFTQzU36icE` | deferred | `Skill Archive Deferred` | yes       | Claude/OpenClaw setup project; duplicate source group with next item.                     |
| `CgDkKoKG7yWsXbUiafqM37` | deferred | `Skill Archive Deferred` | yes       | Duplicate `gstack`; captured in matrix.                                                   |
| `4VnUqzxUVA4ZqNLBLmrt39` | deferred | `Skill Archive Deferred` | yes       | i18n automation project; inventory only.                                                  |
| `PQH14tc6QH1mdmhWz9o9tg` | deferred | `Skill Archive Deferred` | yes       | Terminal emulator project; inventory only.                                                |
| `SHzFor4cZWAakyPDegYDc2` | deferred | `Skill Archive Deferred` | yes       | Spec-driven development toolkit; promising inventory, needs separate content review.      |
| `VMGpNU6nxJSrNSZWd8bfvU` | deferred | `Skill Archive Deferred` | yes       | Personal agent workflow project; inventory only, not direct source material.              |
| `8NosZop69cwbnEApBMFWgk` | deferred | `Skill Archive Deferred` | yes       | Structured extraction library; inventory only.                                            |
| `A4irUDQnc6YfqwKExutGtG` | deferred | `Skill Archive Deferred` | yes       | OpenClaw dashboard project; inventory only.                                               |
| `HAFGyTr49puaYiEMKfyEjG` | deferred | `Skill Archive Deferred` | yes       | Headless browser/scraping project; inventory only.                                        |
| `JGMLYF9smW4tiJSLkSMmbD` | deferred | `Skill Archive Deferred` | yes       | OpenClaw use-case collection; duplicate source group with next item.                      |
| `fJuXXKnNrYVcxYQDVyppt`  | deferred | `Skill Archive Deferred` | yes       | Duplicate OpenClaw use-case collection; captured in matrix.                               |
| `BQ8qXi79SzTBwp2RxZ6QSy` | deferred | `Skill Archive Deferred` | yes       | AI agent project; inventory only.                                                         |
| `F5YMevKymtRc1YesAFwyKg` | deferred | `Skill Archive Deferred` | yes       | MCP server template project; inventory only until separately reviewed.                    |
| `CU5aZApyBTGRz43eQFhKwq` | deferred | `Skill Archive Deferred` | yes       | Markdown-to-WASM renderer project; inventory only.                                        |
| `7zW3nNsAjaSWYqEtTaL4t4` | deferred | `Skill Archive Deferred` | yes       | Agentic data optimization/RAG project; inventory only.                                    |
| `Pz1KZgwrmw8K4mGtP96uj`  | deferred | `Skill Archive Deferred` | yes       | AI voice studio project; inventory only.                                                  |
| `XsXgVDrcW8mMoXFP2dFVcL` | deferred | `Skill Archive Deferred` | yes       | Git terminal UI project; inventory only.                                                  |
| `3XQQq2PQkmuApdAEXV5r5D` | deferred | `Skill Archive Deferred` | yes       | Fuzzy finder CLI project; inventory only.                                                 |
| `9t45ZkiEX4kiaGBgWCidTz` | rejected | `Skill Archive Rejected` | yes       | Low-signal local client prospecting skill repo; not source material.                      |
| `MXXjcLWqJo1d4vx8b6aexj` | deferred | `Skill Archive Deferred` | yes       | Self-hosted bookmark/AI tagging app; inventory only.                                      |
| `2TgKLCJJFDy2hbwbMHrJUS` | deferred | `Skill Archive Deferred` | yes       | AI research automation project; inventory only.                                           |
| `RqHwf3eUjViwScDTTDsNpA` | deferred | `Skill Archive Deferred` | yes       | Async history utility project; inventory only.                                            |
| `3LgnFZjUmQWq6VTYwFRe3m` | rejected | `Skill Archive Rejected` | yes       | Very small/low-signal MLX VLM agent repo; not source material.                            |
| `TiHsrtmxQbGdjfTPcZgtYn` | deferred | `Skill Archive Deferred` | yes       | Fetch client builder project; inventory only.                                             |
| `9dwxhw7Y6RBqGmGYNKVzEA` | deferred | `Skill Archive Deferred` | yes       | Cookbook example repo; inventory only, not a durable guide by itself.                     |
| `FW2e5iQzydxEDNqWcfByE1` | deferred | `Skill Archive Deferred` | yes       | Monitoring app project; inventory only.                                                   |
| `ETyRhv66ugLt8fQgZ5bUP5` | rejected | `Skill Archive Rejected` | yes       | Stale task automation package last committed 2020; package-shopping source.               |
| `JzkuZHTygnU7pbLHX65UuA` | deferred | `Skill Archive Deferred` | yes       | Firecrawl alternative project; inventory only.                                            |
| `8MrnbUhVY1vccUUscPPQJs` | deferred | `Skill Archive Deferred` | yes       | AI agents collection; inventory only.                                                     |
| `U8Jyi8TQPfCRbBanBJswda` | deferred | `Skill Archive Deferred` | yes       | 37signals-style external skill/reference repo; defer to separate external-skill review.   |
| `QYBNq3iWdWB4w2Dk9NLVkz` | deferred | `Skill Archive Deferred` | yes       | OpenClaw context-management plugin; inventory only.                                       |
| `Hbsw5VrRcuruFntttjtzBN` | deferred | `Skill Archive Deferred` | yes       | Multimodal fine-tuning project; inventory only.                                           |
| `2inqPnwXhfZTPAkewGPmV7` | deferred | `Skill Archive Deferred` | yes       | External skills repo; duplicate source group with next item.                              |
| `HzFRi3RVdpgdvJHTkeNnTL` | deferred | `Skill Archive Deferred` | yes       | Duplicate `mattpocock/skills`; captured in matrix.                                        |
| `8HEiXcqePi1VydGSWgAqsU` | deferred | `Skill Archive Deferred` | yes       | AI memory system project; inventory only.                                                 |
| `MuSAmXBiGxFKfUKmBGUejt` | deferred | `Skill Archive Deferred` | yes       | AI agent training project; inventory only.                                                |
| `TCakNDK4Ygzq4j9zRdLWQS` | deferred | `Skill Archive Deferred` | yes       | Document-to-Markdown project; inventory only.                                             |
| `NEUPkjRLJC3hsiwd3XyjBS` | rejected | `Skill Archive Rejected` | yes       | Media editing app is interesting but outside software skill-source scope.                 |
| `85MT2kiE5Zqi28oCJps23Q` | deferred | `Skill Archive Deferred` | yes       | AI agent orchestration project; inventory only.                                           |
| `QYhPFZo2BCkRBAhDkS3ZAu` | deferred | `Skill Archive Deferred` | yes       | React performance issue detector project; inventory only until paired with docs/articles. |
| `8MWLt6LqczxC6wNvDtgiTw` | rejected | `Skill Archive Rejected` | yes       | Home Assistant Sankey chart card; private/home dashboard tooling.                         |
| `5PSrivz68m6JWqauQGYi6J` | deferred | `Skill Archive Deferred` | yes       | Text-to-speech model project; inventory only.                                             |
| `UyiFcaGARKv2kL8cHcDn1P` | rejected | `Skill Archive Rejected` | yes       | macOS window-management app; unrelated to skill-source review.                            |
| `XXTiuXV7Hco8yEUq7GRmxo` | deferred | `Skill Archive Deferred` | yes       | AI agency agents collection; inventory only.                                              |
| `HCqZndLXVhXZWQvvXUW2dA` | deferred | `Skill Archive Deferred` | yes       | Research-summary skill repo; external-skill inventory only.                               |
