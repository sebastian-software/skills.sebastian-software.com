# Problem Framing

Document the problem space as a system of real situations, behavior,
expectations, and consequences before committing to a feature or screen model.
The goal is not to prove that the initial brief was right; it is to make the
next design exploration more relevant and challengeable.

## Bound the problem space

Describe:

- actors and affected people, including those who do not directly operate the
  product
- triggering situations and conditions
- goals, responsibilities, and progress people are trying to make
- current activities, tools, artifacts, handoffs, workarounds, and alternatives
- important objects, information, rules, permissions, and dependencies
- physical, social, organizational, and technical environment
- consequences before, during, and after the focal activity
- observed variations, contradictions, exclusions, and unresolved questions

Keep observations and inference distinguishable. Link important claims to
research evidence and label stakeholder beliefs or supplied requirements as
assumptions until supported.

Do not define the boundary as “the part our proposed app handles.” Activities
usually begin with an external trigger and end with an effect elsewhere in a
person's life or work. Include that wider arc so the team can see where a
product should connect, stay out of the way, or support recovery.

## Map expectations and mental models

A mental model describes how people understand and conduct an activity, not the
navigation of the current product. Build it from observed language, sequence,
decisions, strategies, objects, and causal beliefs.

For each meaningful stage capture:

1. trigger and desired progress
2. activities, decisions, and alternatives
3. objects, tools, people, and information used
4. expected cause and effect
5. uncertainty, attention, emotion, and adaptation
6. result, reflection, and what happens outside the product

Average or abstract only where the evidence supports a useful pattern. Preserve
important variants rather than forcing every participant into one tidy journey.
Give the model a readable narrative, but do not invent connective events to
make the story more satisfying.

Compare three views when a product already exists or a direction is emerging:

- **User model:** how people believe the domain and activity work.
- **Designed model:** the concepts, structure, and causality communicated by
  the interface.
- **System model:** how data, state, permissions, and operations actually work.

Identify gaps explicitly. Decide whether to align the design with an established
expectation, teach a necessary new model, expose more of the system, or change
the underlying system. Do not hide a consequential mismatch with friendlier
microcopy alone.

## Frame problems without prescribing solutions

A useful problem statement names a situated actor, desired progress, observed
barrier, and why it matters. It does not smuggle the team's preferred feature
into the need.

```text
When [situation], [actor] needs to [make progress], but [observed condition]
interferes, which leads to [meaningful consequence].
```

Test the statement:

- Is every factual clause supported or labeled as a hypothesis?
- Does it describe behavior and consequence rather than a missing interface?
- Is the boundary narrow enough to explore but broad enough for multiple
  solutions?
- Does it avoid treating the person as defective, lazy, or irrational?
- Would solving it improve the person's outcome, not merely product usage?

## Add empowerment framing

Problem language can overemphasize deficiency and steer teams toward rescue,
control, or forced compliance. Pair it with an empowerment statement that names
existing capability and the conditions that would increase agency.

```text
[Actor] can already [capability or strategy]. They should be able to
[desired agency or outcome] when [situation], with support for [conditions]
without requiring [harmful tradeoff].
```

Use both frames. The problem statement makes a consequential obstacle visible;
the empowerment statement prevents the design from erasing successful coping,
flexibility, dignity, or choice.

## Create opportunity questions

Turn supported tensions into several open questions. “How might we” is useful
only when the question remains plural and decision-relevant.

- Avoid embedding a component, channel, or reward mechanic.
- Include the context and outcome that make the opportunity specific.
- State safety, accessibility, privacy, or autonomy constraints when ignoring
  them would invite harmful concepts.
- Write questions at multiple altitudes, then discard those too broad to guide
  exploration or too narrow to permit alternatives.
- Include a “How might we avoid…” or explicit non-goal when the obvious product
  incentive conflicts with user well-being.

Separate generation from selection. For each supported question, generate
materially different ideas before debating feasibility. Record products,
services, environments, or conventions that demonstrate relevant fragments so
precedent is visible rather than unconsciously copied. Then compare ideas with
cross-functional input on likely impact, evidence, strategic fit, feasibility,
uncertainty, risk, and the cost of being wrong. Do not let the loudest person or
the easiest implementation become the selection method.

Keep high-impact uncertain ideas as focused explorations, not automatic scope.
Treat easy low-impact ideas as optional, and explicitly set aside ideas that are
both weak and expensive. Select a coherent first exploration rather than a
complete roadmap, and preserve the remaining ideas for later reconsideration.
Frequency alone must not erase rare but severe cases.

This comparison chooses what design should explore next; it does not set product
priority, roadmap order, release scope, or investment. Route those decisions to
[`product-management`](../../product-management/SKILL.md) with the exploration
evidence and tradeoffs attached. Describe the output here as an exploration
order unless product management has already supplied an accepted priority.

## Problem-space deliverable

Provide:

- boundary, actors, context, and evidence register
- current activity, object, system, and alternative map
- behavioral patterns and meaningful variations
- mental model with external triggers and effects
- user/designed/system-model gaps
- problem and empowerment statements
- opportunity questions ordered for design exploration, plus non-goals
- assumptions, contradictions, risks, and next evidence needed

Stop before a final screen list. The next step is to use these materials to
explore competing solution systems and interaction models.
