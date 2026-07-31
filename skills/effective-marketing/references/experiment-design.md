# Experiment Design

Use this reference to choose a proportionate learning method, design a
randomized comparison when justified, or build an honest alternative when
traffic, risk, or implementation makes randomization unsuitable.

## Start with the Decision

State:

- decision the evidence will inform and the authorized owner;
- eligible population and exposure moment;
- mechanism hypothesis and intervention;
- primary user and business outcome;
- guardrails and unacceptable harm;
- smallest effect worth acting on in this context;
- evidence window, stop conditions, and follow-up horizon.

Do not begin with a test format or a desired significance result.

## Decide Whether to Experiment

A randomized comparison is useful when:

- genuine uncertainty remains about a reversible intervention;
- assignment can be stable and contamination controlled;
- exposure and outcomes can be measured faithfully;
- traffic and event frequency can support a decision-relevant effect;
- people are not exposed to known harm or denied a clear requirement.

Fix the issue, run research, or escalate instead when an experiment would delay
an accessibility correction, safety response, legal requirement, severe
failure, or removal of deception.

## Design the Comparison

Specify:

1. unit of randomization and unit of analysis;
2. eligibility, exclusions, assignment, persistence, and re-entry;
3. control and one or more variants that isolate the mechanism;
4. exposure event and checks for assignment or sample imbalance;
5. primary metric, guardrails, and downstream follow-up;
6. baseline range and smallest practically meaningful effect;
7. sample and duration logic including weekly cycles or known seasonality;
8. treatment of missing, repeated, delayed, and conflicting outcomes;
9. predeclared segments and multiple metrics;
10. launch, ramp, pause, rollback, and completion authority.

Validate that control and treatment receive events consistently before
interpreting uplift. An allocation mismatch, selective exposure, or variant
failure can invalidate the comparison.

## Protect People and the Product

Review every intervention for:

- informed choice and clear consequence;
- accessibility and alternate input;
- truthful price, claim, scarcity, and availability;
- easy refusal, reversal, cancellation, and recovery;
- privacy, consent, sensitive inference, and tracking scope;
- regret, refunds, complaints, support burden, and downstream value.

Do not use artificial urgency, hidden cost, obstructed exits, disguised choice,
or repeated pressure as conversion techniques. A guardrail must have a decision
rule and owner, not merely appear on a dashboard.

## Learn with Low Traffic

When a randomized test cannot distinguish a meaningful effect:

- observe representative people attempting the task with realistic content;
- interview recent completers, abandoners, non-deciders, sales, support, or
  customer-success participants with sampling limits visible;
- repair measurement and examine complete journeys rather than more variants;
- roll out one reversible change to a bounded cohort or sequence;
- compare repeated stable periods while recording seasonality and concurrent
  changes;
- analyze naturally occurring differences only with explicit confounding;
- use operational signals, task success, comprehension, and downstream quality
  to triangulate.

These methods can reveal severe friction and improve a decision. They do not
automatically establish the causal effect a well-run randomized comparison
could support. State what remains unknown.

## Hand Off Implementation

Give `effective-web`:

- control and variant behavior;
- eligibility, assignment, persistence, and exposure semantics;
- instrumentation and data-quality checks;
- accessibility, content, responsive, performance, and error requirements;
- ramp, pause, rollback, and cleanup conditions.

Do not let implementation convenience silently change the hypothesis, audience,
metric contract, or guardrails.
