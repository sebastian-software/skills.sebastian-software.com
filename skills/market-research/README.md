[← Sebastian Software Skills](../../README.md)

# Market Research

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Turn consequential customer and market uncertainty into traceable evidence
that product, design, and go-to-market teams can actually use.**

Market Research helps agents design and execute research programs, work
responsibly with participants and public or internal sources, synthesize
contradictory evidence, and hand findings to the people who own the resulting
product, experience, positioning, or pricing decision.

## What It Can Deliver

- a decision-led research brief and method plan
- recruitment criteria, screeners, interview guides, and fieldwork operations
- customer, user, buyer, win/loss, churn, and contextual research
- survey plans and analyses with explicit sampling limits
- transcript, support, sales, review, community, and Voice of Customer synthesis
- category, alternative, competitor-customer, and market-size evidence
- traceable Jobs to Be Done and behavioral personas
- owner-specific handoffs into Product Management, Product Design, Product
  Marketing, and Pricing and Packaging

## Use It When

Use this skill when a team needs to gather or assess evidence rather than ask a
product, design, or marketing owner to reason from assumptions. It fits new
research programs, existing research corpora, mixed primary and secondary
research, and research repositories whose findings must remain traceable over
time.

## Example Prompts

```text
Design a research program to learn why operations leaders start evaluating this
category, what alternatives they use, and what evidence would change our target
market decision.

Recruit and interview recent switchers, non-deciders, users, and buyers. Keep
the buying sequence separate from the day-to-day experience and return the
appropriate findings to Product Management and Product Design.

Synthesize these interview transcripts, support tickets, sales notes, and
reviews. Preserve exact denominators, contradictions, source bias, and a
traceable Voice of Customer bank.

Build a current category and alternative map using primary sources and
competitor-customer evidence. Do not infer a competitor roadmap or market share
from marketing pages.

Audit this market-size estimate. Separate sourced counts from our incidence,
reach, adoption, and annual-value assumptions, then produce bounded scenarios.
```

See [SKILL.md](SKILL.md) for the research workflow, focused routes, evidence
rules, default deliverable, and handoff boundaries.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill market-research
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian market-research
dalo approve skill sebastian:market-research
dalo sync
```

## Related Skills

- [Product Management](../product-management/README.md) supplies the product or
  market decision, target situation, uncertainty, and consequence; it receives
  the resulting evidence and owns the product choice.
- [Product Design](../product-design/README.md) supplies experience and
  behavioral questions and turns situated findings into problem framing,
  interaction models, prototypes, and design decisions.
- [Product Marketing](../product-marketing/README.md) turns buyer, category,
  alternative, win/loss, language, and proof evidence into segment,
  positioning, message, launch, and enablement decisions.
- [Pricing and Packaging](../pricing-and-packaging/README.md) owns
  willingness-to-pay method, value metrics, prices, packages, trials, discounts,
  and migrations.
- [Web Legal Compliance](../web-legal-compliance/README.md) scopes current
  requirements for recruitment, recording, personal data, incentives,
  testimonials, direct marketing, and online research surfaces.

## Scope

This skill owns research design, recruitment, fieldwork, source work,
traceability, synthesis, and handoff. It does not invent respondents, demand,
market size, prevalence, competitor facts, or quotes, and it does not make the
downstream product, experience, positioning, pricing, or legal decision.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
