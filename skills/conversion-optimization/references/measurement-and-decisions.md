# Measurement and Decisions

Use this reference to validate experiment evidence, interpret uncertainty and
guardrails, and choose ship, iterate, stop, revert, or investigate.

## Validate before Comparing

Check:

- assignment counts, eligibility, exposure, and exclusions;
- event completeness, duplication, identity, order, and delay;
- variant delivery, errors, latency, and performance;
- allocation or exposure imbalance;
- contamination, repeat exposure, and cross-device behavior;
- calendar effects, campaigns, incidents, releases, and offer changes;
- whether the planned evidence and follow-up windows completed.

Stop interpretation when a defect can plausibly create the observed difference.
Repair the measurement or implementation, then decide whether the evidence can
be recovered or the comparison must restart.

## Read the Result as a Decision

Report:

- absolute and relative change with uncertainty;
- practical value compared with the smallest effect worth acting on;
- primary outcome and every consequential guardrail;
- downstream quality, retention, refund, cancellation, complaint, and support
  evidence where relevant;
- planned segment effects and plausible distributional harm;
- novelty, learning, and follow-up limitations;
- result sensitivity to exclusions or metric definitions.

Do not reduce the result to “significant” or “not significant.” A precisely
estimated trivial effect can be unworthy of shipping; an uncertain result can
still rule out a hoped-for large effect or reveal harmful failure.

## Control Analysis Flexibility

Compare the result with the predeclared hypothesis, primary metric, guardrails,
segments, duration, and stop rules.

- Label exploratory findings as exploratory.
- Do not add exclusions because they improve the result.
- Do not search segments until one wins and present it as confirmed.
- Account for several variants, metrics, or repeated looks in the chosen
  inference method.
- Preserve null, negative, and contradictory outcomes.

When the plan changed during the run, state why, when, and how that affects
confidence.

## Decide with Guardrails

Use the combined evidence:

- **Ship:** meaningful improvement, trustworthy data, acceptable guardrails,
  credible mechanism, and operational readiness.
- **Iterate:** mechanism remains plausible but the intervention missed,
  confused, or incompletely addressed it; define the new evidence needed.
- **Stop:** useful effect is absent, too small, too uncertain for the cost, or
  the mechanism is unsupported.
- **Revert:** harm, accessibility regression, deception, data corruption, or
  material guardrail failure outweighs the local gain.
- **Investigate:** data quality, implementation, unexpected segments, novelty,
  or contradictory downstream evidence prevents a sound decision.

Do not average away severe harm to a smaller population. Name who benefits,
who loses, and whether the product can responsibly target or adapt the change.

## Preserve the Learning

Record:

- hypothesis, intervention, audience, dates, and versions;
- metric contracts and analysis plan;
- data-quality findings and deviations;
- result, uncertainty, guardrails, and affected segments;
- decision, owner, rollback or rollout state;
- what was learned about the mechanism;
- follow-up window and conditions that reopen the choice.

Remove experiment-only code and instrumentation after the chosen evidence and
rollback window no longer require them. Keep durable metrics only when they
have an ongoing operational owner and purpose.
