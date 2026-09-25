# Browser Print Scale Calibration

Safari/WebKit can enlarge a **narrow** fixed-format document even when the
native dialog shows the expected paper and 100% scale. Do not diagnose that
result as a font-size, paper-size, or `@page` margin error before measuring it:
WebKit retains a legacy automatic print-scale heuristic for narrow layouts.
Its current source retains a 1.25 minimum print shrink factor; the resulting
automatic scale still depends on the content width and printable area.

Keep these independent layers separate:

| Layer | What it controls | What it does not prove |
| --- | --- | --- |
| CSS absolute units | CSS maps `1in` to `96px` and `1pt` to `1/72in`. | That the browser will emit content at that physical size after its print layout. |
| `@page` margins | The page's physical content origin and available paper area. | That descendants were not automatically scaled; correct margins can coexist with enlarged content. |
| Browser shrink-to-fit | A browser's automatic layout/print scaling when its computed content does not match the printable area. | A user-selected or generator scale. In current WebKit, the legacy minimum layout factor can make narrow content appear enlarged. |
| Print-dialog or PDF-generator scale | A separate explicit output setting; Playwright's PDF scale controls Chromium generation. | That WebKit's automatic factor is disabled: Safari's 100% native-dialog setting preserves it. |

For a fixed paper design, make the **outer** print wrapper exactly the physical
printable width. On A4 with 20mm left and right margins, that is
`210mm - 20mm - 20mm = 170mm`:

```css
@page {
  size: A4 portrait;
  margin: 20mm;
}

@media print {
  .print-document {
    box-sizing: border-box;
    width: 170mm; /* A4 width − left @page margin − right @page margin */
    max-width: none;
  }

  .print-document__measure {
    max-inline-size: 140mm; /* Deliberately narrower reading measure. */
  }
}
```

- Derive a new outer width for Letter, landscape, or asymmetric margins. Include
  its borders and padding with `border-box` so the declared width remains the
  physical width.
- Do not substitute `width: 100%`: WebKit may resolve it against its internally
  widened print layout, not the physical printable width.
- Keep a deliberately narrow column on an inner element, then recheck wrapping
  and pagination after adding the outer wrapper.
- Do not compensate with a fixed `107%`, `transform: scale()`, a Safari-only
  CSS hack, or user-agent sniffing. The automatic factor is content-dependent;
  transforms do not reflow pagination; and no robust CSS query identifies
  Safari. The physical outer-width constraint is browser-neutral and leaves
  Chromium and Firefox's normal absolute-unit mapping unchanged.

Use the [minimal calibration fixture](../fixtures/print-webkit-scale-calibration.html) to
compare the narrow 140mm case with the 170mm outer-wrapper case. Its five
one-inch vector bars (`25.4mm`, `1in`, `72pt`, `96px`, and `6rem` at a 16px root)
should measure 72 PDF points; its 90px control should measure 67.5 points.

## Verification

When physical scale or Safari parity matters, print the fixture and real
artifact to PDF from native Safari with recorded paper, margins, and dialog
settings. Measure a known vector length; a raster screenshot cannot separate
content scaling from display scaling. Compare native Firefox output when
cross-engine physical parity is required. Chromium PDF generation does not
emulate Safari printing.

## Production Sources

- [CSS Values and Units Level 4: absolute lengths and resolution units](https://www.w3.org/TR/css-values-4/#absolute-lengths) — CSS reference units, including `px`, `pt`, and `dpi`
- [CSS Paged Media Module Level 3](https://www.w3.org/TR/css-page-3/) — page-based media rules and the `@page` model
- [WebKit print shrink factors](https://github.com/WebKit/WebKit/blob/main/Source/WebCore/page/PrintContext.h#L93-L104) and [automatic-scale calculation](https://github.com/WebKit/WebKit/blob/main/Source/WebCore/page/PrintContext.cpp#L218-L253) — current legacy layout and scale behavior
- [WebKit bug 29042](https://bugs.webkit.org/show_bug.cgi?id=29042) — historical request for predictable custom print shrink factors
- [Chromium's inherited-heuristic correction](https://chromium.googlesource.com/chromium/src/+/f6529c7990744370869e4ab2794caae6c46ba044%5E%21/) — 96px/72pt conversion and replacement of the old 1.25 factor
