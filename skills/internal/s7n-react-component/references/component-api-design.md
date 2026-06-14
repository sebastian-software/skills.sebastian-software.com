# Component API Design

Design React component APIs so composition, state, styling, and semantics remain predictable as components are reused.

## Working Rules

- Prefer clear composition over prop surfaces that encode every possible layout.
- Use polymorphic `as` APIs only when the semantic element truly must vary.
- Keep accessible names, roles, focus behavior, and disabled behavior explicit.
- Expose styling hooks without forcing consumers to know private DOM structure.

## Additional Rules

- Advanced composition guidance for separating layout, behavior, and extension points in reusable React component APIs.
- Use as typed polymorphic component API guidance; require semantic safety before adding an `as` prop.
- Swipe-action implementation is useful as a component interaction example; pair with touch, keyboard, reduced-motion, and destructive-action recovery rules.
- Use as component resilience guidance for async states, composition, portals, refs, server/client boundaries, and defensive APIs.
- Preserve semantic HTML through component APIs.
