# Value Metrics and Models

Load this reference when deciding what to charge for, how the bill changes, or
whether subscription, seat, usage, outcome, transaction, or hybrid pricing fits
the product.

## Start With the Value Event

Describe:

- the customer situation and desired progress
- the product event that creates or captures value
- who experiences the value and who controls the charged unit
- how value, usage, and delivery cost vary by segment
- the time between use, realized value, measurement, and billing

Do not select a metric merely because it is easy to meter or common in adjacent
products.

## Screen Candidate Value Metrics

Assess each candidate against:

| Test | Question |
| --- | --- |
| Alignment | Does more of the unit usually mean more customer value? |
| Comprehension | Can buyers and users explain what changes the bill? |
| Predictability | Can a customer budget and detect unusual use? |
| Measurability | Can the unit be measured consistently, promptly, and audibly? |
| Control | Can customers influence the unit without harming their outcome? |
| Segment fit | Does the relationship hold across relevant customer sizes and workflows? |
| Cost fit | Does the model account for material variable delivery or support cost? |
| Integrity | Is the unit resistant to gaming, duplication, and ambiguous attribution? |
| Adoption effect | Will charging the unit discourage useful product behavior? |
| Operations | Can sales, billing, support, analytics, and contracts represent it? |

A weak metric may still work with allowances, caps, minimums, committed use, or
a hybrid structure. Make the compensating mechanism explicit rather than
declaring the metric universally good.

## Compare Pricing Models

Use the buying and value context to compare:

- **Flat subscription:** simple and predictable when customer value and cost do
  not vary enough to justify a metered bill.
- **Per seat:** legible where authorized users approximate value, but risky when
  collaboration, automation, or shared access creates value.
- **Usage based:** aligns expansion with consumption when the unit tracks value;
  requires metering, bill predictability, and protection from accidental spikes.
- **Transaction based:** fits mediated economic activity when transaction value
  and product value remain connected.
- **Outcome based:** can align incentives when the outcome is attributable,
  timely, auditable, and within both parties' control.
- **Tiered allowance:** combines predictability with usage differences but can
  create cliffs around boundaries.
- **Hybrid:** combines a base commitment with seats, usage, or outcomes when one
  metric cannot fairly represent access, value, and variable cost.
- **One-time or service fee:** fits discrete delivery or onboarding work when it
  should not be hidden inside recurring product price.

These are design options, not maturity stages. More components usually mean
more explanation, billing logic, support work, and customer uncertainty.

## Model Customer Bills

For each relevant segment, model several realistic histories:

```text
bill = fixed commitments + variable units + services + adjustments
```

Include:

- low, typical, high, seasonal, and accidental usage
- first period, mature usage, renewal, expansion, contraction, and cancellation
- allowances, minimums, caps, overages, credits, proration, and taxes as
  applicable inputs rather than hidden assumptions
- gross revenue, variable delivery cost, support burden, and collection risk
- the customer's expected value and their ability to forecast the bill

Show discontinuities. A tiny increase in use should not cause an unexplained
large increase in bill unless the package creates a genuinely different value
or service commitment.

## Check Incentives and Failure Modes

Ask what behavior the model rewards:

- Will users avoid collaboration, data ingestion, experimentation, automation,
  or successful usage to control the bill?
- Can one party create cost while another owns the budget?
- Can an integration loop, retry storm, abuse event, or employee mistake create
  unbounded charges?
- Does the metric encourage splitting or combining accounts artificially?
- Can customers verify the billed quantity and dispute it with shared evidence?
- Does revenue expand when customer value expands, or merely when friction does?

Add alerts, estimates, caps, grace behavior, administrative controls, and clear
usage records where the risk warrants them.

## Choose at the Supported Precision

Recommend:

1. target segment and value hypothesis
2. selected metric and rejected candidates
3. pricing model and bill formula
4. modeled customer and business scenarios
5. measurement and billing requirements
6. key risks, guardrails, and unknowns
7. evidence or test needed before exact amounts are committed

No formula supplies a correct price without customer, transaction, product, and
economic evidence. Use ranges and scenarios when exact values would be false
precision.
