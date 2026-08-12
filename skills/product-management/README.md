[← Sebastian Software Skills](../../README.md)

# Product Management

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Turn customer and business evidence into a focused product decision, a
coherent experience, and a useful learning loop.**

This skill helps agents reason about what to build, why it matters, who it is
for, how small the first valuable scope can be, and what evidence should decide
the next move. It keeps discovery, strategy, delivery quality, distribution,
and post-release learning connected instead of treating them as separate
handoffs.

## What It Can Deliver

- opportunity assessments and evidence registers
- decision-readiness audits for product briefs, roadmaps, and recommendations
- claim-to-evidence reviews with explicit gates and closure conditions
- focused product-decision, go-to-market-claim, and launch-readiness reviews
- behavioral review calibration with counterfactual cases and outcome learning
- customer-problem and Jobs-to-be-Done synthesis
- product briefs, strategy, outcomes, and initial scope
- marketplace and multi-sided product strategy, cold-start, and liquidity plans
- empowered-team and product-operating-model recommendations
- AI-assisted exploration portfolios with evidence and commitment gates
- prioritization decisions and outcome-oriented roadmaps
- initiative gates that decide whether to start, delegate, park, or reject a
  substantial idea before allocating capacity
- feature-request and quality-bar reviews
- AI-era selection and subtraction decisions that protect whole-product
  coherence when implementation becomes cheap
- release, experiment, adoption, retention, and post-launch recommendations
- plans for turning service expertise into a repeatable product

## Use It When

Use Product Management when the hard question is what should be built, for
whom, why now, or whether it is ready to ship. The workflow separates observed
behavior, measured outcomes, commitments, stakeholder claims, and assumptions
so confident storytelling does not replace evidence.

## Example Prompts

```text
Turn these customer interviews and usage signals into an evidence-led MVP
recommendation.

Review this roadmap and identify where output commitments have replaced product
outcomes.

Run this proposed initiative through a decision gate. Show its leverage,
evidenced constraint, timing, displaced work, and smallest reversible test,
then recommend start, delegate, park, or reject.

Audit this polished product brief for decision readiness. Trace every important
claim to supplied evidence and tell me what blocks approval.

Review these launch claims against product behavior and customer proof, qualify
what we cannot support, and identify the product evidence marketing still needs.

Calibrate our product-review rubric against these past decisions without
overfitting to one preferred response or judging the original choice by hindsight.

Decide whether this feature is ready to ship, including its quality bar,
distribution path, and post-release learning plan.

Help us turn this consulting workflow into a repeatable software product without
inventing demand we have not validated.

Our team keeps accepting the first plausible AI-generated solution. Design an
exploration cadence that gets us to materially different options quickly
without confusing prototypes with customer evidence.

AI can build twelve plausible features this week. Decide which, if any, belong
in the product and use subtraction to preserve one coherent experience.

Turn this executive feature list into an empowered-team brief with an outcome,
constraints, shared product-design-engineering responsibilities, and honest
commitment gates.

Determine whether this referral loop is a real network effect, then design a
cold-start plan for the smallest market where reliable matches are possible.

Our marketplace has many registered users but poor matches in most cities.
Diagnose local liquidity, the difficult side, trust failures, and the next
expansion decision without inventing a universal density threshold.
```

See [SKILL.md](SKILL.md) for the evidence model, workflow routes, operating
rules, and default deliverable.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill product-management
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian product-management
dalo approve skill sebastian:product-management
dalo sync
```

## Related Skills

- [Market Research](../market-research/README.md) designs and executes customer
  and market research programs, then returns traceable evidence for the product
  decision.
- [Product Naming](../product-naming/README.md) turns a stable product thesis
  into researched name candidates.
- [Product Design](../product-design/README.md) turns product evidence and scope
  into a problem model, interaction system, and prototype plan.
- [Pricing and Packaging](../pricing-and-packaging/README.md) carries a stable
  target customer, product promise, and economic constraints into pricing
  research, value metrics, packages, and price changes.
- [Effective Web](../effective-web/README.md) designs and implements the browser
  experience after outcomes and scope are clear.
- [Decision Records](../decision-records/README.md) preserves durable product
  choices, tradeoffs, and review triggers.
- [LinkedIn Social Selling](../linkedin-social-selling/README.md) connects a
  stable offer to positioning, relationships, content, and pipeline.
- [Web Legal Compliance](../web-legal-compliance/README.md) handles privacy,
  consent, tracking, endorsements, and jurisdiction-specific web requirements.

## Scope

This skill supports product judgment; it does not manufacture customer
research, demand, metrics, commitments, network effects, or certainty. It
diagnoses product and market mechanisms but does not operate marketplace
participants or decide regulated market access. Design, implementation, legal,
and channel execution remain outside its scope except where a first-party skill
named above owns the handoff.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
