# Baseline and Browser Support

Use current browser-support evidence before turning modern web-platform features into defaults. Baseline, official documentation, and project support policy should drive adoption, not novelty.

## Working Rules

- Prefer Baseline and official platform documentation over anecdotal support guesses.
- Separate feature-radar sources from implementation-rule sources.
- Add `@supports`, progressive enhancement, fallback behavior, or project-specific support constraints when using newly available features.
- Connect support policy to Browserslist, linting, CI, and design-system defaults where possible.

## Source-Backed Guidance

### Adactio: Journal-CSS snippets

- Things ID(s): `4m11kz8ZUfiaRXQosiPdmx`
- Source: <https://adactio.com/journal/21896>
- Decision: `secondary`
- Target: `baseline`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for baseline/design-system practice: practitioner default snippets around logical properties, reduced-motion guarded View Transitions, custom properties, OKLCH, focus-visible, text-wrap, hanging punctuation, low-specificity :where(), cascade layers, and line-height units; useful as habit/radar source, not a normative rule source.

