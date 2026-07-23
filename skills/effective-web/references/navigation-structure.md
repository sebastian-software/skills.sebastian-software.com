# Navigation Structure

Use this module to choose and mark up a navigation system. Start from the
destination and frequency of use, not a preferred visual pattern.

## Choose the Smallest Familiar Pattern

- Use a horizontal list for a small, stable set of top-level destinations; use
  a sidebar when sections are numerous, persistent, or hierarchical.
- Use tabs only for peer views of the same object or content area, not as a
  substitute for global navigation. Use breadcrumbs for location and upward
  traversal, not for primary tasks.
- A disclosure or menu is justified when it reduces genuine density. Do not
  hide common destinations behind a generic icon on wide screens without a
  clear product reason.
- Avoid deep cascading fly-outs, vague labels, and invented patterns. Prefer a
  searchable or indexable structure when the information architecture is large.

## Mark It Up for Orientation

- Use `<nav>` with an accessible label when several landmarks exist, and use a
  list for a set of links. Links navigate; buttons only open or change local UI.
- Expose the current destination with `aria-current="page"` (or the appropriate
  current value). Provide a skip link before repeated primary navigation.
- Keep the destination, visible label, URL, and page heading consistent so a
  user can orient after following a link or returning with browser history.

## Check

Verify landmark names, source and focus order, visible current state, long
labels, keyboard access, and whether the pattern still works when JavaScript or
hover is unavailable.

For a change driven by available width, coarse pointers, a sticky header, or a
mobile bar, continue with [responsive navigation](navigation-responsive.md).

For uncommon menu patterns, sticky-header details, or an expanded anti-pattern
catalog, consult the [deep navigation appendix](navigation.md).
