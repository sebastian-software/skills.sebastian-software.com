# Change-Scoped Interface Review

Review the interface behavior a resolved change affects, not the whole product
and not only the final lines. Use this when `effective-delivery` supplies a PR
or branch delta. It owns Git scope, provider state, publication, and the merge
decision; this reference owns browser-interface findings and evidence.

## Require a Checkable Handoff

Obtain base/head identity; separately named local overlays; changed components,
styles, tokens, assets, routes, and strings; stated intent; relevant removed
signals and direct consumers; preview or fixture access; and base evidence for
any proposed Regression. Resolve only a missing item that can change judgment.
Without a checkable delta, use ordinary Design Review without change-status
labels.

## Expand Files into Surfaces

A changed file is evidence; its rendered surfaces are the subject. Start with
changed routes and components, then inspect direct renderers. For shared tokens
or primitives, inspect one additional hop because one line can reach the whole
product.

Keep expansion risk-led: prioritize the stated primary task; choose consumers
that differ by theme, density, content, input, or viewport; inspect at most five
representative consumers unless wider or automated coverage is justified; and
state plausible consumer classes omitted by that bound. A source relationship
proves reach, not clipping, contrast, focus visibility, or motion quality.

## Read Both Sides

Inspect removed lines and base behavior for lost:

- semantics, accessible names, focus, keyboard, announcements, or reduced motion;
- responsive constraints, logical properties, overflow, targets, or collision protection;
- interaction, disabled, loading, empty, error, theme, locale, or narrow states;
- semantic tokens, icon variants, product vocabulary, recovery copy, or translations;
- intrinsic media dimensions, loading boundaries, and animation or observer cleanup.

A removal is a lead, not a finding. Confirm that the behavior mattered and no
equivalent replacement exists; moved labels, consolidated tokens, or native
platform behavior may preserve the contract with less code.

## Classify Causally

- **Introduced:** new code creates the defect, or the promised change omits a
  state needed to make its own feature usable.
- **Regression:** base evidence proves a previously correct interface contract
  was weakened or removed.
- **Pre-existing:** a nearby issue was neither created nor worsened by the delta.

Classify by causal change, not file proximity. A removed token can regress an
unchanged consumer; a defect beside a hunk can remain Pre-existing. Source may
prove a semantic regression when base rendering is unavailable, but not a
runtime visual claim. State that limit. Return consequential Pre-existing items
separately and sparingly; they do not become author blame or merge conditions.

## Check the Promised State

Compare the result with the accepted intent. A new variant may require its
reachable focus, active, disabled, loading, content-length, theme, locale, and
responsive states; a new string may require the product vocabulary and
translation contract; a new flow may require reachable empty, error, retry, and
permission states. Missing delivery inside accepted scope is not scope creep,
but do not demand unreachable states, speculative features, or a redesign.

## Match Evidence to the Claim

Use source evidence for semantics, token reach, state wiring, and structure.
Use a preview, component workshop, fixture, or existing browser check for
rendering and interaction claims. Mark each relevant domain or state:

- **Finding:** inspected evidence supports an actionable problem.
- **Clear:** relevant evidence was inspected and no problem remains.
- **Not reviewed:** evidence was absent, rendering unavailable, or scope bounded it out.

Not reviewed is coverage, not automatically a defect. Never convert missing
verification into a finding or call an unexercised domain Clear.

## Return the Receipt

Return exact scope, representative consumers, exclusions, and unreviewed states;
consolidated Introduced and Regression findings ordered by user impact;
separate consequential Pre-existing observations; exact source/browser evidence
and unavailable checks; and the smallest correction plus closure verification.
Do not impose a finding quota, invent rejected candidates, or hide blockers for
brevity. Mention a rejected candidate only when it explains an important
judgment boundary. Stay read-only unless implementation is separately authorized.
