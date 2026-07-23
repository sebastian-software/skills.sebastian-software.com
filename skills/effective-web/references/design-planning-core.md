# Design Planning Core

Decision rules for planning UI before writing code, so the first implementation
is specific instead of a generic first draft. Load the deep
[design-planning.md](design-planning.md) appendix for the full treatment:
design-intent/browser-evidence protocol, bounded-prototype lifecycle, the
complete pre-code question bank, each adjustment lens in detail, earned delight,
review/change contracts, and the full brief and readiness templates.

Plan when the request is net-new, ambiguous, high-stakes, or visually important.
Skip planning for a small change inside an existing, well-understood component.
The goal is not an iterative polishing loop — it is choosing the right register,
structure, and interaction model from the start.

## Read Before Asking

Read accepted ADRs, the design system, representative screens, content, and
brand guidance first. An accepted decision is a constraint until explicitly
superseded — do not silently redesign around it. Treat design artifacts as
hypotheses about a responsive system, not complete specs; validate them against
realistic content, viewports, inputs, and user settings, but keep accepted
product/brand/design decisions binding.

For net-new or materially changed surfaces run the compact Design Read from
[design-directions.md](design-directions.md). For an existing experience, first
classify it as greenfield, preserve, or overhaul and read
[redesign-preservation.md](redesign-preservation.md); visual modernization does
not authorize a content rewrite, framework migration, or contract change. When
the experience model or direction is still open, route decision-grade
exploration to the `product-design` skill and bring the chosen qualities back.

If a missing answer would materially change layout, interaction, or
communication, ask **one** concise discriminating question; otherwise state a
responsible assumption and proceed. Do not ask users to choose between vague
adjectives or re-answer preserved decisions.

## Pre-Code Questions

Answer from the prompt, product context, or existing code; ask only what cannot
be inferred. Cover: purpose, primary user and context, the one primary action,
register (product / brand / content-heavy), product domain or brand point of
view, required content (min/typical/max cases), states (default, empty, loading,
error, success, permission-limited), existing constraints (design system,
framework, a11y, i18n, performance), device/input context, competing attention,
user mental model, and anti-goals. The full annotated list is in the appendix.

## Decide Before Styling

Before colours, spacing, shadows, or type, decide:

- Information hierarchy — what is dominant, secondary, and quiet.
- Layout topology: single column, split pane, table, master-detail, dashboard
  grid, wizard, timeline, canvas, or article.
- Interaction model: inline edit, explicit submit, autosave, modal, popover,
  route change, optimistic update, or background task. For AI-assisted work pick
  the modality deliberately — do not choose chat merely because an LLM is used.
- Surface density: sparse, normal, dense, or data-heavy.
- Primary (and optional secondary) direction from
  [design-directions.md](design-directions.md), not a fixed style preset.
- Tone, and the meaning of structural devices (numbers, eyebrows, badges,
  dividers should communicate sequence/status/grouping, not decorate).

Do not start with card grids, hero templates, gradients, or animation before the
surface has a clear job.

## Specificity

- **Product surfaces:** specificity comes from the product's world — name domain
  concepts, data shapes (compare rows / monitor exceptions / approve batches /
  debug incidents), and one signature move that could only belong to this
  product. Avoid sidebar-plus-generic-cards and icon-number-label metrics.
- **Brand surfaces:** decide the point of view first — audience and promise,
  concrete voice, the category reflex to avoid, primary credibility evidence,
  and one memorable signal. Let the first viewport express the thesis through
  real evidence, not a headline-stat-gradient default.
- If the only claim is "it looks polished", the direction is still too generic.

## Context Adaptation

Adaptation is not scaling. Moving desktop→mobile, product→print, or
pointer→touch may need a different structure while preserving the same
information architecture. Decide device/viewport, input, use case, connection,
and platform expectations up front. Do not hide core functionality on small
screens — change the interaction model. Use content-driven breakpoints,
container queries for components, media queries for page layout, and
`pointer`/`hover` queries to detect input capability.

## Adjustment Lenses

Pick the lens that prevents the wrong first draft (details in the appendix):

- **Bolder** — a brand/launch surface needs a clearer point of view: raise
  hierarchy contrast, make one thing unmistakably dominant.
- **Quieter** — too loud for repeated/high-stakes use: cut decorative colour,
  motion, and shadows; let structure and states carry confidence.
- **Distill** — complexity is the risk: remove duplicate actions and ornamental
  containers; preserve capability, remove decision noise.
- **Minimalist** — a context lens (editorial/utilitarian/premium), not a
  default: let type, measure, whitespace, and content carry hierarchy. Do not
  apply to dense operational tools or bolder brand pages.

## Anti-Pattern and Readiness Checks

For generic or agent-generated output read
[ui-antipatterns.md](ui-antipatterns.md): separate objective defects from
context-dependent advisories, look for clusters, and preserve patterns justified
by task, register, or accepted decision. If a cluster appears, change the owning
brief decision rather than polishing around it.

Write a **compact design brief** for ambiguous or net-new UI (surface, register,
direction, primary user/action, brand or product signature, layout strategy,
interaction model, required states, content, context adaptation, browser
evidence, constraints, anti-goals) in concrete nouns — the full template is in
the appendix. Record durable register/direction/communication decisions through
`decision-records`.

Then check readiness — mark each as `ready`, `clarify`, or `change direction`:
register fit, primary action, hierarchy, state coverage, interaction risk,
content realism, accessibility risk, design-system fit. All `ready` → implement;
any `clarify` → ask the smallest resolving question; any `change direction` →
revise the brief before styling. Do not score the design numerically.
