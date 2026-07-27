[← Sebastian Software Skills](../../README.md)

# Conversion Optimization

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Find the real constraint in a funnel, then learn whether a responsible change
improves valuable completion without borrowing from trust or long-term value.**

Conversion Optimization helps agents connect funnel data, research, friction
and objection hypotheses, experiment design, guardrails, and result decisions.
It favors the strongest evidenced bottleneck over cosmetic test volume and
offers honest qualitative, sequential, and observational paths when traffic
cannot support a useful randomized comparison.

## What It Can Deliver

- funnel and measurement-contract audits
- quantitative and qualitative bottleneck diagnoses
- evidence-linked friction and objection hypotheses
- ethical experiment or alternative learning plans
- primary metrics, accessibility and trust guardrails, and stop conditions
- low-traffic qualitative, sequential, and observational approaches
- ship, iterate, stop, revert, or investigate decisions

## Use It When

Use this skill for signup, checkout, activation, lead, upgrade, onboarding, or
retention funnels; unclear drop-off; experiment backlogs; low-traffic products;
conflicting metrics; or a reported uplift whose data quality, practical value,
or downstream effects need review.

## Example Prompts

```text
Diagnose this checkout funnel from the supplied events, support records, and
usability observations. Prioritize the best-supported constraint, not button
color ideas.

We have too little traffic for a conventional A/B test. Design a qualitative
and sequential learning plan and state what it cannot prove causally.

Review this experiment plan for exposure errors, sample assumptions, stopping
rules, accessibility, trust, retention, refunds, and support guardrails.

The primary metric improved, but cancellations, complaints, and failed keyboard
completion worsened. Decide whether to ship, revert, segment, or investigate.
```

See [SKILL.md](SKILL.md) for the complete diagnosis, experiment, measurement,
and decision workflow.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill conversion-optimization
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian conversion-optimization
dalo approve skill sebastian:conversion-optimization
dalo sync
```

## Related Skills

- [Product Marketing](../product-marketing/README.md) owns segment, position,
  messaging, proof, launch, and market-learning choices; Conversion Optimization
  diagnoses and tests their funnel expression.
- [Product Management](../product-management/README.md) owns the target user,
  core product value, journey, scope, quality bar, and release decision.
- [Pricing and Packaging](../pricing-and-packaging/README.md) owns value
  metrics, prices, packages, discounts, trials, and customer migrations.
- [Effective Web](../effective-web/README.md) implements and verifies approved
  browser variants, forms, analytics, accessibility, and performance.
- [Web Legal Compliance](../web-legal-compliance/README.md) scopes current
  consent, tracking, privacy, claims, disclosure, and online-sales requirements.

## Scope

This skill covers diagnosis, research synthesis, learning design, guardrails,
and result decisions. It does not invent evidence, guarantee causal certainty,
implement browser changes, authorize deceptive patterns, or replace qualified
legal, privacy, or statistical review where the stakes require it.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
