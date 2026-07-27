# Packaging and Changes

Load this reference when designing packages, tiers, allowances, discounts,
trials, or a price change. Treat packaging as a customer and operating model,
not just a comparison table.

## Design Packages From Customer Situations

For each target situation, identify:

- job, value, urgency, and expected usage
- buyer, user, approver, procurement, and support needs
- required reliability, security, administration, integration, and service
- expansion path and reasons to move to another package
- delivery, support, and sales cost

Group needs that naturally belong together. A package should make a coherent
promise to a recognizable customer situation.

Do not assume three tiers. One offer, two packages, modular add-ons, usage
allowances, negotiated enterprise terms, or another structure may fit better.

## Evaluate Fences and Entitlements

For every difference between packages, ask:

- Does it reflect different value, usage, risk, service, or buying needs?
- Can a customer understand it before purchase?
- Can the product enforce it consistently?
- Can billing, sales, support, analytics, and contracts describe the same rule?
- Does it block the product's core promise or create an unsafe degraded state?
- Does it support a credible expansion path without holding customer data or
  essential accessibility hostage?

Avoid artificial scarcity that makes the lower package fail at its advertised
job. Keep security, privacy, legal, accessibility, and basic reliability needs
out of coercive upsell mechanics.

## Specify Package Operations

Document:

- included capabilities, units, allowances, and service levels
- overage, cap, grace, upgrade, downgrade, cancellation, and renewal behavior
- entitlement source of truth and billing-system representation
- proration, credits, failed payment, refunds, and disputed usage
- sales discretion and approval authority
- customer-visible explanations and in-product state
- analytics events needed to understand adoption, expansion, and friction

Test a package against realistic lifecycle states, not only a new customer's
first purchase.

## Design Discounts and Trials

Treat a discount as a policy:

- purpose and hypothesis
- eligible customer and qualifying event
- amount or mechanism
- duration, expiration, renewal, and stacking behavior
- approval authority and exception record
- customer communication
- billing representation and revenue effect
- abuse and channel-conflict risk
- measurement and stop condition

A trial must identify the product behavior needed to reach credible value, the
time and data required, what remains available after expiry, and how consented
conversion works. Do not rely on accidental renewal, hidden terms, or obstructed
cancellation.

Compare a free plan, time-limited trial, usage credit, pilot, guarantee, demo,
or paid proof of value based on the real adoption path. None is a universal
default.

## Plan an Existing-Customer Change

Separate new-customer pricing from migration. Before changing an existing
customer's commercial contract, inventory:

- current contract, renewal date, currency, taxes, discounts, and commitments
- purchased entitlements, usage history, integrations, and critical workflows
- current and modeled future bill
- customer tenure, support context, and known promises
- billing and entitlement-system capabilities
- legal, finance, sales, support, and operational dependencies

Define cohorts intentionally. Possible treatments include immediate change at
renewal, delayed migration, time-bound legacy terms, credits, negotiated
transition, or a maintained legacy package. Model the cost and trust impact of
each; do not call indefinite complexity “free.”

For every cohort, specify:

- effective date and contractual trigger
- old-to-new entitlement mapping
- notice timing, channel, language, and accountable sender
- clear old and new bills using representative usage
- customer action required and available choices
- support scripts, escalation authority, and exception policy
- monitoring, rollback, and correction process

Do not silently remove purchased value or turn an internal migration assumption
into a customer promise.

## Validate Before Broad Rollout

Use the lowest-risk method that can answer the decision:

- customer interviews with realistic offer and bill examples
- proposal or sales-call observation
- package prototype comprehension tests
- limited new-customer offer tests
- renewal or migration pilots with representative cohorts
- qualitative research when traffic is too low for a credible experiment

Define guardrails beyond conversion and revenue:

- activation, retained use, and product success
- confusion, support load, disputes, refunds, and failed payments
- bill predictability and usage suppression
- churn, contraction, trust, and accessibility
- delivery cost and operational exceptions

Set an observation window appropriate to the purchase and renewal cycle. Avoid
declaring a winner from early conversion when long-term value has not had time
to appear.

## Change Deliverable

Return:

1. package or policy definition
2. customer situations and evidence
3. entitlement and billing rules
4. customer bill and business scenarios
5. new-customer and existing-customer treatment
6. communication, support, and exception plan
7. validation, guardrails, monitoring, and rollback
8. unresolved specialist questions and approval owners
