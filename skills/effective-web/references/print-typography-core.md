# Print Typography Core

Decision rules and most-used values for print typography. Load the deep
[print-typography.md](print-typography.md) appendix for the full cookbook:
detailed OpenType, glyph substitution, optical sizing, stylistic alternates,
standfirst and drop-cap recipes, resume/ATS specifics, and rare edge cases.

CSS `pt` = Word `pt` = 1/72 inch. Fonts differ visually at the same pt size —
verify on output; adjust by half-points (10.5pt, 11.5pt) when needed.

## Size and Line-Height Defaults

| Element | Size | Line-height |
|---------|------|-------------|
| Body | 11pt | 1.35–1.4 |
| h1 | 22–24pt | 1.05–1.1 (below 1.0 OK for all-caps display) |
| h2 | 16–18pt | 1.1–1.15 |
| h3 | 13–14pt | 1.15–1.2 |
| h4 | 11pt bold | 1.2–1.3 |
| Captions / footnotes | 8–9pt | 1.2–1.25 |
| Code | 9pt | 1.3–1.4 |

- Functional text (captions, labels, footnotes) never below **75%** of body.
- Heavier/darker faces need more leading; lighter ones less — tune by squinting
  at the block's overall gray value, not by the fixed range alone.
- Validate leading with the "double cap-height" test: mentally double a capital
  H; if it reaches the baseline above, body line-height is too tight.

Document-type starting points:

| Property | Resume/CV | Article/Blog | Book/Report |
|----------|-----------|--------------|-------------|
| Body size | 9.5–10.5pt | 11pt | 11–12pt |
| Line-height | 1.3–1.4 | 1.35 | 1.4–1.5 |
| Text-align | Left | Justify | Justify |
| Hyphens | No | Yes | Yes |

## Scale and Font Choice

- Print needs less size contrast than screen: use **minor third (1.2)** as the
  default ratio, **major second (1.125)** for dense/compact documents.
- Both serif and sans work in print; choose by brand identity. Body faces need
  low-to-medium stroke contrast and open apertures (reserve high-contrast
  Bodoni/Didot for display). Restrain personality in body type.
- Pairing rules: match x-heights, match historical period and structural
  skeleton, contrast on **one axis only** (serif/sans *or* weight *or* width),
  max 2–3 typefaces, prefer superfamilies, never pair two similar faces.

## Font Safety and Stacks

`font-synthesis: none` — never let the browser fake bold/italic (crude at
300 DPI). Only declare a weight/style whose real font file is loaded.
`font-size-adjust` normalizes x-height across fallbacks (0.5pt matters on paper).

```css
@media print {
  body {
    font-family: Charter, 'Bitstream Charter', Cambria, Georgia, serif;
    font-size: 11pt;
    line-height: 1.35;
    font-size-adjust: 0.465;   /* normalize x-height across fallbacks */
    font-optical-sizing: auto; /* thicken strokes small, refine large */
    font-synthesis: none;
  }
  code, pre { font-family: 'Courier New', monospace; font-size: 9pt; }
}
```

## Wrapping and Hyphenation

- `text-wrap: balance` + `hyphens: none` on headings.
- `text-wrap: pretty` on body; `hyphens: auto` needs a `lang` attribute.
- **Justify only** when line length ≥ 50 chars (ideally 60+) **and** hyphenation
  works — both mandatory. Narrow columns (sidebars, captions): `text-align: left`.

```css
@media print {
  h1, h2, h3, h4, h5, h6 { text-wrap: balance; hyphens: none; }
  p, li, dd, blockquote {
    text-wrap: pretty; text-align: justify;
    hyphens: auto; -webkit-hyphens: auto;
    hyphenate-limit-chars: 6 3 2;
    hyphenate-limit-lines: 2;
    hyphenate-limit-zone: 8%;
    hyphenate-limit-last: always;
  }
}
```

Use `<wbr>` to allow a break without a hyphen (long URLs/identifiers) and
`&shy;` to place a break point where a hyphen *should* appear if broken.

## Paragraph Separation

Choose one convention — never combine spacing and indentation:

- **Spacing** (articles/reports/resumes): `p { margin-bottom: 0.8em; }`.
- **Indentation** (books/literary): `p { margin: 0 } p + p { text-indent: 1em }`
  — first paragraph after a heading/figure/list stays un-indented automatically.

## OpenType Figures

- Body prose: `oldstyle-nums proportional-nums`.
- Tables: `lining-nums tabular-nums`. Headings: `lining-nums` (old-style clashes
  with capitals).
- The `font` shorthand resets `font-kerning`; re-declare `font-kerning: normal`.

## Letter-Spacing

- Body: `normal` — never track lowercase body text.
- ALL CAPS / small-caps: `0.05em`–`0.12em`, plus
  `font-variant-ligatures: no-common-ligatures`.
- Large display: `-0.01em`; big/bold/wide display: `-0.03em`.

## Hierarchy

- Fewer heading levels than screen (3 usually suffice); differentiate by weight,
  style, caps, or spacing — not size alone.
- More space **before** a heading than after (groups it with following content).
- A multi-line heading's internal leading must be tighter than its margins
  (Gestalt proximity), or readers mis-group the lines.
- Modest ~1.2x scale between levels.

## Special Characters

Use `–` (en dash) for ranges, `×` (`&times;`) for dimensions, `−` (`&minus;`)
for subtraction, `…` for ellipsis, `'` (U+2019) for apostrophe, and a narrow
no-break space (U+202F, `&#8239;`) between numbers and units. Locale-specific
quotation marks, dashes, and spacing route to `locale-typography` — see
[print-locale.md](print-locale.md).
