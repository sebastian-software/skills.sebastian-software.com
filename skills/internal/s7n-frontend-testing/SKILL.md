---
name: s7n-frontend-testing
description: |
  This skill should be used when the user asks to "add frontend tests", "choose a frontend testing strategy", "set up visual regression", "write Playwright tests", "test Storybook states", "use Vitest Browser Mode", "fix flaky screenshot tests", "review UI tests", or "wire frontend tests into CI". It covers unit, component, browser, visual regression, E2E, Storybook, Playwright, Vitest, and CI baseline review workflows.
license: MIT
metadata:
  author: sebastian-software
  version: "1.0"
---

# S7N Frontend Testing

Use this skill to choose, implement, or review frontend tests for browser-facing applications.

## Workflow

1. Inspect the project stack: framework, package manager, existing test runners, Storybook, browser automation, CI, and current scripts.
2. Choose the narrowest useful test layer:
   - pure logic: unit test,
   - component state or interaction: Storybook/Vitest/component test,
   - visible UI drift: visual regression,
   - integrated route or workflow: Playwright-style E2E,
   - static guarantees: linting, type checking, accessibility checks.
3. Reuse existing fixtures and stories before inventing parallel setup.
4. Stabilize browser tests before adding baselines: fixed viewport, deterministic data, mocked time/randomness, loaded fonts, disabled animations, and masked dynamic regions.
5. Treat generated tests as drafts. Review locators, assertions, waits, and scope before committing.
6. Make baseline updates explicit, reviewed, and tied to an intentional UI change.

## Reference Files

- [references/testing-layer-decision.md](references/testing-layer-decision.md) - Choose unit, component, visual, E2E, or static checks.
- [references/storybook-component-testing.md](references/storybook-component-testing.md) - Use stories as component state fixtures.
- [references/visual-regression-stability.md](references/visual-regression-stability.md) - Stabilize screenshots and visual baselines.
- [references/playwright-e2e-workflows.md](references/playwright-e2e-workflows.md) - Keep Playwright tests user-centered and maintainable.
- [references/ci-and-baseline-review.md](references/ci-and-baseline-review.md) - Define CI ordering and baseline update review.
- [references/vendor-tool-notes.md](references/vendor-tool-notes.md) - Treat vendor tools as implementation options, not defaults.

## Boundaries

Do not use this skill for backend-only tests, load tests, security testing, vendor procurement, or simply running an existing test command without changing or interpreting the test strategy.

