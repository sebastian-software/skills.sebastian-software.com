# Deliverables

Choose one primary deliverable. Add supporting artifacts only when they remove
an identified implementation or review gap.

## Compliance Inventory

Use for an audit or planning request:

1. Scope and as-of date
2. Confirmed operator and service facts
3. Target-jurisdiction rationale
4. Applicability matrix
5. Current implementation evidence
6. Required actions, conditional actions, and recommendations
7. Missing facts and counsel decisions
8. Source log

Rank implementation work by user harm, enforcement exposure, blocked launch or
transaction, breadth of affected people, and confidence in applicability. Do
not invent penalty totals to create a severity score.

## Page and Surface Map

Map requirements to the place where a person encounters the relevant action:

| Surface | Typical purpose |
| --- | --- |
| Operator or legal notice | Entity, contact, registration, professional, or publisher facts |
| Privacy notice | Actual personal-data practices and rights |
| Consent controls | Choices before and after device access or optional processing |
| Terms | Contract rules and service allocation |
| Offer and checkout | Pre-contract facts, price, renewal, cancellation, withdrawal, order action |
| Marketing message | Sender, disclosure, consent, and unsubscribe information |
| Claim or endorsement | Material connection and claim qualification at point of influence |
| Rights request flow | Authentication, submission, appeal, and status handling |

Do not force every item into the footer. Ensure required information is clear,
reachable, consistent across locales and devices, and placed at the legally
relevant moment.

## Draft with Placeholders

Draft only after building the fact and applicability inventories.

- Use the operator's real local terminology and required language.
- Keep one placeholder per unknown fact: `[REGISTER AUTHORITY — REQUIRED]`.
- Annotate conditional sections outside the publishable text.
- Link each non-obvious clause to a source-log entry during review.
- Avoid warranty language, broad promises, and rights descriptions that the
  operating process cannot honor.
- Return a missing-facts list and a counsel-review list beside the draft.

Never translate approved legal text silently. Identify the controlling version,
translator or reviewer, and locale. Use `locale-typography` only after wording
is approved.

## Implementation Review

Test both content and behavior:

- Links from all relevant pages, locales, mobile layouts, and app shells
- Content consistency with register records, checkout, invoices, consent
  categories, vendors, and support processes
- Tracker behavior before choice, after rejection, after acceptance, and after
  withdrawal
- Consent schema, policy version, migrations, regional or signal routing, and
  the interpretation of previously stored choices
- Agreement between app-owned state, tag managers, vendor SDK configuration,
  server-side events, privacy text, and the preference center
- Rights, unsubscribe, cancellation, and complaint flows end to end
- Keyboard, screen-reader, zoom, and reduced-motion access to legal choices
- Evidence captured without collecting unnecessary personal data

Separate findings into legal-content changes, product or process changes,
frontend implementation, and counsel decisions. Route frontend work to
`effective-web` with the precise requirement and acceptance criteria.
