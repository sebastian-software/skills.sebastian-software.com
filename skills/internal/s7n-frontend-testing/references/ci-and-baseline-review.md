# CI and Baseline Review

CI should make frontend regressions visible without making every visual change painful.

## Working Rules

- Run fast deterministic checks before slower browser suites.
- Keep visual baseline updates explicit and reviewed in PRs.
- Store artifacts so reviewers can inspect actual, expected, and diff output.
- Separate scheduled broad checks from required smoke checks when full coverage is expensive or flaky.
- Document who can approve baseline changes and what evidence is required.

## Source-Backed Guidance

