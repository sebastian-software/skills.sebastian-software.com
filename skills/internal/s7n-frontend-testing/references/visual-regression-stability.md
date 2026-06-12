# Visual Regression Stability

Visual tests are only useful when the rendering environment is controlled enough that diffs represent product changes, not noise.

## Working Rules

- Prefer component or element screenshots over full-page screenshots unless page composition is the subject.
- Fix viewport, browser, OS/container image, fonts, locale, timezone, data, and motion.
- Disable animations and mask dynamic regions when they are not the subject.
- Set thresholds intentionally and document why they are acceptable.
- Review baseline updates as product/design decisions, not as automatic test maintenance.

## Source-Backed Guidance

