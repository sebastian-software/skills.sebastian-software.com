---
name: conversion-optimization
description: >-
  Diagnose and improve funnels, activation paths, signup, checkout, lead,
  upgrade, and other conversion journeys through evidence-led research,
  friction and objection hypotheses, ethical experiment design, guardrails,
  measurement, and ship, iterate, or stop decisions. Use for funnel drop-off,
  conversion audits, low-traffic learning plans, A/B test design or review,
  experiment interpretation, and prioritization of conversion opportunities
  without sacrificing trust, accessibility, or long-term customer value.
---

# Conversion Optimization

Help more eligible people complete a valuable task by finding the best-supported
constraint and learning whether a responsible change removes it. Optimize the
user outcome and the business outcome together; a local metric increase is not
success when it creates confusion, exclusion, regret, support burden, or
downstream harm.

## Workflow

1. Define the decision before choosing a test:
   - eligible audience, entry condition, unit of analysis, and primary task
   - funnel steps, completion event, time window, and downstream value
   - business objective, user benefit, constraints, and decision authority
   - current evidence, instrumentation limits, traffic, seasonality, and risk
2. Audit the measurement boundary. Verify event meaning, eligibility,
   denominators, identity, duplicate handling, exposure, attribution window,
   missing data, and important segments. Do not diagnose from a percentage whose
   population or event contract is unclear.
3. Read [Diagnosis and research](references/diagnosis-and-research.md) to locate
   the strongest evidenced bottleneck and synthesize behavioral data, customer
   accounts, usability observation, support or sales signals, and journey
   inspection without inventing intent.
4. Turn evidence into a mechanism hypothesis: identify who encounters which
   friction, uncertainty, objection, accessibility barrier, or mismatch; state
   why it blocks valuable progress and what evidence could disconfirm it.
5. Prefer the highest-consequence supported constraint over cosmetic novelty.
   If the product, audience, position, offer, or instrumentation is the real
   problem, route it to its owner rather than testing button styling around it.
6. Read [Experiment design](references/experiment-design.md) to choose a
   proportionate learning method, intervention, allocation, primary metric,
   guardrails, sample and duration logic, quality checks, stop conditions, and
   implementation handoff.
7. When traffic or conversions cannot support a decision-worthy randomized
   comparison, use qualitative task observation, targeted interviews,
   sequential rollouts, repeated stable measurement windows, or transparent
   observational analysis. State the weaker causal claim instead of inventing
   statistical certainty.
8. Route approved browser implementation and frontend verification to
   `effective-web`. Validate instrumentation and exposure before relying on the
   result; treat an experiment with broken measurement as inconclusive.
9. Read [Measurement and decisions](references/measurement-and-decisions.md) to
   analyze data quality, effect size and uncertainty, guardrails, novelty,
   segments, practical value, and downstream outcomes before deciding to ship,
   iterate, stop, revert, or investigate.
10. Preserve the result, decision, evidence limits, affected cohorts, guardrail
    effects, follow-up owner, and conditions that would reopen the decision.

## Operating Rules

- Optimize completion of a legitimate user goal, not compliance with a prompt,
  accidental clicks, obstructed cancellation, hidden cost, or metric capture.
- Keep observed behavior, customer statements, interpretation, hypothesis, and
  causal conclusion distinguishable. Never fabricate traffic, quotes, intent,
  baseline rates, sample size, significance, or experiment results.
- Diagnose the funnel end to end. Increasing an early click can reduce
  qualified completion, activation, retention, or customer value downstream.
- Treat accessibility as a conversion requirement and a guardrail. A change
  that excludes people is not an optimization.
- Include trust, comprehension, reversibility, privacy, support burden, refunds
  or regret, retention, and long-term value where the intervention can affect
  them.
- Predefine the important decision logic before observing results. Do not stop
  when a preferred metric happens to cross a convenient threshold.
- Use segmentation to test a stated mechanism or detect harm, not to search
  endlessly for one flattering subgroup after an overall miss.
- Avoid arbitrary weighted scoring and universal uplift, sample, confidence, or
  duration thresholds. Use evidence, meaningful effect, risk, reversibility,
  traffic, and decision cost in context.
- Do not run a randomized experiment when a direct fix, instrumentation repair,
  accessibility correction, legal requirement, or severe user harm already has
  a clear decision.

## Default Deliverable

Return the smallest decision-ready package containing:

1. funnel scope, eligible population, metric contracts, and evidence limits;
2. quantified and qualitative diagnosis with the best-supported bottleneck;
3. ranked mechanism hypotheses with evidence, unknowns, and disconfirming signs;
4. selected intervention and why it outranks cosmetic or unrelated changes;
5. learning method, allocation or sequence, duration logic, and quality checks;
6. primary outcome, guardrails, downstream signals, and stop conditions;
7. implementation and instrumentation handoff;
8. ship, iterate, stop, revert, or investigate rule with evidence limits.

## Routing Boundaries

- Use `product-management` when the target user, product value, core journey,
  scope, quality bar, or release decision is unresolved or must change.
- Use `product-marketing` when the evidence points to segment, position,
  category, message, claim, proof, launch, or channel choice. Use this skill to
  diagnose and test how an approved market choice performs in a funnel.
- Use `pricing-and-packaging` for willingness-to-pay, value metrics, price,
  package, discount, trial, entitlement, or customer-migration decisions. Test
  only approved commercial hypotheses and constraints here.
- Use `effective-web` to specify, implement, and verify browser UI, forms,
  analytics delivery, accessibility, responsive behavior, performance, and
  experiment variants after the learning design is approved.
- Use `web-legal-compliance` for current jurisdiction-specific requirements
  affecting consent, tracking, privacy, claims, testimonials, disclosures,
  direct marketing, or online sales.
- This skill owns conversion diagnosis, learning design, and result judgment.
  It does not authorize deceptive interfaces, manufacture research, implement
  browser changes, or replace legal, privacy, or specialist statistical review
  when risk and uncertainty exceed the available evidence.
