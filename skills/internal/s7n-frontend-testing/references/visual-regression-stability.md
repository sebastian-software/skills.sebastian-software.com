# Visual Regression Stability

Visual tests are only useful when the rendering environment is controlled enough that diffs represent product changes, not noise.

## Working Rules

- Prefer component or element screenshots over full-page screenshots unless page composition is the subject.
- Fix viewport, browser, OS/container image, fonts, locale, timezone, data, and motion.
- Disable animations and mask dynamic regions when they are not the subject.
- Set thresholds intentionally and document why they are acceptable.
- Review baseline updates as product/design decisions, not as automatic test maintenance.

## Additional Rules

- Use as Playwright visual-regression workflow example with vendor-bias caveat; prefer Playwright and Vitest docs for exact APIs.
- Use Vitest Browser Mode visual-regression guidance for screenshot stability, masking, thresholds, and animation control.
- Use visual-testing workflow for UI baselines, review loops, and Storybook/Chromatic-backed visual state coverage.
