# Native Dialog Foundation

Use this module to implement a modal, non-modal dialog, or lightweight popover
with the platform primitive that matches the interaction.

## Choose the Primitive

- Use `<dialog>.showModal()` for an interrupting task that must temporarily
  block the rest of the page. The browser manages the top layer and makes the
  background inert.
- Use `<dialog>.show()` for a persistent non-modal surface when it still needs
  dialog semantics. Use the Popover API for lightweight, non-modal disclosure
  such as menus, tooltips, or pickers that should not become a dialog.
- Do not use a dialog merely to position a card above content. A visual overlay
  does not create a correct focus model.

## Make the Lifecycle Explicit

- Give the surface a clear accessible name, a visible close path, and an
  intentional initial focus target. Restore focus to the trigger or a more
  useful successor when it closes.
- Use `form method="dialog"` and `returnValue` for simple, well-defined dialog
  outcomes. Preserve a normal form path when submission is the task.
- Style `::backdrop` deliberately and guard entry or exit transitions for
  reduced motion. Delay closure only when the state remains unambiguous and
  focus behavior stays correct.

For the choice between inline expansion, a page, confirmation friction, or a
toast, continue with [dialog product decisions](dialog-decisions.md).

For focus edge cases, `closedby` fallback behavior, animations, and full markup
patterns, consult the [deep dialog appendix](dialog-modal.md).
