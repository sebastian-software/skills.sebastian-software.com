# Testing Layer Decision

Choose the smallest test layer that proves the user-facing risk.

## Working Rules

- Use unit tests for pure logic, formatting, hooks, reducers, parsers, and deterministic transformations.
- Use component or Storybook tests for reusable UI states, interaction behavior, accessibility states, and visual state matrices.
- Use visual regression when the important behavior is visible layout, styling, spacing, or rendering.
- Use E2E tests for critical integrated workflows that cross routing, network, auth, persistence, or backend boundaries.
- Keep E2E suites small and stable; do not use them to exhaustively test component state permutations.

## Source-Backed Guidance

