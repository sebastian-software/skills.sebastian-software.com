# CRM Automations

## Design an automation

Useful triggers include valid form submission, meeting booked or moved, contact
created, opportunity stage changed, or follow-up overdue. For each trigger,
state the condition, expected action, repeat behavior, owner, and recovery path.

| Part | Question |
| --- | --- |
| Trigger | Which distinct event starts the flow? |
| Filter | Which records qualify? |
| Lookup | Does the contact or opportunity already exist? |
| Change | Which fields change and from what source? |
| Repeat | What happens if the event is delivered again? |
| Failure | Who sees the error and how is it repaired? |

Do not automate a process whose human rules are still unclear. If a field update
triggers the same automation, guard against loops with stable IDs, state checks,
and idempotent actions. Rate-limit alerts so one fault cannot flood the team.

## Pattern 1: New inquiry

1. Receive the event and retain a technical event ID.
2. Find the contact through a stable identifier; update only missing or reliably
   newer data.
3. Find an active matching opportunity; create one only if needed.
4. Save campaign source without overwriting the original acquisition source.
5. Assign an owner using a documented rule.
6. Create a due first-contact task without duplicating it on replay.
7. Send an acknowledgment only when channel and contact basis allow it.
8. Route errors and affected record IDs into a workable exception view.

## Pattern 2: Meeting change

Find the opportunity using meeting or contact ID. Update date and status, then
create or move the preparation task. A rescheduled meeting should not count as a
no-show. After a real no-show, create an appropriate follow-up task. A changed
appointment must not create a new opportunity each time.

## Pattern 3: Stage change

On qualification, check required facts and assign the next role. On win, trigger
delivery handoff. On loss, require a reason and close obsolete sales tasks
unless a distinct future task remains. Every action needs a guard that prevents
re-trigger loops.

## Reliability and review

Use an event ID as an idempotency key when available; otherwise combine stable
record key, event type, and a defined time window. Log event time, action,
target, and result without unnecessary personal data. Limit automatic retries
and provide a human exception queue. Define replay and rollback procedures.

Check error records, duplicate contacts, unowned opportunities, and overdue
tasks regularly. On a change, record version and owner, exercise new, existing,
incomplete, and duplicate cases, then inspect real CRM objects after activation.
Success in the automation tool is not proof that the intended CRM state exists.
