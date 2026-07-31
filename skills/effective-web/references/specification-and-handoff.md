# Specification and Handoff

Load this reference when turning captured evidence into a design,
implementation, comparison, or generation brief.

## Build the Observation Ledger

Use one row per meaningful claim:

| Evidence | Observation | Interpretation | Confidence or gap | Resulting requirement |
| --- | --- | --- | --- | --- |
| File, frame, URL region, or timestamp | What is directly visible or inspectable | Why it may work this way | Verified, likely, or unknown | Portable behavior to preserve or test |

Do not let an interpretation silently become an observed fact. Requirements
with weak evidence become bounded hypotheses and acceptance checks.

## Specify the Experience

Select only sections relevant to the task:

### Structure and pacing

- page or screen regions, order, dominant hierarchy, and density;
- repeated modules and intentional rhythm changes;
- sticky, pinned, layered, full-bleed, or nested composition;
- real content requirements that make the layout meaningful.

### Visual system

- typographic roles and contrast rather than guessed font identity;
- color relationships and semantic roles rather than sampled swatches alone;
- spacing, shape, line, depth, texture, image, and icon behavior;
- repeated motif and the conditions under which it changes.

### Interaction and state

- object, trigger, precondition, state transition, feedback, completion, and
  recovery;
- pointer, keyboard, touch, assistive-technology, and programmatic paths;
- loading, empty, error, permission, disabled, and success behavior where shown
  or required by the target.

### Motion timeline

For each effect record:

| Trigger | Start state | Transition | End state | Interruption/reversal | Reduced-motion result |
| --- | --- | --- | --- | --- | --- |

Name the needed capability before a library. Include scroll ownership,
visibility lifecycle, offscreen cost, and static fallback.

### Responsive contract

Describe relationship changes rather than copying device frames:

- what remains invariant;
- what reflows, wraps, collapses, reorders, or becomes scrollable;
- content, container, and viewport conditions that cause the change;
- minimum usable width, shallow viewport, zoom, localization, and input-mode
  expectations;
- unknown ranges that require implementation probes.

### Assets and implementation

Record asset role, provenance status supplied by the user, crop or focal point,
format and resolution needs, responsive variants, loading priority, fallback,
and whether the asset is source-specific and must be replaced.

Separate required behavior from possible mechanisms:

```text
Requirement: scrub a reversible product-state sequence with native scroll.
Possible mechanisms: sticky DOM states, video, image sequence, canvas, or SVG.
Selection evidence: asset availability, accessibility, device budget, and
existing stack.
```

## Preserve Inspiration Without Cloning

Create a transformation matrix:

| Keep as portable grammar | Change materially | Exclude entirely |
| --- | --- | --- |
| hierarchy principle, pacing, interaction mechanism, density relationship | composition, palette, type system, subjects, motifs, content structure | source names, marks, copy, claims, proprietary assets, recognizable identity |

The target may feel related without reproducing the source's complete identity
or distinctive combination. When faithful reproduction is requested, record
the user's supplied ownership or authorization boundary rather than assuming it.

## Finish With Acceptance Checks

Checks must be observable:

- the specified states and interactions can be reached;
- desktop and narrow behavior follow the relationship contract;
- content and semantics survive without optional motion or enhancement;
- timings and ordering match timestamped evidence where fidelity is required;
- source-specific identity and assets are absent from inspiration work;
- performance and accessibility constraints are testable;
- every unresolved inference is named rather than hidden in implementation prose.
