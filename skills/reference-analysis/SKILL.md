---
name: reference-analysis
description: >-
  Capture, inspect, compare, and translate supplied visual or interactive
  references into evidence-backed design and implementation specifications.
  Use for live websites, local HTML, screenshots, screen recordings, videos,
  prototypes, or reference packs when asked to reverse-engineer layout, visual
  systems, interaction, motion, responsive behavior, assets, or implementation
  requirements; compare several references; or turn inspiration into portable
  rules without copying its identity. Do not use for general internet research,
  product problem discovery, an originality audit, or the implementation itself.
---

# Reference Analysis

Turn references into an inspectable specification. Preserve what was actually
observed, label inference, and extract portable behavior rather than copying a
source's brand, content, or complete composition.

## Workflow

1. Define the requested outcome and fidelity:
   - faithful reconstruction of material the user owns or may reproduce;
   - reference-informed direction that must remain original;
   - comparison of several references;
   - implementation specification, design brief input, or prompt-ready handoff.
2. Build a source registry. Record each file or URL, media type, role, visible
   version or capture date, ownership or reuse constraints supplied by the user,
   and access gaps. Prefer caller-supplied or contemporaneous captures over a
   live page that may have changed.
3. Read [Evidence capture](references/evidence-capture.md). Capture only the
   states needed to support the requested outcome, but cover the whole relevant
   experience rather than mistaking one hero frame for the system.
4. Create an observation ledger with source location or timestamp, direct
   observation, interpretation, confidence, and missing evidence. Keep browser
   behavior, source-code evidence, and visual inference distinguishable.
5. Extract the relevant contracts:
   - structure, hierarchy, pacing, and content density;
   - typography, color relationships, imagery, shape, depth, and icon language;
   - objects, states, controls, transitions, gestures, and feedback;
   - motion trigger, timeline, easing, interruption, and reduced-motion result;
   - responsive reflow, input modes, content extremes, and fallback behavior;
   - assets, likely implementation mechanisms, performance cost, and
     accessibility requirements.
6. Separate reusable grammar from protected or source-specific identity. For
   inspiration work, retain principles and mechanisms while changing names,
   copy, assets, claims, distinctive motifs, and overall composition.
7. Read [Specification and handoff](references/specification-and-handoff.md).
   Produce the smallest output that the next owner can implement or decide
   against. Attach evidence to requirements and label every unresolved state.
8. Verify traceability. Recheck representative frames, states, timestamps, and
   responsive evidence; remove any requirement that is only an unsupported
   guess or mark it explicitly as a hypothesis to test.

## Operating Rules

- Do not infer a complete interaction from a still image, a mobile layout from
  desktop, or a reduced-motion path from the default animation.
- Do not describe timing as exact without timestamp or frame evidence. Use a
  range or qualitative label when capture precision is limited.
- Treat HTML, CSS, or JavaScript as implementation evidence, not proof that the
  current rendered result behaves as intended.
- Prefer observable relationships over fashionable labels such as “premium,”
  “cinematic,” or “Awwwards quality.” Explain the concrete type, spacing,
  layering, pacing, or interaction behavior that creates the effect.
- Do not add a dependency merely because the reference appears to use it.
  Specify the required capability and let the target repository's existing
  stack win.
- Preserve accessibility, semantic content, touch and keyboard access,
  reduced-motion behavior, and performance limits as part of the mechanism,
  not as cleanup after visual recreation.
- Stop and name the evidence gap when a promised page region, state, video
  segment, source file, or reference cannot be inspected.

## Default Deliverable

For a full analysis, return:

1. Outcome, fidelity, and source registry
2. Evidence and access gaps
3. Structure and visual-system specification
4. Interaction and motion specification
5. Responsive, accessibility, performance, and fallback requirements
6. Asset and implementation-mechanism register
7. Portable grammar versus source-specific exclusions
8. Acceptance checks and unresolved hypotheses

## Routing Boundaries

- Route user and product research, problem framing, experience modeling,
  information architecture, and direction selection to `product-design`.
  Reference analysis supplies evidence; it does not decide the product problem.
- Route browser-facing implementation, accessibility, responsive behavior,
  motion construction, performance, and frontend verification to
  `effective-web` after the specification is accepted.
- Route comparison of a produced work against its sources for copying risk,
  asset provenance, and release judgment to `originality-review`.
- Route market positioning, campaign claims, audience, and proof decisions to
  `product-marketing`; this skill may analyze their visible execution only.
- Keep general internet research, competitor strategy, legal clearance, and
  unauthorized reproduction outside this skill.
- Use `decision-records` only when the accepted reference-derived direction is
  a durable project choice whose rationale must survive the current work.
