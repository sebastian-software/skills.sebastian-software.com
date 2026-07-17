[← Sebastian Software Skills](../../README.md)

# Consultant Profile

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Turn a career history into a credible professional thesis that helps the
right client understand why they should hire this consultant next.**

Consultant Profile helps agents create, audit, rewrite, localize, and improve
consultant CVs, LinkedIn and XING profiles, case studies, project lists, bios,
and senior technology-consulting resumes. It replaces reverse-chronological
inventory with evidence-led positioning and a coherent career narrative.

## What It Can Deliver

- a clear target-reader and buying-situation analysis
- a profile thesis and differentiated positioning
- evidence-led project selection and prominence
- complete case studies with context, responsibility, decisions, and outcomes
- a connected professional narrative instead of a loose project list
- gap analysis and interview questions for missing evidence
- synchronized CV, website, LinkedIn, XING, bio, and project-list content
- localized versions that preserve meaning and professional credibility

## Use It When

Use this skill when a profile needs to help a buyer, recruiter, partner, or
staffing lead quickly understand the consultant's unusual strengths, trusted
contexts, industries, level of responsibility, demonstrated impact, and best
next engagement.

## Example Prompts

```text
Audit this consultant CV for positioning, completeness, project prominence, and
evidence gaps.

Turn these project notes into three buyer-relevant case studies without
inventing metrics or responsibilities.

Build one coherent narrative across my website profile, LinkedIn, and the CV I
send to staffing partners.

Interview me for the missing information needed to position me as a senior
frontend and product consultant.
```

See [SKILL.md](SKILL.md) for the profile principles, narrative workflow,
interview process, persuasion boundaries, and quality bar.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill consultant-profile
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian consultant-profile
dalo approve skill sebastian:consultant-profile
dalo sync
```

## Related Skills

- [LinkedIn Social Selling](../linkedin-social-selling/README.md) connects the
  profile to target accounts, content, conversations, and qualified meetings
  after Consultant Profile owns the professional evidence and field-level
  profile content.
- [Product Naming](../product-naming/README.md) handles a consultant business,
  productized-service, or company name once the positioning is clear.
- [Metro English](../metro-english/README.md) adapts supporting communication to
  natural US professional English.
- [Locale Typography](../locale-typography/README.md) applies the correct
  visible-prose conventions to localized profile versions.

## Scope

The skill does not invent clients, responsibilities, outcomes, testimonials,
metrics, credentials, or career history. It improves selection, structure, and
language while keeping every substantive claim traceable to evidence.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
