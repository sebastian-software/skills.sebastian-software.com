# Cluster Brief: AI Agents, Visual Assets, Knowledge

## Scope

This pass reviews the small Things clusters `Skill: AI Agents`, `Skill: Visual
Assets`, and `Skill: Knowledge` as a source-review buffer. No Skills or Things
were edited. Links were opened through web fetch and/or direct `curl` where
reachable.

The cluster contains three different knowledge areas:

- agentic coding workflows, including coding-agent docs, prompt mechanics,
  subagent patterns, and Codex integration surfaces;
- SVG/icon/image asset workflows, including inline SVG, sprite systems, icon
  delivery, brand icon libraries, and image loading techniques;
- miscellaneous knowledge links, mostly Storybook/tooling, web APIs, and UI
  design notes that do not belong in an AI or visual-assets skill.

Decision meanings in this brief:

- `candidate` - should feed a new skill or source-backed proposal.
- `keep` - worth preserving as an existing-skill/reference update, but not a
  new skill candidate from this cluster.
- `defer` - news, product churn, vendor churn, or useful later but not this pass.
- `reject` - duplicate, dead, too weak, stale, irrelevant, or misclassified.

## Access Notes

- Anthropic Claude Code overview redirected from
  `docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview` to
  `https://code.claude.com/docs`; it was reachable.
- OpenAI Codex for OSS and Codex Security were reachable through web fetch, but
  direct `curl` returned `403`. The review treats this as reachable with a curl
  access caveat.
- Storybook theme switcher addon returned `404`.
- Storybook test runner docs at `/docs/writing-tests/test-runner` returned
  `404`. A later Storybook docs path may exist, but this Things URL is stale.
- GitHub Octicons redirected from `github.com/blog/...` to `github.blog/...`.
- Storybook main config docs redirected from the React-specific path to the
  current generic docs path.

## Dedupe And Misclassification

- `HYcJnAikVZnZTV5CgLuvxh` and `4gsbJYcqimixCn8c1QFxtE` are the same Josh W.
  Comeau SVG source after ignoring the newsletter query string. Keep the Visual
  Assets item as canonical; reject the AI Agents copy as duplicate and
  misclassified.
- `BmogJdzzdNtTyusnTJ1Q8m` and `LL3wanC6CZhVDhyoU7M7Vm` are exact duplicate
  Claude Code overview URLs. Keep the first; reject the duplicate.
- `2s9CgbhTEusPBnW7aQuvuW` and `Q9MfChRJMMeESe2GBFTnJD` are exact duplicate
  Simon Willison "Using LLMs to write code" URLs. Keep the first; reject the
  duplicate.
- `GL5jKtGiNcsMHvRmJVk134` is a JavaScript `Array.sort` explainer, not an AI
  Agents source.
- Storybook links in `Knowledge` are better classified as JS Tooling or Testing,
  not general Knowledge.
- `RpKSGJZKBTdJiRVHE6cac5` is UX course marketing for complex apps; it may be
  useful elsewhere but is not an AI Agents source.

## Proposed Outcome

Decision: `new skill candidate` plus `existing skill/reference updates`

Target skill or proposed skill names:

- `skills/internal/s7n-agentic-coding-workflows/` - plausible, narrow candidate.
  Do not create from news links. Base it on durable workflow sources only:
  Claude Code overview, OpenAI prompt guidance, OpenAI Codex app-server docs,
  and durable practice writing from Simon Willison.
- `skills/internal/s7n-svg-icons-assets/` - plausible, narrow candidate or a
  reference split from `s7n-svg-textures`. This cluster is stronger than the AI
  one because several sources point at the same repeatable workflow: choosing,
  structuring, delivering, and maintaining SVG/icon assets.
- Existing reference updates only:
  `skills/internal/s7n-ui-design/references/01-fundamentals.md`,
  `skills/internal/s7n-ui-design/references/04-layout-spacing.md`,
  `skills/internal/s7n-ui-design/references/09-seo.md`, and a future
  Storybook/testing reference if that cluster is opened.

Do not create a broad AI news, model-release, or Storybook-roadmap skill from
this pass.

## Skill Boundary

Use `s7n-agentic-coding-workflows` when the user asks to:

- structure a complex coding task across agents, subagents, tools, repo
  instructions, and verification loops;
- decide whether reusable agent guidance belongs in a prompt, `AGENTS.md`,
  skill, plugin, MCP server, hook, or automation;
- design durable handoff, review, and repair loops for agent-written code;
- integrate Codex or Claude-style coding agents into a product or local workflow
  with explicit tool and security boundaries.

Do not use it when:

- the user asks for current model news, benchmark comparisons, pricing, or vendor
  launch coverage;
- the task is simply "write a better prompt" without a repeatable coding
  workflow;
- official product facts are needed and the existing `openai-docs` or vendor
  docs should be checked directly.

Use `s7n-svg-icons-assets` when the user asks to:

- create, audit, or integrate SVG icons, icon systems, sprite sheets, favicons,
  brand icons, or inline SVG assets;
- choose between inline SVG, external SVG, icon fonts, sprites, npm icon
  packages, and CDN-delivered assets;
- make SVG assets accessible, themeable, cacheable, tree-shakeable, and
  maintainable.

Do not use it when:

- the user wants SVG filter textures, noise, procedural backgrounds, or
  organic surface effects. That remains `s7n-svg-textures`;
- the user wants general image optimization or LQIP/background loading. That is
  an existing UI/performance reference update;
- the user wants generated illustrations or raster assets.

## Proposed Structure

```text
skills/internal/s7n-agentic-coding-workflows/
|-- SKILL.md
|-- README.md
|-- references/
|   |-- task-decomposition.md
|   |-- prompt-and-context-design.md
|   |-- subagents-and-delegation.md
|   |-- tool-boundaries.md
|   |-- app-server-integrations.md
|   `-- verification-and-review-loops.md
`-- evals/
    `-- evals.json

skills/internal/s7n-svg-icons-assets/
|-- SKILL.md
|-- README.md
|-- references/
|   |-- svg-fundamentals.md
|   |-- icon-system-architecture.md
|   |-- sprites-and-delivery.md
|   |-- brand-icons-and-licensing.md
|   |-- accessibility-and-theming.md
|   `-- favicons-and-app-icons.md
`-- evals/
    `-- evals.json
```

## Reference Plan

- `references/prompt-and-context-design.md` - use OpenAI prompt guidance for
  specific prompt mechanics and constraints, but keep model- and API-specific
  facts out of the skill body unless checked against official docs.
- `references/app-server-integrations.md` - use Codex app-server docs only for
  embedding Codex into product workflows, not for ordinary agent use.
- `references/subagents-and-delegation.md` - use Claude Code overview as primary
  product-doc context; treat awesome-subagents as discovery material, not
  authority.
- `references/svg-fundamentals.md` - use Josh W. Comeau for inline SVG, viewBox,
  CSS/JS addressability, primitives, and readable SVG source.
- `references/icon-system-architecture.md` - use CSS-Tricks and GitHub Octicons
  for the move away from icon fonts toward SVG and for system tradeoffs.
- `references/sprites-and-delivery.md` - use the SVG sprite sheet source for a
  pipeline-oriented reference.
- `references/brand-icons-and-licensing.md` - use Simple Icons for brand icon
  lookup, package/CDN usage, and legal disclaimer caveats.
- Existing `s7n-ui-design` references - fold in focus-visible, image loading,
  and favicon/app-icon notes where relevant rather than creating separate skills.
- Future Storybook/testing reference - consolidate Storybook 10, main config,
  and any current test-runner path in a testing/tooling cluster.

## Eval Ideas

- Prompt: "Design a repeatable workflow for using coding agents on a risky
  refactor with tests, review, and fallback."
  Expected behavior: identifies task boundaries, context sources, tool limits,
  verification loop, and what belongs in skills versus repo instructions.
- Prompt: "Should we create subagents for this migration?"
  Expected behavior: distinguishes useful specialization from unnecessary
  context fragmentation, and asks for clear handoff contracts.
- Prompt: "Build an SVG icon system for a React app with brand icons and a
  favicon set."
  Expected behavior: chooses icon source strategy, accessibility rules,
  theming/currentColor, delivery/cache strategy, licensing checks, and favicon
  outputs.
- Prompt: "Convert an icon-font setup to SVG."
  Expected behavior: explains migration tradeoffs, avoids layout shifts, keeps
  accessible names intact, and chooses inline/sprite/package delivery based on
  project constraints.

## Source Decisions

|   # | Things ID                | Intake cluster | Opened result                                                   | Decision  | Target                                           | Notes                                                                                                 |
| --: | ------------------------ | -------------- | --------------------------------------------------------------- | --------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
|   1 | `HYcJnAikVZnZTV5CgLuvxh` | AI Agents      | Josh W. Comeau SVG tutorial, reachable                          | reject    | Dedupe to #22                                    | Duplicate of #22 and misclassified as AI.                                                             |
|   2 | `DLx6dtUvvNku6kAheFKDwn` | AI Agents      | Heise GPT-4 Turbo news, 2023-11-07, reachable                   | defer     | None                                             | Product/news churn; no durable workflow value.                                                        |
|   3 | `BmogJdzzdNtTyusnTJ1Q8m` | AI Agents      | Claude Code overview, reachable after redirect                  | candidate | `s7n-agentic-coding-workflows`                   | Primary vendor docs for agentic coding tool capabilities and integration surfaces.                    |
|   4 | `LL3wanC6CZhVDhyoU7M7Vm` | AI Agents      | Same Claude Code overview URL                                   | reject    | Dedupe to #3                                     | Exact duplicate.                                                                                      |
|   5 | `61RUMT9FQ9SaS2kbVsBXno` | AI Agents      | Simon Willison note on Claude Code remote control, 2026-02-25   | defer     | Possible later agent workflow note               | Product-feature churn; maybe revisit if remote-control workflows become a skill section.              |
|   6 | `GL5jKtGiNcsMHvRmJVk134` | AI Agents      | Piccalilli link to `Array.sort` comparator explainer            | reject    | None                                             | JavaScript fundamentals, not AI Agents.                                                               |
|   7 | `2s9CgbhTEusPBnW7aQuvuW` | AI Agents      | Simon Willison "Using LLMs to write code", 2025-03-11           | candidate | `s7n-agentic-coding-workflows`                   | Durable practice article for human-in-the-loop coding, verification, and use of LLMs as accelerators. |
|   8 | `WdF3S4Egk3rDJNUTeiD95N` | AI Agents      | OpenAI prompt guidance, reachable                               | candidate | `s7n-agentic-coding-workflows` / `openai-docs`   | Primary docs for prompt mechanics; keep narrow and version-aware.                                     |
|   9 | `9aJpJAKmPr21rxGQxKvmBx` | AI Agents      | OpenAI Codex app-server docs, reachable                         | candidate | `s7n-agentic-coding-workflows`                   | Primary docs for embedding Codex into apps; narrow integration reference.                             |
|  10 | `8JFjCZidLfYGZd1pU2KpiZ` | AI Agents      | Awesome Claude Code subagents GitHub repo, reachable            | defer     | Possible subagent discovery appendix             | Useful list but not authoritative enough as core guidance.                                            |
|  11 | `VaxkmeooV4gNpm6uQBDSUG` | AI Agents      | OpenAI Codex for OSS form, web reachable, curl 403              | reject    | None                                             | Program/form link, not a durable source card.                                                         |
|  12 | `UyfbZGhEAhtJibi77LpT5f` | AI Agents      | OpenAI Codex Security research preview, web reachable, curl 403 | defer     | Possible security/vendor review later            | Product preview and marketing/news; useful context but not stable skill guidance.                     |
|  13 | `Q9MfChRJMMeESe2GBFTnJD` | AI Agents      | Same Simon Willison LLM coding article as #7                    | reject    | Dedupe to #7                                     | Exact duplicate.                                                                                      |
|  14 | `4LEiJ6BLxmHXdzTehGWouW` | AI Agents      | Heise Q\* / OpenAI hype article, 2023-12-01, reachable          | defer     | None                                             | Speculative news; no repeatable agent workflow.                                                       |
|  15 | `Jf7Rc2e1PxJiagPEECB4td` | AI Agents      | Simon Willison MiniMax M2 link post, 2025-10-29                 | defer     | None                                             | Model-release and pricing churn.                                                                      |
|  16 | `RpKSGJZKBTdJiRVHE6cac5` | AI Agents      | NN/g complex apps course page, reachable                        | reject    | Possible UI research elsewhere                   | UX course marketing, not AI Agents.                                                                   |
|  17 | `C5VKLTYvZpi7zqjPzHcWwB` | AI Agents      | Heise GPT Store news, 2024-01-11, reachable                     | defer     | None                                             | Product/news churn.                                                                                   |
|  18 | `7tqRSDoVHc9pq7kQsQWVqq` | AI Agents      | Simon Willison gpt-oss model article, 2025-08-05                | defer     | None                                             | Model-release analysis; not an agent workflow reference.                                              |
|  19 | `YMNd5vorAg5a5ytDrHuCUU` | AI Agents      | Storybook 8 release post, 2024-03-08                            | reject    | Future Storybook/testing cluster                 | Misclassified as AI Agents.                                                                           |
|  20 | `2kzXeJ9mQBRqL9sSWaBADy` | AI Agents      | Piccalilli link on SVG sprite sheets, reachable                 | candidate | `s7n-svg-icons-assets`                           | Misclassified, but strong source for sprite/icon delivery workflow.                                   |
|  21 | `SNLr2zJcERSMLPaDx9Ybbg` | AI Agents      | Heise ChatGPT development background, 2023-03-08, reachable     | defer     | None                                             | Historical/news context, not durable workflow material.                                               |
|  22 | `4gsbJYcqimixCn8c1QFxtE` | Visual Assets  | Josh W. Comeau SVG tutorial, reachable                          | candidate | `s7n-svg-icons-assets`                           | Canonical copy for SVG fundamentals, inline SVG, viewBox, primitives, and CSS/JS control.             |
|  23 | `39Zh3qKNDgcdRjBxSNfXGr` | Visual Assets  | CSS-Tricks blur-up background images, 2015-12-07                | keep      | Existing UI/performance reference                | Durable concept but old implementation context; use as background image loading note, not icon skill. |
|  24 | `Ya4p6mpMcbHQg284vzK93L` | Visual Assets  | Simple Icons GitHub repo, reachable                             | candidate | `s7n-svg-icons-assets`                           | Strong brand-icon source with npm/CDN/API and licensing caveats.                                      |
|  25 | `UCaVjsNAni29P5GXAbyXgb` | Visual Assets  | CSS-Tricks Images in PostCSS, 2016-04-28                        | reject    | None                                             | Old PostCSS image-processing article; too stale and narrow for current skill material.                |
|  26 | `PYxhJXgGc323sQFmAsbvx6` | Visual Assets  | CSS-Tricks SVG icon system, 2017-06-23                          | candidate | `s7n-svg-icons-assets`                           | Good system-level source on SVG icon delivery and tradeoffs, despite age.                             |
|  27 | `RFLZcQheZd1Q6c2QTBHMQT` | Visual Assets  | GitHub Octicons SVG delivery, 2016-02-23, redirected            | candidate | `s7n-svg-icons-assets`                           | Durable migration rationale from icon fonts to SVG; note age/version caveat.                          |
|  28 | `CdRGfJodx35Yo5z8ypsfcX` | Knowledge      | Adactio focus-visible note, 2025-03-26                          | keep      | Existing `s7n-ui-design` accessibility reference | Tiny but practical UI/accessibility note; not a new skill.                                            |
|  29 | `Lu5iweaS9neHVthPqcw41w` | Knowledge      | MDN CookieStore docs, reachable                                 | reject    | None in this pass                                | Web API docs, not connected to the reviewed AI/visual/source-review skill candidates.                 |
|  30 | `38gF2o7eCNHZYoEWkEjMCM` | Knowledge      | Storybook 2023 roadmap, 2023-01-04                              | defer     | Future Storybook/testing cluster                 | Roadmap/product churn; stale for current Storybook guidance.                                          |
|  31 | `QZ1jUa3ZkDh6gzxqSWMFvM` | Knowledge      | Storybook 7 type safety post, 2023-02-08                        | keep      | Future Storybook/testing reference               | Durable CSF/TypeScript idea, but should be checked against current Storybook 10 docs.                 |
|  32 | `Vbyu2TNig2VpdmsvhJcCyF` | Knowledge      | Storybook theme switcher addon URL, 404                         | reject    | None                                             | Dead link.                                                                                            |
|  33 | `PRgS3nnR3gEojuQ66kyojT` | Knowledge      | Smashing Magazine Success at Scale preorder page, 2023-05-25    | reject    | None                                             | Book/product announcement; too indirect for a skill reference.                                        |
|  34 | `8FA4TdvRCtP23boNj8cir5` | Knowledge      | Storybook 10 release post, 2025-10-28                           | keep      | Future Storybook/testing reference               | Current-ish Storybook release context: ESM-only, automocking, CSF factories.                          |
|  35 | `7hPmaKFZJXrhdZ9wuurZCN` | Knowledge      | Storybook 7 beta, 2022-12-16                                    | reject    | None                                             | Old beta announcement superseded by later Storybook releases.                                         |
|  36 | `VbgccuTXoJunvMiyAtAKJJ` | Knowledge      | Storybook 8 beta, 2024-02-06                                    | reject    | None                                             | Beta announcement superseded by Storybook 8/10 release docs.                                          |
|  37 | `J4gWnH6zhLcfrzcEDKZUqM` | Knowledge      | Storybook main config docs, reachable after redirect            | keep      | Future Storybook/testing reference               | Current docs are useful, but belong in a Storybook/tooling cluster.                                   |
|  38 | `E6EAYebqrj5DaUNh9ztnoY` | Knowledge      | Storybook test runner docs URL, 404                             | reject    | None                                             | Stale URL; use current docs path only if opened in a Storybook/testing pass.                          |

## Open Questions

- Should `s7n-agentic-coding-workflows` be created as a Sebastian Software
  skill, or kept as operating notes because it overlaps with existing
  `skill-creator`, `Skill Development`, and `openai-docs` capabilities?
- Should `s7n-svg-icons-assets` split from `s7n-svg-textures`, or should the
  first step be a smaller `s7n-ui-design` reference update for icons, favicons,
  and SVG delivery?
- Should Storybook sources be moved into the Testing/JS Tooling source-review
  pass before any action is taken?

## Things Actions

| Things ID                | Decision  | Final tag                 | Complete? | Reason                                                                                                |
| ------------------------ | --------- | ------------------------- | --------- | ----------------------------------------------------------------------------------------------------- |
| `HYcJnAikVZnZTV5CgLuvxh` | rejected  | `Skill Archive Rejected`  | yes       | Duplicate of #22 and misclassified as AI Agents.                                                      |
| `DLx6dtUvvNku6kAheFKDwn` | deferred  | `Skill Archive Deferred`  | yes       | Heise GPT-4 Turbo article is product/news churn.                                                      |
| `BmogJdzzdNtTyusnTJ1Q8m` | candidate | `Skill Archive Candidate` | yes       | Primary Claude Code docs for agentic coding workflow proposal.                                        |
| `LL3wanC6CZhVDhyoU7M7Vm` | rejected  | `Skill Archive Rejected`  | yes       | Exact duplicate of #3.                                                                                |
| `61RUMT9FQ9SaS2kbVsBXno` | deferred  | `Skill Archive Deferred`  | yes       | Claude Code remote-control feature is product churn unless a remote workflow section is later needed. |
| `GL5jKtGiNcsMHvRmJVk134` | rejected  | `Skill Archive Rejected`  | yes       | JavaScript `Array.sort` explainer, not an AI Agents source.                                           |
| `2s9CgbhTEusPBnW7aQuvuW` | candidate | `Skill Archive Candidate` | yes       | Durable Simon Willison practice article for LLM-assisted coding.                                      |
| `WdF3S4Egk3rDJNUTeiD95N` | candidate | `Skill Archive Candidate` | yes       | Primary OpenAI prompt guidance for narrow agentic workflow reference.                                 |
| `9aJpJAKmPr21rxGQxKvmBx` | candidate | `Skill Archive Candidate` | yes       | Primary Codex app-server docs for product integration workflows.                                      |
| `8JFjCZidLfYGZd1pU2KpiZ` | deferred  | `Skill Archive Deferred`  | yes       | Awesome list is useful discovery material but not authoritative.                                      |
| `VaxkmeooV4gNpm6uQBDSUG` | rejected  | `Skill Archive Rejected`  | yes       | Codex for OSS form is not durable skill/reference material.                                           |
| `UyfbZGhEAhtJibi77LpT5f` | deferred  | `Skill Archive Deferred`  | yes       | Codex Security research preview is product/news churn.                                                |
| `Q9MfChRJMMeESe2GBFTnJD` | rejected  | `Skill Archive Rejected`  | yes       | Exact duplicate of #7.                                                                                |
| `4LEiJ6BLxmHXdzTehGWouW` | deferred  | `Skill Archive Deferred`  | yes       | Speculative Q\* news article, no repeatable workflow value.                                           |
| `Jf7Rc2e1PxJiagPEECB4td` | deferred  | `Skill Archive Deferred`  | yes       | MiniMax M2 article is model-release and pricing churn.                                                |
| `RpKSGJZKBTdJiRVHE6cac5` | rejected  | `Skill Archive Rejected`  | yes       | NN/g course page is UX course marketing, not AI Agents.                                               |
| `C5VKLTYvZpi7zqjPzHcWwB` | deferred  | `Skill Archive Deferred`  | yes       | GPT Store article is product/news churn.                                                              |
| `7tqRSDoVHc9pq7kQsQWVqq` | deferred  | `Skill Archive Deferred`  | yes       | gpt-oss article is model-release analysis, not agent workflow guidance.                               |
| `YMNd5vorAg5a5ytDrHuCUU` | rejected  | `Skill Archive Rejected`  | yes       | Storybook 8 is misclassified as AI Agents.                                                            |
| `2kzXeJ9mQBRqL9sSWaBADy` | candidate | `Skill Archive Candidate` | yes       | SVG sprite-sheet source supports `s7n-svg-icons-assets`.                                              |
| `SNLr2zJcERSMLPaDx9Ybbg` | deferred  | `Skill Archive Deferred`  | yes       | ChatGPT development article is historical/news context.                                               |
| `4gsbJYcqimixCn8c1QFxtE` | candidate | `Skill Archive Candidate` | yes       | Canonical SVG fundamentals source for visual assets.                                                  |
| `39Zh3qKNDgcdRjBxSNfXGr` | candidate | `Skill Archive Candidate` | yes       | Keep as existing UI/performance reference for background image loading.                               |
| `Ya4p6mpMcbHQg284vzK93L` | candidate | `Skill Archive Candidate` | yes       | Simple Icons supports brand SVG asset workflow and licensing notes.                                   |
| `UCaVjsNAni29P5GXAbyXgb` | rejected  | `Skill Archive Rejected`  | yes       | Old PostCSS image-processing article is stale and too narrow.                                         |
| `PYxhJXgGc323sQFmAsbvx6` | candidate | `Skill Archive Candidate` | yes       | CSS-Tricks SVG icon-system article supports icon delivery guidance.                                   |
| `RFLZcQheZd1Q6c2QTBHMQT` | candidate | `Skill Archive Candidate` | yes       | GitHub Octicons post supports icon-font-to-SVG migration rationale.                                   |
| `CdRGfJodx35Yo5z8ypsfcX` | candidate | `Skill Archive Candidate` | yes       | Keep as existing UI accessibility reference for focus-visible styling.                                |
| `Lu5iweaS9neHVthPqcw41w` | rejected  | `Skill Archive Rejected`  | yes       | MDN CookieStore docs do not fit this AI/visual/source-review pass.                                    |
| `38gF2o7eCNHZYoEWkEjMCM` | deferred  | `Skill Archive Deferred`  | yes       | Storybook 2023 roadmap is stale product churn.                                                        |
| `QZ1jUa3ZkDh6gzxqSWMFvM` | candidate | `Skill Archive Candidate` | yes       | Keep for future Storybook/testing reference with current-docs caveat.                                 |
| `Vbyu2TNig2VpdmsvhJcCyF` | rejected  | `Skill Archive Rejected`  | yes       | Storybook theme switcher URL returned 404.                                                            |
| `PRgS3nnR3gEojuQ66kyojT` | rejected  | `Skill Archive Rejected`  | yes       | Smashing book preorder page is too indirect for skill material.                                       |
| `8FA4TdvRCtP23boNj8cir5` | candidate | `Skill Archive Candidate` | yes       | Keep for future Storybook/testing reference.                                                          |
| `7hPmaKFZJXrhdZ9wuurZCN` | rejected  | `Skill Archive Rejected`  | yes       | Old Storybook 7 beta announcement is superseded.                                                      |
| `VbgccuTXoJunvMiyAtAKJJ` | rejected  | `Skill Archive Rejected`  | yes       | Old Storybook 8 beta announcement is superseded.                                                      |
| `J4gWnH6zhLcfrzcEDKZUqM` | candidate | `Skill Archive Candidate` | yes       | Keep current Storybook main-config docs for a future tooling/testing pass.                            |
| `E6EAYebqrj5DaUNh9ztnoY` | rejected  | `Skill Archive Rejected`  | yes       | Storybook test-runner URL returned 404.                                                               |
