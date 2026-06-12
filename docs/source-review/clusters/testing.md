# Cluster Brief: Frontend Testing

## Metadata

| Field | Value |
| --- | --- |
| Things cluster | `Skill: Testing` |
| Reviewed on | 2026-06-10 |
| Reviewer | Codex |
| Write scope | `docs/source-review/clusters/testing.md` only |

## Scope

This cluster covers repeatable frontend testing decisions for agents working in
JavaScript/TypeScript web apps: when to use unit tests, Storybook component
tests, visual regression tests, and Playwright/Cypress-style E2E tests; how to
stabilize browser-based screenshots; and how to wire the checks into CI without
turning every UI change into brittle test maintenance.

The cluster points toward a possible `s7n-frontend-testing` skill, but this file
is only an intermediate review artifact. No skill files were changed.

## Dedupe Summary

- 21 Things tasks reviewed.
- 21 distinct URLs after expanding the multi-URL snapshot-tools task.
- 3 exact duplicate task groups:
  - `DFw6VdPXpwH4vxZKr8EU34`, `R8uUkK7XeGGQ9QvEhPdWHi`
  - `KurSGZy9V8u4BzVbi3phmL`, `Q3mLHe4EuCoNdPqnbtYdzo`
  - `ANkTcBFxPyLjCTDb3LayDz`, `NRTqMTKvuJNCstP85xtQo4`
- 1 original URL is now a hard 404 with a reachable mirror:
  `https://storybook.js.org/blog/storybook-test/`.
- 1 original URL redirects to a current vendor location:
  `https://blog.hichroma.com/introducing-chromatic-ui-testing-for-react-c5cc01a79aaa`.
- 1 original URL is now a hard 404 with no useful current MDN replacement found:
  `https://developer.mozilla.org/en-US/Firefox/Headless_mode`.

## Per-Thing Decisions

| # | Things ID | Title | URL group | Decision | Notes |
| ---: | --- | --- | --- | --- | --- |
| 1 | `DFw6VdPXpwH4vxZKr8EU34` | `@storybook-test: more streamlined and powerful testing` | `storybook-test` | `candidate` | Original Storybook URL is 404; Medium mirror is readable. Useful for `@storybook/test` package consolidation and explicit spy/action patterns, but version-sensitive. |
| 2 | `R8uUkK7XeGGQ9QvEhPdWHi` | `@storybook-test: more streamlined and powerful testing` | `storybook-test` | `candidate` | Exact duplicate of item 1; dedupe under the same source group. |
| 3 | `5VhreUhQbwfsJgC8ZvHSUP` | `Code coverage with Storybook test runner` | `storybook-coverage` | `candidate` | Durable idea: stories as coverage surface. Details mention experimental 2022/2023 tooling, so use as secondary reference. |
| 4 | `QZDSrCD9CX66F1v6wu5wxm` | `Complete guide on Playwright visual regression testing - Lost Pixel` | `lost-pixel-playwright-visual` | `keep` | Practical Playwright visual regression and CI workflow, with caveat that vendor comparisons are biased toward Lost Pixel. |
| 5 | `5yq1bxx85VTJjKvgWikMj4` | `Component Test with Storybook and Vitest` | `storybook-vitest-component-test` | `keep` | Strongest current Storybook source for the component-testing layer: interaction, accessibility, visual tests, coverage, and CI. |
| 6 | `8gEgkCSpcPb9mbkafEUxfA` | `E2E-Testing mit Playwright: Der Weg der Mitte` | `heise-playwright-e2e` | `candidate` | Useful German background on Playwright architecture and Cypress/Selenium comparison; 2022 date makes it historical. |
| 7 | `DTMCSHmbZKTxic9eZTcfDc` | `Firefox Headless mit trivialer Screenshot API` | `mdn-firefox-headless` | `reject` | Original MDN page redirects then 404s. The standalone Firefox screenshot angle is obsolete and not needed for a modern frontend-testing skill. |
| 8 | `KurSGZy9V8u4BzVbi3phmL` | `jest-image-snapshot` | `jest-image-snapshot` | `candidate` | Useful as low-level visual regression tool reference; not enough to drive the skill by itself. |
| 9 | `Q3mLHe4EuCoNdPqnbtYdzo` | `jest-image-snapshot duplicate` | `jest-image-snapshot` | `candidate` | Exact duplicate of item 8; dedupe under the same source group. |
| 10 | `XNcRweYAzmPGAcQZN4ijUi` | `Storybook interaction testing` | `storybook-interaction-testing` | `keep` | Durable concept: stories plus `play` functions as browser-executed component tests with interactive debugging. |
| 11 | `YSZuYHRj88E66L8qWWqm93` | `Vitest 3.2` | `vitest-3-2` | `defer` | Release news. It supports background context on Browser Mode and `projects`, but should not shape the durable skill without checking current Vitest docs. |
| 12 | `Ku9oWS7s6CcZKvJUXwAKNE` | `Jest snapshot tools` | `snapshot-tools` | `candidate` | Multi-URL vendor/tool bundle: Loki, Sauce Visual/Screener, Percy, Chromatic. Useful for vendor/tool review, not for direct implementation guidance. |
| 13 | `ANFaGjt7bZgYFMXy7hkE57` | `Modern frontend testing with Vitest, Storybook, and Playwright` | `defined-modern-frontend-testing` | `keep` | Best stack-level source. Clearly separates unit, component, visual snapshot, E2E, and static analysis responsibilities. |
| 14 | `RaQYW8s5DFcmoWypkrRs3E` | `Playwright Network record/replay` | `playwright-network` | `candidate` | Official docs page is reachable, but the requested record/replay anchor no longer appears. Current content still covers route-based mocking, response handling, and service-worker caveats. |
| 15 | `4sRpKwoh1N8KALAkHpRQ2w` | `Storybook Visual Tests addon beta` | `storybook-visual-addon-beta` | `defer` | Product beta/news post superseded by later stable Storybook visual-testing material. |
| 16 | `X22tAQxZX3Mja2UJ4Wrm4Y` | `Playwright Test generator` | `playwright-codegen` | `keep` | Durable official doc for generating starter E2E tests and locator-first workflows. |
| 17 | `GYeWqswXtuQbm4FKbJeuCn` | `Cypress` | `cypress-homepage` | `candidate` | Relevant vendor surface for Cypress vs Playwright comparison. Homepage is marketing-heavy, so use only for vendor review. |
| 18 | `DwjDaAfMi8Hi6eKr9nPFtT` | `Testing Pipeline 101` | `smashing-testing-pipeline` | `candidate` | Broad CI/CD and frontend pipeline framing; useful background, but less specific than Storybook/Vitest/Playwright sources. |
| 19 | `Cgj2eRVB6hSkje2Gai1Rrw` | `Vitest visual regression` | `vitest-visual-regression` | `keep` | Strong official source for screenshot instability, environment control, thresholds, masking dynamic content, and disabling animations. |
| 20 | `ANkTcBFxPyLjCTDb3LayDz` | `Visual testing Storybook` | `storybook-visual-testing` | `keep` | Strong conceptual source for visual tests as UI snapshot tests, baseline review, and Storybook/Chromatic workflows. |
| 21 | `NRTqMTKvuJNCstP85xtQo4` | `Visual testing Storybook duplicate/tracking URL` | `storybook-visual-testing` | `keep` | Exact duplicate of item 20; dedupe under the same source group. |

## Source Groups

### `storybook-vitest-component-test`

- URL: <https://storybook.js.org/blog/component-test-with-storybook-and-vitest/>
- Source / date: Storybook, Michael Shilman, published and updated 2025-07-29.
- Access: reachable.
- What is behind the link: Storybook 9 component-testing overview built around
  Vitest, with interaction tests, accessibility tests, visual tests, coverage,
  and a test widget/CI workflow.
- Useful ideas:
  - Component tests occupy the middle layer between unit tests and E2E tests.
  - Stories are already UI state fixtures; tests should reuse those states
    instead of duplicating setup.
  - A frontend-testing skill should ask which layer is responsible before
    adding tests.
- Caveats: vendor source from Storybook/Chromatic maintainers; API names and
  Storybook major versions are date-sensitive.

### `defined-modern-frontend-testing`

- URL: <https://www.defined.net/blog/modern-frontend-testing/>
- Source / date: Defined Networking, Ian VanSchooten, 2023-11-09.
- Access: reachable.
- What is behind the link: practical team write-up that separates frontend
  testing into Vitest unit tests, Storybook component tests, Chromatic visual
  snapshots, Playwright E2E tests, and static analysis.
- Useful ideas:
  - Unit tests should cover reusable logic, hooks, and pure code.
  - Storybook should cover components and page-like states with mocked data.
  - Visual snapshots should protect styling and layout regressions where
    assertions are a poor fit.
  - E2E tests should stay small and verify real integration with backend flows.
- Caveats: one team's React product context, but the layer boundaries are
  durable and highly applicable.

### `vitest-visual-regression`

- URL: <https://main.vitest.dev/guide/browser/visual-regression-testing.html>
- Source / date: Vitest documentation, current main docs observed at
  `v5.0.0-beta.4`.
- Access: reachable.
- What is behind the link: official Vitest Browser Mode visual regression
  documentation for `toMatchScreenshot`, screenshot naming, comparator
  thresholds, masking, and animation handling.
- Useful ideas:
  - Visual tests are unstable across machines unless browser, OS, fonts, GPU,
    and headless settings are controlled.
  - Prefer component/element screenshots over full-page screenshots unless the
    page itself is the subject.
  - Mock or mask dynamic content, disable animations, and set mismatch ratios
    intentionally.
- Caveats: main docs may describe beta behavior; validate against the installed
  Vitest version before implementation.

### `storybook-visual-testing`

- URL: <https://storybook.js.org/blog/visual-testing-is-the-greatest-trick-in-ui-development/>
- Source / date: Storybook, Michael Shilman, published 2024-06-20, updated
  2025-11-10.
- Access: reachable.
- What is behind the link: conceptual and workflow argument for visual tests as
  image snapshot tests over Storybook stories, with baseline update/review loops
  and Chromatic-backed Storybook Visual Tests addon.
- Useful ideas:
  - Visual tests can replace brittle UI-detail assertions when the behavior is
    expressed through visible state.
  - Baseline review is a product decision: accept intentional changes, reject
    regressions.
  - Stories plus visual snapshots scale better than hand-coded assertions for
    many visual states.
- Caveats: promotional toward Chromatic; still useful for workflow language.

### `storybook-interaction-testing`

- URL: <https://storybook.js.org/blog/interaction-testing-with-storybook/>
- Source / date: Storybook, Michael Shilman, published 2022-02-23, updated
  2023-06-05.
- Access: reachable.
- What is behind the link: Storybook interaction testing beta article using
  `play` functions, Testing Library queries, assertions, and a browser-backed
  runner.
- Useful ideas:
  - Put test behavior next to the story state where possible.
  - Prefer user-facing queries and interaction steps over implementation
    details.
  - Browser-visible debugging is a major advantage over opaque JSDOM failures.
- Caveats: older API package names have changed; use for concepts, not exact
  imports.

### `lost-pixel-playwright-visual`

- URL: <https://lost-pixel.com/blog/post/playwright-visual-regression-testing>
  redirects to
  <https://www.lost-pixel.com/blog/playwright-visual-regression-testing>.
- Source / date: Lost Pixel blog, date not captured in page excerpt.
- Access: reachable via redirect.
- What is behind the link: hands-on Playwright visual regression tutorial using
  `toHaveScreenshot`, filesystem baselines, GitHub Actions, and comparison with
  a cloud service.
- Useful ideas:
  - Playwright native screenshots are a viable baseline for simple visual tests.
  - CI workflows need explicit snapshot update/review rules.
  - Visual assertions after meaningful interactions can catch state-specific UI
    regressions.
- Caveats: vendor article; compare advice against official Playwright docs.

### `playwright-codegen`

- URL: <https://playwright.dev/docs/codegen>
- Source / date: Playwright official docs, current site observed in 2026.
- Access: reachable.
- What is behind the link: official Test Generator documentation for recording
  user actions, generating locators, and adding visibility/text/value
  assertions.
- Useful ideas:
  - Codegen is best used as a starting point, not as unchecked final test code.
  - Generated locators should prioritize user-visible role/text/test id
    selectors.
  - A skill can instruct agents to simplify and harden generated flows.
- Caveats: generated tests can overfit recorded behavior; require review.

### `playwright-network`

- URL: <https://playwright.dev/docs/network#record-and-replay-requests>
- Source / date: Playwright official docs, current site observed in 2026.
- Access: reachable, but the `record-and-replay-requests` anchor did not expose
  a matching section during review.
- What is behind the link: current network docs for request/response
  observation, route-based mocking, modifying requests/responses, glob matching,
  WebSockets, and service-worker caveats.
- Useful ideas:
  - Prefer Playwright's built-in routing when the test needs network visibility.
  - Service workers can hide requests from Playwright routing; block them or
    adjust the mocking approach.
  - E2E tests can be made more deterministic by controlling network boundaries.
- Caveats: source title in Things does not match the current page content.

### `storybook-coverage`

- URL: <https://storybook.js.org/blog/code-coverage-with-the-storybook-test-runner/>
- Source / date: Storybook, Yann Braga, published 2022-10-26, updated
  2023-05-10.
- Access: reachable.
- What is behind the link: Storybook test runner coverage workflow using
  `@storybook/addon-coverage`, Istanbul instrumentation, `test-storybook
  --coverage`, and `nyc` reports.
- Useful ideas:
  - Coverage can show missing story states and untested branches, not just
    report a vanity percentage.
  - Component-state coverage should guide story additions.
- Caveats: article calls the addon experimental at the time; verify modern
  Storybook coverage commands before use.

### `storybook-test`

- Original URL: <https://storybook.js.org/blog/storybook-test/>
- Mirror opened: <https://medium.com/storybookjs/storybook-test-more-streamlined-and-powerful-testing-f88ffb278872>
- Source / date: Storybook on Medium, Joe, 2023-11-15.
- Access: original Storybook URL returns 404; Medium mirror is reachable.
- What is behind the link: announcement of `@storybook/test`, consolidating
  previous Storybook Jest/Testing Library utilities, with Vitest-powered
  `expect` and spies plus explicit action args.
- Useful ideas:
  - Explicit `fn()` action args make story behavior less dependent on docgen.
  - Story test utilities should be portable across Storybook and external test
    runners.
- Caveats: original canonical link is dead; use only as historical migration
  context.

### `heise-playwright-e2e`

- URL: <https://www.heise.de/hintergrund/E2E-Testing-mit-Playwright-Der-Weg-der-Mitte-7310444.html?wt_mc=rss.red.ho.ho.atom.beitrag.beitrag>
- Source / date: heise online, Rainer Hahnekamp, 2022-10-18.
- Access: reachable.
- What is behind the link: German background article comparing Playwright with
  Cypress and Selenium/WebDriver, explaining Playwright's browser-control
  architecture and developer experience.
- Useful ideas:
  - Playwright's value is a middle path: outside-browser control with better
    reliability and developer tooling than older WebDriver patterns.
  - E2E tool choice affects cross-browser support, flake risk, and debugging.
- Caveats: historical 2022 view; do not use for current feature comparison.

### `jest-image-snapshot`

- URL: <https://github.com/americanexpress/jest-image-snapshot>
- Source / date: GitHub repository, Apache-2.0 license visible.
- Access: reachable.
- What is behind the link: Jest matcher for image comparisons using pixelmatch,
  baseline updates, thresholds, blur/noise handling, and diff layout controls.
- Useful ideas:
  - Good low-level model for visual snapshot mechanics: baseline, actual, diff,
    thresholds, and accepted updates.
  - Useful when a project is Jest-centric and not already using Playwright,
    Vitest Browser Mode, or Storybook visual tooling.
- Caveats: narrower and older than current browser-runner workflows.

### `snapshot-tools`

- URLs:
  - <https://loki.js.org/>
  - <https://screener.io/> redirects to
    <https://saucelabs.com/products/visual-testing>
  - <https://percy.io/>
  - <https://blog.hichroma.com/introducing-chromatic-ui-testing-for-react-c5cc01a79aaa>
    redirects to
    <https://www.chromatic.com/blog/introducing-chromatic---ui-testing-for-react/>
- Access: Loki reachable; Screener redirects to Sauce Visual; Percy returns a
  JS-heavy app shell with title metadata; Chromatic redirect reachable.
- What is behind the links: visual testing vendors/tools for Storybook or
  broader UI snapshot review.
- Useful ideas:
  - Vendor review should compare where baselines live, PR checks, browser/device
    coverage, Storybook integration, CI ergonomics, and pricing/lock-in.
  - Loki is notable for Storybook-focused headless visual regression with Docker
    Chrome as the reproducible path.
- Caveats: vendor pages are marketing-heavy; the old Chromatic launch post is
  historical.

### `smashing-testing-pipeline`

- URL: <https://www.smashingmagazine.com/2022/02/testing-pipeline-101-frontend-testing/>
- Source / date: Smashing Magazine, 2022-02.
- Access: reachable.
- What is behind the link: broad frontend testing pipeline introduction with
  CI/CD terminology and staged automation.
- Useful ideas:
  - Testing advice should connect local checks to CI and release confidence.
  - The skill should include pipeline ordering, not only test APIs.
- Caveats: broad educational piece; not enough implementation specificity for a
  skill reference by itself.

### `vitest-3-2`

- URL: <https://vitest.dev/blog/vitest-3-2.html>
- Source / date: Vitest release blog, 2025-06-02.
- Access: reachable.
- What is behind the link: release notes focused on Browser Mode, TypeScript,
  annotations, scoped fixtures, and deprecating `workspace` in favor of
  `projects`.
- Decision rationale: defer. Useful for version history, but release notes
  should not drive durable guidance without checking current docs.

### `storybook-visual-addon-beta`

- URL: <https://storybook.js.org/blog/visual-tests-addon-beta/>
- Source / date: Storybook, Joe Vaughan, 2024-02-15, updated 2024-03-12.
- Access: reachable.
- What is behind the link: beta announcement for Storybook's Visual Tests addon.
- Decision rationale: defer. Superseded by stable Storybook 8/9 material and
  the later visual-testing article.

### `cypress-homepage`

- URL: <https://www.cypress.io>
- Source / date: Cypress marketing site, current site observed in 2026.
- Access: reachable.
- What is behind the link: product homepage for Cypress App/Cloud with E2E,
  component, visual review, analytics, and AI-assisted authoring claims.
- Decision rationale: candidate for vendor review only. It is not a durable
  implementation source.

### `mdn-firefox-headless`

- URL: <https://developer.mozilla.org/en-US/Firefox/Headless_mode>
- Access: redirects to `/en-US/docs/Mozilla/Firefox/Headless_mode`, then 404.
- What is behind the link: no current MDN content reachable from the provided
  URL.
- Decision rationale: reject. The source is dead and the standalone Firefox
  screenshot API topic is not needed for a modern Storybook/Vitest/Playwright
  testing skill.

## Proposed Outcome

Decision: `new skill`

Target skill or proposed skill name: `s7n-frontend-testing`

Rationale: The kept and candidate sources form a coherent agent workflow:
choose the right testing layer, generate or improve tests, stabilize visual
snapshots, define CI/baseline review, and avoid adding brittle assertions where
Storybook or visual tests would be better.

## Skill Boundary

Use when the user asks to:

- choose or improve a frontend testing strategy for a web app.
- add or review Vitest, Storybook, Playwright, Cypress, or visual regression
  tests.
- decide whether a behavior belongs in unit, component, visual, or E2E tests.
- stabilize screenshot/visual tests by controlling environment, animations,
  dynamic data, thresholds, and baseline update flows.
- wire frontend tests into CI and define PR review expectations.
- turn Playwright codegen output into maintainable tests.

Do not use when:

- the task is backend-only, load testing, security testing, or formal QA process
  design.
- the user only asks to run an existing test command.
- the task is vendor procurement/pricing without implementation implications.
- the project has no browser-facing UI.

## Proposed Structure

```text
skills/s7n-frontend-testing/
├── SKILL.md
├── README.md
├── SOURCE.md
├── references/
│   ├── testing-layer-decision.md
│   ├── storybook-component-testing.md
│   ├── visual-regression-stability.md
│   ├── playwright-e2e-workflows.md
│   ├── ci-and-baseline-review.md
│   └── vendor-tool-notes.md
└── evals/
    ├── choose-testing-layer.md
    ├── harden-playwright-visual-test.md
    ├── storybook-play-function-review.md
    └── ci-baseline-policy.md
```

## Reference Plan

- `references/testing-layer-decision.md` -- decision matrix for unit vs
  component vs visual vs E2E vs static analysis, based primarily on Defined
  Networking and Storybook component-test sources.
- `references/storybook-component-testing.md` -- Storybook stories as state
  fixtures, `play` functions, `@storybook/test`, interaction tests, a11y tests,
  coverage, and current-version caveats.
- `references/visual-regression-stability.md` -- screenshot stability checklist:
  fixed browser/OS/font environment, element-level screenshots, dynamic-content
  masking, animation control, thresholds, and baseline review.
- `references/playwright-e2e-workflows.md` -- Playwright codegen as draft input,
  locator review, network mocking boundaries, service-worker caveats, traces,
  and when E2E should stay small.
- `references/ci-and-baseline-review.md` -- PR/CI flow for test ordering,
  screenshot update rules, artifact review, and scheduled E2E checks.
- `references/vendor-tool-notes.md` -- non-authoritative notes on Chromatic,
  Lost Pixel, Percy, Sauce Visual/Screener, Loki, Cypress, and
  jest-image-snapshot.

## Eval Ideas

- Prompt: "This React app has Vitest unit tests and Playwright E2E tests, but
  every CSS refactor breaks production. Propose what tests to add."
  Expected behavior: recommends Storybook state coverage plus visual regression,
  not more brittle DOM assertions.
- Prompt: "Use Playwright codegen output to create a maintainable checkout
  smoke test."
  Expected behavior: treats generated code as a draft, improves locators,
  removes incidental waits, scopes assertions to the user goal, and keeps the
  flow small.
- Prompt: "A visual regression test flakes across macOS laptops and Linux CI."
  Expected behavior: diagnoses environment and dynamic rendering differences,
  recommends stable browser/container/font setup, masking, disabled animations,
  and intentional thresholds.
- Prompt: "Where should I test a modal's empty, error, loading, and success
  states?"
  Expected behavior: puts state matrix in Storybook component tests, uses unit
  tests only for pure logic, and reserves E2E for one integrated user path.

## Open Questions

- Should the proposed skill be general frontend testing, or should visual
  regression become a separate narrower skill?
- Should vendor notes live in `SOURCE.md`, `references/vendor-tool-notes.md`, or
  a separate vendor-review artifact?
- Should current official docs for Storybook 9, Vitest 4/5, and Playwright be
  re-checked immediately before any skill implementation?
- Should Things tags be updated manually after this review, or should tag updates
  wait until a skill proposal is approved?

## Things Actions

| Things ID | Decision | Final tag | Complete? | Reason |
| --- | --- | --- | --- | --- |
| `DFw6VdPXpwH4vxZKr8EU34` | candidate | `Skill Archive Candidate` | yes | Original Storybook URL is 404, but reachable Medium mirror documents useful `@storybook/test` migration context. |
| `R8uUkK7XeGGQ9QvEhPdWHi` | candidate | `Skill Archive Candidate` | yes | Exact duplicate of `DFw6VdPXpwH4vxZKr8EU34`; duplicate reason documented in the brief. |
| `5VhreUhQbwfsJgC8ZvHSUP` | candidate | `Skill Archive Candidate` | yes | Storybook coverage workflow is useful as secondary, version-sensitive reference. |
| `QZDSrCD9CX66F1v6wu5wxm` | candidate | `Skill Archive Candidate` | yes | Practical Playwright visual regression and CI workflow source. |
| `5yq1bxx85VTJjKvgWikMj4` | candidate | `Skill Archive Candidate` | yes | Primary current source for Storybook/Vitest component-testing layer. |
| `8gEgkCSpcPb9mbkafEUxfA` | candidate | `Skill Archive Candidate` | yes | Historical Playwright E2E architecture and Cypress/Selenium comparison source. |
| `DTMCSHmbZKTxic9eZTcfDc` | rejected | `Skill Archive Rejected` | yes | MDN page redirects to 404 and the standalone Firefox screenshot topic is stale for this skill. |
| `KurSGZy9V8u4BzVbi3phmL` | candidate | `Skill Archive Candidate` | yes | Low-level visual snapshot matcher reference. |
| `Q3mLHe4EuCoNdPqnbtYdzo` | candidate | `Skill Archive Candidate` | yes | Exact duplicate of `KurSGZy9V8u4BzVbi3phmL`; duplicate reason documented in the brief. |
| `XNcRweYAzmPGAcQZN4ijUi` | candidate | `Skill Archive Candidate` | yes | Durable Storybook interaction-testing concept source. |
| `YSZuYHRj88E66L8qWWqm93` | deferred | `Skill Archive Deferred` | yes | Vitest release news; useful only after checking current docs. |
| `Ku9oWS7s6CcZKvJUXwAKNE` | candidate | `Skill Archive Candidate` | yes | Multi-URL vendor/tool bundle for visual testing vendor review. |
| `ANFaGjt7bZgYFMXy7hkE57` | candidate | `Skill Archive Candidate` | yes | Primary stack-level source for unit, component, visual, E2E, and static-analysis boundaries. |
| `RaQYW8s5DFcmoWypkrRs3E` | candidate | `Skill Archive Candidate` | yes | Official Playwright network docs are useful, though the requested record/replay anchor no longer matches. |
| `4sRpKwoh1N8KALAkHpRQ2w` | deferred | `Skill Archive Deferred` | yes | Storybook Visual Tests beta post is superseded by later stable material. |
| `X22tAQxZX3Mja2UJ4Wrm4Y` | candidate | `Skill Archive Candidate` | yes | Official Playwright codegen source for generated-test draft workflows. |
| `GYeWqswXtuQbm4FKbJeuCn` | candidate | `Skill Archive Candidate` | yes | Cypress homepage is relevant only as vendor-review context. |
| `DwjDaAfMi8Hi6eKr9nPFtT` | candidate | `Skill Archive Candidate` | yes | Broad frontend testing pipeline and CI/CD framing source. |
| `Cgj2eRVB6hSkje2Gai1Rrw` | candidate | `Skill Archive Candidate` | yes | Primary official Vitest visual regression stability source. |
| `ANkTcBFxPyLjCTDb3LayDz` | candidate | `Skill Archive Candidate` | yes | Primary Storybook visual-testing workflow source. |
| `NRTqMTKvuJNCstP85xtQo4` | candidate | `Skill Archive Candidate` | yes | Exact duplicate of `ANkTcBFxPyLjCTDb3LayDz`; duplicate reason documented in the brief. |
