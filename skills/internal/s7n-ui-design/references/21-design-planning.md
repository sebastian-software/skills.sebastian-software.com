# Design Planning

Plan enough before writing UI code that the first implementation can be
specific. The goal is not to create an iterative polishing workflow. The goal is
to avoid generic first drafts by choosing the right register, structure, and
interaction model from the beginning.

Use this planning pass when the request is net-new, ambiguous, high-stakes, or
visually important. Skip it when the task is a small change inside an existing,
well-understood component.

## Pre-Code Questions

Answer these from the prompt, product context, existing code, or a short user
question when the information cannot be inferred.

1. **Purpose:** What problem does this surface solve?
2. **Primary user:** Who uses it, in what context, and how often?
3. **Primary action:** What is the one action or understanding the design must
   make easiest?
4. **Register:** Is this product, brand, or content-heavy UI?
5. **Content:** What data, text, media, or controls must appear? What are
   realistic minimum, typical, and maximum cases?
6. **States:** What must happen for default, empty, loading, error, success, and
   permission-limited states?
7. **Constraints:** Which design system, components, framework, performance,
   accessibility, i18n, or browser constraints already exist?
8. **Anti-goals:** What would be a wrong direction for this audience or product?

## Decide Before Styling

Before choosing colours, spacing, shadows, or typography, decide:

- The information hierarchy.
- The layout topology: single column, split pane, table, master-detail,
  dashboard grid, wizard, timeline, canvas, or article.
- The interaction model: inline edit, explicit submit, autosave, modal,
  popover, route change, optimistic update, or background task.
- The surface density: sparse, normal, dense, or data-heavy.
- The tone: quiet utility, confident product, instructional, editorial,
  promotional, or immersive.

These decisions make the visual layer follow from the job. Do not start with
card grids, hero templates, gradients, or animation before the surface has a
clear job.

## Adjustment Lenses

Use these lenses before implementation when the brief exposes a directional
risk. They are not separate workflows. Pick the lens that prevents the wrong
first draft.

### Bolder

Use when a brand or launch surface needs a clearer point of view.

- Increase contrast in hierarchy, not random decoration.
- Commit to one stronger composition, colour strategy, image choice, or
  typographic voice.
- Make one thing unmistakably dominant instead of making every section louder.

### Quieter

Use when the surface is too loud for repeated use or high-stakes work.

- Reduce decorative colour, motion, shadows, and competing accents.
- Let product structure, labels, and states carry confidence.
- Keep primary actions clear while making inactive states calmer.

### Distill

Use when complexity is the main risk.

- Remove repeated explanations, duplicate actions, ornamental containers, and
  choices that do not affect the user's next step.
- Combine related controls and reveal secondary options only when needed.
- Preserve capability; remove presentation and decision noise.

## Generic UI Failure Modes

Check these before choosing a visual direction. They are not timeless taste
laws; they are current generated-UI failure modes that often indicate the design
was chosen by category reflex instead of product intent.

- Generic hero plus metrics row plus identical card grid.
- Decorative gradient text, glass panels, or soft shadows with no information
  role.
- Over-rounded cards, nested cards, or every section framed as a card.
- Tiny labels or numbered markers repeated as section scaffolding.
- Warm neutral backgrounds or dark dashboards chosen by category default rather
  than context.
- Placeholder imagery where the subject requires real product, place, person,
  object, or state evidence.
- Dense product surfaces decorated like brand pages.
- Brand surfaces made invisible by excessive product restraint.

If a failure mode appears, do not "polish" around it. Change the brief decision:
register, hierarchy, media strategy, density, or interaction model.

## Compact Design Brief

For ambiguous or net-new UI, write a compact brief before implementation. Keep
it short enough to guide code, not long enough to become a separate project.

Use this structure:

```md
## Design Brief

- Surface: [what is being built]
- Register: [product / brand / content-heavy]
- Primary user and context: [who, where, frequency, state of mind]
- Primary action: [the one thing the design must make easiest]
- Layout strategy: [topology, hierarchy, density, major regions]
- Interaction model: [form submit, inline edit, route, popover, modal, etc.]
- Required states: [default, empty, loading, error, success, permissions]
- Content and media: [real data, copy, images, diagrams, examples]
- Constraints: [design system, framework, accessibility, i18n, performance]
- Anti-goals: [wrong directions to avoid]
```

Write the brief in concrete nouns and decisions. "Modern and clean dashboard"
is not a brief. "Dense product table for finance admins comparing 200 invoices;
primary action is approving selected invoices; errors appear inline per row" is
specific enough to shape UI.

## Brief Quality Check

The brief is ready when it answers:

- What should be visually dominant?
- What should be quiet?
- What state is most likely to break the design?
- Which existing components or tokens should be reused?
- Which reference chapters should be loaded before implementation?

If these answers are still vague, clarify before writing UI code. A precise
brief is faster than rebuilding a generic first draft.

## Design Readiness Check

Do not score the design numerically. Scores encourage post-hoc polishing loops
and make subjective judgment look more exact than it is. Use this check before
implementation to decide whether the first serious UI pass has enough direction.

Mark each dimension as `ready`, `clarify`, or `change direction`:

| Dimension | Ready when |
|-----------|------------|
| Register fit | The surface clearly follows product, brand, or content-heavy priorities |
| Primary action | The one most important action or understanding is obvious |
| Hierarchy | The dominant, secondary, and quiet elements are already decided |
| State coverage | Default, empty, loading, error, success, and permission states are known |
| Interaction risk | Modals, overlays, destructive actions, forms, and async flows have a chosen pattern |
| Content realism | Minimum, typical, maximum, and long-text cases are accounted for |
| Accessibility risk | Contrast, focus, keyboard, semantics, target size, and announcements have no obvious blockers |
| Design-system fit | Existing tokens, components, and comparable screens have been checked |

Interpretation:

- **All ready:** implement the UI.
- **Any clarify:** ask the smallest question that resolves the gap before
  coding.
- **Any change direction:** revise the brief before styling. Do not implement a
  direction that already fails the register, primary action, or interaction
  model.
