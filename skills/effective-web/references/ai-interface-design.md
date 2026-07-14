# AI Interface Design

Use this reference when a web feature predicts, generates, summarizes,
recommends, or acts on a user's behalf. Start with the user's task and the
consequences of error; do not start with a chat window.

## Capability and task fit

- Name the user outcome, the model's bounded contribution, the authoritative
  data, and the human judgment that must remain outside the model.
- Prefer deterministic UI for deterministic work. A normal form, filter,
  command, search result, or calculation should not become probabilistic merely
  to advertise AI.
- Identify the cost of false positives, false negatives, delay, disclosure, and
  unwanted action. The higher the cost, the more the interface needs evidence,
  review, reversibility, and a non-AI path.
- Design the handoff: where AI starts, where the user verifies or edits, and how
  the user resumes the underlying workflow without losing context.

## Match modality to context

Audit input and output separately:

- **Input constraints:** Are hands available? Is typing practical? Is the source
  already structured, selected, or visible in context?
- **Output constraints:** Can the user safely look at a screen? Do they need a
  glanceable signal, editable draft, comparison, detailed evidence, or audio?
- **Social constraints:** Is speaking or audible output appropriate in the
  user's environment? Could input expose private material nearby?
- **Cognitive load:** Is the user monitoring, deciding quickly, or doing deep
  analysis? Match density, pacing, and persistence to that job.

Choose the smallest fitting surface:

- Inline suggestion or completion for a local, reversible edit.
- Structured controls and previews when inputs, outputs, or constraints are
  known.
- Batch review for repeated proposals that need accept/reject/edit decisions.
- Background status plus notification for long-running work.
- Conversation for genuinely exploratory, ambiguous, iterative work where
  follow-up questions are the interaction model.
- Voice, haptics, or ambient signals only when the physical and social context
  makes them more usable than screen interaction.

## Uncertainty, control, and recovery

- Show what is a suggestion, what source or scope it used, and what will happen
  before an action commits. Do not decorate probabilistic output as settled fact.
- Give users meaningful edit, retry, reject, undo, cancel, and manual paths.
  Confirmation without the ability to inspect the proposed action is not control.
- Preserve user input and intermediate work when generation fails, times out, is
  refused, or produces unusable output.
- Separate progress from theater. Report durable states such as queued,
  working, waiting for approval, partially complete, failed, and complete when
  the system can actually know them.
- Keep high-impact actions explicit and attributable. Log what changed and make
  recovery proportional to the possible harm.

## Streaming and partial output

- Treat streaming as an explicit state machine: queued, streaming, stopped with
  partial output, failed, and complete. Do not present a canceled or interrupted
  response as complete, and preserve the prompt/context so retry does not make
  the user reconstruct their work.
- Auto-follow only while the reader is already near the end. Stop moving the
  viewport when they scroll up, resume only when they return to the end, and
  keep Stop, Retry, and adjacent controls from shifting under pointer or focus.
- Decouple network arrival from rendering. Buffer incremental chunks and batch
  DOM writes to animation frames; extend stable nodes instead of rebuilding the
  whole response for every token. Cancellation must abort the source, clear
  pending buffers, remove transient cursors, and expose the incomplete state.
- Make concurrent streams independent; never let two operations append into the
  same output surface or reuse stale buffers and listeners.
- Use a suitable persistent transcript such as `role="log"` with carefully
  tested polite, non-atomic announcements when updates must be spoken. Avoid
  announcing every token, keep Stop keyboard-reachable, focus newly relevant
  recovery actions intentionally, and respect reduced motion.

## Review checklist

- Would a familiar non-chat pattern serve the task better?
- Can users provide input and consume output in their real environment?
- Is uncertainty visible at the decision point rather than buried in help text?
- Can users inspect, edit, reject, cancel, undo, and take a manual path?
- Does failure preserve their data and place in the workflow?
- Are accessibility, latency, streaming updates, and reduced-motion behavior
  specified for every state?
