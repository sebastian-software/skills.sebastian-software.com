# Cluster Brief: JS Tooling Queue 07

Reviewed: 2026-06-10

## Scope

This queue chunk contains 50 GitHub project links. The group is dominated by
AI-agent infrastructure, external skill repositories, CLI tools, scraping/OCR,
PDF/document, memory, and analytics projects. Under the current archive policy,
these are tracked in the GitHub Project Matrix and are not direct skill sources.

All links were inspected through matrix metadata: canonical repository,
description, stars, archive status, language, latest release, and last commit.

## Decision Summary

| Status      | Count | Rationale                                                                                                         |
| ----------- | ----: | ----------------------------------------------------------------------------------------------------------------- |
| `candidate` |     0 | No direct article/doc/spec source in this chunk.                                                                  |
| `deferred`  |    41 | Active or potentially interesting projects captured in the GitHub matrix.                                         |
| `rejected`  |     9 | Low-signal/personal project, old changelog/plugin, generic package link, macOS utility, or otherwise weak source. |

## Deferred Project Groups

- Agent infrastructure and skill repos: `hermes-agent-self-evolution`,
  `hermes-paperclip-adapter`, `nullclaw`, `superpowers`, `openclaw/agent-skills`,
  `clawsweeper`, `paperclip`, `awesome-cursorrules`, `agent-skills`,
  `openclaw-mission-control`, `agentmemory`, `rtk`, `code-review-expert`,
  `antigravity-awesome-skills`, `skills`, `agent-scripts`,
  `openclaw-supermemory`, `supermemory`, `brainctl`, `api-to-mcp`.
- Content/document/search/scraping tools: `VidBee`, `onyx`, `opendataloader-pdf`,
  `retext`, `scrapy`, `ferromark`, `summarize`, `Stirling-PDF`.
- AI/speech/model tools: `VoxCPM`, `stenoai`, `qwen3_asr_rs`, `SwiftLM`,
  `speech-swift`.
- Developer and app tooling: `rybbit`, `fetch-extras`, `starship`,
  `code-review-graph`, `tremor-npm`, `ts-reset`.

These projects are useful inventory, not immediate skill-source material.

## Rejected Themes

- Very low-signal or tiny project links: `petekp/agent-skills`,
  `tforschbach/CodexRemote`.
- Old historical/churn links: React Router changelog anchor,
  Relay compiler Webpack plugin from 2017.
- Package/tool picks without durable guidance: `fetch-extras`, `ts-reset`,
  `tremor-npm` are active and therefore deferred, but should not become skill
  material without article/docs support.
- Private/local system utility: `tw93/Mole` Mac cleanup tool.

## Proposed Outcome

Decision: `defer/reject only`

No skill changes should be made from this chunk. Use the matrix rows as project
inventory for future tool review or external-skill review.

## Things Actions

| Things ID                | Decision | Final tag                | Complete? | Reason                                                                             |
| ------------------------ | -------- | ------------------------ | --------- | ---------------------------------------------------------------------------------- |
| `B6DQQ6sSm2C1dVsk7p87Lu` | deferred | `Skill Archive Deferred` | yes       | Video download project; matrix inventory only.                                     |
| `VTqV3XszKc5JCUCPCeaNbV` | deferred | `Skill Archive Deferred` | yes       | Agent self-evolution project; inventory only.                                      |
| `BXRcCvrUaBuXaiReCHTxA3` | deferred | `Skill Archive Deferred` | yes       | Agent adapter project; inventory only.                                             |
| `CKPAo8AzUibDUgg2rnqEUi` | deferred | `Skill Archive Deferred` | yes       | AI assistant infrastructure project; inventory only.                               |
| `Dho2g9FUFNQzrfnZZPuj8a` | deferred | `Skill Archive Deferred` | yes       | Agentic skills framework; duplicate source group with next item.                   |
| `FWrCyjciyuPVd76ioHjbRf` | deferred | `Skill Archive Deferred` | yes       | Duplicate `obra/superpowers`; captured in matrix.                                  |
| `SH2oEGCSDvRdYzEsMy6mJ1` | deferred | `Skill Archive Deferred` | yes       | Open-source AI platform project; inventory only.                                   |
| `RNh1DiCzB4dfheGToHrB3v` | deferred | `Skill Archive Deferred` | yes       | Text-to-speech model project; inventory only.                                      |
| `BAR7YjqE9dUAmaCdoakYtd` | deferred | `Skill Archive Deferred` | yes       | External agent skill file; defer to separate external-skill review.                |
| `HfKYUCsU1rAq3Xejau9ifW` | deferred | `Skill Archive Deferred` | yes       | PR/issue cleanup agent project; inventory only.                                    |
| `3Je34bHzKwGbUtzzCBtCEu` | deferred | `Skill Archive Deferred` | yes       | PDF parser/accessibility project; inventory only.                                  |
| `7erVKZaVUGwJ7GJXqDQyLR` | deferred | `Skill Archive Deferred` | yes       | Agent management app project; duplicate source group with next item.               |
| `Q3U3XvjGRzCkqTwyCuW1bp` | deferred | `Skill Archive Deferred` | yes       | Duplicate `paperclip`; captured in matrix.                                         |
| `H6cjjTYeHdfNGDmRj6Ue9g` | deferred | `Skill Archive Deferred` | yes       | Cursor rules collection; inventory only.                                           |
| `7BELJK7nYz6aCQJZZALhqb` | rejected | `Skill Archive Rejected` | yes       | Very low-signal small agent-skills repo; not source material.                      |
| `ExwydPgbgjxJHvsmyjC5pL` | rejected | `Skill Archive Rejected` | yes       | React Router changelog anchor; release churn, not durable source.                  |
| `7MTYVhoktW75djdkH7gRfR` | deferred | `Skill Archive Deferred` | yes       | Text-processing project; inventory only.                                           |
| `K7PsCjJ5XaLKURDiWqrjy6` | deferred | `Skill Archive Deferred` | yes       | OpenClaw GUI project; inventory only.                                              |
| `AYJjhhQjmQLeYWFgUbu9HB` | deferred | `Skill Archive Deferred` | yes       | AI coding-agent memory project; inventory only.                                    |
| `FSZeKWS1iSTci31hYUekkm` | deferred | `Skill Archive Deferred` | yes       | Token-reducing CLI proxy project; inventory only.                                  |
| `PtLqCkbYaFxi7NVZtVKjE`  | deferred | `Skill Archive Deferred` | yes       | AI conversation notes project; inventory only.                                     |
| `KjRdaJMT3odKjbA5iXboct` | deferred | `Skill Archive Deferred` | yes       | Privacy-friendly analytics project; inventory only.                                |
| `6MmkZgA5H1J7kANqTnkE94` | deferred | `Skill Archive Deferred` | yes       | Code-review skill repo; external-skill inventory only.                             |
| `VJW48byXwuCY7L36yvGB6b` | deferred | `Skill Archive Deferred` | yes       | Scraping framework project; inventory only.                                        |
| `7uWPmCa8y7wRV1dCRTwtLe` | deferred | `Skill Archive Deferred` | yes       | Markdown parser project; inventory only.                                           |
| `mWMUS4Z3CTMRh2hQ34PuY`  | deferred | `Skill Archive Deferred` | yes       | Speech-recognition project; inventory only.                                        |
| `SoWTJuaJ3SFYR9XhHfMPeu` | deferred | `Skill Archive Deferred` | yes       | CLI file viewer project; inventory only.                                           |
| `RXYZsdYM5pzLbiy9CBMxRv` | deferred | `Skill Archive Deferred` | yes       | Swift LLM inference server; inventory only.                                        |
| `LyAWCwUHn9Pkdi7ht4kjtt` | deferred | `Skill Archive Deferred` | yes       | OpenClaw memory plugin; inventory only.                                            |
| `Ht8Y6Nxk54A6M8v4ozwwgT` | deferred | `Skill Archive Deferred` | yes       | Agentic skills library; duplicate source group with next item.                     |
| `T98GMWvhGHaVJtcdYuhB4h` | deferred | `Skill Archive Deferred` | yes       | Duplicate `antigravity-awesome-skills`; captured in matrix.                        |
| `LCjxWxxUtVSiWFqS7XX78W` | rejected | `Skill Archive Rejected` | yes       | Fetch utility package link; use platform/docs articles before skill material.      |
| `4DaRcLjqn1ZjXY5Qa1y8ZL` | deferred | `Skill Archive Deferred` | yes       | External skills repo; duplicate source group with next item.                       |
| `7v1Zg22xHz1zkf6WTNVU6d` | deferred | `Skill Archive Deferred` | yes       | Duplicate `slavingia/skills`; captured in matrix.                                  |
| `DQqBF17ifJZWH1afAym2bv` | deferred | `Skill Archive Deferred` | yes       | Apple Silicon speech toolkit; inventory only.                                      |
| `K6Q98m7fbJm8j6woTM1bLP` | deferred | `Skill Archive Deferred` | yes       | Shell prompt project; inventory only.                                              |
| `SHYuJi3KtaYZvNTVCHVFMR` | deferred | `Skill Archive Deferred` | yes       | External skill file in agent scripts; defer to external-skill review.              |
| `6qqfktN3dXLNM8jxFuPUMY` | deferred | `Skill Archive Deferred` | yes       | Summarization CLI/extension project; inventory only.                               |
| `FHqdFTR5NrFqTBtPfiHHK9` | deferred | `Skill Archive Deferred` | yes       | PDF app project; duplicate source group with next item.                            |
| `qGebBaAr9DTjMMBeQcaxa`  | deferred | `Skill Archive Deferred` | yes       | Duplicate `Stirling-PDF`; captured in matrix.                                      |
| `B1QeDe2rAzF4JkxEVA2FBE` | deferred | `Skill Archive Deferred` | yes       | OpenClaw memory plugin; inventory only.                                            |
| `6KVtyLJ8VQ9Eh55xndQGDY` | deferred | `Skill Archive Deferred` | yes       | AI memory app/API project; inventory only.                                         |
| `TfPcaSurDhXHqvJjFtAHKY` | rejected | `Skill Archive Rejected` | yes       | Low-signal Swift remote app with no useful source context.                         |
| `97KPg7NR1BwBhWWUcvYvj8` | rejected | `Skill Archive Rejected` | yes       | Old Relay compiler Webpack plugin last committed 2017; stale build-tooling source. |
| `YAvhfCtQLx4qiDErJVVAC4` | deferred | `Skill Archive Deferred` | yes       | Local code intelligence graph project; inventory only.                             |
| `VAi8xmsqUQMoTZSMUfSBSe` | rejected | `Skill Archive Rejected` | yes       | TypeScript reset package link; use explanatory TS sources before skill material.   |
| `CZ8ZZAyyaTWnpMQ4NWRQwN` | rejected | `Skill Archive Rejected` | yes       | React dashboard component package; package-shopping source.                        |
| `59qB5P2AEAVzJnv5x7xgKW` | deferred | `Skill Archive Deferred` | yes       | AI memory MCP project; inventory only.                                             |
| `RR6Enyz5hgfW1asTwxMEKh` | rejected | `Skill Archive Rejected` | yes       | macOS cleanup/monitoring utility, not skill-source material.                       |
| `VdrDKkj8o5RVxKKGy9YWgb` | rejected | `Skill Archive Rejected` | yes       | Low-signal API-to-MCP tool project; not enough source context.                     |
