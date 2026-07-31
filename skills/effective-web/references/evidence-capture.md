# Evidence Capture

Load this reference when a source must be inspected or captured before analysis.
Use the permitted browser, media, filesystem, and document tools available in
the host; do not make one named tool a prerequisite for the skill.

## Choose Evidence by Source

| Source | Minimum useful evidence | Common gap |
| --- | --- | --- |
| Live website | viewport captures, full relevant scroll, interactive states, URL and date | lazy or animated content omitted |
| Local HTML/build | rendered page plus source and console state | source treated as rendered truth |
| Screenshot | pixels, dimensions, crop context, known viewport | interaction and responsive behavior unknown |
| Video/screen recording | duration, representative frames, timestamped transitions, playback direction | timing or offscreen structure guessed |
| Prototype/design file | named frames, components, variants, interactions, annotations | production behavior assumed |
| Mixed reference pack | manifest connecting every artifact to its role | attractive files treated as one coherent system |

## Capture Live and Long Pages

1. Record the exact URL, viewport, zoom, theme, locale, authentication state,
   and capture date.
2. Let fonts and above-the-fold media settle, then scroll through the relevant
   page normally so lazy content, reveal effects, sticky regions, and canvas
   scenes initialize.
3. Capture the full composition and focused regions. When one full-page capture
   is blank, sparse, duplicated, or missing fixed and canvas content, use
   overlapping viewport captures and preserve their top-to-bottom order.
4. Exercise only the states required by the brief: hover and focus, open and
   closed controls, loading and completion, route changes, scroll sequences, or
   responsive navigation.
5. Keep a visible failure log. A blocked route, missing login, unsupported
   codec, or failed canvas capture remains an evidence gap.

Do not hide browser chrome, consent state, injected banners, or loading failure
when they materially affect what the source actually showed.

## Analyze Video and Motion

- Record duration, frame rate when known, viewport or crop, and whether the
  video shows continuous behavior or an edited montage.
- Build a sparse timeline around state changes rather than extracting every
  frame. Include the moment before a transition, the transition, the settled
  state, and any reversal or interruption.
- Cite timestamps for claims about order and approximate duration. Inspect more
  densely only where easing, masking, scroll scrubbing, or a fast handoff makes
  the mechanism ambiguous.
- Distinguish camera or editing motion from interface motion. A zoom added in
  post-production is not evidence that the page itself zooms.
- Treat absent keyboard, touch, mobile, or reduced-motion demonstrations as
  unknown.

## Capture Source and Runtime Together

When code or HTML is available:

- map visible regions to owning elements or components;
- inspect semantic structure, assets, CSS, event ownership, and animation
  mechanisms;
- verify the relevant behavior in the rendered surface;
- record console or network failures that change the observation;
- do not copy selectors, component names, or library choices into the target
  specification unless they are genuine compatibility requirements.

## Minimal Capture Log

For each artifact record:

```text
ID:
Source path or URL:
Captured or observed at:
Viewport/state/timestamp:
What it proves:
What it cannot prove:
Access or quality limits:
```

Delete redundant captures after the evidence set is stable when repository
policy allows it. Preserve only artifacts needed for traceability, review, or
authorized reusable examples.
