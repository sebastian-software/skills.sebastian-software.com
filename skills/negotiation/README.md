[← Sebastian Software Skills](../../README.md)

# Negotiation

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Prepare credible options, learn what matters, and reach professional
agreements without bluffing past your authority.**

Negotiation helps agents support commercial, product, and technical
conversations from preparation through written closure. It makes interests,
real alternatives, limits, authority, exchangeable terms, proposals, and
concessions explicit while keeping tentative exploration separate from an
authorized commitment.

## What It Can Deliver

- a negotiation brief with parties, facts, interests, and unknowns
- real alternatives, targets, limits, and an escalation path
- several multi-term packages instead of a single-position demand
- an information-gathering and conversation plan
- conditional proposal and concession language
- commercial, product, and technical context checks
- a written outcome separating agreed, conditional, open, and rejected terms
- execution owners, dependencies, dates, and review triggers

## Use It When

Use this skill for customer and vendor terms, authorized pricing conversations,
scope or roadmap tradeoffs, delivery commitments, service levels, technical
migrations, procurement discussions, impasses, or cross-team agreements.

## Example Prompts

```text
Prepare this vendor renewal negotiation. Separate facts from assumptions,
identify our real alternatives, and give me three coherent term packages.

Help me respond to a customer asking for a discount, a custom feature, and a
faster launch. Keep every trade conditional and within the mandate below.

Plan a technical migration negotiation between two teams. Surface dependencies,
unknowns, risk ownership, service levels, and the approvals needed before dates
become commitments.

Turn these meeting notes into a written summary that distinguishes tentative
options, agreement in principle, authorized terms, and unresolved points.
```

See [SKILL.md](SKILL.md) for the complete preparation, conversation, proposal,
and closure workflow.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill negotiation
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian negotiation
dalo approve skill sebastian:negotiation
dalo sync
```

## Related Skills

- [Pricing and Packaging](../pricing-and-packaging/README.md) owns evidence-led
  price, package, discount, trial, and migration-policy decisions before their
  authorized terms enter a negotiation.
- [Product Management](../product-management/README.md) owns product direction,
  roadmap, scope, priorities, and release tradeoffs before they become promises.
- [Software Architecture](../software-architecture/README.md) establishes
  technical feasibility, operational risk, and credible migration options.
- [Decision Records](../decision-records/README.md) preserves durable internal
  product or technical choices after an agreement; it is not a contract store.

## Scope

The skill supports professional commercial, product, and technical
negotiations. It does not cover crisis or hostage negotiation, coercive
situations, legal representation, jurisdiction-specific contract advice, or
signing on another person's behalf.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
