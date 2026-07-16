# Line Height and Measure

Treat typeface, font size, line length, and line height as one system. Tune
leading after the text role, typeface, size, and measure are known; do not apply
one ratio or a viewport table to every text style.

## Contents

- [Decision Model](#decision-model)
- [Starting Ranges](#starting-ranges)
- [Adapt to Measure](#adapt-to-measure)
- [Adapt to Font Size and Metrics](#adapt-to-font-size-and-metrics)
- [CSS Validity and Inheritance](#css-validity-and-inheritance)
- [WCAG Requirements](#wcag-requirements)
- [Verification](#verification)
- [Sources](#sources)

## Decision Model

1. Choose and load the real typeface plus representative fallbacks. Typeface
   width, x-height, weight, script coverage, and glyph metrics change the
   apparent density even at the same `font-size` and `line-height`.
2. Classify the text role: single-line control, multiline UI copy, heading,
   lead, body prose, code, caption, or dense data.
3. Set the font size and weight for that role.
4. Bound the actual measure. Use the width of the text block, not the viewport,
   as the relevant input. Prefer narrowing an excessively wide reading column
   before compensating with extreme leading.
5. Tune the line height. Longer reading lines often benefit from more leading
   because the return sweep is longer; large display type usually needs a
   smaller unitless ratio because its absolute line box is already large.
6. Verify with real content and fonts. Treat formulas and ranges as hypotheses,
   not substitutes for visual, accessibility, and reading tests.

The interaction is real, but the exact optimum is not universal. Published
recommendations range from roughly `1.2–1.45` for most text to `1.5–1.6` for
long web-reading lines. Reading studies also report different outcomes by
task, script, medium, and preference. Encode tolerances and role-specific
defaults rather than claiming one scientifically ideal table.

## Starting Ranges

Use these only to begin testing:

| Role and likely wrapping | Initial unitless range | Main checks |
| --- | --- | --- |
| Single-line buttons, labels, counters | `1–1.2` | Glyph clipping, fallback metrics, text-spacing override, localization that forces wrapping |
| Multiline UI copy, captions, compact cards | `1.25–1.45` | Touch density, three-plus lines, translated text, error/help states |
| Large headings and display text | `1–1.2` | Ascenders, descenders, accents, fallback fonts, balanced wraps, narrow containers |
| Leads and medium display copy | `1.2–1.45` | Weight, line count, paragraph separation, actual measure |
| Body prose around `45–75ch` | `1.4–1.65` | Typeface color, return sweep, long paragraphs, user overrides |

Do not infer line height from line length alone. A wide or large-x-height face,
heavy weight, uppercase text, code, mixed scripts, or dense diacritics can move
the useful range. A heading that is one line at one width and four lines in a
translation needs multiline testing even if its nominal role is “display.”

## Adapt to Measure

Prefer a small number of unitless steps. This preserves unitless inheritance
and makes the design intent reviewable:

```css
.prose {
  container-type: inline-size;
  max-inline-size: 70ch;
}

.prose :where(p, li, blockquote) {
  line-height: 1.4;
}

@container (inline-size >= 45ch) {
  .prose :where(p, li, blockquote) {
    line-height: 1.5;
  }
}

@container (inline-size >= 60ch) {
  .prose :where(p, li, blockquote) {
    line-height: 1.58;
  }
}
```

Use thresholds that match the real text measure and typeface. This pattern
should normally stop once the prose reaches its maximum measure. If the
container continues growing while the text column is capped, the container is
no longer a truthful proxy for line length.

Smooth interpolation is possible, but it changes `line-height` from a number
to a length because container query units are lengths:

```css
.prose {
  container-type: inline-size;
  max-inline-size: 70ch;
}

.prose :where(p, li, blockquote) {
  line-height: clamp(1.4em, calc(1.25em + 0.8cqi), 1.6em);
}
```

Apply the `cqi` expression to descendants of the query container. Container
units resolve against the nearest eligible ancestor container, not the element
that establishes containment for its own descendants. With no eligible
ancestor, container units fall back to the small viewport dimension.

Prefer stepped unitless values unless smooth interpolation produces a visible
benefit. The length-based version inherits as a computed length, so re-declare
it on descendants or text roles that change font size. Do not apply the body
formula blindly to headings, controls, code, or nested components.

## Adapt to Font Size and Metrics

Pair font size and leading in role tokens. As font size increases, absolute
line height should still increase, but its unitless ratio commonly decreases:

```css
:root {
  --text-body-size: 1rem;
  --text-body-leading: 1.5;
  --text-heading-size: clamp(2rem, 1.4rem + 2vw, 4rem);
  --text-heading-leading: 1.08;
}
```

An x-height-based approximation such as `calc(4px + 2ex)` can make the ratio
tighten as the font grows and respond to the chosen face's x-height. Treat it
as a font-specific experiment, not a universal formula:

```css
.display-heading {
  font-size: var(--text-heading-size);
  line-height: calc(4px + 2ex);
}
```

Because this computes to a length, descendants inherit the computed result,
not the formula relative to their own font. Set it alongside each affected
font-size role, retune the fixed term for every real/fallback font set, and test
accents, diacritics, inline emphasis, and multiline headings. Prefer explicit
unitless role tokens when the metric formula does not clearly outperform them.

## CSS Validity and Inheritance

`line-height` accepts `normal`, a number, or a length/percentage. Math-function
arguments must have compatible types.

```css
/* Invalid: numbers and a length cannot be added or clamped together. */
line-height: clamp(1.35, 1.2 + 0.6cqi, 1.6);

/* Valid length result, with the inheritance caveat described above. */
line-height: clamp(1.35em, calc(1.2em + 0.6cqi), 1.6em);
```

Use unitless values by default for inherited typography because descendants
multiply the number by their own font size. Do not turn that preference into
“always unitless”: fluid measure-aware formulas necessarily return lengths
unless implemented as discrete number changes through container queries.

Avoid fixed-height text containers, clipping, line clamps on essential text,
and geometry that assumes one authored line height. User styles must be able to
increase text spacing without losing content or functionality.

## WCAG Requirements

- WCAG 2.2 SC 1.4.12 (AA) does **not** require authors to set all text to
  `line-height: 1.5`. It requires content to survive a user override to at least
  `1.5` times font size, paragraph spacing of at least `2` times font size,
  letter spacing of `0.12em`, and word spacing of `0.16em` without loss of
  content or functionality.
- WCAG 2.2 SC 1.4.8 (AAA) requires a mechanism that can achieve, for blocks of
  text, a width no greater than 80 characters (40 for CJK), line spacing of at
  least 1.5, and paragraph spacing at least 1.5 times larger than line spacing.
  The authored default is not required to use those values.
- Language and writing-system exceptions matter. Do not impose Latin paragraph
  spacing or line-length assumptions on scripts that use different conventions.

A body default near `1.5` remains a useful robust starting point when only one
value is available. Treat that as a design heuristic, not as the literal AA
conformance requirement.

## Verification

- Render the actual production and fallback fonts, not only a design-tool
  approximation.
- Test short, representative, and very long paragraphs at continuous container
  widths, including just around each leading threshold.
- Test 200% and 400% zoom, larger default text, and WCAG 1.4.12 spacing
  overrides. Confirm no clipping, overlap, lost controls, or forced
  bidirectional scrolling.
- Test headings with two to four lines, accents, deep descenders, uppercase,
  mixed weights, inline code, links, superscripts, and supported scripts.
- Compare typographic color and return-sweep comfort; do not optimize only for
  reading speed or only for subjective airiness.
- Check that the line-height rule follows the actual text column when a prose
  component sits inside a wider shell, grid, sidebar, or nested container.
- Revalidate after any font, weight, font-size, measure, language, or content
  density change.

## Sources

- [Tim Brown: Molten leading](https://tbrown.org/11/) - original size/leading/measure model.
- [Oliver Schöndorfer: The ideal line length and line height](https://pimpmytype.com/line-length-line-height/) - typeface- and measure-sensitive web practice.
- [Matthew Butterick: Line spacing](https://practicaltypography.com/line-spacing.html) and [line length](https://practicaltypography.com/line-length.html) - contrasting practical ranges.
- [Aleksandr Hovhannisyan: Do not use a fixed line height](https://www.aleksandrhovhannisyan.com/blog/dont-use-a-fixed-line-height/) - size-aware ratios and the `ex` approximation with inheritance caveats.
- [CSS Inline Layout Module Level 3](https://www.w3.org/TR/css3-linebox/#line-height-property) - accepted value types and inheritance behavior.
- [CSS Values and Units Level 4](https://www.w3.org/TR/css-values-4/#calc-type-checking) - math-function type compatibility.
- [CSS Containment Level 3](https://www.w3.org/TR/css-contain-3/#container-lengths) - container-unit resolution and fallback.
- [WCAG 2.2 Understanding 1.4.12](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing) and [1.4.8](https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation) - actual accessibility obligations.
- [Shaikh and Chaparro: Effects of line length on online news reading](https://doi.org/10.1177/154193120504900514) - evidence that speed, comprehension, and preference do not yield one universal optimum.
