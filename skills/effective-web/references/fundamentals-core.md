# Core Interface Decisions

Use this module for a broad design review before loading a focused layout,
component, accessibility, or motion route. It is the default entry point for
general UI judgment, not a checklist to apply mechanically.

## Decide What Must Become Easier

1. Name the user's primary outcome, the next action, and the highest-cost
   failure.
2. Remove or demote elements that do not improve recognition, orientation,
   trust, comprehension, or recovery.
3. Make the current state, available action, and consequence understandable
   before adding visual polish.
4. Preserve familiar patterns unless evidence shows they harm the task. A novel
   control must repay its learning cost with a clear benefit.

## Shape a Coherent System

- Inspect the existing visual language before inventing tokens, controls, or
  page treatments. Diagnose drift by its source: an absent token, a missing
  component contract, a one-off product requirement, or an unreviewed override.
- Define a small set of purposeful choices for type, color, spacing, elevation,
  radius, icon treatment, and interaction states. Reuse them by role rather
  than copying visual values.
- Use grouping, alignment, hierarchy, and generous but intentional space to
  show relationships. Do not default every group to a card or every important
  action to a saturated button.
- Prefer progressive disclosure when extra controls, explanation, or advanced
  options are not needed for the first successful pass.

## Protect the Interaction Contract

- Actions need visible affordance and feedback. Buttons perform actions; links
  navigate; disabled, loading, error, and success states must preserve the
  user's mental model.
- Keep keyboard focus visible, unobscured, and returned predictably after a
  transient surface closes. Never disable zoom or make pointer precision a
  requirement.
- Treat accessibility, localization, slow loading, and narrow layouts as
  normal states of the design rather than exceptions to patch later.
- Use motion only to clarify change, spatial continuity, or completion; the
  static and reduced-motion paths must carry the same information.

## Review Questions

- Can a new user identify the purpose, current state, next action, and risk in
  a quick scan?
- Are repeated patterns genuinely the same job, with the same semantics and
  state behavior?
- Does each visual emphasis correspond to importance, urgency, or a meaningful
  relationship?
- Can keyboard, zoom, long content, errors, and reduced motion complete the
  same primary task?

For rare design-system diagnosis, composite-widget keyboard mechanics, or
platform-animation details, consult the [deep fundamentals appendix](fundamentals.md)
after identifying the exact concern.
