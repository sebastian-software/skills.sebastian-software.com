# Evidence Review

Review an existing product artifact for decision readiness. Judge the support
behind its recommendations, not the confidence, polish, length, or authority of
the writing.

## Set the Review Contract

Name:

- the artifact and decision it is meant to support
- the accountable audience and decision window
- the product stage, exposure, reversibility, and important risks
- the matching product-management route whose criteria apply

If the decision or artifact is unclear, state the smallest useful review scope
instead of silently choosing one.

## Run Two Distinct Passes

First run an artifact-only baseline:

1. Extract the consequential claims and recommendations.
2. Record only evidence present in or supplied with the artifact.
3. Preserve contradictions, missing provenance, and uncertainty.
4. Do not repair the argument or import expected product language yet.

Then calibrate against the matching product-management guidance:

1. Test whether the evidence addresses the actual decision.
2. Apply the relevant discovery, strategy, scope, quality, shipping, or
   go-to-market criteria.
3. Keep new domain guidance separate from evidence the artifact already had.
4. Never upgrade a claim merely because it matches a preferred framework.

This separation prevents a plausible template from being mistaken for support.

## Build a Claim-Evidence Register

Classify each consequential claim with one status:

- `supported`: direct, sufficiently current evidence addresses the claim and
  decision context
- `partially_supported`: relevant evidence exists but leaves a material gap,
  limitation, or segment mismatch
- `unsupported`: the artifact asserts the claim without relevant evidence
- `contradicted`: supplied evidence materially points against the claim
- `unknown`: provenance or context is too weak to classify responsibly
- `not_applicable`: the claim is outside the declared decision scope

For each claim record:

| Field | Content |
| --- | --- |
| Claim | The smallest consequential assertion or recommendation |
| Status | One classification from the vocabulary above |
| Evidence | Source, date, segment, context, metric, or exact artifact excerpt |
| Limitation | Bias, missing comparison, stale context, or alternative explanation |
| Decision effect | Why the support level changes the proposed decision |

Do not treat a long source list as strong evidence. Apply the evidence ladder,
segment fit, recency, incentives, and decision relevance from the matching
route.

## Apply Decision-Readiness Gates

For a decision-ready artifact, mark each gate `pass`, `fail`, `unknown`, or
`not_applicable`:

1. Target user and triggering situation are specific enough to act on.
2. Desired user progress and intended business result are distinguishable from
   product output.
3. The recommendation's riskiest assumption has evidence or is explicitly
   framed as a hypothesis with a falsification test.
4. Scope, non-goals, constraints, and critical quality or trust guardrails fit
   the decision's risk and reversibility.
5. Distribution, adoption, delivery, or operating implications are addressed
   when they affect feasibility.
6. An accountable owner, decision window, next signal, and keep, change, stop,
   or escalate rule exist.

A failed critical gate blocks a `ready` verdict even when other dimensions are
strong. Use `insufficient evidence` when the review cannot distinguish failure
from missing input.

## Prefer Anchored Verdicts Over Aggregate Scores

Use one verdict:

- `ready`: all critical gates pass and the evidence supports acting at the
  declared exposure
- `conditionally ready`: action is reasonable only within named constraints,
  staged exposure, or closure conditions
- `not ready`: a failed critical gate makes the proposed action irresponsible
  or incoherent
- `insufficient evidence`: the supplied material cannot support a responsible
  readiness judgment

Do not average a contradiction or failed trust gate into a reassuring score.
When the user explicitly requests scoring, score each applicable dimension from
0 to 3 and keep the final verdict gate-based:

- `0`: absent or contradicted
- `1`: assertion or weak indirect signal
- `2`: useful but incomplete or context-limited support
- `3`: current, direct, decision-grade support

Expose the evidence behind every score and do not calculate decimals or a
weighted overall score.

## Deliver the Review

Return:

1. Decision, artifact, scope, and verdict
2. Claim-evidence register
3. Decision-readiness gates and blocking failures
4. Strongest support, material contradictions, and important unknowns
5. Prioritized corrections, each with owner, decision window, and closure
   condition
6. Smallest next action that reduces the highest-leverage uncertainty
7. Evidence or changed conditions that would change the verdict

Rank corrections by decision consequence, not editorial convenience. Preserve
valid uncertainty rather than rewriting the artifact into false certainty.
