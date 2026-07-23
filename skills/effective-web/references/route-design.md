# Design and Review

Use this route as the broad web-design orchestrator. Evaluate the overall shape
of an experience: hierarchy, clarity, coherence, interaction cost, cognitive
load, and whether the result is good enough to ship.

Do not use this skill as a source archive. Article-derived input has already been distilled into rules, workflows, and references.

## Use First For

- Overall UI reviews, product surface critiques, redesign direction, and visual polish.
- Early design planning before choosing layout, component, motion, or copy details.
- AI-assisted features where the task, modality, uncertainty, user control, and
  handoff need to be designed before choosing a chat surface.
- Quality gates before shipping a frontend experience.
- Deciding which focused Effective Web route should handle a specific problem.

## Route Specific Work

When a narrow problem (layout, typography, color, components, forms, tables,
accessibility, motion, SEO, CSS, i18n, copy, states, auth, print, performance,
React, or testing) becomes the primary task, hand off to the matching focused
route rather than expanding this one. Use the **Route by Intent** table in
[SKILL.md](../SKILL.md) to pick the destination; do not re-list the sibling
routes here.

## Review Workflow

1. Read accepted ADRs and existing design, content, brand, and component-system
   evidence before proposing a direction.
2. For an existing experience, classify the work as greenfield, preserve, or
   overhaul and read [Redesign preservation](redesign-preservation.md) before
   changing visual or behavioral contracts.
3. Identify the job-to-be-done, primary user, primary action, and failure modes;
   select the surface register from [Design registers](design-registers.md).
4. Choose a primary direction and compatible axes from
   [Design directions](design-directions.md). Ask one discriminating question
   only when the missing answer would materially change the result.
5. Read [Cognitive UX](cognitive-ux.md) when the task involves attention,
   learnability, complex modes, unfamiliar concepts, or a mismatch between the
   system and what users expect. Check whether the UI has one clear information
   hierarchy and one clear next action per state. Remove elements that do not
   clarify, accelerate, reassure, express the intended relationship, or prevent
   mistakes.
6. For generic or agent-generated output, classify findings with
   [UI anti-patterns](ui-antipatterns.md). Fix objective defects first and treat
   stylistic tells as context-dependent advisories or clusters, not taste laws.
7. Route narrow issues to the focused routes above instead of expanding this
   route. Record new durable direction or communication decisions through
   `decision-records` rather than a tool-specific memory file.
8. Verify the rendered result and implementation against the accepted direction,
   redesign baseline when applicable, and quality gates before considering the
   UI done.

## Baseline Rules

- Every visible element needs a job. Decoration is acceptable only when it improves recognition, trust, orientation, or comprehension.
- Optimize for scanning first, then reading. Users should understand state, next action, and risk without decoding the layout.
- Keep interaction cost low: related controls belong near the content they affect, destructive actions need recoverability, and repeated workflows need density.
- Treat attention as a user resource. Interrupt only when urgency or otherwise
  missed consequential state justifies taking focus.
- Preserve autonomy when emphasizing a likely action, and prefer recognition
  over recall for routine, infrequent, or high-stress work.
- Do not make accessibility, responsive behavior, localization, or loading/error states late-stage patches.
- Prefer fewer stronger patterns over many local exceptions.

## References

Select by the primary concern of the current step; load one module, then add
another only when the work genuinely shifts concern.

| Primary concern | Reference |
|-----------------|-----------|
| Broad UI design decisions, quality heuristics, reduction, and restraint (load the deep appendix only for an identified edge case) | [fundamentals-core.md](fundamentals-core.md) |
| Setting the design intent, register, and decision framing | [design-registers.md](design-registers.md) |
| Choosing combinable directions, axes, ambiguity questions, and conflict resolution | [design-directions.md](design-directions.md) |
| Modernizing an existing experience under preserve/overhaul contracts (brand, IA, copy, analytics, accessibility) | [redesign-preservation.md](redesign-preservation.md) |
| Planning the workflow before implementation (load the deep appendix only for the full question bank, lens detail, and brief templates) | [design-planning-core.md](design-planning-core.md) |
| Reviewing generated UI and copy for defects, advisories, clusters, and accepted exceptions | [ui-antipatterns.md](ui-antipatterns.md) |
| Designing an AI-assisted feature: capabilities, modalities, uncertainty, control, and constraints | [ai-interface-design.md](ai-interface-design.md) |
| Running the final review gates before shipping | [ui-quality-gates.md](ui-quality-gates.md) |
| Attention budgets, satisficing, task grouping, perceptual hierarchy, conventions, mental models, and learnability | [cognitive-ux.md](cognitive-ux.md) |
