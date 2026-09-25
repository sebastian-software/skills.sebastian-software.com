# Forms, Handoffs, and Measurement

## Ask only useful questions

Separate contact fields, qualification questions, and optional context. A B2B
form might need name, business contact, company, role, problem, timing, and
decision participants. A consumer service needs different signals. Every
question should support routing, call preparation, or a clear fit decision. Do
not transplant B2B fields into consumer forms.

Wording matters. “What is your budget?” can be vague; “What range have you
considered for [defined project]?” gives more context. Too many required fields
can turn away suitable people. Compare a short form with a more qualified one
using downstream conversation quality, not form completion alone.

## After submission

Confirm what actually happened: inquiry received, appointment booked, or another
action required. State who will respond and what to expect. An optional
intermediate page or short video can explain the next meeting and required
preparation, but written instructions should still be clear.

```text
Valid submission → find or update contact → find or create opportunity
→ assign owner → save source and answers → create task or notification
→ confirm to prospect → record valid conversion event
```

Define behavior for incomplete data, duplicate submissions, and integration
failure. A notification without a CRM record may be lost; a record without an
owner may never be handled. Preserve original attribution when later
interactions occur.

## Event definitions

| Event | Count it when | Common error |
| --- | --- | --- |
| Page view | Page actually loads | Duplicate tags inflate count |
| Form start | A person interacts with the form | Mere visibility is counted |
| Lead | Valid submission succeeds | Button click counts despite an error |
| Appointment | Booking is confirmed | Redirect counts without booking |

Define events before adding tags. Test whether form, CRM, and analytics agree on
a complete trial submission. Tracking, consent, data handling, and mandatory
page disclosures vary by market; check current official rules for the actual
deployment. Do not treat one jurisdiction's consent model as universal.

## End-to-end check

Open the page on phone and desktop. Submit a valid test inquiry and an
intentionally invalid one. Check validation, thank-you state, CRM object, owner,
notification, and recorded event. Repeat the complete path after meaningful
changes. A lead event should represent successful intake, not an optimistic
click.
