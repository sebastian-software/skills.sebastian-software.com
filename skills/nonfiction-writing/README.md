[← Sebastian Software Skills](../../README.md)

# Nonfiction Writing

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Turn ideas and evidence into clear, credible, persuasive prose without losing
the author's voice.**

Nonfiction Writing helps agents plan, draft, revise, and critique articles,
essays, newsletters, reports, thought leadership, content marketing, case
studies, About pages, and product descriptions. It joins long-form craft with
legitimate marketing intent while keeping claims, quotations, examples, and
outcomes tied to real source material.

## What It Can Deliver

- focused theses, outlines, leads, transitions, and endings
- complete articles, essays, newsletters, and explanatory pieces
- thought leadership and content marketing with credible persuasive structure
- case studies, About pages, and product or service descriptions
- structural, evidentiary, voice, and line-level revisions
- prioritized critiques that distinguish errors, tradeoffs, and preferences

## Use It When

Use this skill when notes must become a coherent factual piece, a draft needs
stronger structure or cleaner prose, an author's real voice should survive
editing, or informative writing should also demonstrate expertise and support
a commercial next step. It can work alone or supply prose craft inside a
channel-specific first-party workflow.

## Example Prompts

```text
Turn these workshop notes into a 1,500-word article for product leaders. Make a
clear argument, preserve my direct voice, and flag any proof we still need.

Revise this essay for structure, rhythm, and clarity without flattening its
personal tone or changing the facts.

Write a useful thought-leadership article that demonstrates our approach and
ends with a credible invitation to talk—without turning every paragraph into a
sales pitch.

Convert these supplied project facts and measured outcomes into a case study.
Do not invent customer quotes or imply results beyond the measurement window.
```

See [SKILL.md](SKILL.md) for the workflow, evidence rules, writing routes,
revision passes, and routing boundaries.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill nonfiction-writing
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian nonfiction-writing
dalo approve skill sebastian:nonfiction-writing
dalo sync
```

## Related Skills

- [LinkedIn Posts](../linkedin-posts/README.md) owns LinkedIn-specific ideas,
  formats, cadence, and engagement context.
- [Consultant Profile](../consultant-profile/README.md) selects and structures
  professional evidence and positioning before the prose is written.
- [Tech Docs](../tech-docs/README.md) derives technical documentation from
  implemented software contracts and verifies it with repository tooling.
- [Effective Web](../effective-web/README.md) owns interface copy and the
  surrounding browser experience.
- [Locale Typography](../locale-typography/README.md) applies locale-specific
  punctuation and typographic conventions.

## Scope

This skill creates and improves factual prose from supplied or verifiable
material. It does not invent experience, evidence, quotations, testimonials,
citations, outcomes, product behavior, or independent editorial endorsement,
and it does not replace channel strategy, technical verification, or interface
implementation.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
