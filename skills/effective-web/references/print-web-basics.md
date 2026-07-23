# Web Print Basics

Use this module for an ordinary web page that needs a useful printed artifact.
Start with the reader's paper task: reference, review, handoff, archive, or
form completion. Do not copy every screen decoration onto paper.

## Start with a Small Print Layer

```css
@media print {
  nav, aside, .controls, .transient-ui { display: none; }
  body { background: #fff; color: #000; }
  a { color: inherit; text-decoration: underline; }
}
```

- Prefer a blacklist of genuinely irrelevant chrome; retain useful provenance,
  context, and wayfinding. A page-specific `data-print-keep` contract can make
  exceptions explicit.
- Set `@page` size and margins only when the artifact requires it. Browsers and
  printers retain final control over pagination and print-dialog choices.
- Remove shadows, filters, and ink-heavy backgrounds unless they carry meaning.
  Test monochrome output and use `print-color-adjust: exact` only for selected
  meaningful surfaces.
- Use tested body typography, intentional margins, and a linear reading order.
  CSS `px` is a reference unit; size raster assets from final physical width and
  required output density instead of treating screen pixels as printer density.

## Verify the Artifact

Check browser print preview, at least one representative PDF or printer path,
page breaks, narrow tables, links, images, and a grayscale result. Screen media
emulation is helpful but does not replace the print preview's actual pagination.

For uncommon page rules and the full starter stylesheet, consult the [deep web
print appendix](print-web-styles.md).
