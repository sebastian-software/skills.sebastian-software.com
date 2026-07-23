# Dialog Product Decisions

Use this module to decide whether a dialog is appropriate and how much friction
the user should face. A dialog is a cost: it interrupts reading, changes focus,
and can hide necessary context.

## Choose the Least Interrupting Surface

- Use inline expansion for reversible detail that benefits from surrounding
  context. Use a new page for deep, multi-step, shareable, or URL-addressable
  work. Use a modal only for a bounded task or consequential decision that needs
  temporary focus.
- Ask whether the user can explain why the interruption appeared, what choice is
  required, what each result means, and how to leave safely. If not, improve the
  flow before tuning the overlay.
- Prefer undo for a reversible destructive action. A confirmation dialog earns
  its friction for irreversible, high-cost, or broad-impact work; its primary
  action must name the consequence rather than say only “OK”.

## Respect Mobile and Notification Context

- Adapt a narrow-screen dialog to content and reachable actions; a full-height
  sheet can be clearer than a tiny centered box. Do not nest modals.
- Use toast notifications for non-blocking feedback, with enough visible time,
  an accessible announcement where appropriate, and a durable alternative for
  consequential messages.

For friction tiers, action-sheet implementation, scroll locking, and extended
notification patterns, consult the [deep dialog appendix](dialog-modal.md).
