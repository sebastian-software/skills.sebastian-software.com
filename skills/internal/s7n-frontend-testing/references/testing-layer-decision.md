# Testing Layer Decision

Choose the smallest test layer that proves the user-facing risk.

## Working Rules

- Use unit tests for pure logic, formatting, hooks, reducers, parsers, and deterministic transformations.
- Use component or Storybook tests for reusable UI states, interaction behavior, accessibility states, and visual state matrices.
- Use visual regression when the important behavior is visible layout, styling, spacing, or rendering.
- Use E2E tests for critical integrated workflows that cross routing, network, auth, persistence, or backend boundaries.
- Keep E2E suites small and stable; do not use them to exhaustively test component state permutations.

## Decision Matrix

| Risk to prove | Preferred layer | Avoid |
| --- | --- | --- |
| Pure calculation, parser, mapper, formatter | Unit test | Browser test setup for deterministic logic. |
| Hook/reducer/state transition | Unit or component test | Full E2E when no browser integration is involved. |
| Component states, disabled/loading/error/success variants | Storybook, component test, or Vitest Browser Mode | Recreating state fixtures separately from stories. |
| Keyboard/focus behavior in a reusable widget | Component browser test plus manual a11y check for complex widgets | Snapshot-only tests. |
| Responsive layout, spacing, visual styling | Visual regression with controlled viewport and fonts | Assertions on CSS implementation details. |
| Route, auth, persistence, network, checkout/signup/save flow | Playwright-style E2E | Large E2E matrices for every component permutation. |
| Accessibility semantics | Static axe-style check plus manual keyboard/screen-reader verification for custom widgets | Assuming automated checks prove full accessibility. |
| Cross-browser platform behavior | Targeted browser test across configured engines | Running all tests in all browsers by default when only one path is engine-sensitive. |

## Coverage Shape

Build a small pyramid for each feature:

1. Unit tests for deterministic logic and data shaping.
2. Component/story tests for state variants and local interaction.
3. One or two integrated E2E tests for the business-critical path.
4. Visual snapshots only for states where visual drift is the failure mode.
5. Manual or scripted accessibility checks for custom semantics and focus behavior.

Prefer fewer high-signal tests over broad brittle coverage. A test should fail because user-facing behavior changed, not because implementation details moved.

## Additional Rules

- Use as stack-level testing strategy guidance separating unit, Storybook component, visual snapshot, E2E, and static analysis responsibilities.
- Use as broad frontend testing pipeline and CI/CD framing, subordinate to more specific Storybook, Vitest, and Playwright sources.
