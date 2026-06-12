# Storybook Component Testing

Use stories as reusable UI state fixtures. Prefer one state source that supports documentation, review, interaction testing, accessibility checks, and visual snapshots.

## Working Rules

- Put meaningful UI states in stories before duplicating setup in tests.
- Use user-facing queries and interactions rather than implementation details.
- Keep story `play` functions focused on behavior that belongs to the component state.
- Treat Storybook version and addon APIs as current-version details; verify before coding exact imports.

## Source-Backed Guidance
### @storybook-test: more streamlined and powerful testing

- Things ID(s): `DFw6VdPXpwH4vxZKr8EU34`, `R8uUkK7XeGGQ9QvEhPdWHi`
- Source: <https://storybook.js.org/blog/storybook-test/>
- Decision: `secondary`
- Target: `frontend-testing/storybook`
- URL recheck: 2026-06-13, HTTP 404
- Guidance: Historical @storybook/test consolidation source; useful for explicit action spies and migration context, but original canonical URL is dead and exact API details are version-sensitive.
### Code coverage with Storybook test runner

- Things ID(s): `5VhreUhQbwfsJgC8ZvHSUP`
- Source: <https://storybook.js.org/blog/code-coverage-with-the-storybook-test-runner/>
- Decision: `secondary`
- Target: `frontend-testing/storybook`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use Storybook coverage as a way to find missing component states and story coverage gaps; verify current commands before implementation.
### Component Test with Storybook and Vitest

- Things ID(s): `5yq1bxx85VTJjKvgWikMj4`
- Source: <https://storybook.js.org/blog/component-test-with-storybook-and-vitest/>
- Decision: `primary`
- Target: `frontend-testing/storybook`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Treat Storybook stories as component state fixtures that can support interaction, accessibility, visual tests, coverage, and CI review.
### https://storybook.js.org/blog/interaction-testing-with-storybook/

- Things ID(s): `XNcRweYAzmPGAcQZN4ijUi`
- Source: <https://storybook.js.org/blog/interaction-testing-with-storybook/>
- Decision: `secondary`
- Target: `frontend-testing/storybook`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use Storybook play functions and user-facing queries as component interaction tests close to the story state; verify modern package names.
### I18n with Storybook

- Things ID(s): `EZeoRB2JKjAzHqREbUNFUy`
- Source: <https://storybook.js.org/blog/internationalize-components-with-storybook/>
- Decision: `primary`
- Target: `frontend-testing`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use I18n with Storybook as primary source for localized UI state coverage.
### Improved type safety in Storybook 7

- Things ID(s): `QZ1jUa3ZkDh6gzxqSWMFvM`
- Source: <https://storybook.js.org/blog/improved-type-safety-in-storybook-7/>
- Decision: `secondary`
- Target: `frontend-testing`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use Storybook type-safety source for story typing and component fixture quality.

