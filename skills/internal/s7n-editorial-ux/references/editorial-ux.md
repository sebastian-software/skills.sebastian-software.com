# Editorial UX

Design long-form reading and content-heavy layouts for comprehension, trust, and continued reading. Treat article semantics, reader-mode resilience, link behavior, media placement, and performance as part of the reading experience.

## Working Rules

- Use semantic `main`, `article`, heading hierarchy, skip links, captions, and meaningful alt text.
- Set body copy at 16-20px so prose stays comfortable on a phone without zooming; never drop reading text below 16px.
- Constrain measure to roughly 45-75 characters (about 60ch) and set line height around 1.5-1.7 so the eye returns to the right next line.
- Keep paragraph rhythm and inter-element spacing consistent so vertical flow signals where one block ends and the next begins.
- Underline inline links in body text rather than relying on color alone, so links are distinguishable without color perception and survive theme changes.
- Use layout breakout patterns (full-bleed images, pull quotes, asides) only when they support content comprehension, and keep the main text column anchored so scanning is not disrupted.
- Place figures, captions, and embeds inline near the text they support; give every image explicit `width`/`height` (or `aspect-ratio`) so layout does not shift as media loads.
- Lazy-load below-the-fold media and defer non-essential scripts so the first screen of text is readable before heavy assets arrive.
- For documentation and learning surfaces, prefer runnable or interactive code examples over static snippets so readers can experiment in place; keep them progressively enhanced so the prose still reads without JavaScript.
- Preserve readability in print, reader mode, RSS/email reuse, dark mode, and narrow viewports.

## Review Checklist

- Is the document built from semantic landmarks (`main`, `article`, ordered headings) with a working skip link?
- Does body text stay at least 16px with a 45-75 character measure and ~1.5 line height?
- Are inline links distinguishable without relying on color, and do they describe their destination?
- Do all images carry explicit dimensions and meaningful (or empty, if decorative) alt text?
- Does the first screen of prose render before heavy media and scripts load?
- Does the content survive reader mode, print, dark mode, RSS/email reuse, and a narrow viewport?
