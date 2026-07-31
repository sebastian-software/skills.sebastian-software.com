[← Sebastian Software Skills](../../README.md)

# Effective Marketing

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Take verified value to market — position it, say it, write it, distribute it,
and learn from what the market answers.**

Effective Marketing is one of six disciplines in this collection. It turns
stable product, customer, and career evidence into a position people
understand, claims they can trust, copy that helps a decision, channels that
reach the right reader, and a learning loop that can revise all of it. It keeps
product evidence, market position, message expression, and channel tactic
separately reviewable, so polished copy never becomes retroactive proof that the
product works.

It replaces the former `product-marketing`, `marketing-writing`,
`conversion-optimization`, `create-social-content`, `linkedin-posts`,
`linkedin-social-selling`, and `consultant-profile` skills. See
[MIGRATION.md](../../MIGRATION.md) for the full mapping.

## Twelve Routes

| Route | Owns |
| --- | --- |
| Positioning and Segmentation | segments, alternatives, category, differentiation |
| Messaging and Proof | message architecture, claim-to-proof checks, objections |
| Launch and Sales Enablement | launch scope, readiness, enablement, guardrails |
| Market Learning | win/loss, adoption analysis, what changes the decision |
| Marketing Copywriting | homepages, landing, product, pricing, campaign, sales, email |
| Conversion Optimization | funnel diagnosis, experiment design, ship/stop decisions |
| Social Content | X, Threads, Bluesky, Instagram, Mastodon, multi-platform |
| LinkedIn Posts | LinkedIn ideas, drafting, formats, content calendars |
| LinkedIn Social Selling | profile-to-pipeline acquisition systems |
| Consultant Profile | CVs, profiles, bios, signature projects, structure |
| Profile Voice and Localization | personality, boundaries, tone, market adaptation |
| Profile Evidence and Interviews | source inventory, interview mode, provider fields |

## What It Can Deliver

- positioning briefs with rejected options and named non-goals
- message hierarchies with claim-to-proof traceability and honest proof gaps
- launch plans with readiness conditions, ownership, and rollout guardrails
- win/loss and adoption reviews that say what the market actually answered
- homepage, landing, product, pricing, campaign, sales, and email copy
- funnel diagnoses, experiment designs, and ship, iterate, or stop decisions
- platform-native social content that adapts rather than truncates
- LinkedIn posts, calendars, and end-to-end social-selling systems
- consultant profiles that sell a thesis instead of listing a career
- interview plans that close the evidence gaps a profile still has

## Use It When

Use this discipline when a real capability needs a market-facing decision: who
it is for, what to claim, what proof supports it, how to say it on a page or a
platform, why a funnel leaks, or how a consultant should be understood by a
buyer. Use it when the answer must come from evidence rather than from
confident wording.

## Example Prompts

```text
We have three customer segments and no clear position. Give me two or three
materially different options with the evidence and tradeoffs for each.

Review these landing-page claims against the proof we actually have. Tell me
which ones we cannot support and what evidence would close the gap.

Signup drops 60% between the plan page and checkout. Diagnose it before
proposing a test, and tell me if this is even an A/B test question.

Rewrite this pricing page for a technical buyer. Keep the exact product terms
and every constraint that keeps the claims true.

Turn this migration write-up into posts for LinkedIn and Mastodon. Do not make
the social version claim more than the source supports.

Audit my consultant profile. What is my thesis, which projects should be
signature, and what evidence is still missing?
```

See [SKILL.md](SKILL.md) for the workflow, evidence boundary, route table, and
routing boundaries.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-marketing
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian effective-marketing
dalo approve skill sebastian:effective-marketing
dalo sync
```

## Related Disciplines

- [Effective Product](../effective-product/README.md) owns customer and market
  research, the product decision itself, pricing and packaging, and the
  Architecture Decision Records that keep durable positioning and voice choices
  from drifting.
- [Effective Writing](../effective-writing/README.md) owns articles, essays,
  newsletters, thought leadership, and editorial case studies — informing and
  explaining, where this discipline owns the commercial choice — plus locale
  typography and AI-pattern audits.
- [Effective Web](../effective-web/README.md) owns page hierarchy, interface
  copy, forms, analytics delivery, experiment implementation, accessibility,
  performance, originality audits, and jurisdiction-aware web compliance.
- [Effective Delivery](../effective-delivery/README.md) owns repository-derived
  technical facts, executable examples, and controlled-language documentation.

## Scope

This discipline works from supplied or verifiable evidence. It does not invent
customer language, testimonials, outcomes, statistics, market size, competitor
behavior, differentiation, or certainty; it does not authorize deceptive
interfaces or dark patterns; and it does not replace legal, privacy, or
specialist statistical review when risk and uncertainty exceed the available
evidence. Drafting content is not permission to publish it.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
