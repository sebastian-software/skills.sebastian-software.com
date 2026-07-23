# Review Modes

Select one primary review mode after applying the core evidence-review contract
in [evidence-review.md](evidence-review.md). Use the mode to add
decision-specific gates and dimensions, not to replace the claim-evidence
register or common verdict vocabulary.

## Select the Smallest Applicable Mode

| Mode | Use for | Load with |
| --- | --- | --- |
| `product-decision` | Product briefs, strategies, prioritization choices, roadmaps, and investment recommendations | Discovery and evidence, Strategy and outcomes, and Scope and prioritization, as relevant |
| `go-to-market-claim` | Positioning inputs, launch claims, sales promises, proof packets, and product-to-marketing handoffs | Go-to-market handoff |
| `launch-readiness` | Release recommendations, rollout plans, exposure changes, and post-pilot scale decisions | Product quality and delight, and Shipping and learning |

Choose the mode from the decision the artifact must support, not its filename.
If an artifact spans several modes, use one primary mode and apply only the
critical secondary gates that can change the verdict. Do not produce three
duplicated checklists.

## Review a Product Decision

Test these dimensions:

1. **Decision clarity:** choice, alternatives, accountable owner, decision
   window, and consequences of waiting
2. **Customer progress:** target user, triggering situation, struggle,
   alternatives, desired progress, and buying or adoption context
3. **Evidence:** source quality, recency, segment fit, contradictions, and the
   riskiest unsupported assumption
4. **Strategic coherence:** wedge, differentiation, business result,
   distribution constraint, touch model, and non-goals
5. **Scope and quality:** smallest coherent path, critical quality bar,
   dependencies, opportunity cost, and reversibility
6. **Learning:** leading and lagging signals, falsification test, next decision,
   and keep, change, stop, or escalate rule

Block a `ready` verdict when the proposed choice is unclear, the target
situation is invented or too broad to act on, the central recommendation has no
support or falsification path, or scope cannot test the claimed outcome
honestly.

Do not promote a feature list into a strategy. Do not use a prioritization score
to hide missing evidence, capacity, or opportunity cost.

## Review Go-to-Market Claims

Review the evidence packet at the product-to-marketing boundary. Do not perform
the downstream positioning, pricing, campaign, or launch work owned by the
specialist marketing skills.

For each consequential external claim, record:

| Field | Question |
| --- | --- |
| Audience and situation | For whom and under which trigger is the claim intended? |
| Product mechanism | What product behavior could make the claim true? |
| Product evidence | Has the mechanism been verified in the supported experience? |
| Customer proof | Did representative customers reach or commit to the claimed outcome? |
| Constraint | Where, when, or for whom does the claim not hold? |
| Qualification | What wording matches the actual confidence and scope? |

Block a `ready` verdict when:

- an outcome, speed, ease, comparison, or universality claim exceeds supplied
  product and customer evidence
- customer language is fabricated, unattributed, or generalized beyond its
  segment
- target user, buyer, trigger, alternative, or material constraint is missing
- the price, channel, sales effort, onboarding, and support model contradict
  the product economics or experience

Recommend removing, narrowing, or qualifying unsupported claims. Do not invent
proof to preserve persuasive wording.

## Review Launch Readiness

Test these dimensions:

1. **Exposure:** target segment, eligibility, release scope, non-goals, rollout
   sequence, and blast radius
2. **Promise:** expected user progress, product mechanism, first and repeated
   value, and claims customers will encounter
3. **Quality and trust:** correctness, accessibility, privacy, security,
   reliability, recovery, data integrity, and unresolved known issues
4. **Operations:** support, ownership, observability, dependencies, capacity,
   billing, cancellation, and incident response
5. **Learning:** instrumentation, expected signals, guardrails, comparison,
   learning window, and alternative explanations
6. **Control:** rollback or containment condition, accountable owner, decision
   date, and keep, change, stop, or expand rule

Block a `ready` verdict when a trust-critical failure is unresolved, the release
cannot be contained or reversed at the declared risk, the team cannot observe
whether users reach value, or no owner and decision rule exist.

Prefer `conditionally ready` with narrow eligibility or staged exposure when
the core promise works but evidence or operational confidence is bounded. Do
not label a broad rollout as an experiment merely because measurement exists.

## Add Mode-Specific Findings to the Core Deliverable

After the common claim register and readiness gates, include:

1. Primary mode and why it fits
2. Mode dimensions with the evidence-backed finding for each
3. Mode-specific blocking gates or exposure constraints
4. One recommended decision and the smallest responsible scope
5. Explicit handoff after the product evidence is stable enough

Keep mode findings subordinate to the supplied evidence. A complete template
with weak support remains incomplete product judgment.
