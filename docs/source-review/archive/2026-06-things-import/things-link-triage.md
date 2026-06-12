# Things Link Triage

Working notes for reviewing links collected in Things and deciding whether they
belong in the Sebastian Software skills archive.

This file is the early triage log. The durable review workflow now lives in
[`docs/source-review/README.md`](source-review/README.md). Do not update skills
directly from this file; turn sources into source cards or cluster briefs first.

## Scope

Source: local Things database, open and non-trashed tasks only.

- Open Things with `http`: 5,639 tasks
- Deduplicated open URLs: 5,325
- First pass classification is heuristic and should be treated as an intake
  queue, not a final judgment.

## Decision Model

Classify each source into one of these outcomes:

1. **Add to existing skill reference** -- the source strengthens a skill that
   already exists.
2. **Create first-party skill** -- the source cluster supports a repeatable
   workflow with clear trigger phrases, success criteria, and enough reference
   material.
3. **Vendor external skill** -- the source is an actual skill repository or
   reusable skill package that passes the external-skill review checklist.
4. **Defer** -- interesting, but too narrow, too volatile, or not enough
   evidence for a skill.
5. **Discard** -- personal shopping, expired news, low-authority, duplicate, or
   already covered.

## Broad Topic Counts

Best-effort category counts from the first pass:

| Category                          | Open URLs |
| --------------------------------- | --------: |
| Frontend UI / CSS                 |     2,817 |
| JavaScript / TypeScript tooling   |       737 |
| AI / LLM / agents                 |       722 |
| Testing / quality                 |       229 |
| Product / marketing / growth      |       145 |
| Home / shopping / personal noise  |       135 |
| Writing / knowledge / learning    |       133 |
| Visual media / print / SVG        |        96 |
| macOS / productivity / automation |        86 |
| Web platform / performance / SEO  |        83 |
| Backend / data / cloud            |        83 |
| Security / privacy                |        37 |
| Business / operations / freelance |        22 |

## Candidate Skill Areas

### Strong Candidates

**`s7n-frontend-testing`**

Why: enough links around Vitest browser mode, Playwright, visual regression,
Storybook test runner, Chromatic, Percy, Loki, Lost Pixel, and snapshot tooling.
This is a good first-party skill candidate because it can encode a repeatable
workflow: pick test type, wire tooling, run local browser verification, compare
screenshots, and report failures.

Initial Things sources:

- <https://main.vitest.dev/guide/browser/visual-regression-testing.html>
- <https://github.com/vitest-dev/vitest/discussions/5828>
- <https://www.smashingmagazine.com/2022/02/testing-pipeline-101-frontend-testing/>
- <https://lost-pixel.com/blog/post/playwright-visual-regression-testing>
- <https://github.com/americanexpress/jest-image-snapshot>

**`s7n-web-platform-performance`**

Why: performance and web-platform work is only partially covered by SEO and UI
references. A skill could cover images, LCP, preload scanner, Server-Timing,
HTTP caching, headers, and Core Web Vitals as implementation guidance.

Initial Things sources:

- <https://web.dev/learn/images/>
- <https://www.smashingmagazine.com/2023/01/optimizing-image-element-lcp/>
- <https://web.dev/preload-scanner/>
- <https://www.smashingmagazine.com/2022/05/rethinking-server-timing-monitoring-tool/>
- <https://developer.chrome.com/blog/web-vitals-extension>

**`s7n-agent-workflows`**

Why: there are many AI/agent links. This should become a skill only if it can be
made operational, for example: subagent design, tool-use policy, prompt
benchmarks, Codex/GitHub workflows, and skill authoring conventions. Avoid
turning news links into reference material.

Initial Things sources:

- <https://github.com/VoltAgent/awesome-claude-code-subagents>
- <https://openai.com/index/codex-security-now-in-research-preview/>
- <https://openai.com/form/codex-for-oss/>

### Medium Candidates

**`s7n-svg-icons-assets`**

Could split from `s7n-svg-textures` because icon systems, sprites, favicons, and
brand icon assets are a different workflow from SVG filters and texture
generation.

Initial Things sources:

- <https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/>
- <https://css-tricks.com/pretty-good-svg-icon-system/>
- <https://github.com/simple-icons/simple-icons>
- <https://pawelgrzybek.com/svg-favicons-that-respect-theme-preference/>

**`s7n-security-auth`**

Could cover passkeys, OAuth, secure headers, and frontend/backend auth
implementation checks. Needs more current primary documentation before becoming
a skill.

Initial Things sources:

- <https://www.smashingmagazine.com/2023/10/passkeys-explainer-future-password-less-authentication/>
- <https://css-tricks.com/passkeys-what-the-heck-and-why/>
- <https://stackoverflow.blog/2022/04/11/the-complete-guide-to-protecting-your-apis-with-oauth2/>
- <https://www.smashingmagazine.com/2017/04/secure-web-app-http-headers/>

**`s7n-backend-edge-serverless`**

Potentially useful, but the current source set is mixed: serverless, edge
runtime, distributed SQLite, Cloudflare Workers, Vercel Functions, and API
protection. Needs clustering before deciding whether this is one skill or
several smaller references.

## Round 1 Reviewed: Modern CSS / UI / Print

These sources are worth keeping, but most should update existing references
rather than create new skills.

| Source                                                                                  | Decision                              | Target                                                                                                      |
| --------------------------------------------------------------------------------------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| <https://frontendmasters.com/blog/what-you-need-to-know-about-modern-css-2025-edition/> | Keep as modern CSS change radar       | `s7n-ui-design`, likely a new `references/23-modern-css-platform.md` or updates across layout/forms/dialogs |
| <https://developer.chrome.com/blog/new-in-web-ui-io-2025-recap?hl=en>                   | Keep                                  | `s7n-ui-design`, modern native UI controls and declarative web platform                                     |
| <https://developer.chrome.com/blog/view-transitions-in-2025?hl=en>                      | Keep                                  | `s7n-ui-design`, motion/page transition guidance                                                            |
| <https://ishadeed.com/article/modern-css-section-layout/>                               | Keep                                  | `s7n-ui-design/references/04-layout-spacing.md`                                                             |
| <https://www.joshwcomeau.com/css/subgrid/>                                              | Keep                                  | `s7n-ui-design/references/04-layout-spacing.md`                                                             |
| <https://developer.chrome.com/blog/a-customizable-select?hl=en>                         | Keep                                  | `s7n-ui-design/references/08-forms.md`                                                                      |
| <https://ishadeed.com/article/field-sizing/>                                            | Keep                                  | `s7n-ui-design/references/08-forms.md`                                                                      |
| <https://piccalil.li/blog/styling-tables-the-modern-css-way/>                           | Keep                                  | `s7n-ui-design/references/12-tables-data.md`                                                                |
| <https://piccalil.li/blog/printing-the-web-making-webpages-look-good-on-paper/>         | Keep                                  | `s7n-print-design/references/layout.md` and maybe `s7n-ui-design/references/18-print-styles.md`             |
| <https://css-tricks.com/there-is-no-need-to-trap-focus-on-a-dialog-element/>            | Already covered                       | `s7n-ui-design/references/11-dialog-modal.md` already contains this principle                               |
| <https://piccalil.li/blog/a-pragmatic-guide-to-modern-css-colours-part-two/>            | Keep if color reference needs refresh | `s7n-ui-design/references/03-colour.md`                                                                     |

## Next Review Queue

Recommended order:

1. Testing / quality cluster -- likely highest-value new skill.
2. Web platform performance cluster -- likely new skill or expanded UI/SEO
   reference.
3. AI / agents cluster -- high volume, but needs strict filtering for evergreen
   workflows vs expired news.
4. SVG icons/assets cluster -- decide whether to split from `s7n-svg-textures`.
5. Security/auth cluster -- only after collecting primary docs.

## Round 2 Reviewed: Frontend Testing / Visual Regression

Decision: **create a first-party `s7n-frontend-testing` skill**.

Reasoning: the existing vendored `antfu-vitest` skill is useful for Vitest API
details, but this cluster needs a broader agent workflow: choose the right test
level, wire the correct tool, stabilize browser output, run local/CI checks,
interpret visual diffs, and explain whether a failure is behavioral,
accessibility, rendering, or baseline drift.

### Proposed Skill Shape

```text
skills/internal/s7n-frontend-testing/
├── SKILL.md
├── README.md
├── references/
│   ├── test-strategy.md
│   ├── vitest-browser-mode.md
│   ├── playwright-visual-regression.md
│   ├── storybook-testing.md
│   ├── ci-and-baselines.md
│   └── flake-control.md
└── evals/
    └── evals.json
```

### Trigger Scope

Use the skill when the user asks to:

- add or fix frontend tests,
- verify UI changes in a browser,
- add screenshot or visual regression tests,
- debug flaky Playwright/Vitest/Storybook tests,
- configure CI for frontend quality checks,
- decide between unit, component, browser, accessibility, and visual tests.

### Initial Source Decisions

| Source                                                                            | Decision                       | Notes                                                                                                                                                                   |
| --------------------------------------------------------------------------------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <https://vitest.dev/guide/browser/visual-regression-testing.html>                 | Primary reference              | Current Vitest docs cover `toMatchScreenshot`, environment stability, baseline screenshots, update workflow, thresholds, viewports, dynamic content, and CI separation. |
| <https://playwright.dev/docs/test-snapshots>                                      | Primary reference              | Use for Playwright-native visual comparison, `toHaveScreenshot`, `maxDiffPixels`, and deterministic stylesheet masking.                                                 |
| <https://storybook.js.org/docs/writing-tests/integrations/test-runner>            | Primary reference with caution | Storybook now recommends the Vitest addon for Vite-powered Storybooks; keep legacy test-runner guidance only for existing setups.                                       |
| <https://www.smashingmagazine.com/2022/02/testing-pipeline-101-frontend-testing/> | Secondary conceptual source    | Useful for test-pyramid framing, but not enough alone for implementation detail.                                                                                        |
| <https://github.com/americanexpress/jest-image-snapshot>                          | Defer                          | Useful historically, but less central if the new skill defaults to Vitest/Playwright.                                                                                   |
| <https://lost-pixel.com/blog/post/playwright-visual-regression-testing>           | Defer                          | Product-specific; revisit only if the skill includes hosted visual review services.                                                                                     |
| <https://percy.io/> / <https://www.chromatic.com/> / <https://loki.js.org/>       | Defer                          | Treat as vendor options, not core workflow, unless a project already uses them.                                                                                         |

### Skill Workflow Draft

1. Inspect the project stack: framework, test runner, Storybook, package
   manager, CI provider, browser automation already installed.
2. Pick the narrowest useful test:
   - pure logic: Vitest unit test,
   - component behavior: Vitest Browser Mode or Testing Library,
   - route/user workflow: Playwright,
   - component catalog coverage: Storybook Vitest addon or test-runner,
   - visual drift: Playwright/Vitest screenshot comparison.
3. Stabilize the environment before adding visual baselines:
   fixed viewport, deterministic data, mocked time/randomness, animations
   disabled, fonts loaded, dynamic regions masked.
4. Keep visual tests isolated from normal unit tests and run them in CI where
   the browser/font/rendering environment is stable.
5. Require baseline review: screenshot updates should be explicit, reviewed,
   and committed intentionally.
6. Report failures by type: code regression, design-intent change, unstable
   fixture, browser/environment drift, or bad threshold.

### Open Questions Before Implementing

- Should `s7n-frontend-testing` depend on the vendored `antfu-vitest` skill by
  reference, or duplicate the small amount of Vitest Browser Mode guidance it
  needs?
- Should the default visual workflow be Playwright-first, Vitest-first, or
  project-detected?
- Should screenshot artifacts be stored through Git LFS by default, or only
  recommended once the suite grows?

## Round 3 Reviewed: Web Platform Performance

Decision: **create a first-party `s7n-web-performance` skill**, separate from
marketing SEO skills.

Reasoning: the source cluster is implementation-heavy. It should guide an agent
through measuring, diagnosing, and fixing performance regressions in an actual
frontend codebase. The existing `marketingskills-seo-audit` skill can identify
SEO and metadata issues, but it should not become the home for Core Web Vitals,
LCP image selection, preload scanner behavior, server timing, and DevTools
diagnosis.

### Proposed Skill Shape

```text
skills/internal/s7n-web-performance/
├── SKILL.md
├── README.md
├── references/
│   ├── measurement-workflow.md
│   ├── core-web-vitals.md
│   ├── lcp-images.md
│   ├── resource-discovery.md
│   ├── fonts-and-css.md
│   ├── server-timing.md
│   └── ci-budgets.md
└── evals/
    └── evals.json
```

### Trigger Scope

Use the skill when the user asks to:

- improve Core Web Vitals, Lighthouse, PageSpeed, or WebPageTest results,
- diagnose slow initial render, LCP, CLS, or INP,
- optimize responsive images, font loading, CSS delivery, or preload hints,
- set performance budgets or CI checks,
- inspect network waterfalls or Chrome Performance traces,
- explain why a page is slow after a framework/build change.

### Initial Source Decisions

| Source                                                                               | Decision                               | Notes                                                                                                                                            |
| ------------------------------------------------------------------------------------ | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| <https://web.dev/articles/vitals>                                                    | Primary reference                      | Core Web Vitals currently focus on LCP, INP, and CLS with 75th percentile measurement across mobile and desktop.                                 |
| <https://web.dev/learn/images/>                                                      | Primary reference                      | Good canonical course for image formats, responsive images, compression/encoding, CDNs, and delivery tradeoffs.                                  |
| <https://www.smashingmagazine.com/2023/01/optimizing-image-element-lcp/>             | Keep as secondary implementation guide | Practical explanation of `srcset`, `sizes`, and LCP image behavior. Pair with web.dev primary docs.                                              |
| <https://web.dev/articles/preload-scanner>                                           | Primary reference                      | Strong candidate for `resource-discovery.md`; covers how markup, lazy loading, CSS backgrounds, inlining, and client-rendering affect discovery. |
| <https://developer.chrome.com/blog/web-vitals-extension>                             | Primary reference for tooling status   | Important because the standalone Web Vitals extension ended support in 2025 and DevTools Performance panel is now the recommended path.          |
| <https://developer.chrome.com/docs/lighthouse/overview/>                             | Primary reference                      | Use for Lighthouse role and limits, not as the only performance signal.                                                                          |
| <https://www.smashingmagazine.com/2022/05/rethinking-server-timing-monitoring-tool/> | Keep as secondary source               | Useful for Server-Timing concepts; should be backed by MDN/spec docs before implementation.                                                      |

### Skill Workflow Draft

1. Establish measurement context: local vs lab vs field data, URL/page type,
   device class, network profile, current metric targets, and whether the
   problem is LCP, INP, CLS, or total load.
2. Collect evidence before editing: Lighthouse/PageSpeed/WebPageTest output,
   Chrome Performance panel trace, network waterfall, bundle stats, and route
   code path.
3. Diagnose by metric:
   - LCP: TTFB, resource load delay, resource load time, element render delay,
     image markup, preload discoverability, font/CSS blocking.
   - INP: long tasks, hydration, event handlers, main-thread work, third-party
     scripts.
   - CLS: missing dimensions, late-loading embeds, font swaps, injected UI.
4. Fix the highest-leverage bottleneck first; avoid cosmetic micro-optimizations
   before proving they affect the target metric.
5. Verify with the same measurement setup and record before/after numbers.
6. For persistent projects, add performance budgets or CI checks only after a
   stable measurement baseline exists.

### Open Questions Before Implementing

- Should this skill own all image optimization guidance, or should UI/print
  skills keep their local image sections and link to this skill for performance
  depth?
- Should it include framework-specific references for Next.js, Astro, Vite, and
  React hydration, or keep framework guidance in separate files loaded only when
  detected?
- Should Lighthouse CI be a default recommendation, or only when a repo already
  has CI and stable deploy previews?

## Round 4 Reviewed: AI / Agents / Codex

Decision: **do not create a broad AI news or prompting skill from this cluster
yet**. Keep a narrower candidate: **`s7n-agentic-coding-workflows`**.

Reasoning: many Things links are news, commentary, product announcements, or
tool directories. Those are useful reading, but poor skill material because they
age quickly and do not define a reusable workflow. The durable part is how to
structure agentic coding work: task decomposition, subagents, skills, repo
instructions, MCP/tools, evaluation loops, security boundaries, and review
handoffs.

### Proposed Narrow Skill Shape

```text
skills/internal/s7n-agentic-coding-workflows/
├── SKILL.md
├── README.md
├── references/
│   ├── task-decomposition.md
│   ├── subagents.md
│   ├── skills-and-references.md
│   ├── eval-and-repair-loops.md
│   ├── tool-boundaries.md
│   └── security-review.md
└── evals/
    └── evals.json
```

### Trigger Scope

Use the skill when the user asks to:

- structure complex work across multiple agents or subagents,
- decide whether knowledge belongs in a prompt, `AGENTS.md`, skill, plugin,
  MCP server, hook, or automation,
- build a repeatable Codex/agent workflow for a codebase,
- design an evaluation or repair loop for agent-generated changes,
- reduce unsafe or noisy agent behavior around tools, files, or external data.

### Initial Source Decisions

| Source                                                                 | Decision                  | Notes                                                                        |
| ---------------------------------------------------------------------- | ------------------------- | ---------------------------------------------------------------------------- |
| <https://developers.openai.com/codex/skills>                           | Primary reference         | Relevant to skill packaging and when reusable workflows belong in skills.    |
| <https://developers.openai.com/codex/subagents>                        | Primary reference         | Relevant if the skill covers delegating work to subagents.                   |
| <https://developers.openai.com/codex/workflows>                        | Primary reference         | Relevant to task handoff and structured Codex workflows.                     |
| <https://developers.openai.com/codex/app-server>                       | Primary reference, narrow | Relevant only for automation/server integration, not general agent workflow. |
| <https://developers.openai.com/api/docs/guides/prompt-guidance>        | Primary reference, narrow | Use for prompt mechanics, but avoid making "prompting" the whole skill.      |
| <https://github.com/VoltAgent/awesome-claude-code-subagents>           | Defer                     | Useful discovery list, but not authoritative enough as core guidance.        |
| <https://www.understandingai.org/p/what-i-learned-trying-seven-coding> | Defer                     | Useful perspective; not implementation reference.                            |
| <https://simonwillison.net/2025/Dec/15/porting-justhtml/>              | Defer                     | Potential case study for agentic coding, but not general enough alone.       |
| Heise/OpenAI/ChatGPT news links                                        | Discard for skill archive | News links age quickly and should not become embedded reference material.    |

### Skill Workflow Draft

1. Identify whether the problem needs better instructions, better tools, better
   decomposition, better verification, or better review.
2. Choose the smallest durable surface:
   prompt/thread for one-off context, `AGENTS.md` for repo conventions, skill
   for reusable workflow, plugin for bundled capabilities, MCP for live data or
   actions, hook for enforcement, automation for scheduled work.
3. Split multi-agent work only where parallelism or specialization helps; avoid
   subagents for tasks that mainly require shared local context.
4. Require a verification loop: expected outputs, tests/checks, review criteria,
   and failure recovery.
5. Capture learnings into the archive only when they are repeatable and
   source-backed.

### Open Questions Before Implementing

- Is this too close to the existing `skill-creator` and `Skill Development`
  skills, or does it cover a broader "how to run agentic coding work" layer?
- Should it be first-party Sebastian Software guidance, or should it remain
  personal operating notes outside the shared skill archive?
- Should OpenAI/Codex-specific content live in this skill, or should this skill
  link out to the existing `openai-docs` skill for all product-specific facts?
