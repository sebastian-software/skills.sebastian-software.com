# Diagnosis and Research

Use this reference to define a trustworthy funnel, locate the strongest
supported constraint, and synthesize quantitative and qualitative evidence
without inventing user intent.

## Define the Funnel Contract

For every step, record:

- eligible population and exclusion rules;
- unit of analysis: person, account, session, order, or another stable unit;
- entry, exposure, progress, completion, and failure events;
- denominator, identity stitching, duplicate and retry handling;
- time window, attribution, late arrival, and timezone;
- platform, channel, cohort, product, offer, and accessibility context; and
- downstream value that distinguishes useful completion from a captured click.

Trace a sample of real journeys through the event stream where access permits.
Compare event counts with source-of-truth records. A precise chart built on
ambiguous eligibility or duplicated events is not reliable evidence.

## Find Where and Why Progress Breaks

Use quantitative evidence to locate patterns:

- step-to-step and end-to-end completion;
- errors, retries, latency, abandonment, and recovery;
- new versus returning, device, channel, cohort, and meaningful segment;
- release, campaign, offer, or operational changes aligned to the shift;
- downstream activation, successful use, retention, refund, cancellation, and
  support outcomes.

Then use qualitative evidence to investigate mechanisms:

- direct observation of realistic tasks;
- supplied interview, sales, support, survey, or customer-success records;
- consented session or journey evidence with sensitive data protected;
- content, interaction, accessibility, policy, performance, and failure-state
  inspection;
- comparison with the actual alternative people use.

Quantitative evidence can locate a pattern without explaining intent.
Qualitative evidence can reveal a mechanism without establishing prevalence.
Use both at the confidence each supports.

## Keep Evidence Layers Separate

Maintain a compact diagnosis register:

| Layer | Example question |
| --- | --- |
| Observed | What behavior, error, statement, or state was actually recorded? |
| Scope | Which people, devices, times, and conditions does it represent? |
| Interpretation | What mechanism could explain the observation? |
| Alternative | What else could produce the same pattern? |
| Missing evidence | What would distinguish the explanations? |
| Decision | What action is justified now? |

Do not manufacture quotations, objections, motivations, or prevalence from
aggregate percentages. Do not generalize a support ticket or observed session
beyond its sampling limits.

## Form a Mechanism Hypothesis

Write hypotheses in decision-carrying language:

> For an eligible population in a defined situation, the observed constraint
> blocks a valuable task through a stated mechanism. A specific change should
> alter an observable behavior or outcome without degrading named guardrails.

Include:

- direct evidence and confidence;
- affected population and context;
- friction, uncertainty, objection, mismatch, or barrier;
- proposed mechanism rather than surface symptom;
- expected proximal and downstream signal;
- disconfirming observation; and
- risk to trust, accessibility, comprehension, privacy, or long-term value.

## Prioritize without False Precision

Prefer a constraint when:

- it affects a consequential part of the eligible journey;
- several evidence types support the same mechanism;
- the intervention targets the mechanism directly;
- the change is proportionate, reversible, and measurable;
- important harm can be observed and stopped.

Do not hide judgment inside arbitrary scores. State why one mechanism outranks
another and which unknown could reverse that order.

Fix directly when evidence already establishes a broken requirement: crashes,
payment or authentication failure, inaccessible controls, misleading prices,
lost data, or a legal obligation do not need an experiment to deserve
correction.
