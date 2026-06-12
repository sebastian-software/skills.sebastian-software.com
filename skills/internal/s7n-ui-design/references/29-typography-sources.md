# Source-Backed Typography Notes

Use this reference for source-backed typography decisions: readable measure, wrapping, fluid sizing, local units, editorial rhythm, and text rendering details.

## Working Rules

- Keep body text readable before applying decorative type behavior.
- Use modern wrapping tools on short headings and compact labels only when they improve scannability.
- Use fluid sizing with zoom and user preferences in mind.
- Align icons, decoration, and local spacing to the type context rather than to arbitrary pixels.

## Source-Backed Guidance

### CSS Text balancing with text-wrap:balance - Ahmad Shadeed

- Things ID(s): `Kuof53aap99153Pe7ng47e`
- Source: <https://ishadeed.com/article/css-text-wrap-balance/>
- Decision: `primary`
- Target: `typography`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for typography with component-development/editorial cross-references: text-wrap: balance can improve headlines, card titles, tooltips, modal titles, and FAQs, but should be limited to short text, understood not to change element width, and checked for whitespace/performance limits.

### Adactio: Journal-Hanging punctuation in CSS

- Things ID(s): `3e6uHvLLCNNKDfCz5D2fAT`
- Source: <https://adactio.com/journal/21027?utm_source=CSS-Weekly&utm_medium=newsletter&utm_campaign=issue-584-april-12-2024>
- Decision: `secondary`
- Target: `typography`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for typography: narrow but useful CSS hanging-punctuation note for editorial polish and punctuation alignment; pair with broader typography rules and current support checks before codifying defaults.

### CSS Cap Unit

- Things ID(s): `AsQgs8eSZoWkUxPyGwpXAg`
- Source: <https://ishadeed.com/article/css-cap-unit/>
- Decision: `secondary`
- Target: `typography`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for typography with component-development cross-reference: useful cap/rcap unit source for aligning icons, spacers, buttons, and type-relative decoration to capital height, but narrow enough to remain a supporting reference.

### Fluid Typography

- Things ID(s): `UfdqoAE5AUXKwqtZGqPwXZ`
- Source: <https://betterwebtype.com/articles/2019/05/14/the-state-of-fluid-web-typography/>
- Decision: `secondary`
- Target: `typography`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for typography: useful historical/context source for fluid type, viewport-unit scaling, controlled type ranges, and accessibility caveats around zoom and user preferences; pair with newer primary sources for clamp(), modern CSS units, and current support.

### Solved With :has(): Vertical Spacing in Long-Form Text

- Things ID(s): `Jny4ki2K9mpmHFq9VEJiMv`
- Source: <https://css-tricks.com/solved-with-has-vertical-spacing-in-long-form-text/>
- Decision: `secondary`
- Target: `typography`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for typography with editorial-ux cross-reference: practical :has()/:where() pattern for vertical rhythm in long-form/CMS content, structural spacing between headings, paragraphs, lists, first/last child handling, section grouping, and low specificity; useful as concrete CSS pattern rather than core typography/a11y source.

