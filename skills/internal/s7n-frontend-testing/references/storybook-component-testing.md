# Storybook Component Testing

Use stories as reusable UI state fixtures. Prefer one state source that supports documentation, review, interaction testing, accessibility checks, and visual snapshots.

## Working Rules

- Put meaningful UI states in stories before duplicating setup in tests.
- Use user-facing queries and interactions rather than implementation details.
- Keep story `play` functions focused on behavior that belongs to the component state.
- Treat Storybook version and addon APIs as current-version details; verify before coding exact imports.

## Source-Backed Guidance

