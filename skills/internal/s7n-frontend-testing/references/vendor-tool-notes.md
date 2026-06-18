# Vendor Tool Selection

Pick a testing tool only after the project's need is concrete. Tools are implementation
options, not defaults — the right choice depends on what the team already runs, where
baselines should live, and how failures get reviewed. Adopt the fewest tools that cover the
need; every added service is another thing to pin, fund, and debug.

## Selection criteria

Evaluate any visual, E2E, or hosted testing tool against these before adopting it:

- Baseline storage: are reference images/snapshots in your repo (reviewable in PRs, free) or
  on a vendor's servers (approval in their UI, ongoing cost, lock-in)? Prefer in-repo unless a
  hosted review workflow is a deliberate requirement.
- PR review workflow: does it surface actual/expected/diff in the pull request, or only in an
  external dashboard? Reviewers should judge a UI change without leaving the PR.
- Browser and device coverage: which engines (Chromium, Firefox, WebKit), viewports, devices,
  DPRs, and OS images run by default, and does that match the audience you actually support?
- Determinism controls: can it pin fonts, disable animations, mask dynamic regions and
  third-party embeds, and set pixel thresholds? A tool that cannot stabilize these will produce
  noisy, ignored diffs.
- Debuggability: does a failure ship a trace, diff image, or replay, or just a red check? Fast
  diagnosis is what keeps a suite alive.
- Local reproduction: can a developer reproduce and regenerate a failing diff without the
  vendor, and what happens to the suite when the vendor service is down?
- Fit with the existing stack: reuse the runner the project already has (Playwright, Vitest,
  Storybook) before introducing a parallel system that duplicates setup and CI time.

## Rules

- Do not adopt a hosted visual-testing service by default; justify the recurring cost and
  lock-in against keeping baselines in-repo and reviewing diffs in the PR.
- Verify a tool's current capabilities against its own up-to-date docs before relying on
  specific features; feature matrices and integrations change between releases.
- Prefer one well-integrated tool per layer over several overlapping ones; consolidate when two
  tools cover the same layer.
- Do not choose a tool from homepage or sales claims; validate it with a small proof of concept
  on one stable component, one responsive page, and one intentionally changed baseline before
  adopting it.
- Keep lock-in low: retain stable selectors, reusable fixtures, and local reproduction commands
  so the suite survives dropping the vendor.

## Selection checklist

- Where do baselines live, and who approves changes to them?
- Are diffs/traces visible in the PR for review?
- Do the default browsers and viewports match the supported audience?
- Can fonts, motion, dynamic regions, and thresholds all be controlled?
- Does it reuse the existing runner, or add a parallel stack?
