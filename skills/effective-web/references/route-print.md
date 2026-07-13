# Print Design

Apply expert CSS print design, paged-media, and web-to-print judgment. Bring the
precision of professional typesetting to HTML and CSS, aiming for print-quality
results without pretending that browsers provide every DTP capability.

## Contents

- [Quick Decision Guide](#quick-decision-guide)
- [References](#references)
- [Print vs. Screen](#print-vs-screen)
- [Architecture and Typography](#architecture)
- [Colors, Fragmentation, Images, Links, and Tables](#colors)
- [Testing](#testing)

## Quick Decision Guide

| Task | Approach |
|------|----------|
| Simple print stylesheet | `@media print` block in existing CSS |
| Screen preview matching print | Paper-simulation technique (see [print layout](print-layout.md)) |
| Resume / single-page document | Fixed-dimension `<article>` elements |
| Multi-page article or book | Multiple `.page` elements with `page-break-after` |

## References

| Category | Reference |
|----------|-----------|
| Typography | [print-typography.md](print-typography.md) — font sizes, stacks, OpenType, text-wrap, hyphenation |
| Layout | [print-layout.md](print-layout.md) — layers, reset, @page, simulation, grid, fragmentation |
| Web Print CSS | [print-web-styles.md](print-web-styles.md) — print styles for ordinary web pages |
| Page Features | [print-page-features.md](print-page-features.md) — headers/footers, counters, bleed, links, element styles |
| Locale | [print-locale.md](print-locale.md) — quotation marks, dashes, numbers, spacing per locale, preprocessing tools |

## Print vs. Screen

| | Print | Desktop | Mobile |
|---|---|---|---|
| **Units** | `pt` | `rem` / `px` | `rem` / `px` |
| **Layout** | Fixed page (A4 / Letter) | Fluid, `max-width` | Fluid, single-column |
| **Colors** | OKLCH; B&W first, CMYK gamut | OKLCH / RGB | OKLCH / RGB |
| **Typography** | 11pt, serif, justify, hyphens | 16px+, variable | 16px+, left-align |
| **Line-height** | 1.35–1.4 (tight) | 1.5–1.6 | 1.5–1.6 |
| **Images** | 300 DPI | 72–96 DPI | 72–96 DPI, lazy load |
| **Backgrounds** | Stripped by browser | Free | Free |
| **Font-weight** | Min 400 (thin vanishes) | Free | Free |
| **Interaction** | None — hide all UI | Full | Touch |
| **Line length** | Page margins control | `max-width` / container | Full width |

## Architecture

- Use `@layer` to separate print from screen — eliminates `!important` wars
- Start with a clean-slate reset: strip backgrounds, shadows, filters to `transparent`/`none`
- Blacklist approach: explicitly hide what doesn't belong (nav, sidebar, ads, buttons)
- Use `print-color-adjust: exact` only where backgrounds carry meaning
- **Generous whitespace** — too much rarely hurts, too little is fatal (cramped layouts are the #1 amateur mistake)

## Typography

- Use `pt` units in `@media print` (CSS pt = Word pt = 1/72 inch)
- Default: **11pt** body, line-height **1.35–1.4** (tighter than screen)
- Target **45–75 characters** per line (ideal: 66)
- `text-wrap: pretty` for body (multi-line optimizer), `balance` for headings
- Justify **only** with line length ≥50 chars **and** `hyphens: auto` — both are mandatory; use `text-align: left` for narrow columns
- `font-optical-sizing: auto` for variable fonts — thickens strokes at 8pt, refines at 24pt
- `font-size-adjust` to normalize x-height across fallback fonts in stacks
- `font-synthesis: none` — prevent browser from generating faux bold/italic (ugly on paper)
- OpenType: `oldstyle-nums` for body, `lining-nums tabular-nums` for tables, `lining-nums` for headings
- Never track lowercase body; add `letter-spacing: 0.05–0.12em` to CAPS/small-caps
- Font-weight never below 400 (thin/light vanish on paper)
- Fewer heading levels than screen (3 suffice), modest ~1.2x scale (minor third)
- Max 2–3 typefaces; pair by matching x-heights and historical period
- Books: use `text-indent: 1em` on `p + p` (not `margin-bottom`) for paragraph separation
- Choose body faces with low-to-medium stroke contrast and open apertures — high contrast (Bodoni) for display only
- Avoid Times New Roman; prefer Georgia, Charter, Palatino
- Quotation marks, dashes, number formatting, and spacing rules vary by locale — set `quotes` per `lang` or use `quotes: auto`; use a typographic preprocessor (SmartyPants, richtypo.js) for automated character substitution at build time

## Colors

- **Design for black & white first** — most users print monochrome
- OKLCH works for print — browser converts to sRGB/PDF; L-channel maps directly to perceived gray value
- Browsers strip backgrounds by default; restore selectively with `print-color-adjust: exact`
- Keep chroma low for print — high-chroma OKLCH values may fall outside CMYK gamut
- Replace box-shadows with borders; replace colored backgrounds with border patterns
- Use pure black (`#000`) for body text — prints as 100% K (black ink only). Avoid "rich black" (CMYK 60/40/40/100) on text — causes registration issues and blurring at small sizes

## Fragmentation

- `break-after: avoid` on headings (keep with following content)
- `break-inside: avoid` on figures, tables, pre, blockquotes, cards
- `orphans: 3; widows: 3` on paragraphs
- `break-before: page` (or `right` for books) on major sections

## Images

- Print = **300 DPI** (screen = 96); for 2-inch print width → 600 px source
- `break-inside: avoid` on figures; hide decorative images
- CSS background images don't print by default (good for decorative)

## Links

- **Never dump raw URLs inline** — clutter the layout, nobody types them
- Use numbered footnotes (CSS counters) or a single QR code, or both
- Expand abbreviations on paper (see [paged-media features](print-page-features.md))

## Tables

- `thead { display: table-header-group; }` — repeats headers on every page
- Minimize borders (one direction only); don't force `width: 100%` — size columns to data
- `font-variant-numeric: lining-nums tabular-nums`, `line-height: 1` in cells
- `tr { break-inside: avoid; }`

## Code Blocks

- Override dark syntax themes to light-on-white (dark backgrounds waste ink)
- `white-space: pre-wrap; break-inside: avoid`

## Testing

1. **Chrome DevTools:** Cmd+Shift+P > "Emulate CSS print media type"
2. **Print Preview:** Cmd+P (shows actual pagination)
3. **Playwright:** `page.emulateMedia({ media: 'print' })` + `page.pdf()` for automated PDF generation and visual regression tests
4. **Actual printers** — laser and inkjet render differently
