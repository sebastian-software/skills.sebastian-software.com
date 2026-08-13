# Review Calibration

Calibrate a repeated or high-stakes product-review process against representative
cases and later outcomes. Improve judgment without training reviewers to mimic
one preferred answer or rewriting past decisions with hindsight. The
claim-evidence classification, readiness gate, critical-gate, and verdict
vocabulary calibrated here is defined in [evidence-review.md](evidence-review.md).

## Define the Calibration Claim

State what must become more reliable:

- claim-evidence classification
- decision-readiness gates
- mode selection
- verdict or exposure recommendation
- prioritization of corrective actions
- confidence and uncertainty communication

Name the artifacts, product stages, risk classes, and decisions covered. Do not
claim that a calibration set generalizes beyond its represented cases.

## Build Decision Cases

Use frozen, inspectable inputs:

1. Original artifact and supplied evidence
2. Decision context, evidence cutoff, and product stage
3. Relevant risk, reversibility, and exposure
4. Human acceptance criteria and material disagreements
5. Expected gate behavior and claims that must not be upgraded

Write behavioral acceptance criteria rather than a golden prose response.
Include strong, weak, contradictory, incomplete, and boundary cases. Preserve
cases where responsible reviewers disagree; they reveal a policy choice or
missing evidence rather than an automatic model failure.

Keep evaluation cases separate from examples shown in the review instructions
when practical. Do not make success depend on memorizing a fixture.

## Test Review Invariants

Use paired or counterfactual cases to check:

- **evidence sensitivity:** replacing a claim with direct relevant evidence may
  improve support, while removing that evidence must not improve it
- **contradiction sensitivity:** adding material contrary evidence must affect
  the claim status, gate, confidence, or verdict
- **gate integrity:** polished writing, authority, or a high average score must
  not override a failed critical gate
- **scope sensitivity:** narrowing segment, exposure, or reversibility may move
  a decision from `not ready` to `conditionally ready` when the risk genuinely
  changes
- **paraphrase stability:** equivalent facts should produce materially
  equivalent classifications and gates
- **framework resistance:** an artifact that uses ideal product terminology
  without support must remain unsupported

Compare decisions, classifications, gates, constraints, and top corrective
actions. Ignore harmless differences in wording, ordering, or formatting.

## Investigate Disagreement

Classify each material mismatch:

- missing or ambiguous review instruction
- evidence provenance or context gap
- artifact interpretation disagreement
- domain-policy disagreement
- inconsistent application of a clear rule
- unsupported confidence or invented evidence

Do not change the rubric merely to make one evaluator pass. Resolve policy
choices with an accountable owner and record the reason, affected cases, and
expected tradeoff.

For high-risk decisions, use an independent second review when available.
Disagreement is a signal to inspect the evidence and gates, not a vote to
average incompatible judgments.

## Learn From Outcomes Without Hindsight Bias

Freeze the original artifact, evidence cutoff, review, recommendation, and
expected signals. After the declared learning window, record:

- observed first and repeated value by relevant segment
- business result and operational or trust consequences
- whether predicted guardrails held
- important interventions or external changes after the decision
- plausible alternative explanations and causal confidence
- which original evidence, assumption, gate, or uncertainty was informative

A good outcome does not prove that a weakly supported decision was sound. A bad
outcome does not prove that a responsible experiment was wrong. Judge the
decision process using information available at the time, then use outcomes to
update future evidence weights or gates only when a defensible pattern emerges.

Preserve the prior review version. Add a new version with the changed rule,
rationale, affected modes, migration consequence, and cases that demonstrate
the improvement.

## Deliver the Calibration

Return:

1. Calibration claim, scope, and represented limits
2. Case inventory and evidence cutoffs
3. Invariant and counterfactual results
4. Material disagreements and their classification
5. Proposed rule changes with supporting cases and tradeoffs
6. Outcome-learning findings separated from hindsight
7. Review version, owner, next calibration window, and stop or expand rule

Prefer a small case set that discriminates meaningful failures over a large set
of easy examples.
