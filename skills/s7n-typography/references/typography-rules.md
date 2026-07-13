# Typography Rules

Use this reference for typography decisions: readable measure, wrapping, fluid sizing, local units, editorial rhythm, and text rendering details.

## Working Rules

- Keep body text readable before applying decorative type behavior.
- Use modern wrapping tools on short headings and compact labels only when they improve scannability.
- Use fluid sizing with zoom and user preferences in mind.
- Align icons, decoration, and local spacing to the type context rather than to arbitrary pixels.
- Use `rem` for global scale decisions and `em`/font-relative units for local component relationships such as icon size, padding, inline gaps, badges, and decorations.
- Prefer `clamp()`-based fluid type within bounded ranges; avoid unbounded viewport-unit type that ignores zoom, user preferences, or narrow/large extremes. Keep at least one term of a fluid `font-size` in a zoom-respecting unit (`rem`/`em`) so text still scales with the browser zoom and default-size settings; never express it in `vw` alone.
- Use `text-wrap: balance` for short headings, card titles, tooltips, modal headings, and FAQs. Do not apply it blindly to long body text or performance-sensitive large blocks; many engines stop balancing after a small number of lines (around 6 in Chromium) and it must not be relied on to change an element's width.
- Use `text-wrap: pretty` for long-form paragraphs to suppress orphans and improve last-line breaks. Treat it as progressive enhancement (support is still uneven across engines and weaker in Firefox), and let it degrade to normal wrapping where unsupported.
- Use `cap` and `rcap` units to size and align type-relative decoration — icons, leading bullets, spacers, and inline buttons — to the cap height of the surrounding text instead of guessing pixels. Provide a pixel or `em` fallback for older engines, since `cap`/`rcap` are recent additions.
- Use `font-size-adjust` to hold perceived text size constant across a webfont swap or a serif/sans mix by pinning the x-height ratio, which removes the size jump and reflow when the fallback is replaced.
- Treat text-box trimming (`text-box-trim` / `text-box-edge`, formerly proposed as `leading-trim`) as the precise way to remove the half-leading above cap height and below the baseline so headings and buttons align to their glyphs rather than their line box. Support is still limited and Chromium-led; gate it behind `@supports` and keep manual optical padding as the fallback.
- For editorial or CMS content, define vertical rhythm from semantic structure rather than arbitrary spacing after every element. Express rhythm with low-specificity selectors — e.g. `:where(h2, h3, p, ul, ol, blockquote, figure)` for the base step and `:has()` for context-sensitive gaps (a heading immediately followed by a paragraph, or a figure between paragraphs) — and reset the first/last child edges so sections do not accumulate stray margins.

## Typography Review Checklist

- Are type sizes bounded at minimum and maximum values, and do they still work at browser zoom?
- Is the line length readable for the content type, especially when media or full-bleed layouts are present?
- Do icons, counters, badges, and inline controls align to the font metrics rather than arbitrary pixel centers?
- Are heading wraps intentional, balanced, and still searchable/copyable text?
- Does long-form content keep rhythm across headings, paragraphs, lists, quotes, figures, and first/last child edges?
- Are newer text metrics features guarded or treated as progressive enhancement?
