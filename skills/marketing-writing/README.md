[← Sebastian Software Skills](../../README.md)

# Marketing Writing

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Turn approved market truth into persuasive copy that readers can recognize,
trust, and act on.**

Marketing Writing combines the useful core of copywriting, marketing
psychology, and copy editing in one evidence-led workflow. It helps agents
shape the reader's path through a commercial choice, create honest emotional
resonance, place claims beside appropriate proof, and revise the result without
inventing customer language, urgency, or conversion certainty.

## What It Can Deliver

- copy briefs grounded in audience, entry context, offer, proof, and constraints
- homepages, landing pages, product and service pages, pricing pages, About
  pages, sales pages, launch assets, campaigns, and marketing emails
- persuasive paths adapted to reader state instead of a universal formula
- truthful emotional framing and responsible behavioral mechanisms
- headlines, section copy, objection handling, proof placement, and calls to
  action
- focused copy critiques, rewrites, and multi-pass marketing copy revision
- explicit evidence gaps and owner handoffs when the brief cannot support a
  claim

## Use It When

Use this skill when the primary job of the writing is to help a specific reader
understand a credible offer and take a proportionate next step. It can start
from an approved brief, rough notes, an existing page, or a finished draft that
needs a marketing-specific edit.

For articles, essays, reports, thought leadership, and other primarily
editorial factual prose, use
[Nonfiction Writing](../nonfiction-writing/README.md). For deciding the audience,
position, message, and claims before drafting, use
[Product Marketing](../product-marketing/README.md).

## Example Prompts

```text
Turn this approved positioning brief, Voice of Customer register, and proof
pack into landing-page copy. Build the argument around the visitor's entry
state, keep each claim traceable, and make the consultation CTA proportionate.

Rewrite this technical product page for engineering leaders. Preserve the
approved terminology and constraints, explain the mechanism clearly, and add
emotional relevance without pretending the product guarantees an outcome.

Review this pricing page in separate passes for message, proof, specificity,
emotional truth, objections, risk, action, voice, and mechanics. Do not change
the package facts or invent urgency.

Create three genuinely different campaign openings: one led by recognition,
one by mechanism, and one by proof. Explain which reader state each serves and
keep all variants inside the same approved position.

Audit this sales copy for psychological pressure. Replace fake scarcity,
loss-heavy framing, and vague social proof with transparent, supportable
reasons to act.
```

See [SKILL.md](SKILL.md) for the workflow, focused writing routes, operating
rules, default deliverables, and routing boundaries.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill marketing-writing
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian marketing-writing
dalo approve skill sebastian:marketing-writing
dalo sync
```

## Related Skills

- [Market Research](../market-research/README.md) supplies traceable customer
  situations, alternatives, objections, language, and proof needs rather than
  synthetic Voice of Customer.
- [Product Marketing](../product-marketing/README.md) owns audience, position,
  message hierarchy, claims, proof, launch strategy, and the writing brief.
- [Pricing and Packaging](../pricing-and-packaging/README.md) owns prices,
  packages, discounts, trials, guarantees, and migration facts before they are
  expressed in copy.
- [Effective Web](../effective-web/README.md) owns page hierarchy, interface
  copy, implementation, accessibility, responsive behavior, and browser
  verification around the finished marketing prose.
- [Conversion Optimization](../conversion-optimization/README.md) diagnoses the
  funnel, approves learning interventions, and judges results; Marketing
  Writing drafts or revises the copy variant.
- [Web Legal Compliance](../web-legal-compliance/README.md) scopes current
  requirements for claims, testimonials, endorsements, disclosures, direct
  marketing, consent, subscriptions, and online sales.

## Scope

This skill owns evidence-bounded commercial prose, persuasive sequence,
emotional and behavioral framing, and marketing-specific revision. It does not
choose the product strategy, position, price, content portfolio, page
implementation, experiment verdict, or legal conclusion, and it never invents
proof, customer language, urgency, or measured impact.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
