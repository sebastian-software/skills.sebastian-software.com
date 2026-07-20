# Examples and Verification

## Make examples executable in spirit and practice

Use the smallest complete example that reaches the promised result from the
documented starting state. Include required imports, setup, authentication
shape, configuration, and cleanup when omitting them would make the example
fail or teach an unsafe pattern.

Prefer examples that can be compiled, typechecked, doctested, executed against
a local fixture, or exercised by repository tests. When a snippet cannot run
directly, label omissions and placeholders explicitly and verify its individual
claims against the implementation.

Do not use live secrets, personal data, production identifiers, destructive
commands, or privileged endpoints as convenient sample data. Use unmistakable
placeholders and safe local or test environments.

## Discover the repository's verification path

Inspect manifests, task runners, CI workflows, docs configuration, and nearby
contribution guidance before inventing a validation command. Use the applicable
layers:

1. formatter and documentation lint;
2. docs build or generated-reference consistency check;
3. internal and external link or anchor validation;
4. compilation, typechecking, doctests, or example tests;
5. CLI or API smoke tests against a safe local or test target; and
6. rendered navigation and layout inspection when structure changed.

Run the narrowest useful check while iterating, then the repository-required
suite before delivery. If a tool is unavailable, report the exact unverified
claim and use a smaller safe check where possible; do not relabel inspection as
execution.

## Guard against drift

- Prefer generated references for exhaustive machine-owned contracts and
  authored guides for tasks and decisions.
- Keep snippets close to tested examples or import them from a verified source
  when the docs toolchain supports it.
- Update versioned examples and migration paths with the interface change that
  invalidates them.
- Test negative or recovery paths when the documentation makes a consequential
  promise about errors, rollback, permissions, or destructive behavior.
- Compare rendered output or generated diffs when navigation, anchors, code
  blocks, tables, or cross-references change.

Finish by naming the commands run and their results. Separate checks that
passed from checks skipped or blocked.
