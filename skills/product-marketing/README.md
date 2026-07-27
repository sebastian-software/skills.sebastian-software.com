[← Sebastian Software Skills](../../README.md)

# Product Marketing

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Turn real product and customer evidence into a position the market can
understand, claims it can trust, and a launch the team can learn from.**

Product Marketing helps agents connect segmentation, category choices,
positioning, messaging, proof, launch readiness, sales enablement, and market
learning. It keeps product facts, market interpretation, message expression,
and channel execution separate so confident copy cannot manufacture certainty.

## What It Can Deliver

- an evidence-backed segment and category recommendation
- positioning options with alternatives, tradeoffs, and non-goals
- a message hierarchy and claim-to-proof register
- a launch scope, readiness review, sequence, and ownership map
- sales discovery, narrative, demonstration, objection, and proof guidance
- a win/loss review that includes non-decisions and selection limits
- adoption analysis across first value, repeated value, and retained use
- a decision loop for changing the position, message, proof, or channel

## Use It When

Use this skill when a product direction is stable enough to explain to a
market, but the team still needs to decide which segment and category context
matter, what it can truthfully claim, how to coordinate a launch, what sales
needs, or what market response should change next.

## Example Prompts

```text
Turn these interview notes, product constraints, and usage outcomes into two
positioning options. Keep unsupported differentiation and customer language
explicit.

Audit this messaging hierarchy. Trace every outcome and comparison claim to
product behavior and customer proof, then qualify or remove what outruns it.

Plan a staged launch for this product update, including audience, readiness,
sales enablement, proof gaps, operational owners, and stop or expand rules.

Review these win, loss, no-decision, and adoption records. Tell us whether the
evidence supports changing the segment, position, message, proof, or channel.
```

See [SKILL.md](SKILL.md) for the agent-facing workflow, evidence rules, routes,
and handoff boundaries.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill product-marketing
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian product-marketing
dalo approve skill sebastian:product-marketing
dalo sync
```

## Related Skills

- [Product Management](../product-management/README.md) supplies the product
  thesis, target user, scope, quality bar, release decision, and verified
  product evidence that positioning must not invent.
- [Pricing and Packaging](../pricing-and-packaging/README.md) owns price
  research, value metrics, models, packages, discounts, trials, and customer
  migrations; Product Marketing communicates approved commercial choices.
- [Nonfiction Writing](../nonfiction-writing/README.md) turns a stable message
  and proof brief into credible finished prose.
- [Effective Web](../effective-web/README.md) implements and verifies the
  resulting landing pages, product pages, forms, analytics, and experiments.
- [LinkedIn Social Selling](../linkedin-social-selling/README.md) adapts the
  approved position and message to LinkedIn relationships, content, and
  pipeline.
- [Web Legal Compliance](../web-legal-compliance/README.md) scopes current
  requirements for claims, testimonials, endorsements, direct marketing,
  consent, tracking, disclosures, and online sales.

## Scope

This skill does not invent product evidence, customer quotations, market facts,
differentiation, or certainty. It does not replace product strategy, pricing
research, legal advice, finished editorial work, web implementation, or
channel-specific operation; those handoffs remain with the related owners.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
