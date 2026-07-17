[← Sebastian Software Skills](../../README.md)

# LinkedIn Social Selling

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Build a coherent B2B path from a specific buyer problem to a useful
conversation and a qualified meeting.**

LinkedIn Social Selling helps agents design an evidence-led acquisition system
across positioning, profile, network, content, outreach, conversations, lead
magnets, funnels, and measurement. It treats those surfaces as one learning
system rather than a collection of growth hacks.

## What It Can Deliver

- target-buyer, problem, proof, and offer positioning
- an inbound profile and featured-section plan
- target-account and relationship-building workflows
- welcome messages, outreach sequences, and conversation guidance
- content pillars connected to commercial intent
- lead-magnet and next-step offers
- funnel specifications from profile visit to opportunity
- experiment plans and measurements for the weakest transition

## How It Thinks

The skill maps the whole path:

```text
target buyer -> profile or content -> relationship signal -> conversation
             -> useful next step -> qualified meeting -> opportunity
```

It identifies the weakest transition before prescribing activity everywhere.
Customer language, testimonials, proof, metrics, and case-study outcomes must
come from evidence rather than marketing imagination.

## Example Prompts

```text
Build a LinkedIn acquisition system for this consulting offer, from profile
positioning through the first qualified meeting.

Audit why our posts get engagement but rarely lead to relevant conversations.

Create a target-account networking and welcome-message workflow that feels
useful rather than automated or extractive.

Design a lead magnet and funnel experiment around this buyer problem and define
what we should measure.
```

See [SKILL.md](SKILL.md) for the complete evidence, positioning, path-mapping,
experiment, and deliverable workflow.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill linkedin-social-selling
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian linkedin-social-selling
dalo approve skill sebastian:linkedin-social-selling
dalo sync
```

## Related Skills

- [LinkedIn Posts](../linkedin-posts/README.md) creates individual posts, ideas,
  and calendars after audience and commercial intent are clear.
- [Consultant Profile](../consultant-profile/README.md) develops the underlying
  CV, biography, case studies, and consultant positioning.
- [Product Management](../product-management/README.md) stabilizes the customer
  problem, promise, evidence, and scope behind the offer.
- [Effective Web](../effective-web/README.md) builds and verifies landing pages,
  forms, analytics delivery, accessibility, and responsive behavior.
- [Web Legal Compliance](../web-legal-compliance/README.md) covers consent,
  tracking, lead forms, email capture, testimonials, and endorsements.

## Scope

This skill is not a spam system. It does not invent proof, impersonate genuine
relationships, optimize for vanity metrics, or treat every contact as a lead.
Post-only requests should use the narrower LinkedIn Posts skill.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
