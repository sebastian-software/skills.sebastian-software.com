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
| Multi-page article or book | Multiple `.page` elements with `break-after: page` (plus legacy `page-break-after` alias) |

## References

| Category | Reference |
|----------|-----------|
| Typography | [print-typography.md](print-typography.md) — font sizes, stacks, OpenType, text-wrap, hyphenation |
| Layout | [print-layout.md](print-layout.md) — layers, reset, @page, simulation, grid, fragmentation |
| Web Print CSS | [print-web-styles.md](print-web-styles.md) — print styles for ordinary web pages |
| Page Features | [print-page-features.md](print-page-features.md) — headers/footers, counters, bleed, links, element styles |
| Locale | [print-locale.md](print-locale.md) — integrate reviewed locale rules into print CSS; route language-level rules to `locale-typography` and follow its verification and safe-preprocessing requirements |

## Print vs. Screen

| | Print | Desktop | Mobile |
|---|---|---|---|
| **Units** | `pt` | `rem` / `px` | `rem` / `px` |
| **Layout** | Fixed page (A4 / Letter) | Fluid, `max-width` | Fluid, single-column |
| **Colors** | OKLCH; B&W first, CMYK gamut | OKLCH / RGB | OKLCH / RGB |
| **Typography** | 11pt starting point; tested body face; justify only with measure and hyphenation | 16px+, variable | 16px+, left-align |
| **Line-height** | 1.35–1.4 (tight) | 1.5–1.6 | 1.5–1.6 |
| **Images** | Raster density matched to physical output; vector where possible | CSS pixels are reference units, not display density | CSS pixels are reference units; optimize transfer size |
| **Backgrounds** | Stripped by browser | Free | Free |
| **Font-weight** | Start at 400; verify thin/light weights on actual output | Free | Free |
| **Interaction** | Hide interactive chrome by default; keep useful provenance or wayfinding | Full | Touch |
| **Line length** | Page margins control | `max-width` / container | Full width |

## Architecture

- Use `@layer` to separate print from screen — eliminates `!important` wars
- Start with a clean-slate reset: strip backgrounds, shadows, filters to `transparent`/`none`
- Blacklist approach: explicitly hide chrome that does not serve the printed artifact (ads, controls, transient overlays); retain selected context or provenance
- Use `print-color-adjust: exact` only where backgrounds carry meaning
- Choose whitespace for the artifact's density, reading distance, and hierarchy; generous space is a design choice, not a universal print rule

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
- Choose body faces by legibility at the target point size, glyph coverage, licensing/availability, and fit with the artifact's hierarchy; Georgia, Charter, Palatino, and Times New Roman are context-dependent options, not a universal ranking
- Quotation marks, dashes, number formatting, and spacing rules vary by locale — route them to `locale-typography`; use `quotes: auto` only after verifying the rendered locale result, and preprocess only rendered prose with an explicit locale

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

- Size raster assets from their final physical width and the required output density: a 2-inch image at 300 ppi needs 600 source pixels; use vector artwork for marks, diagrams, and type where practical. CSS pixels are defined reference units (1 px = 1/96 inch), not a statement about a screen's physical density.
- `break-inside: avoid` on figures; hide decorative images
- CSS background images don't print by default (good for decorative)

## Links

- Prefer human-readable link labels. For citations, offline provenance, or a useful fallback path, include a short URL, numbered footnote, printed source list, QR code, or a deliberate combination; avoid tracking-heavy raw URLs in running text.
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

## Production Sources

- [CSS Values and Units Level 4: absolute lengths and resolution units](https://www.w3.org/TR/css-values-4/#absolute-lengths) — CSS reference units, including `px`, `pt`, and `dpi`
- [CSS Paged Media Module Level 3](https://www.w3.org/TR/css-page-3/) — page-based media rules and the `@page` model
