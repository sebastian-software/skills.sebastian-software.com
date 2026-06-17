# CI and Baseline Review

CI should make frontend regressions visible without making every legitimate visual change
painful to land. Order stages by cost, keep the required gate fast and reliable, and make
baseline changes a reviewed decision rather than a silent overwrite.

## Stage ordering

- Run the cheapest, most deterministic checks first and fail fast: type checking, lint
  (including `jsx-a11y`), and unit tests before any browser is launched. Most defects die
  here in seconds.
- Run component/Storybook and visual tests next, then E2E last. Do not start a multi-minute
  browser suite when a type error would have failed the build immediately.
- Cache dependencies and browser binaries, and shard browser/E2E suites across parallel
  runners so wall-clock time stays bounded as the suite grows.

## Determinism in CI

- Run visual and E2E tests in a pinned container image so font rendering and engine versions
  match the baseline environment exactly; never compare against baselines made on a laptop.
- Quarantine, fix, or delete a flaky test the same day it is spotted — a known-flaky required
  check trains reviewers to ignore red, which is worse than no check.
- Separate broad, expensive, or occasionally flaky coverage into a scheduled (nightly) run from
  the required per-PR smoke checks, so the merge gate stays fast and trustworthy.

## Baseline and artifact review

- Keep visual baseline images in version control and require their updates to appear as an
  explicit, reviewable diff in the PR — never auto-commit new baselines from CI.
- Store actual, expected, and diff images (and Playwright traces) as build artifacts on
  failure, so a reviewer can judge a regression without reproducing it locally.
- Block any baseline change that is not paired with the intentional UI change that caused it;
  a baseline diff in an unrelated PR is a red flag.
- Document who may approve baseline updates and what evidence is required (linked design change,
  before/after images), and enforce it through code review.

## Review checklist

- Do static checks and unit tests run before browser suites and fail fast?
- Are visual/E2E runs pinned to a container image matching the baselines?
- Are baselines version-controlled and updated only via reviewed PR diffs?
- Are diff images and traces retained as artifacts for failed runs?
- Is flaky coverage moved off the required gate and into a scheduled run?
- Is baseline approval ownership documented and enforced?
