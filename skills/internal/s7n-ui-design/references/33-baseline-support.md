# Baseline and Browser Support

Use current browser-support evidence before turning modern web-platform features into defaults. Baseline, official documentation, and project support policy should drive adoption, not novelty.

## Working Rules

- Prefer Baseline and official platform documentation over anecdotal support guesses.
- Separate feature-radar sources from implementation-rule sources.
- Add `@supports`, progressive enhancement, fallback behavior, or project-specific support constraints when using newly available features.
- Connect support policy to Browserslist, linting, CI, and design-system defaults where possible.

## Source-Backed Guidance

