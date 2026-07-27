[← Sebastian Software Skills](../../README.md)

# Pricing and Packaging

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Make pricing decisions that customers can understand, the product can
support, and the available evidence can actually justify.**

Pricing and Packaging helps agents connect customer value, buying behavior,
product economics, and operating constraints. It covers research, value
metrics, pricing models, packages, trials, discounts, and existing-customer
changes without reaching for a universal formula or a decorative three-tier
table.

## What It Can Deliver

- a decision-specific pricing evidence register
- a willingness-to-pay and competitor research plan
- candidate value metrics with customer and business tradeoffs
- modeled subscription, usage, seat, outcome, or hybrid options
- packages and entitlements tied to distinct customer needs
- explicit discount, trial, and exception policies
- an existing-customer migration and communication plan
- a test plan with guardrails, decision rules, and rollback conditions

## Use It When

Use this skill when launching a new paid offer, revisiting an existing price,
choosing what to charge for, designing packages, setting trial or discount
policy, or moving existing customers to a new commercial model.

## Example Prompts

```text
Compare seat-based, usage-based, and hybrid pricing for this product using the
evidence we have. Make the unknowns and required research explicit.

Design packages for these three customer situations without assuming that we
need three tiers or hiding essential value behind arbitrary feature fences.

Plan a price increase for existing customers, including cohorts, notices,
contract constraints, support readiness, exceptions, monitoring, and rollback.

Review this competitor-pricing spreadsheet. Separate dated facts from inference
and propose the smallest research step before we commit to exact prices.
```

See [SKILL.md](SKILL.md) for the complete evidence, model, package, and rollout
workflow.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill pricing-and-packaging
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian pricing-and-packaging
dalo approve skill sebastian:pricing-and-packaging
dalo sync
```

## Related Skills

- [Product Management](../product-management/README.md) resolves the target
  customer, product promise, strategy, and viability assumptions that pricing
  depends on.
- [Decision Records](../decision-records/README.md) preserves an approved
  pricing choice, its tradeoffs, migration policy, and reopening conditions.
- [Web Legal Compliance](../web-legal-compliance/README.md) handles
  jurisdiction-aware disclosures, privacy, consent, and website requirements
  around presenting or testing an offer.

## Scope

The skill supports professional product and commercial decision-making, not
tax, accounting, revenue-recognition, antitrust, regulated-pricing, or
jurisdiction-specific contract advice. Exact market facts and platform
capabilities require current verification.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
