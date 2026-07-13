# UX Patterns

Choose interaction patterns from the user's task, navigation model, content volume, recovery path, and accessibility requirements. Familiar patterns are useful only when their tradeoffs match the workflow.

## Working Rules

- Choose pagination, load more, infinite scroll, filtering, and search from the user's need to compare, resume, scan, or complete. With infinite scroll, keep footer content and recovery actions reachable, and only choose it when users scan rather than seek a specific item.
- Preserve URL state, scroll position, focus position, and back-button behavior when lists or navigation change. Announce added items, filtered counts, and result changes to screen readers through a live region.
- Treat navigation as information architecture and orientation, not decoration. Keep primary navigation visible on larger screens, put menus in expected locations, and always show the current location. Provide local navigation for related content, write short scannable front-loaded labels, signify submenus with a caret, and meet contrast and target-size minimums.
- Keep menus, navigation, footers, and recovery actions reachable. Prefer click or tap activation over hover-only behavior, and avoid deep cascading fly-out menus and novel or gimmicky navigation patterns.
- Make pattern behavior explicit for keyboard, screen-reader, touch, and reduced-motion contexts.
