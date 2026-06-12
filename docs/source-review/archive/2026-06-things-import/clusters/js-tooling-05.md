# Cluster Brief: JS Tooling Queue 05

Reviewed: 2026-06-10

## Scope

This queue chunk contains 50 GitHub links, mostly AI-agent projects, Claude
skill repositories, scraping/OCR/document tools, CLI tools, and a few app demos
or package links. Under the current archive policy, these are not direct skill
sources. They were inspected through GitHub Project Matrix metadata and routed
to deferred inventory or rejected when too weak, stale, or misclassified.

## Decision Summary

| Status      | Count | Rationale                                                                                                                                  |
| ----------- | ----: | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `candidate` |     0 | No article/doc/spec source in this chunk strong enough for direct skill use.                                                               |
| `deferred`  |    42 | Interesting active projects captured in the GitHub matrix.                                                                                 |
| `rejected`  |     8 | App demos, narrow UI packages, low-signal project links, archived framework source, or PR/repo links that should not drive skill material. |

## Deferred Project Groups

- Agent and skill inventory: `goose`, `agent-skills`, `seo-geo-claude-skills`,
  `awesome-claude-skills`, `avoid-ai-writing`, `crewAI`,
  `claude-code-skills`, `claude-token-efficient`, `browser-harness`,
  `mission-control`, `code-overhaul-skill`.
- AI/OCR/document/content tools: `SimpleMem`, `llmfit`, `zvec`,
  `prompt-eng-interactive-tutorial`, `mlx-audio`, `mlx-vlm`, `paperless-ai`,
  `Scrapling`, `chandra`, `soprano`, `ST3GG`, `sitefetch`.
- Developer/CLI/tooling inventory: `cloc`, `electrobun`, `delta`,
  `microbundle`, `docmd`, `eza`.
- Product/research inventory: `GitNexus`, `blinko`, `ClawRouter`,
  `Personal_AI_Infrastructure`, `open-seo`, `ladder`.

These remain useful for separate project/tool review, not for immediate skill
changes.

## Rejected Themes

- App/demo repos with no durable source value: healthcare platform demo,
  open-source TypeForm clone.
- Narrow UI/icon/animation package picks: `number-flow`, weather icon set.
- Weak or low-signal project links without enough context: `unplugin-parcel-macros`,
  `litter`.
- Archived or non-source project links: `facebook/fbt`, React PR #36173.
- Dubious/private browsing utility: `ladder` was kept deferred as project
  inventory because it is active and tracked in the matrix, but should not be
  used as skill material without a separate ethics/legal review.

## Proposed Outcome

Decision: `defer/reject only`

No skill changes and no source cards should be created from this chunk. If a
skill-development or AI-agent source pass later wants to evaluate external
skill repositories, use this chunk's deferred items as a starting inventory and
review the actual skill content then.

## Things Actions

| Things ID                | Decision | Final tag                | Complete? | Reason                                                                                                     |
| ------------------------ | -------- | ------------------------ | --------- | ---------------------------------------------------------------------------------------------------------- |
| `2LW4PHR3Kjeg1ZPCpuNMn7` | deferred | `Skill Archive Deferred` | yes       | Active AI agent project; matrix inventory only.                                                            |
| `VSVtviqwNq1cJ87X4gruz5` | deferred | `Skill Archive Deferred` | yes       | Claude SEO/GEO skills repo; defer to separate external-skill review.                                       |
| `N6jX9NUwjka9XHVVZ85epQ` | deferred | `Skill Archive Deferred` | yes       | Code-intelligence project; matrix inventory only.                                                          |
| `8YmeKxNKkYRbDdfDPDZBgz` | deferred | `Skill Archive Deferred` | yes       | Agent skills repo; external-skill inventory, not direct source material.                                   |
| `BRSZVjFNig9TGL9i79qMZU` | deferred | `Skill Archive Deferred` | yes       | Duplicate `addyosmani/agent-skills`; captured in matrix.                                                   |
| `8w3yPgWQkhzQYy2Bg4eKuu` | rejected | `Skill Archive Rejected` | yes       | Healthcare app demo/tutorial repo; not reusable skill-source material.                                     |
| `Hr9Zed9qW5uqBwfmb9wDcb` | deferred | `Skill Archive Deferred` | yes       | LLM memory project; matrix inventory only.                                                                 |
| `UJUxrwA3BeW6HfNhWv7etF` | deferred | `Skill Archive Deferred` | yes       | Source line-counting CLI project; inventory only.                                                          |
| `TxhwVmxrVM26kC7hiBzJw8` | deferred | `Skill Archive Deferred` | yes       | Local model/hardware fitting tool; inventory only.                                                         |
| `3maSZZsZpiaEdWdhkUW3aY` | deferred | `Skill Archive Deferred` | yes       | Vector DB project; duplicate source group with next item.                                                  |
| `MRx6CjmmEXJVcjgtwNEtjo` | deferred | `Skill Archive Deferred` | yes       | Duplicate `alibaba/zvec`; captured in matrix.                                                              |
| `KrF5ytFsggg2En6oEAJgtU` | deferred | `Skill Archive Deferred` | yes       | Anthropic prompt-engineering tutorial repo; promising, but needs separate content review before skill use. |
| `9GFXmN6PLymtSg5XvSKJWj` | rejected | `Skill Archive Rejected` | yes       | Animated-number UI component package; narrow package-shopping source.                                      |
| `MGxzpA9b8dvwipXSr2UQM`  | rejected | `Skill Archive Rejected` | yes       | Weather icon set; visual asset inventory, not skill source material.                                       |
| `EX1mjbLVUtEGK1q2PsPwbo` | deferred | `Skill Archive Deferred` | yes       | Desktop app runtime project; matrix inventory only.                                                        |
| `H6cdvEJ1UAeM1UboevHt2U` | deferred | `Skill Archive Deferred` | yes       | MLX audio project; inventory only.                                                                         |
| `LASvE29AFePQfQF67EmkMT` | deferred | `Skill Archive Deferred` | yes       | MLX vision-language model project; duplicate source group with next item.                                  |
| `WwdJZYdz7V4w3t3BbgMQpe` | deferred | `Skill Archive Deferred` | yes       | Duplicate `mlx-vlm`; captured in matrix.                                                                   |
| `8XeXxPWUfTvhPnRfAyyvEX` | deferred | `Skill Archive Deferred` | yes       | Personal AI note project; matrix inventory only.                                                           |
| `HR39aJaGere8aaJGrcVnNQ` | deferred | `Skill Archive Deferred` | yes       | LLM router project; matrix inventory only.                                                                 |
| `6Q9et29MAjXYC6h3niJCC8` | deferred | `Skill Archive Deferred` | yes       | Browser automation harness project; matrix inventory only.                                                 |
| `U943g74shZxY4Shkz4dWKg` | deferred | `Skill Archive Deferred` | yes       | Agent orchestration project; matrix inventory only.                                                        |
| `TSWy31MjxxagXxMEYutTQP` | deferred | `Skill Archive Deferred` | yes       | Claude Code setup collection; external-tool inventory only.                                                |
| `NJp8fctW83rotZAYyguXgP` | deferred | `Skill Archive Deferred` | yes       | Document-analysis project; matrix inventory only.                                                          |
| `MenFGzNVC25qCbvnU9AoBZ` | deferred | `Skill Archive Deferred` | yes       | Claude skills list; external-skill inventory, not direct source material.                                  |
| `Gt6urvD9hw9yDxB9EXS8tx` | deferred | `Skill Archive Deferred` | yes       | AI-writing cleanup skill repo; defer to external-skill review.                                             |
| `B7nCgP7VvmEYFTxwXNm8HJ` | deferred | `Skill Archive Deferred` | yes       | Multi-agent framework project; matrix inventory only.                                                      |
| `5yb97yitqwZMHki5hPFiqa` | deferred | `Skill Archive Deferred` | yes       | Personal Claude skills repo; inventory only.                                                               |
| `VejA6USbpDUTL1CPWcYk2B` | deferred | `Skill Archive Deferred` | yes       | Web scraping framework project; matrix inventory only.                                                     |
| `4BsPUNfiFt2cUFNqMTM2MR` | rejected | `Skill Archive Rejected` | yes       | TypeForm clone app repo; product clone/demo, not source material.                                          |
| `CGqrqA4Xz6SthssjN2bc4y` | deferred | `Skill Archive Deferred` | yes       | Git/diff CLI project; inventory only.                                                                      |
| `HLuHfRoYCBtQLxhBUvuRGR` | deferred | `Skill Archive Deferred` | yes       | Personal AI infrastructure repo; inventory only.                                                           |
| `7Y7pgs2nRhA7g4Pqc6KSSw` | deferred | `Skill Archive Deferred` | yes       | OCR/layout model project; inventory only.                                                                  |
| `QTWmFXhG1JrRzDMZc4x6rW` | deferred | `Skill Archive Deferred` | yes       | Claude Code skills marketplace repo; external-skill inventory.                                             |
| `YTLTDSzVQ4ZiywZNXGkhvA` | deferred | `Skill Archive Deferred` | yes       | Bundler source link; matrix inventory, not direct source material.                                         |
| `VshboHmWqxH8tcyqvNuob9` | rejected | `Skill Archive Rejected` | yes       | Low-signal macro plugin repo without durable source context.                                               |
| `UCSHSGshuV1TFycs9H6HwT` | rejected | `Skill Archive Rejected` | yes       | Low-signal project link without description; not source material.                                          |
| `LxVxqjMoLZVkxvj1hVz8zM` | deferred | `Skill Archive Deferred` | yes       | Documentation generator project; matrix inventory only.                                                    |
| `TGxnNS9BsFvBGJKk7dyBKT` | deferred | `Skill Archive Deferred` | yes       | CLAUDE.md token-efficiency repo; defer to external prompt/skill review.                                    |
| `Rad8GAqctDRYATQFQmKzoJ` | deferred | `Skill Archive Deferred` | yes       | AI agent skills repo; inventory only.                                                                      |
| `XdJrToQzSJR7EWC2Va4ovU` | deferred | `Skill Archive Deferred` | yes       | Site-to-text fetch project; matrix inventory only.                                                         |
| `L7FbvpWrsKgv899oVa9oKP` | deferred | `Skill Archive Deferred` | yes       | Code-overhaul skill repo; external-skill inventory only.                                                   |
| `6mjn9EhKnU7CDWiqxicsvc` | deferred | `Skill Archive Deferred` | yes       | Text-to-speech project; duplicate source group with next item.                                             |
| `CKCHyTCMtyj33kAWrtJLBz` | deferred | `Skill Archive Deferred` | yes       | Duplicate `soprano`; captured in matrix.                                                                   |
| `DQJgbF8VkXb5y8PD6L8zPK` | deferred | `Skill Archive Deferred` | yes       | Steganography project; security/tool inventory only.                                                       |
| `SUn4t4pXh8vxyrHVPk2XGq` | deferred | `Skill Archive Deferred` | yes       | SEO tooling project; matrix inventory only.                                                                |
| `SLtaBeh1ws9kvE7i3wJGc2` | deferred | `Skill Archive Deferred` | yes       | Active proxy/project inventory; do not use for skill material without ethics/legal review.                 |
| `JZ54Sx6fNxzjBCjHpR5L8o` | deferred | `Skill Archive Deferred` | yes       | Modern `ls` replacement project; inventory only.                                                           |
| `5fgrgwsNbFBKFg1af6oRY7` | rejected | `Skill Archive Rejected` | yes       | Archived JavaScript i18n framework project; not current source material.                                   |
| `PkDJxeq9jFbk9yphJXN9AT` | rejected | `Skill Archive Rejected` | yes       | React PR link; project churn, not durable source material without explanatory docs.                        |
