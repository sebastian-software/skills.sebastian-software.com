# Print Design

Apply expert CSS print design, paged-media, and web-to-print judgment. Bring the
precision of professional typesetting to HTML and CSS, aiming for print-quality
results without pretending that browsers provide every DTP capability.

## Contents

- [Quick Decision Guide](#quick-decision-guide)
- [References](#references)
- [Print vs. Screen](#print-vs-screen)
- [Browser Print Scale Calibration](#browser-print-scale-calibration)
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
| Typography | [print-typography-core.md](print-typography-core.md) — sizes, scale, stacks, wrapping/hyphenation, and figure decisions (load the deep print-typography appendix only for the full cookbook) |
| Layout | [print-layout.md](print-layout.md) — layers, reset, @page, simulation, grid, fragmentation |
| Web Print CSS | [print-web-basics.md](print-web-basics.md) — start for ordinary web pages; it selects content and paper-order details when needed |
| Page Features | [print-page-features.md](print-page-features.md) — headers/footers, counters, bleed, links, element styles |
| Locale | [print-locale.md](print-locale.md) — integrate reviewed locale rules into print CSS; route language-level rules to `effective-writing` and follow its verification and safe-preprocessing requirements |
| Physical scale / Safari parity | [print-scale-calibration.md](print-scale-calibration.md) — load only for scale diagnosis or a physical-parity requirement |

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

## Browser Print Scale Calibration

Use [print scale calibration](print-scale-calibration.md) when a fixed-format
document prints at the wrong physical size or native Safari parity matters.
It contains the WebKit mechanism, wrapper correction, measurement procedure,
and [calibration fixture](../fixtures/print-webkit-scale-calibration.html).
Ordinary print styling does not require this diagnostic path.

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
- Start body text at 400; use lighter weights only after verifying them on the actual output (thin strokes can vanish on paper)
- Fewer heading levels than screen (3 suffice), modest ~1.2x scale (minor third)
- Max 2–3 typefaces; pair by matching x-heights and historical period
- Books: use `text-indent: 1em` on `p + p` (not `margin-bottom`) for paragraph separation
- Choose body faces with low-to-medium stroke contrast and open apertures — high contrast (Bodoni) for display only
- Choose body faces by legibility at the target point size, glyph coverage, licensing/availability, and fit with the artifact's hierarchy; Georgia, Charter, Palatino, and Times New Roman are context-dependent options, not a universal ranking
- Quotation marks, dashes, number formatting, and spacing rules vary by locale — route them to `effective-writing`; use `quotes: auto` only after verifying the rendered locale result, and preprocess only rendered prose with an explicit locale

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

1. **Chrome DevTools:** Cmd+Shift+P > "Emulate CSS print media type" for quick
   CSS inspection; it is not native print evidence.
2. **Print Preview:** Cmd+P to inspect actual pagination and the chosen paper,
   margins, headers, and dialog scale.
3. **Playwright Chromium:** use `page.emulateMedia({ media: 'print' })` plus
   `page.pdf()` for automated Chromium PDF and visual-regression checks. It
   does not emulate Safari/WebKit printing.
4. **Native WebKit:** when Safari parity or physical scale matters, follow
   [print scale calibration](print-scale-calibration.md).
5. **Native Firefox:** use its print-to-PDF path too when cross-engine physical
   parity is a requirement, then compare vector measurements and pagination.
6. **Actual printers** — laser and inkjet render differently.

## Production Sources

- [CSS Values and Units Level 4: absolute lengths and resolution units](https://www.w3.org/TR/css-values-4/#absolute-lengths) — CSS reference units, including `px`, `pt`, and `dpi`
- [CSS Paged Media Module Level 3](https://www.w3.org/TR/css-page-3/) — page-based media rules and the `@page` model
