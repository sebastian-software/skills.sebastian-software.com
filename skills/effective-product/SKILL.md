---
name: effective-product
description: >-
  Decide what to build and how the product should work, on gathered rather than
  invented evidence: decision-led customer and market research from interviews,
  surveys, observation, review and community mining, and market landscapes to
  Voice of Customer, Jobs to Be Done, personas, and market sizing; product
  discovery, evidence review, strategy, outcomes, scope, prioritization,
  roadmaps, experiments, release decisions, marketplaces and network effects,
  and product operating models; design research, problem framing, object and
  journey modeling, information architecture, wireframes, prototypes, and habit
  and retention loops; product and feature naming; pricing, packaging, value
  metrics, tiers, and trials; and Architecture Decision Records. Use when
  evidence must be gathered or a product decision made: what, whether, or for
  whom to build, how the experience should behave, what to charge, what to name
  it, or how to record the decision. Do not use to implement the product, write
  marketing copy, or operate a channel.
---

# Effective Product

Decide what to build and how it should work. Turn gathered evidence into a
focused product decision, a coherent experience, a defensible price, and a
learning loop — and record the durable choices so they survive the people who
made them.

Treat discovery, design, scope, quality, pricing, and post-release behavior as
one system rather than separate handoffs.

## Workflow

1. Name the decision, the artifact it needs, the accountable owner, and the
   consequence of being wrong.
2. Build an evidence register before proposing anything. Separate observed
   behavior, measured outcomes, commitments, participant accounts, stakeholder
   claims, and assumptions. Never invent research, demand, metrics, customer
   language, market size, or willingness to pay.
3. Select one primary route from the table. Read that route before acting.
4. Load only the references the route names for this task.
5. Present options with consequences. Recommend one at the confidence the
   evidence supports, and name what would change the recommendation.
6. Define the smallest next action that reduces the most important uncertainty,
   plus an owner, a decision window, and a keep, change, or stop rule.

When evidence is absent, deliver a plan, a hypothesis, or a clearly labeled
provisional model — never a confident answer.

## Route by Intent

| User intent | Read |
| --- | --- |
| Explore an opportunity, run Jobs to be Done work, or judge whether an artifact, claim set, or recommendation is ready to decide on | [Discovery and Evidence Review](references/route-discovery.md) |
| Set a product thesis, outcomes, differentiation, or operating model; work on marketplaces, network effects, cold starts, or liquidity | [Strategy and Operating Model](references/route-strategy.md) |
| Choose initial scope, handle feature requests, build a roadmap, set a quality bar, or decide release readiness | [Scope, Quality, and Shipping](references/route-scope-and-shipping.md) |
| Plan or synthesize behavioral research, frame a problem space, or map expectations and mental-model gaps | [Design Research and Problem Framing](references/route-design-research.md) |
| Model objects, actions, relationships, flows, and journeys; build information architecture, wireframes, or prototypes | [Solution Modeling and Prototyping](references/route-design-modeling.md) |
| Design or review habit loops, triggers, rewards, investment, gamification, engagement, or retention mechanics | [Behavioral and Retention Design](references/route-behavioral-design.md) |
| Design a research program, recruit participants, run interviews, surveys, or observation, mine reviews and communities, or size a market | [Customer and Market Research](references/route-research.md) |
| Choose a value metric, pricing model, packages, entitlements, discounts, trials, or an existing-customer migration | [Pricing and Packaging](references/route-pricing.md) |
| Generate, screen, and shortlist a product, feature, company, or initiative name | [Product and Feature Naming](references/route-naming.md) |
| Create, review, supersede, or audit an Architecture Decision Record | [Decision Records](references/route-decisions.md) |

Discovery, Strategy, and Scope share the
[product decision contract](references/product-decision-contract.md). The three
design routes share the
[design inquiry contract](references/design-inquiry-contract.md).

## Operating Rules

- Optimize for user progress and business viability, not feature volume,
  technical novelty, stakeholder enthusiasm, or roadmap completion.
- Prefer specific past behavior and meaningful commitment over hypothetical
  intent. Sign-ups, compliments, traffic, and survey votes are weaker evidence
  than repeated use, switching, payment, or operational adoption.
- Research a decision, not a topic in the abstract. Remove research questions
  whose answers would not change anything.
- Report exact denominators rather than implying prevalence from a convenient
  sample. Use no universal minimum sample, confidence label, recency window, or
  saturation threshold.
- Reduce scope before reducing the critical-path quality bar.
- Keep observations, participant language, interpretation, principles,
  opportunities, and solution ideas in distinguishable layers.
- Treat behavioral influence as a design responsibility, not an automatic
  violation — and reject deception, coercion, disproportionate harm, and
  mechanics that depend on blocking informed choice.
- Price the value context, not the effort spent building the product. Separate
  willingness to pay from ability to pay, stated preference from behavior, and a
  published list price from an actual transaction.
- Separate registrability, availability, and desirability when naming. Never
  report domain, handle, or trademark status without a current dated check, and
  describe trademark research as preliminary screening, not legal clearance.
- Use AI to expose materially different options, assumptions, and missing
  questions. Never let it simulate participants or fill evidence gaps.
- Verify volatile market, competitor, platform, price, and regulatory facts at
  the time of use, and preserve observation dates.

## Routing Boundaries

- Route segment and category choice, positioning, messaging, claims and proof,
  launch planning, sales enablement, market learning, funnel diagnosis,
  conversion experiments, marketing copy, social and LinkedIn content, and
  consultant profile positioning to `effective-marketing`. This discipline
  supplies approved product facts, pricing facts, evidence limits, and
  constraints; return adoption or market evidence here when it changes the
  product decision.
- Route specification, implementation, and verification of the browser
  experience — UI, visual systems, accessibility, responsive behavior,
  performance, frontend testing — to `effective-web`, once the design direction
  and interaction model are ready.
- Route capture of supplied websites, screenshots, prototypes, or videos into a
  traceable visual and interaction specification, comparison of a produced
  result against those references for source overlap, and privacy, consent,
  tracking, testimonial, direct-marketing, and jurisdiction-specific legal
  requirements to `effective-web`.
- Route system architecture, data models, language-level engineering depth, and
  test design to `effective-engineering`.
- Route repository workflows — audits, ports, pull-request review, dependency
  updates, validation runs, technical documentation — to `effective-delivery`.
  Route the team system around the product work, such as unclear ownership,
  delegation, decision paths, meeting load, or cognitive load, there as well.
- Route articles, essays, thought leadership, editorial case studies, locale
  typography, and internal team-message rewriting to `effective-writing`.
- This discipline does not replace formal statistical, legal, regulated
  human-subjects, scientific, tax, accounting, antitrust, or specialist industry
  review when a decision exceeds the available competence and evidence.
