# Route: CRM and Sales Operations

Use this route for CRM data models, pipelines and stages, fields, imports,
saved views, handoffs between roles, reporting terms, inquiry intake from forms
and bookings, and CRM automations. Model the actual sales process before
configuring fields and automation. Every active opportunity needs a state, an
owner, and a next action.

## Read

- [Data model](crm-data-model.md) — contacts, accounts, opportunities,
  activities, field dictionary, pipeline entry rules, and imports.
- [Operating rhythm](crm-operating-rhythm.md) — role handoffs, saved views,
  daily and weekly rhythm, and reporting terms.
- [Intake and events](crm-intake-and-events.md) — form questions, post-submission
  flow, event definitions, and the end-to-end check.
- [Automations](crm-automations.md) — triggers, idempotency, loop guards, and
  reliability review.

## Apply

- Map contact paths, roles, qualification, and decisions first. Define stages
  with observable entry rules and add only fields needed for a decision or
  handoff.
- Create views for new, due, and at-risk work, each with an owner and review
  rhythm.
- Automate only after the manual rule is clear. Success in an automation tool
  is not proof that the intended CRM state exists; inspect real records after a
  change.
- Check current vendor behavior before giving click instructions. Preserve the
  meaning of existing data and stages.
- Capture contact permissions, suppression, retention, and deletion under the
  applicable market rules.

## Cross-links

- Stage definitions depend on the qualification standard in
  **Consultative sales**.
- Campaign source and cost-per-stage reporting feed **Paid campaigns** and
  **Conversion**.
- Webhook handling, idempotency keys, and data-model decisions that belong to
  the application's own system rather than a CRM product go to
  `effective-engineering`.
- Form implementation, analytics tags, and consent belong to `effective-web`.
