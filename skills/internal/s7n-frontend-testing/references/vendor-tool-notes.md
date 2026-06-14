# Vendor Tool Notes

Use vendor tools only after the project need is clear. Compare where baselines live, how PR review works, which browsers/devices are covered, how dynamic states are stabilized, and how easy failures are to debug.

## Selection Criteria

Choose a vendor or hosted visual testing tool only after answering:

- What problem does the local stack fail to solve: review UI, browser coverage, artifact storage, flake triage, team workflow, or hosted infrastructure?
- Where do baselines live, and can they be reviewed in normal PR flow?
- Which browsers, devices, DPRs, fonts, and OS images are actually covered?
- Can dynamic regions, animation, clocks, network data, and third-party embeds be stabilized or masked?
- How are diffs approved, rejected, regenerated, and audited?
- Can failures be reproduced locally without the vendor?
- Does the tool support Storybook, Playwright, Vitest Browser Mode, or the project's existing fixture source?
- What happens when the vendor service is down?

## Tooling Defaults

- Prefer project-native tools first when they provide enough signal: Playwright screenshots, Vitest Browser Mode, Storybook interaction tests, and CI artifacts.
- Add hosted review tools when human visual review, parallel browser infrastructure, or baseline governance is the bottleneck.
- Do not choose a vendor from homepage claims alone. Validate with a small proof of concept on one stable component, one responsive page, and one intentionally changed baseline.
- Keep lock-in low: retain stable selectors, reusable fixtures, and local reproduction commands.

## Additional Rules

- Treat snapshot and hosted visual-testing tools as vendor options; compare baseline storage, PR review, browsers, and debugging before adopting.
- Treat Cypress homepage as vendor-context only; do not use it as direct implementation guidance.
