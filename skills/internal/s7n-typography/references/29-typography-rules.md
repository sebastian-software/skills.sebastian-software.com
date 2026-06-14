# Typography Rules

Use this reference for typography decisions: readable measure, wrapping, fluid sizing, local units, editorial rhythm, and text rendering details.

## Working Rules

- Keep body text readable before applying decorative type behavior.
- Use modern wrapping tools on short headings and compact labels only when they improve scannability.
- Use fluid sizing with zoom and user preferences in mind.
- Align icons, decoration, and local spacing to the type context rather than to arbitrary pixels.
- Use `rem` for global scale decisions and `em`/font-relative units for local component relationships such as icon size, padding, inline gaps, badges, and decorations.
- Prefer `clamp()`-based fluid type within bounded ranges; avoid unbounded viewport-unit type that ignores zoom, user preferences, or narrow/large extremes.
- Use `text-wrap: balance` for short headings, card titles, tooltips, modal headings, and FAQs. Do not apply it blindly to long body text or performance-sensitive large blocks.
- Use text-box trimming, cap units, and hanging punctuation as polish only when support and fallback behavior are acceptable for the product.
- For editorial or CMS content, define vertical rhythm from semantic structure rather than arbitrary spacing after every element.

## Typography Review Checklist

- Are type sizes bounded at minimum and maximum values, and do they still work at browser zoom?
- Is the line length readable for the content type, especially when media or full-bleed layouts are present?
- Do icons, counters, badges, and inline controls align to the font metrics rather than arbitrary pixel centers?
- Are heading wraps intentional, balanced, and still searchable/copyable text?
- Does long-form content keep rhythm across headings, paragraphs, lists, quotes, figures, and first/last child edges?
- Are newer text metrics features guarded or treated as progressive enhancement?

## Additional Rules

- Text-wrap: balance can improve headlines, card titles, tooltips, modal titles, and FAQs, but should be limited to short text, understood not to change element width, and checked for whitespace/performance limits.
- Narrow but useful CSS hanging-punctuation note for editorial polish and punctuation alignment; pair with broader typography rules and current support checks before codifying defaults.
- Cap/rcap unit guidance for aligning icons, spacers, buttons, and type-relative decoration to capital height, but narrow enough to remain a supporting rule.
- Historical/context guidance for fluid type, viewport-unit scaling, controlled type ranges, and accessibility caveats around zoom and user preferences; pair with newer sources for clamp(), modern CSS units, and current support.
- :has()/:where() pattern for vertical rhythm in long-form/CMS content, structural spacing between headings, paragraphs, lists, first/last child handling, section grouping, and low specificity; useful as concrete CSS pattern rather than core typography/a11y guidance.
- Fluid typography reasoning and viewport-unit caveats, but 2016 implementation details should be superseded by modern clamp(), container units, zoom/accessibility, and current browser-support sources.
- Font-size-adjust supports consistent perceived type sizing across fallback/webfont changes.
- Use text-box trimming for type alignment and box metrics when support is acceptable.
- Duplicate support for hanging punctuation guidance already integrated.
- Use simplified fluid typography as supporting for clamp-based type scales and zoom caveats.
- Use modern fluid typography with CSS clamp as for responsive type ranges and accessibility caveats.
- Use rem/em sizing for global vs local sizing policy in components and design tokens.
- Use base-element unit as typography/unit radar; verify support before rules.
