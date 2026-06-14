# CI and Baseline Review

CI should make frontend regressions visible without making every visual change painful.

## Working Rules

- Run fast deterministic checks before slower browser suites.
- Keep visual baseline updates explicit and reviewed in PRs.
- Store artifacts so reviewers can inspect actual, expected, and diff output.
- Separate scheduled broad checks from required smoke checks when full coverage is expensive or flaky.
- Document who can approve baseline changes and what evidence is required.

## CI Ordering

Use a layered order so failures are cheap to understand:

1. Formatting, linting, type checking, and static accessibility rules.
2. Unit tests and deterministic component tests.
3. Browser component tests or Storybook interaction tests.
4. Required Playwright smoke paths for critical user journeys.
5. Visual regression on selected stable states.
6. Scheduled or manual broad browser/device sweeps.

Do not make the slowest, broadest browser matrix the first signal developers see.

## Required vs Scheduled

- Required PR checks should be fast, deterministic, and tied to high-value risk.
- Scheduled checks can cover extra browsers, locales, themes, devices, and long flows.
- Expensive visual matrices should run only on touched areas, selected story tags, or scheduled review unless the project has the infrastructure to keep them fast.
- Upload traces, videos, screenshots, console logs, and network logs for browser failures.

## Baseline Review Policy

Define:

- where visual baselines are stored,
- who can approve baseline changes,
- what evidence reviewers need,
- how to regenerate baselines locally,
- when a baseline update requires design approval,
- how to handle browser/font/toolchain version changes.

Reject baseline updates that bundle unrelated visual drift with feature work.
