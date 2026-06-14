# Storybook Component Testing

Use stories as reusable UI state fixtures. Prefer one state source that supports documentation, review, interaction testing, accessibility checks, and visual snapshots.

## Working Rules

- Put meaningful UI states in stories before duplicating setup in tests.
- Use user-facing queries and interactions rather than implementation details.
- Keep story `play` functions focused on behavior that belongs to the component state.
- Treat Storybook version and addon APIs as current-version details; verify before coding exact imports.

## Additional Rules

- Historical @storybook/test consolidation guidance; useful for explicit action spies and migration context, but original canonical URL is dead and exact API details are version-sensitive.
- Use Storybook coverage as a way to find missing component states and story coverage gaps; verify current commands before implementation.
- Treat Storybook stories as component state fixtures that can support interaction, accessibility, visual tests, coverage, and CI review.
- Use Storybook play functions and user-facing queries as component interaction tests close to the story state; verify modern package names.
- Use I18n with Storybook as for localized UI state coverage.
- Use Storybook type-safety for story typing and component fixture quality.
- Use Storybook 10 as platform/version radar for current Storybook workflows.
- Use Storybook main configuration docs for setup/configuration checks.
