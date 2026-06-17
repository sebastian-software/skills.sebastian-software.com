---
name: s7n-component-primitives
description: |
  Buttons, navigation, dialogs, menus, component primitives, interaction states, component APIs, and reusable UI patterns. Use when implementing or reviewing UI components, button hierarchy, modals, nav bars, command surfaces, component contracts, or design-system primitives.
license: MIT
metadata:
  author: sebastian-software
  version: "1.0"
---

# S7N Component Primitives

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

## References

- [references/buttons.md](references/buttons.md) - button hierarchy, labels, and states.
- [references/navigation.md](references/navigation.md) - navigation structure and affordances.
- [references/dialog-modal.md](references/dialog-modal.md) - dialogs, modals, and confirmation flows.
- [references/component-development.md](references/component-development.md) - component API and implementation rules.
- [references/ux-patterns.md](references/ux-patterns.md) - reusable UX patterns.
