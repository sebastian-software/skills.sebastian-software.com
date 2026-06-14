# Visual Regression Stability

Visual tests are only useful when the rendering environment is controlled enough that diffs represent product changes, not noise.

## Working Rules

- Prefer component or element screenshots over full-page screenshots unless page composition is the subject.
- Fix viewport, browser, OS/container image, fonts, locale, timezone, data, and motion.
- Disable animations and mask dynamic regions when they are not the subject.
- Set thresholds intentionally and document why they are acceptable.
- Review baseline updates as product/design decisions, not as automatic test maintenance.

## Stabilization Checklist

- Use deterministic fixtures: fixed dates, seeded randomness, stable IDs, predictable network responses, and known auth state.
- Load the same fonts in local and CI, or use a stable CI font stack.
- Freeze or remove animations, transitions, caret blinking, video, canvas noise, live clocks, skeleton shimmer, and rotating content unless they are the subject of the test.
- Mask dynamic user-generated content, ads, maps, analytics banners, and third-party embeds.
- Capture the smallest useful region: component, dialog, table row, or viewport section before whole-page screenshots.
- Run at named viewports that reflect layout decisions, not arbitrary device marketing names.
- Keep dark mode, high contrast, locale, and RTL screenshots only where those states are part of the risk being guarded.
- Store actual, expected, and diff artifacts for every CI failure.

## Baseline Update Rules

- Baselines are product artifacts. A changed screenshot should be reviewed like a design change.
- Never auto-update baselines in required CI.
- Require a short reason for baseline updates: intended design change, browser/tool update, font update, or fixture update.
- If a baseline changes because the environment changed, update the environment lock or document the tool/browser version change in the PR.
- If a test needs a high threshold to pass, narrow the screenshot, stabilize the fixture, or split the assertion before raising the threshold.

## Additional Rules

- Use as Playwright visual-regression workflow example with vendor-bias caveat; prefer Playwright and Vitest docs for exact APIs.
- Use Vitest Browser Mode visual-regression guidance for screenshot stability, masking, thresholds, and animation control.
- Use visual-testing workflow for UI baselines, review loops, and Storybook/Chromatic-backed visual state coverage.
