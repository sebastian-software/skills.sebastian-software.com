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

### Viewport-Sized-Fonts: JS Lösung in dem Fall besser?

- Things ID(s): `TdjvmTShj5R1BoWacaMLUG`
- Source: <https://www.smashingmagazine.com/2016/05/fluid-typography/>
- Decision: `secondary`
- Target: `typography`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for typography with responsive-design cross-reference: durable fluid typography reasoning and viewport-unit caveats, but 2016 implementation details should be superseded by modern clamp(), container units, zoom/accessibility, and current browser-support sources.
### Homepage: CSS Font-Size-Adjust für Gleichmachung Größeneindruck unte

- Things ID(s): `NizE9fkVjBwjeGJDD2Bs2c`
- Source: <https://www.sitepoint.com/improve-web-typography-css-font-size-adjust/>
- Decision: `secondary`
- Target: `typography`
- URL recheck: 2026-06-13, HTTP 403
- Guidance: Retarget to typography: font-size-adjust supports consistent perceived type sizing across fallback/webfont changes.
### Two CSS Properties for Trimming Text Box Whitespace

- Things ID(s): `27oUgqy5BVRRqi8eQNVXS7`, `68BarThK7k4XBNGkPcUoQA`
- Source: <https://css-tricks.com/two-css-properties-for-trimming-text-box-whitespace/>
- Decision: `primary`
- Target: `typography`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use text-box trimming source for type alignment and box metrics when support is acceptable.
### Adactio: Journal-Hanging punctuation in CSS

- Things ID(s): `GvuG23prSPcK66eZJbib2e`
- Source: <https://adactio.com/journal/21027>
- Decision: `secondary`
- Target: `typography`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Duplicate support for hanging punctuation source already integrated.
### https://css-tricks.com/simplified-fluid-typography/

- Things ID(s): `FSjG6W4nrS1FvNtvR4wb6i`
- Source: <https://css-tricks.com/simplified-fluid-typography/>
- Decision: `secondary`
- Target: `typography`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use simplified fluid typography as supporting source for clamp-based type scales and zoom caveats.
### https://www.smashingmagazine.com/2022/01/modern-fluid-typography-css

- Things ID(s): `7AwpfiLoDAXVKCCzF8WKoB`
- Source: <https://www.smashingmagazine.com/2022/01/modern-fluid-typography-css-clamp/>
- Decision: `primary`
- Target: `typography`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use modern fluid typography with CSS clamp as primary source for responsive type ranges and accessibility caveats.
### Use `rem` For Global Sizing; Use `em` For Local Sizing | CSS-Tricks

- Things ID(s): `Q9PFZMTQ6MqBEBrrDDeZgC`
- Source: <https://css-tricks.com/rem-global-em-local/>
- Decision: `primary`
- Target: `typography`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use rem/em sizing source for global vs local sizing policy in components and design tokens.
### We Might Need Something Between Root and Relative CSS Units for "Bas

- Things ID(s): `S9FU71oDXYyxejy31L3iLJ`
- Source: <https://css-tricks.com/we-might-need-something-between-root-and-relative-css-units-for-base-elements/>
- Decision: `secondary`
- Target: `typography`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use base-element unit source as typography/unit radar; verify support before rules.

