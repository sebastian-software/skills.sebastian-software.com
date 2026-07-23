# Responsive Navigation

Use this module after choosing a sound navigation structure and when the
available width or input method changes its presentation.

## Preserve Destinations and Orientation

- Decide which destinations remain directly visible, which can move into a
  labelled disclosure, and how the user returns to the same location. Do not
  make a responsive breakpoint silently remove a primary task.
- Use a real button with `aria-expanded` and `aria-controls` for a disclosure.
  Its label and state must be clear before and after opening.
- Keep the opened panel in a predictable source and focus order. Close it on
  Escape when it behaves as a transient layer, restore focus to its trigger,
  and do not trap focus in an ordinary site-navigation disclosure.
- For horizontally overflowing tabs, preserve a visible current tab and give
  the row a scroll affordance rather than hiding off-screen choices.

## Sticky and Mobile Chrome

- A sticky header needs scroll padding or margins so anchor targets and focus
  targets are not obscured. Account for safe-area insets on fixed mobile bars.
- A bottom tab bar suits a few frequent, top-level destinations; labels remain
  necessary when icons could be ambiguous. Do not turn a long site map into a
  bottom bar.
- Test pointer, keyboard, narrow screens, zoom, long localized labels, and
  browser back/forward behavior.

For menu implementations, scroll-snap tabs, and unusual patterns, consult the
[deep navigation appendix](navigation.md).
