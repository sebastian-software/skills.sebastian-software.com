# CRM Data Model and Pipeline

## Separate the objects

- **Contact:** a person and relatively stable information.
- **Company or account:** the organization and shared attributes, if supported.
- **Opportunity or deal:** a specific potential purchase with offer, value,
  stage, and owner.
- **Activity:** a call, email, meeting, note, or task with time and outcome.

One contact can have multiple opportunities. Put proposed value and current
sales stage on the opportunity, not on the permanent contact record. Make a
field required only at the point when its value is genuinely needed.

## Field dictionary

| Field | Object | Purpose and rule |
| --- | --- | --- |
| Name and reachable channel | Contact | Record only known details, format, and origin |
| Company and segment | Account or contact | Use controlled values when reporting requires them |
| Original source and campaign | Contact or opportunity | Preserve initial origin separately from later interactions |
| Contact status | Contact | New, attempt, reached, do not contact; separate from sales stage |
| Need and goal | Opportunity | Briefly describe in the customer's words |
| Fit and exclusion reason | Opportunity | Consistent values for qualification learning |
| Offer and estimated value | Opportunity | Identify the actual opportunity; label estimates |
| Owner and next task | Opportunity or task | One responsible person, date, and action |
| Meeting status | Activity or opportunity | Booked, attended, moved, missed; not a win/loss state |
| Outcome and loss reason | Opportunity | Clear closed status with reason |

For each field, define type, permitted values, when it becomes required,
responsible role, and report usage. Eliminate fields nobody uses. Keep “unknown”
distinct from “no.” Capture contact permissions or restrictions only as
appropriate under the applicable market rules.

## Pipeline with entry criteria

| Stage | Observable entry rule | Next action |
| --- | --- | --- |
| Intake | Unique inquiry or researched prospect exists | Verify source and assign owner |
| Working | First attempt or active exchange is recorded | Continue contact or conversation |
| Qualified | Need, decision path, timing, and basic fit are known | Arrange a suitable consultation |
| Meeting booked | Date and participants confirmed | Prepare and confirm expectations |
| Proposal or decision | Solution, price, and decision step discussed | Follow the agreed next action |
| Won | Binding commitment under the business's definition | Handoff to delivery |
| Lost | No active opportunity remains | Record reason and any permitted future action |

No-show, waiting on the customer, and later follow-up can be stages or saved
views. Choose the representation the team will actually use. Avoid a stage that
means only “follow up sometime” without an owner and date. Outbound prospecting
may merit a separate pipeline for research, attempts, interest, and meeting.

## Import and cleanup

Define stable IDs or matching rules before import. Map fields, then import a
small trial set. Check identity, permissible contact basis, duplicates, source,
owner, stage, and next task. Keep original IDs to support correction and
reimport. Document merges and follow the applicable retention and deletion
rules. A successful import is one that leaves each active record actionable, not
merely present.
