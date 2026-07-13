# Storybook Component Testing

Use stories as the single source of UI state. One story should drive documentation,
manual review, interaction tests, accessibility checks, and visual snapshots — so a
state is defined once and exercised everywhere, instead of being re-stubbed per test.

## Working Rules

- Define each meaningful state as its own named story before duplicating setup in a
  test file: default, loading, empty, error, disabled, long-content, and any
  data-variant that changes layout. The story name is the spec.
- Type stories so the args stay in sync with the component. Use
  `satisfies Meta<typeof Component>` on `meta` and `StoryObj<typeof meta>` for each
  story; this surfaces prop drift at compile time instead of in a broken snapshot.
- Drive behavior from `play` functions using `@storybook/test` (`within`,
  `userEvent`, `expect`, `fn`). Query through `canvas.getByRole`/`getByLabelText`
  and interact via `userEvent`; never reach into component internals or query by
  generated class names.
- Assert on side effects with spy args: pass `fn()` from `@storybook/test` to
  callback props (`onClick`, `onChange`) and assert `expect(args.onChange)
  .toHaveBeenCalledWith(...)` in the `play`. This verifies the contract a parent
  relies on, not the implementation.
- Keep each `play` scoped to one component's behavior. A `play` that navigates routes,
  hits a real backend, or coordinates multiple pages is an E2E test in disguise — move
  it to Playwright.
- Stub inputs at the story boundary so the state is deterministic: provide data through
  args or loaders, wrap with decorators for theme, router, and i18n providers, and pin
  the locale, timezone, and any randomness the component reads.
- Cover localized and RTL states explicitly. Add stories that render under each
  supported locale (and `dir="rtl"`) when text length or direction changes layout;
  these double as visual-regression and accessibility fixtures.
- Use Storybook's coverage and the test runner to find missing states: an interactive
  branch with no story is an untested state. Add the story rather than a bespoke test.
- Treat Storybook and addon APIs as version-specific. Confirm the installed major
  version and its package/import names (the test utilities have moved between packages
  across releases) before writing exact imports.

## Audit an inherited or agent-generated UI

Do not begin by trusting `AGENTS.md`, design notes, or the running happy path as
the source of truth. Reconcile them with the code that is actually reachable.

- Inventory component files, imports, routes, stories, tokens, and icon sources
  with deterministic repository tooling. Classify live, unreachable, duplicate,
  and unknown components; do not delete an unreferenced export until dynamic
  imports, framework discovery, package consumers, and tests are checked.
- Render every meaningful conditional state in isolation. Agent-generated UI
  often hides loading, empty, error, permission, long-content, and invalid states
  behind branches that no normal demo reaches.
- Add accessibility checks to the rendered state catalog and CI, then manually
  verify keyboard flow, names, focus, announcements, zoom, and high contrast.
  Automated results are a floor, not proof of accessibility.
- Surface design-system drift alongside stories: raw colors and spacing,
  undefined tokens, competing primitives, inconsistent icons, and components
  that express the same job through different interaction models.
- Map routes and core journeys in addition to isolated components so missing
  connections, dead flows, and state handoffs are visible.
- Store structured findings and compare audits over time. Turn confirmed defects
  into explicit work; do not use one aggregate health score to hide severity.

## Review checklist

- Does every visible state and interaction branch have a named story?
- Do `play` functions query by role/label and assert via spied callback args?
- Are theme, router, locale, timezone, and randomness pinned by decorators/args?
- Do RTL and per-locale stories exist where direction or text length shifts layout?
- Is `meta` typed with `satisfies Meta` so prop changes break the build, not a snapshot?
- Does any `play` cross page or backend boundaries that belong in E2E instead?
- For an inherited UI, is there a code-backed live/dead/unknown inventory and a
  rendered catalog of every meaningful state rather than only the happy path?
