[← Sebastian Software Skills](../../README.md)

# Effective Writing

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Prose that people trust and act on — at article length, at Slack length, and
down to the punctuation a locale expects.**

Effective Writing is one of six disciplines in this collection. It turns
supplied ideas and evidence into factual prose a particular reader can
understand, believe, and use: long-form articles and case studies, evidence-led
audits of formulaic AI-sounding text, relaxed US team English for internal
messages, and locale-correct typography for thirteen European languages. Claims,
quotations, examples, outcomes, and product behavior stay tied to real source
material.

It replaces the former `nonfiction-writing`, `metro-english`, and
`locale-typography` skills. See [MIGRATION.md](../../MIGRATION.md) for the full
mapping.

## Seven Routes

| Route | Owns |
| --- | --- |
| Structure and Story | thesis, scope, leads, sequence, transitions, endings |
| Prose and Revision | clarity, syntax, verbs, rhythm, voice, line editing |
| Human Voice Editing | generated-sounding prose, evidence-based pattern audits |
| Persuasive Nonfiction | thought leadership, content marketing, editorial case studies |
| Technical Subject Matter | engineering blog posts, technical articles, project pages |
| Metro English | Slack, issue, PR, and async team messages; German-to-English |
| Locale Typography | quotation marks, spacing, dashes, numbers, dates, hyphenation |

## What It Can Deliver

- focused theses, outlines, leads, transitions, and endings
- Minto pyramids, MECE logic audits, and actionable restructuring plans
- complete articles, essays, newsletters, and explanatory pieces
- technical articles and project pages with stable terminology and natural prose
- thought leadership and content marketing with credible persuasive structure
- editorial case studies and professional narratives
- structural, evidentiary, voice, and line-level revisions
- minimal edits that remove formulaic patterns without flattening the author
- evidence-based pattern audits without AI-authorship scores or guesses
- Slack messages, issue and PR comments, and async updates that sound human
- German source text turned into natural US team English
- locale-correct typography in Markdown, HTML, JSX, templates, UI copy, and print

## Use It When

Use this discipline when notes must become a coherent factual piece, a draft
needs stronger structure or cleaner prose, an author's real voice should survive
editing, an internal message reads like a press release, or visible text has to
match what a German, French, Polish, or Nordic reader expects to see.

## Example Prompts

```text
Turn these workshop notes into a 1,500-word article for product leaders. Make a
clear argument, preserve my direct voice, and flag any proof we still need.

Revise this essay for structure, rhythm, and clarity without flattening its
personal tone or changing the facts.

Minto this proposal before rewriting it. Extract the reader's question and
governing point, test every grouping for summary, logical kind, order, and MECE,
then give me an executable restructuring plan without inventing evidence.

Audit this draft for formulaic or AI-sounding patterns. Quote the evidence and
suggest the smallest useful fix, but do not rewrite it or guess who wrote it.

Convert these supplied project facts and measured outcomes into a case study.
Do not invent customer quotes or imply results beyond the measurement window.

Turn these verified architecture notes into an article for engineering leaders.
Keep the technical terms and constraints exact without making it read like a
manual.

Rewrite this German status note as a Slack update that sounds like a teammate
wrote it, not a press release.

Our German interface strings use straight quotes and English dash spacing.
Correct the typography to match de-DE conventions without touching the keys.
```

See [SKILL.md](SKILL.md) for the workflow, evidence rules, route table, and
routing boundaries.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-writing
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian effective-writing
dalo approve skill sebastian:effective-writing
dalo sync
```

## Related Disciplines

- [Effective Marketing](../effective-marketing/README.md) owns commercial-choice
  copy — homepages, landing, product, pricing, campaign, and sales pages, social
  and LinkedIn content, and professional profile positioning. Positioning and
  supported claims are settled there before market-adjacent prose is drafted
  here.
- [Effective Delivery](../effective-delivery/README.md) owns durable technical
  documentation and controlled-language standards, including ASD-STE100. This
  discipline keeps editorial structure and public voice.
- [Effective Web](../effective-web/README.md) owns interface copy, page
  hierarchy, accessibility, localization UX, and browser implementation.
- [Effective Product](../effective-product/README.md) records a durable
  communication or voice direction as an Architecture Decision Record.

## Scope

This discipline creates and improves factual prose from supplied or verifiable
material. It does not invent experience, evidence, quotations, testimonials,
citations, outcomes, product behavior, or independent editorial endorsement, and
a pattern audit does not establish whether AI wrote a text. It corrects
typography rather than spelling, grammar, translation, or tone, and it does not
replace commercial copywriting, channel strategy, technical verification,
controlled-language documentation, or interface implementation.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
