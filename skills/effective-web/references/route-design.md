# Design Review and Modernization

Use this route to critique, modernize, polish, or quality-gate an existing
experience. Evaluate hierarchy, clarity, coherence, interaction cost, cognitive
load, preservation constraints, and whether the result is good enough to ship.

Do not use this skill as a source archive. Article-derived input has already been distilled into rules, workflows, and references.

## Use First For

- Overall UI reviews, product surface critiques, redesign direction, and visual polish.
- Modernization under brand, content, route, analytics, and accessibility
  preservation constraints.
- Quality gates before shipping a frontend experience.
- Deciding which focused Effective Web route should handle a specific problem.

## Route Specific Work

Use Design Planning from the **Route by Intent** table in
[SKILL.md](../SKILL.md) for a greenfield direction or AI-assisted feature. When
a narrow problem (layout, typography, color, components, forms, tables,
accessibility, motion, SEO, CSS, i18n, copy, states, auth, print, performance,
React, or testing) becomes the primary task, hand off to the matching focused
route instead of expanding this one.

## Review Workflow

1. Read accepted ADRs and existing design, content, brand, and component-system
   evidence before proposing a direction.
2. For an existing experience, classify the work as greenfield, preserve, or
   overhaul and read [Redesign preservation](redesign-preservation.md) before
   changing visual or behavioral contracts.
3. Identify the job-to-be-done, primary user, primary action, and failure modes.
4. Read [Cognitive UX](cognitive-ux.md) when the task involves attention,
   learnability, complex modes, unfamiliar concepts, or a mismatch between the
   system and what users expect. Check whether the UI has one clear information
   hierarchy and one clear next action per state. Remove elements that do not
   clarify, accelerate, reassure, express the intended relationship, or prevent
   mistakes.
5. For generic or agent-generated output, classify findings with
   [UI anti-patterns](ui-antipatterns.md). Fix objective defects first and treat
   stylistic tells as context-dependent advisories or clusters, not taste laws.
6. Route narrow issues through the **Route by Intent** table in
   [SKILL.md](../SKILL.md) instead of expanding this route. Record new durable
   direction or communication decisions through `decision-records` rather than
   a tool-specific memory file.
7. Verify the rendered result and implementation against the accepted direction,
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
| Modernizing an existing experience under preserve/overhaul contracts (brand, IA, copy, analytics, accessibility) | [redesign-preservation.md](redesign-preservation.md) |
| Reviewing generated UI and copy for defects, advisories, clusters, and accepted exceptions | [ui-antipatterns.md](ui-antipatterns.md) |
| Running the final review gates before shipping | [ui-quality-gates.md](ui-quality-gates.md) |
| Attention budgets, satisficing, task grouping, perceptual hierarchy, conventions, mental models, and learnability | [cognitive-ux.md](cognitive-ux.md) |
