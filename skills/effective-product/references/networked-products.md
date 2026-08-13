# Networked Products

Use this route for marketplaces and other products whose value depends on
interactions among participants. Treat the network mechanism, cold start,
liquidity, and expansion as product hypotheses supported by local evidence.
Do not infer them from category labels or aggregate user counts.

## Frame the core interaction

Describe the smallest exchange that creates value:

```text
participant A has a need
  -> discovers a relevant participant B
  -> both can evaluate and commit
  -> the interaction succeeds
  -> each side has a reason to return
```

Record:

- each participant role, including buyers, users, providers, payers, and
  intermediaries
- the triggering situation and desired outcome for each role
- what each side contributes and receives
- the product's role in discovery, evaluation, coordination, transaction,
  fulfillment, and recovery
- the market boundary within which participants can realistically interact
- trust, safety, legal, operational, capacity, and economic constraints
- current alternatives, including direct relationships and competing networks

Do not assume a two-sided model. One participant may occupy several roles, and
some roles may create cost or risk without receiving the product's main value.

## Test the network-effect claim

A network effect exists only when an additional relevant participant changes
the product's value for other participants through a credible mechanism. State
who gains, from whose participation, in which market boundary, and under what
conditions.

Distinguish:

- **same-side effects:** additional participants directly improve or reduce
  value for participants of the same role
- **cross-side effects:** additional participants on one side improve value for
  another side
- **learning effects:** additional interactions improve decisions or outcomes
  only when the resulting learning reaches relevant participants and remains
  useful
- **negative effects:** congestion, noise, competition, abuse, delays, or lower
  quality make additional participation harmful

Do not relabel adjacent mechanisms:

- referrals acquire another participant but do not necessarily improve the
  product for existing participants
- viral distribution describes how acquisition spreads, not whether value
  compounds
- social proof can reduce uncertainty without changing the delivered value
- scale economies can lower unit cost without creating participant-to-
  participant value
- a large account or user total says nothing about relevance, availability,
  interaction quality, or retention

Use a counterfactual: holding the product and acquisition channel constant,
would adding this participant to this bounded network improve a meaningful
outcome for other participants? Name the expected mechanism and observable
result. Preserve the claim as a hypothesis when the evidence cannot isolate it.

## Define the smallest viable network

Find the narrowest market cell in which the core interaction can succeed
reliably enough to produce repeat value. Bound the cell using the dimensions
that determine relevance:

- geography or organizational boundary
- category, use case, or skill
- time window and urgency
- participant role and segment
- price, service level, risk, or trust requirement

The boundary is empirical. A local network may be a neighborhood during a
specific hour, a professional community with one workflow, or a team inside one
company. Do not impose a universal participant count or density threshold.

For the candidate cell, state:

1. the minimum roles and contributions required for a successful interaction
2. which side is constrained and why
3. how participants currently solve the problem
4. what makes participation and return worthwhile for each side
5. which failure would invalidate the cell
6. what evidence permits staying, narrowing, or expanding

Prefer one dense, observable cell over broad geographic or category coverage
that hides failed interactions behind aggregate growth.

## Find the difficult side

Identify the side that is hardest to acquire, activate, retain, or make
available at the required quality. Do not assume supply is always difficult.
Compare:

- urgency and frequency of the underlying need
- acquisition cost and reachable concentration
- onboarding, verification, and setup burden
- capacity, availability, and response-time constraints
- expected earnings, savings, status, access, or workflow value
- alternatives, switching costs, and willingness to multihome
- risk exposure and reasons to distrust the product or counterpart
- retention after the first successful interaction

Separate a temporary participant shortage from a weak value proposition. More
promotion does not fix unattractive economics, unreliable demand, low-quality
counterparts, or operational friction.

## Design an honest cold start

Choose a wedge that can create complete interactions before attempting scale.
Options include:

- recruit a concentrated community or an existing group with shared context
- seed the difficult side through direct, permission-based outreach
- provide a useful single-role workflow that later supports interaction
- operate matching, scheduling, curation, or fulfillment manually at first
- batch demand into explicit time windows or scheduled events
- constrain categories or eligibility until quality is repeatable
- partner with a trusted institution that already coordinates the participants

Label manual work and seeded inventory honestly. Never fabricate profiles,
availability, reviews, demand, deadlines, or successful activity. A waitlist
can test interest, but it does not prove that participants will interact or
return.

Define the transition from manual seeding to a repeatable mechanism. Include an
owner, capacity limit, participant promise, cost boundary, and evidence that
decides whether to automate, continue manually, narrow, or stop.

## Diagnose liquidity and match quality

Liquidity means relevant participants can complete a valuable interaction with
acceptable effort, timing, quality, and risk. Trace the whole path:

```text
eligible arrival
  -> relevant availability
  -> discovery
  -> response
  -> accepted match
  -> successful fulfillment
  -> trusted outcome
  -> repeat participation
```

Choose measures that match the product and the decision, such as:

- eligible demand and available capacity in the same market cell
- time to relevant result, response, or accepted match
- search or request success rate
- acceptance, cancellation, no-show, dispute, and fulfillment rates
- outcome quality, participant satisfaction, and recovery burden
- repeat interaction and retained availability by participant role
- contribution margin and manual operations required per successful outcome

Inspect distributions and cohorts, not only averages. Segment by the dimensions
that define the local network and examine failures, non-matches, low-quality
matches, and participants who leave. Set contextual decision criteria before
reading results; do not borrow an unsupported industry threshold.

Separate acquisition from liquidity. Adding participants who are unavailable,
irrelevant, untrusted, or unlikely to respond can worsen discovery and match
quality even while the headline user count grows.

## Protect trust and limit abuse

Treat trust as part of the core interaction, not a later conversion layer.
Identify the harms and asymmetric risks each role faces:

- identity, qualification, or eligibility fraud
- misleading inventory, availability, pricing, or outcomes
- harassment, discrimination, unsafe encounters, or prohibited activity
- payment loss, chargebacks, non-delivery, or off-platform disputes
- manipulation of ratings, ranking, reputation, or scarcity
- privacy leakage and inappropriate participant contact

Match controls to evidence and consequence. Possible controls include scoped
verification, transparent reputation, eligibility rules, moderation, payment
protection, reporting, dispute handling, reversible enforcement, and human
escalation. Measure false positives, exclusion, response time, and recovery as
well as abuse reduction.

Do not remove safeguards merely to improve sign-up or match counts. Use
`effective-web` to scope jurisdiction-specific web disclosures, privacy,
consent, consumer, and digital-marketplace obligations. Employment
classification, competition, payments, regulated activities, and other
specialized legal questions require qualified counsel outside this skill.

## Account for multihoming and disintermediation

Expect participants to use alternatives when doing so improves reach, price,
reliability, or bargaining power. Determine:

- which side multihomes and at what cost
- whether participants bring the same capacity to every network
- what makes one network the first or fallback choice
- whether the product creates durable workflow, trust, coordination, or
  reputation value beyond initial discovery
- why participants transact directly after meeting and what they lose or gain

Respond by improving participant value, reliability, differentiation, and
appropriate protection. Do not invent exclusivity, conceal alternatives,
punish legitimate portability, or use coercive friction as a substitute for
value. Escalate legal or contractual restrictions to qualified counsel.

## Expand one supported cell at a time

Expand only after the initial network has a repeatable interaction, understood
failure modes, and an operating model that does not depend on hidden,
unbounded intervention.

For each adjacent cell:

1. state what is shared with the proven cell
2. identify what changes in participants, density, timing, trust, or operations
3. test the difficult side and core interaction again
4. preserve separate local metrics until the new cell is stable
5. set a containment boundary and stop rule

Do not let a strong market subsidize weak-market metrics invisibly. Global
averages can mask local shortages, declining match quality, and operational
loss.

## Recognize saturation and limits

Network value does not grow without bound. Look for:

- stable demand with excess participant capacity
- longer discovery time or lower visibility for participants
- rising cancellations, congestion, spam, or low-quality supply
- falling earnings, conversion, retention, or contribution margin
- increasingly similar offers and weaker differentiation
- trust or moderation costs that rise faster than successful interactions

At saturation, improve allocation, quality, retention, specialization, or
participant economics before maximizing account growth. Consider whether an
additional participant improves, redistributes, or destroys value. Treat a
ceiling as a product constraint, not automatically as an acquisition failure.

## Make the decision explicit

Return:

1. core interaction and participant roles
2. claimed network mechanism and competing explanations
3. smallest viable network and difficult side
4. cold-start or seeding plan with honest operating boundaries
5. local liquidity and match-quality evidence
6. trust, abuse, multihoming, and disintermediation risks
7. stay, narrow, expand, or stop recommendation
8. owner, decision window, guardrails, and evidence that changes the decision

Keep network claims proportional to observed outcomes. When evidence is missing,
propose the smallest bounded test rather than presenting network strength,
critical mass, or expansion readiness as fact.
