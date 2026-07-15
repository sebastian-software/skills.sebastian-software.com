# Design Planning

Plan enough before writing UI code that the first implementation can be
specific. The goal is not to create an iterative polishing workflow. The goal is
to avoid generic first drafts by choosing the right register, structure, and
interaction model from the beginning.

Use this planning pass when the request is net-new, ambiguous, high-stakes, or
visually important. Skip it when the task is a small change inside an existing,
well-understood component.

## Decision Sources and Design Read

Before asking preference questions, read accepted ADRs, the existing design
system, representative screens, content, and brand or editorial guidance. An
accepted decision is a constraint until it is explicitly superseded; do not
silently redesign around it.

## Design Intent and Browser Evidence

Treat design artifacts as hypotheses about a responsive system, not complete
descriptions of every browser condition. Keep accepted product, brand, and
design decisions binding while validating the proposed implementation with
realistic content, viewports, inputs, user settings, and browser behavior.

When browser evidence requires a different implementation:

- Preserve the underlying intent rather than copying the supplied geometry.
- Record the observed constraint, affected users or states, simpler option,
  agreed divergence, and resulting behavior.
- Show the behavior in a resizable browser example when a static screenshot
  cannot communicate the tradeoff.
- Ask for approval when the change alters product intent, scope, content, or an
  accepted decision. Do not use "the browser is the source of truth" as license
  to make those changes silently.

For net-new or materially changed surfaces, use the compact Design Read from
[Design directions](design-directions.md): surface register, audience, primary
job, primary direction, expression, density, motion, depth, communication,
signature, and category default to avoid.

For an existing experience, first classify the work as greenfield, preserve, or
overhaul and read [Redesign preservation](redesign-preservation.md). Capture the
smallest baseline that protects routes, information architecture, behavior,
brand, communication, analytics, accessibility, SEO, and operational contracts
affected by the work. Visual modernization does not silently authorize a content
rewrite, framework migration, or contract change.

If a missing answer would materially change the layout, interaction, or
communication direction, ask one concise discriminating question. Otherwise
state a responsible assumption and proceed. Do not ask users to choose between
vague adjectives or re-answer decisions already preserved in the project.

## Pre-Code Questions

Answer these from the prompt, product context, existing code, or a short user
question when the information cannot be inferred.

1. **Purpose:** What problem does this surface solve?
2. **Primary user:** Who uses it, in what context, and how often?
3. **Primary action:** What is the one action or understanding the design must
   make easiest?
4. **Register:** Is this product, brand, or content-heavy UI?
5. **Product domain:** For product surfaces, what domain concepts, data shapes,
   workflows, and user vocabulary should make this feel specific?
6. **Brand point of view:** For brand surfaces, what should make this feel
   specific rather than like the category default?
7. **Content:** What data, text, media, or controls must appear? What are
   realistic minimum, typical, and maximum cases?
8. **States:** What must happen for default, empty, loading, error, success, and
   permission-limited states?
9. **Constraints:** Which design system, components, framework, performance,
   accessibility, i18n, or browser constraints already exist?
10. **Context:** Which devices, inputs, orientation, connection, and physical
    usage conditions matter?
11. **Attention:** What may already distract, fatigue, interrupt, or reduce the
    user's ability to interpret this surface?
12. **Mental model:** Which system concepts and interaction expectations do users
    bring, and which unfamiliar gap must the design bridge?
13. **Anti-goals:** What would be a wrong direction for this audience or product?
14. **Modality:** Can users provide input and consume output through the proposed
    interface in their real physical, social, and cognitive context?

## Visual Decomposition and Oversight Audit

For net-new, ambiguous, visually important, or risky surfaces, decompose the
design before turning it into tickets or production components. Keep the pass
rough and decision-oriented:

- Mark page regions, layout systems, reusable patterns, global rules, content
  dependencies, and component ownership boundaries.
- Identify behavior that a static frame cannot answer, such as wrapping,
  reordering, scrolling, sticky positioning, overlap, disclosure, and focus.
- Check minimum, typical, and maximum CMS content; localization and long words;
  source, reading, and focus order; hidden or duplicated content; contradictory
  responsive states; fixed dimensions; asset constraints; zoom; short
  viewports; and keyboard, touch, pointer, and reduced-motion input.
- Resolve likely design mistakes and requirement gaps with the owning designer
  or stakeholder before writing compensating CSS.
- Convert only the remaining implementation uncertainty into a bounded
  prototype. Do not prototype decisions that existing evidence already settles.

## Bounded Browser Prototypes

Use a prototype to answer one named layout or interaction question. State its
hypothesis, focus, non-goals, fidelity, and exit condition before building it.
Use realistic semantics and enough representative content to test the behavior,
but keep the artifact reversible and intentionally cheaper than production.

Create a small local prototype autonomously when it stays within the accepted
intent and can be discarded safely. Ask before continuing when its result would
change product intent, scope, content, or an accepted decision.

Close the prototype with one explicit outcome:

- **Discard:** the idea failed or the question no longer matters.
- **Rebuild:** preserve the learned behavior, then implement it with production
  semantics, tokens, support policy, accessibility, and ownership.
- **Productionize:** retain code only when the prototype became sufficiently
  representative, then review it as production code and replace rough values,
  shortcuts, fixtures, and assumptions.

Feed the conclusion back into the design brief, implementation plan, and any
durable decision record. Do not leave the prototype as an unexplained parallel
implementation.

## Decide Before Styling

Before choosing colours, spacing, shadows, or typography, decide:

- The information hierarchy.
- The layout topology: single column, split pane, table, master-detail,
  dashboard grid, wizard, timeline, canvas, or article.
- The interaction model: inline edit, explicit submit, autosave, modal,
  popover, route change, optimistic update, or background task.
- For AI-assisted work, the interface modality: inline suggestion, structured
  control, preview-and-approve flow, batch action, conversation, voice, or a
  combination. Do not choose chat merely because the capability uses an LLM.
- The surface density: sparse, normal, dense, or data-heavy.
- The primary and optional secondary direction, using
  [Design directions](design-directions.md) rather than a fixed style preset.
- The tone: quiet utility, confident product, instructional, editorial,
  promotional, or immersive, aligned with recorded audience relationship,
  form of address, voice, and channel exceptions.

These decisions make the visual layer follow from the job. Do not start with
card grids, hero templates, gradients, or animation before the surface has a
clear job.

## Product Domain Specificity

For dashboards, admin panels, tools, and data interfaces, specificity comes from
the product's world, not from adding decoration. Before choosing layout or
tokens, name:

- Domain concepts: the objects, verbs, roles, and constraints users already
  think in.
- Data shapes: whether users compare rows, monitor exceptions, inspect
  timelines, approve batches, configure settings, or debug incidents.
- Signature opportunity: one visual, structural, or interaction decision that
  could only belong to this product.
- Obvious defaults to avoid: sidebar plus generic cards, icon-number-label
  metrics, charts without decisions, status colours without workflow meaning.

The signature does not need to be loud. It might be a domain-specific queue, a
timeline shaped around the real process, a comparison surface tuned to the data,
or token names that reflect actual product semantics. If the product name were
removed, the main structure should still hint at what the tool is for.

## Brand Point of View

For brand surfaces, decide the point of view before layout and styling:

- Audience and promise: who is being addressed, and what should they believe
  after the first viewport?
- Voice: choose concrete language such as precise, physical, rebellious,
  editorial, calm, generous, technical, or ceremonial; avoid empty style labels.
- Category reflex to avoid: name the expected palette, type, layout, imagery, or
  hero pattern that would make the surface feel interchangeable.
- Primary evidence: identify the product, place, person, object, screenshot,
  diagram, or real outcome that should carry credibility.
- Memorable signal: choose one dominant design move the rest of the surface can
  support.

If the point of view is unknown, keep the surface restrained and ask the
smallest question that reveals audience, voice, evidence, or anti-goal. Do not
fill the gap with a generic category template.

## Context Adaptation

Adaptation is not scaling. A design that moves from desktop to mobile, product
to print, app shell to email, or pointer to touch may need a different structure
while preserving the same information architecture.

Decide the target context before implementation:

- **Device and viewport:** phone, tablet, laptop, wide desktop, TV, print, email.
- **Input:** touch, mouse, keyboard, stylus, voice, mixed input.
- **Use case:** quick glance, repeated task, focused reading, data comparison,
  presentation, offline use.
- **Connection and device power:** fast desktop, low-end mobile, slow network,
  offline-capable.
- **Platform expectations:** bottom navigation, side panels, sheets, menus,
  keyboard shortcuts, print headers, email-safe layouts.

Rules:

- Do not hide core functionality on smaller screens; change the interaction
  model so it still works.
- Use content-driven breakpoints: resize until the content breaks, then add a
  breakpoint.
- Use container queries for reusable components and media queries for page-level
  layout decisions.
- Detect input capability with `pointer` and `hover` queries. Screen size alone
  does not tell you whether hover, touch, or keyboard is available.
- Preserve the same conceptual model across contexts. A mobile version can
  reveal less at once, but it should not become a different product.

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

### Minimalist

Use when the surface should feel editorial, utilitarian, calm, or premium
through restraint. This is a context lens, not the default for all products.

- Let typography, measure, alignment, whitespace, and content structure carry
  most of the hierarchy.
- Use a narrow palette and scarce accents; colour should identify action,
  state, or brand voice, not decorate every section.
- Prefer flat surfaces, fine dividers, and subtle elevation over heavy shadows,
  glass effects, and gradient spectacle.
- Keep component shapes crisp and modest. Avoid turning every badge, card, or
  button into a pill unless the existing system already uses that language.
- Use realistic content and concrete labels. Minimalism collapses when copy is
  vague.

Do not apply this lens to dense operational tools that need stronger scanning
affordances, brand pages that need a bolder point of view, or consumer products
where warmth, illustration, or expressiveness is part of the value.

## UI Anti-Pattern Check

For generic or agent-generated output, read
[UI anti-patterns](ui-antipatterns.md). Separate objective defects from
context-dependent advisories, look for clusters across independent choices, and
preserve patterns justified by the task, register, design system, or accepted
decision. If a cluster appears, do not polish around it. Change the owning brief
decision: register, hierarchy, media strategy, density, communication, or
interaction model.

## Specificity Check

Before implementation, ask what makes the design specific to this product,
audience, and moment. The answer does not have to be loud.

Good specificity can come from:

- A product flow that exposes exactly the right next action and hides the rest.
- A comparison surface tuned to the real data users scan.
- An empty state that teaches the actual component in context.
- Navigation and data presentation that reflect the product's mental model, not
  generic application scaffolding.
- A brand surface anchored by real product, place, person, object, or outcome
  evidence.
- A typographic, colour, spacing, or imagery decision that follows the brand
  point of view rather than the category default.
- A content-heavy surface whose navigation, examples, and reading rhythm make
  the material easier to trust.

If the only answer is "it looks polished", the direction is still too generic.
Clarify register, audience, evidence, hierarchy, or interaction model before
writing UI code.

## Earned Delight

Plan delight only where the moment earns it. Delight should make the right
design more memorable, not compensate for a weak flow.

Good moments:

- First successful action.
- Completion of meaningful work.
- Helpful recovery after an error.
- Empty states that invite a useful first step.
- Brand moments where the surface is meant to be remembered.

Rules:

- Never delay core functionality for delight.
- Match the emotional context. Do not make high-stakes errors playful.
- Keep product delight specific and brief; repeated task UI should remain quiet.
- Avoid generic joke copy and novelty loading messages. The detail should be
  specific to what the product actually does.
- Respect reduced motion and performance budgets.

## Review and Change Contracts

Do not hand a visual build over as a bare URL. Send a compact review brief that
states:

- What is complete and ready to inspect.
- Which feedback is needed now and which areas are intentionally out of scope.
- Which responsive, interaction, accessibility, or browser evidence matters.
- Which joint decisions explain intentional divergence from earlier artifacts.
- Which unresolved questions need one named decision.

Use a short recording or resizable preview when behavior matters, and preserve
the conclusions in a written thread or decision record. Escalate requirement,
accessibility, and primary-flow problems immediately; batch cosmetic findings
when delay will not hide user harm or rework.

For a late request, record the desired outcome, source, evidence, expected cost
and risk, displaced work, decision owner, and the funded planning boundary or
condition for reconsideration. Do not let private messages silently expand the
active implementation scope.

When a deadline requires a bounded compromise, record the acceptable current
state, desired state, known limitation, owner, and concrete follow-up trigger.
Do not label invisible debt as pragmatic delivery.

## Compact Design Brief

For ambiguous or net-new UI, write a compact brief before implementation. Keep
it short enough to guide code, not long enough to become a separate project.

Use this structure:

```md
## Design Brief

- Surface: [what is being built]
- Register: [product / brand / content-heavy]
- Direction: [primary direction, optional secondary influence, and why]
- Primary user and context: [who, where, frequency, state of mind]
- Primary action: [the one thing the design must make easiest]
- Brand point of view: [audience, voice, category reflex to avoid, memorable signal; omit when not relevant]
- Product signature: [domain concepts, data shape, default pattern to avoid; omit when not relevant]
- Layout strategy: [topology, hierarchy, density, major regions]
- Interaction model: [form submit, inline edit, route, popover, modal, etc.]
- Required states: [default, empty, loading, error, success, permissions]
- Content and media: [real data, copy, images, diagrams, examples]
- Context adaptation: [devices, inputs, orientation, connection, platform expectations]
- Browser evidence: [responsive constraints, tested behavior, and agreed divergence from design artifacts]
- Open behavior questions: [bounded prototype hypothesis and exit condition; omit when none]
- Communication: [audience relationship, form of address, stable voice, and state/channel tone constraints]
- Constraints: [design system, framework, accessibility, i18n, performance]
- Anti-goals: [wrong directions to avoid]
```

Write the brief in concrete nouns and decisions. "Modern and clean dashboard"
is not a brief. "Dense product table for finance admins comparing 200 invoices;
primary action is approving selected invoices; errors appear inline per row" is
specific enough to shape UI.

When the brief establishes or changes a durable register, audience relationship,
direction, density, motion, depth, or cross-channel communication choice, use
`decision-records` to record its rationale, alternatives, consequences, and
review triggers. Keep exact token values and copy libraries in their owning
artifacts. Do not create an `effective-web` or design-specific dot folder.

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
