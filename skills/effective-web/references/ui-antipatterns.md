# UI Anti-Patterns

Use anti-patterns to expose an unexamined design reflex, not to turn current
taste into permanent law. Read the brief, accepted ADRs, design system,
representative screens, content, and surface register before judging a pattern.

## Classify Before Correcting

| Class | Meaning | Response |
| --- | --- | --- |
| Defect | Observable user harm or broken implementation, such as unreadable contrast, overflow, lost functionality, or an inaccessible control | Treat as blocked or risky according to impact; verify and fix |
| Advisory | A current generated-output tell or weak default that may still be valid in context | Name the reflex and ask what product, audience, or brand decision justifies it |
| Cluster | Several advisory tells reinforce the same generic template or aesthetic | Change the owning direction, hierarchy, media, copy, or interaction decision instead of polishing each symptom |
| Accepted exception | The pattern follows a real task, sequence, brand system, content form, or recorded decision | Keep it, verify execution, and avoid inventing a second system to satisfy the checklist |

Do not escalate an advisory to a defect merely because it is easy to detect.
One familiar font, card, glow, serif headline, or numbered label is not evidence
of generic design. Repetition without purpose and clusters across independent
choices are stronger signals.

## Separate Evidence From Judgment

Use deterministic checks only for claims the implementation can establish:

- broken or placeholder image references;
- contrast against the rendered background;
- text, content, and viewport overflow;
- positioned overlays clipped by an overflow ancestor;
- heading structure, accessible names, focus behavior, and target size;
- long lines, unreadably small text, or destructive tracking and leading;
- values drifting from the owning design tokens or component system;
- core functionality removed rather than adapted for a smaller context.

Use rendered inspection and design judgment for category reflex, specificity,
materiality, typography personality, copy cadence, and whether decoration earns
its cost. A clean static scan cannot prove that the direction fits the brief.
When an automated rule is added, test a true positive, an intentional exception,
and a plausible false positive. Prefer an advisory finding with evidence over a
confident but context-free prohibition.

## Structural and Layout Reflexes

Review these as advisory signals:

- A generic hero, metrics strip, and identical feature-card grid could serve any
  product after replacing the logo and colours.
- Every section becomes a bordered or elevated card; cards are nested inside
  cards instead of grouping through hierarchy, spacing, dividers, or surfaces.
- Each feature repeats the same rounded-square icon tile, heading, and paragraph
  with no relationship to the actual content.
- Tiny tracked eyebrow labels or `01 / 02 / 03` markers scaffold every section.
  Keep numbers when order carries real meaning, such as a process or timeline.
- A thick coloured side stripe decorates rounded cards, list items, or callouts
  without communicating state or category.
- Decorative sparklines and charts imply evidence but do not support a decision.
- Modals become the default container for complex work that deserves inline
  space, a sheet, or a dedicated route.

Ask what information structure would remain if borders, icons, and labels were
removed. If the answer is nothing, redesign the hierarchy rather than replacing
one decoration with another.

## Visual and Typographic Reflexes

- Cream, beige, purple gradients, cyan-on-dark, or a dark dashboard are category
  defaults unless the physical context, brand palette, or content demands them.
- Gradient text, decorative glass, neon glow, blurred orbs, generic diffuse
  shadows, grid overlays, or repeating stripes accumulate without an
  information, depth, or interaction role.
- A long sentence is enlarged to display scale until it dominates or overflows
  the first viewport. Match type scale to copy length and available measure.
- Display tracking is crushed until glyph shapes or word recognition suffer.
- An italic serif hero is used as shorthand for premium or editorial quality.
  Keep it when the editorial or brand register genuinely owns that voice.
- Monospace is used to make an unrelated product appear technical rather than
  for code, identifiers, aligned data, or a documented brand voice.
- One familiar font is blamed for generic output even though hierarchy, role,
  optical sizing, weight, measure, and content are the actual problems.

Do not maintain a blacklist of fonts, colours, or effects. Judge whether the
combination follows the owning system and creates a distinctive, usable result.

## Motion and Interaction Reflexes

- Every section receives the same reveal animation regardless of content.
- Images scale, rotate, or drift on every card hover without indicating an
  action or revealing information.
- Bounce, spring, glow, or continuous motion is applied to frequent task UI.
  Reserve expressive motion for an earned, non-blocking moment and keep the
  reduced-motion path complete.
- Width, height, margin, or padding animation causes avoidable layout work.
- Every action is styled as primary, so the interface has no decision hierarchy.
- Mobile removes important actions because the desktop layout does not fit.

Distinguish style from behavior. A playful spring can be an accepted exception;
hidden functionality, inaccessible motion, or layout jank remains a defect.

## Copy and Marketing Reflexes

Check language together with the recorded audience relationship, form of
address, voice, terminology, claim policy, locale, and channel.

Advisory signals include:

- generic transformation verbs or unsupported status claims replace a concrete
  capability, audience, object, or outcome;
- repeated manufactured contrast such as "not X, but Y" or short rebuttal
  fragments creates the same cadence across sections;
- headings, introductions, labels, helper text, and captions restate one another;
- technical, rebellious, warm, or premium language is performed through stock
  vocabulary rather than product evidence;
- punctuation, sentence length, or rhetorical structure repeats so consistently
  that it sounds generated rather than spoken in the recorded voice.

Do not ban individual words, em dashes, short sentences, humour, or informal
address. Evaluate density and repetition in the relevant language. Rewrite
generic copy with concrete nouns, verbs, evidence, limits, and recovery paths
while preserving intentional `du`/`Sie`, formality, proximity, and terminology.
Record durable voice changes through `decision-records`; keep phrase libraries
and campaign copy in their editorial owners.

## Review Sequence

1. Identify the surface register, primary job, audience, and accepted decisions.
2. Verify objective defects first and classify their user impact.
3. Mark advisory tells without treating them as failures.
4. Look for a cluster across structure, type, colour, material, motion, and copy.
5. Trace a cluster to its owning brief decision and revise that decision.
6. Preserve justified exceptions and verify their execution.
7. Recheck the rendered surface with real content, long text, responsive states,
   keyboard input, reduced motion, and the owning design system.

Report a small number of actionable findings. State the evidence, class, user or
brand impact, and the owning decision to change. Do not return a taste score or
a list of every detectable stylistic feature.
