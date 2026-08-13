[← Sebastian Software Skills](../../README.md)

# Effective Product

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Decide what to build and how it should work — on evidence you gathered, not
evidence you assumed.**

Effective Product is one of six disciplines in this collection. It runs the
research that produces the evidence, frames the product decision, shapes the
experience, sets the price, finds the name, and records the durable choices so
they survive the people who made them. Discovery, design, scope, quality,
pricing, and post-release behavior stay one system rather than separate
handoffs.

It replaces the former `product-management`, `product-design`,
`market-research`, `product-naming`, `pricing-and-packaging`, and
`decision-records` skills. See [MIGRATION.md](../../MIGRATION.md) for the full
mapping.

## Ten Routes

| Route | Owns |
| --- | --- |
| Discovery and Evidence Review | opportunities, Jobs to be Done, decision-readiness audits |
| Strategy and Operating Model | theses, outcomes, network effects, empowered teams |
| Scope, Quality, and Shipping | initial scope, roadmaps, quality bars, release calls |
| Design Research and Problem Framing | research plans, problem space, mental models |
| Solution Modeling and Prototyping | objects, flows, journeys, IA, wireframes, prototypes |
| Behavioral and Retention Design | habit loops, rewards, gamification, retention |
| Customer and Market Research | programs, recruitment, fieldwork, VoC, market sizing |
| Pricing and Packaging | value metrics, models, tiers, trials, migrations |
| Product and Feature Naming | territories, generation, screening, shortlists |
| Decision Records | ADR creation, review, supersession, audits |

## What It Can Deliver

- research briefs, screeners, interview protocols, and traceable evidence
  registers
- Voice of Customer, Jobs to Be Done, evidence-based personas, market sizing
- opportunity assessments, product briefs, and decision-readiness audits
- product theses, outcomes, and operating-model change plans
- marketplace and network-effect analysis with local-liquidity reasoning
- initial scope, roadmaps, non-goals, and explicit quality bars
- release recommendations with instrumentation and stop-or-keep rules
- design briefs, problem framing, object models, flows, IA, and prototype plans
- habit and retention designs that reject coercive mechanics
- pricing and packaging options with customer and business scenarios
- name shortlists with dated domain, language, and preliminary trademark
  evidence
- Architecture Decision Records that follow the repository's own convention

## Use It When

Use this discipline when the open question is what to build, whether to build
it, for whom, how the experience should behave, what to charge, what to call it,
or how to make sure the reasoning is still findable in a year — and when the
answer must come from evidence rather than from confident wording.

## Example Prompts

```text
We think enterprise teams want an audit log. Design the research that would
tell us whether that is true, and what would falsify it.

Review this product brief for decision readiness. Which claims are supported,
which are assumptions wearing a framework, and what is missing?

Turn these behavioral findings into an object model, key flows, and a prototype
plan. Show me two structurally different directions.

We charge per seat and customers are gaming it. Give me two or three value
metrics with realistic billing scenarios and migration paths.

Name this feature so it works in German and English, is spellable after hearing
it once, and does not collide with an obvious trademark.

Record why we chose event sourcing here, what we rejected, and what would
reopen the decision.
```

See [SKILL.md](SKILL.md) for the workflow, evidence rules, route table, and
routing boundaries.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-product
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian effective-product
dalo approve skill sebastian:effective-product
dalo sync
```

## Related Disciplines

- [Effective Marketing](../effective-marketing/README.md) owns segment and
  category choice, positioning, messaging, launch, funnels, and channels. This
  discipline supplies the approved product and pricing facts; that one takes
  them to market.
- [Effective Web](../effective-web/README.md) owns the browser experience once
  the design direction is ready, plus reference capture, originality audits, and
  jurisdiction-aware compliance.
- [Effective Engineering](../effective-engineering/README.md) owns system
  architecture, data models, and the code itself.
- [Effective Delivery](../effective-delivery/README.md) owns repository
  workflows and the team system around the product work.

## Scope

This discipline gathers and judges evidence; it does not invent it. It does not
fabricate participants, quotes, observations, demand, prevalence, competitor
behavior, market size, or willingness to pay, and it does not implement the
product, write marketing copy, or operate a channel. It does not replace formal
statistical, legal, regulated human-subjects, scientific, tax, accounting,
antitrust, or specialist industry review when a decision exceeds the available
competence and evidence.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
