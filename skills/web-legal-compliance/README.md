[← Sebastian Software Skills](../../README.md)

# Web Legal Compliance

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Turn “make this website compliant” into a jurisdiction-aware, evidence-backed
work product instead of generic boilerplate.**

Web Legal Compliance helps agents scope, research, draft, and review the legal
surfaces of websites, web apps, online stores, and digital services across the
EU and EEA, the United Kingdom, Canada and its provinces, and the United States
and its states.

## What It Can Deliver

- a jurisdiction and obligation map
- an operator, audience, transaction, and data-flow questionnaire
- issue inventories and implementation reviews
- page and disclosure maps
- legal notice or Impressum drafts with explicit placeholders
- privacy, cookie, consent, and tracking requirements
- online-sales, marketing, endorsement, and testimonial disclosures
- counsel-ready briefs that separate facts, assumptions, and open questions

## Why It Works Differently

Legal text is the visible result of operational facts and decisions. The skill
therefore establishes the operator, places of establishment, targeted markets,
audience, transactions, data flows, marketing channels, publishing model, and
regulated activities before drafting. Unknown facts stay unknown instead of
being filled with plausible-looking inventions.

## Example Prompts

```text
Audit this SaaS website's disclosures and consent flow for customers in the EU,
UK, Canada, and California.

Create a questionnaire and placeholder-based legal-notice draft for this German
company; do not invent missing registration or contact details.

Review whether our cookie banner behavior matches the claims in the privacy and
cookie notices.

Prepare a counsel-ready brief for launching this online service in the United
States and Canada, including unresolved business facts.
```

See [SKILL.md](SKILL.md) for the evidence workflow, regional routes, consent
guidance, operating rules, and deliverables.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill web-legal-compliance
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian web-legal-compliance
dalo approve skill sebastian:web-legal-compliance
dalo sync
```

## Related Skills

- [Effective Web](../effective-web/README.md) implements and verifies footer
  navigation, forms, consent UI, accessibility, and frontend behavior after the
  requirements are established.
- [Locale Typography](../locale-typography/README.md) applies locale-specific
  visible-prose rules after wording and target locales are approved.
- [Product Management](../product-management/README.md) aligns product scope,
  markets, and release decisions with unresolved compliance constraints.
- [Decision Records](../decision-records/README.md) preserves durable consent,
  tracking, and disclosure decisions where appropriate.

## Scope

This skill does not replace qualified legal advice. Penetration testing,
security architecture, records of processing, vendor contracts, tax advice,
employment law, and corporate filings remain outside its scope unless they
directly determine a web disclosure.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
