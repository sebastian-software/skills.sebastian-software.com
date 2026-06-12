# Visual Regression Stability

Visual tests are only useful when the rendering environment is controlled enough that diffs represent product changes, not noise.

## Working Rules

- Prefer component or element screenshots over full-page screenshots unless page composition is the subject.
- Fix viewport, browser, OS/container image, fonts, locale, timezone, data, and motion.
- Disable animations and mask dynamic regions when they are not the subject.
- Set thresholds intentionally and document why they are acceptable.
- Review baseline updates as product/design decisions, not as automatic test maintenance.

## Source-Backed Guidance
### Complete guide on Playwright visual regression testing - Lost Pixel

- Things ID(s): `QZDSrCD9CX66F1v6wu5wxm`
- Source: <https://lost-pixel.com/blog/post/playwright-visual-regression-testing>
- Decision: `secondary`
- Target: `frontend-testing/visual`
- URL recheck: 2026-06-13, HTTP 200, redirects to https://www.lost-pixel.com/blog/playwright-visual-regression-testing
- Guidance: Use as Playwright visual-regression workflow example with vendor-bias caveat; prefer official Playwright and Vitest docs for exact APIs.

