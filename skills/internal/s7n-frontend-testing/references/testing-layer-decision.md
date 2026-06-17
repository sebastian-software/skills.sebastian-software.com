# Testing Layer Decision

Choose the smallest test layer that proves the user-facing risk. Each layer up the
pyramid is slower, flakier, and more expensive to maintain, so push every assertion
to the lowest layer that can still observe the behavior that matters.

## Working Rules

- Use unit tests for pure logic: formatters, hooks, reducers, parsers, selectors,
  validation, and deterministic transformations. Assert inputs and outputs directly;
  do not mount a DOM to test a function.
- Use component or Storybook tests for reusable UI states, interaction behavior,
  rendered accessibility (roles, names, focus order), and visual state matrices
  (loading, empty, error, disabled, long-content, RTL).
- Use Vitest Browser Mode (or another real-browser component runner) instead of
  jsdom when a test depends on real layout, scrolling, focus, pointer events,
  `IntersectionObserver`, `ResizeObserver`, or computed styles. jsdom fakes these
  and silently passes or fails for the wrong reason.
- Use visual regression when the risk is in pixels: layout, spacing, color, typography,
  z-index, or responsive breakpoints that assertions cannot economically describe.
- Use E2E tests for critical integrated workflows that cross routing, network, auth,
  persistence, or backend boundaries — sign-in, checkout, the primary create/edit flow.
- Use static checks (type checking, lint, `eslint-plugin-jsx-a11y`, dependency and
  import rules) as the cheapest layer; they catch whole classes of bugs with zero
  runtime cost, so run them first and treat them as required.

## Anti-patterns

- Do not use E2E tests to exhaustively cover component state permutations; that belongs
  in component/Storybook tests where setup is cheap and failures are local.
- Do not write a slow integration test for logic that a unit test already proves.
- Do not test framework internals or third-party libraries; test your usage of them.
- Do not duplicate one behavior across three layers. Pick the layer that owns it and
  delete the redundant coverage elsewhere.

## Decision checklist

- Is this pure logic with no DOM? -> unit test.
- Is it one component's behavior or rendered state? -> component/Storybook test.
- Does it need real browser layout or events? -> Browser Mode component test.
- Is the risk purely visual? -> visual regression on the component, not the page.
- Does it span routes, network, or auth? -> a small, stable E2E test.
- Could a type or lint rule catch it for free? -> prefer the static check.
