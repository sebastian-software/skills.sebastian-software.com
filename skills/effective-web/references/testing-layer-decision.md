# Testing Layer Decision

Choose the smallest test layer that proves the user-facing risk. Each layer up the
pyramid is slower, flakier, and more expensive to maintain, so push every assertion
to the lowest layer that can still observe the behavior that matters.

First decide whether durable automated coverage is warranted. Use the brief,
supported component states, observed regression, primary task, and relevant
accessibility or data consequence to establish reachability and impact. Compare
the evidence gained with fixture, runtime, flake, and maintenance cost; do not
invent probability estimates. Existing static coverage plus a focused rendered
inspection can be sufficient for a trivial, low-risk visual edit.

## Working Rules

- Use unit tests for pure logic: formatters, hooks, reducers, parsers, selectors,
  validation, and deterministic transformations. Assert inputs and outputs directly;
  do not mount a DOM to test a function.
- Use component or Storybook tests when reusable UI state, interaction behavior,
  rendered accessibility (roles, names, focus order), or a representative
  loading, empty, error, disabled, long-content, or RTL case carries the risk.
- Use Vitest Browser Mode (or another real-browser component runner) instead of
  jsdom when a test depends on real layout, scrolling, focus, pointer events,
  `IntersectionObserver`, `ResizeObserver`, or computed styles. jsdom fakes these
  and silently passes or fails for the wrong reason.
- Use visual regression when the risk is in pixels: layout, spacing, color, typography,
  z-index, or responsive breakpoints that assertions cannot economically describe.
- Use E2E tests for critical integrated workflows that cross routing, network, auth,
  persistence, or backend boundaries — sign-in, checkout, the primary create/edit flow.
- Run relevant established static checks (type checking, lint,
  `eslint-plugin-jsx-a11y`, dependency and import rules) first because they can
  catch whole classes cheaply. Do not add a tool or broad rule set merely
  because execution is fast; its warning triage and maintenance still have cost.
- Treat automated accessibility checks (axe-style scans) as a floor, not a proof of
  accessibility. For custom widgets, add manual keyboard and screen-reader verification of
  focus order, roles, and names.

## Anti-patterns

- Do not use E2E tests to exhaustively cover component state permutations; that belongs
  in component/Storybook tests where setup is cheap and failures are local.
- Do not write a slow integration test for logic that a unit test already proves.
- Do not test framework internals or third-party libraries; test your usage of them.
- Do not duplicate one behavior across three layers. Pick the layer that owns it and
  delete the redundant coverage elsewhere.
- Do not multiply themes, locales, viewport sizes, input methods, and browser
  engines into an exhaustive matrix. Select representative combinations that
  expose a named risk, and add a specific case when history or platform evidence
  shows the dimensions interact.
- Do not run every test across every browser engine by default. Run a targeted browser
  test on the specific path that is engine-sensitive instead of multiplying the whole
  suite across engines.

## Decision checklist

- Is this pure logic with no DOM? -> unit test.
- Is it one component's behavior or rendered state? -> component/Storybook test.
- Does it need real browser layout or events? -> Browser Mode component test.
- Is the risk purely visual? -> visual regression on the component, not the page.
- Does it span routes, network, or auth? -> a small, stable E2E test.
- Can an established type or lint rule catch it precisely? -> prefer that check.
