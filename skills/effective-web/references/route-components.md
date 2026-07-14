# Component Primitives

Use this skill for reusable UI building blocks and the interaction rules attached to them.

## Workflow

1. Define the component's job, states, inputs, outputs, and failure modes.
2. Pick the native HTML element first; add ARIA only when semantics are missing.
3. Specify default, hover, focus, active, disabled, loading, error, and success states where applicable.
4. Keep component APIs small, semantic, and hard to misuse.
5. Verify keyboard behavior, pointer behavior, responsive behavior, and text overflow.

## Rules

- Use visible text labels where users need recognition. Icon-only controls require a clear accessible name and tooltip when unfamiliar.
- Prefer undo over confirmation for reversible actions.
- Reserve confirmation dialogs for irreversible, high-cost, or batch operations.
- Menus, dialogs, popovers, and navigation need explicit focus management.
- Components must preserve size and mental model during loading and error states.
- Prefer recent interoperable platform primitives over custom state and geometry
  code when the product's Baseline target permits them; preserve semantics and a
  coherent fallback independently of their visual capability.

## References

- [buttons.md](buttons.md) - button hierarchy, labels, and states.
- [navigation.md](navigation.md) - navigation structure and affordances.
- [dialog-modal.md](dialog-modal.md) - dialogs, modals, and confirmation flows.
- [component-development.md](component-development.md) - component API and implementation rules.
- [ux-patterns.md](ux-patterns.md) - reusable UX patterns.
- [platform-feature-radar.md](platform-feature-radar.md) - dated leads for recent
  native controls, state selectors, and positioning capabilities.
