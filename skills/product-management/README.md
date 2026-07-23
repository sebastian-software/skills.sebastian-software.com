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
- customer-problem and Jobs-to-be-Done synthesis
- product briefs, strategy, outcomes, and initial scope
- prioritization decisions and outcome-oriented roadmaps
- feature-request and quality-bar reviews
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

Audit this polished product brief for decision readiness. Trace every important
claim to supplied evidence and tell me what blocks approval.

Review these launch claims against product behavior and customer proof, qualify
what we cannot support, and identify the product evidence marketing still needs.

Decide whether this feature is ready to ship, including its quality bar,
distribution path, and post-release learning plan.

Help us turn this consulting workflow into a repeatable software product without
inventing demand we have not validated.
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

- [Product Naming](../product-naming/README.md) turns a stable product thesis
  into researched name candidates.
- [Product Design](../product-design/README.md) turns product evidence and scope
  into a problem model, interaction system, and prototype plan.
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
research, demand, metrics, commitments, or certainty. Dedicated design,
implementation, legal, and channel work should move to the relevant specialist
skill once the product decision is stable.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
