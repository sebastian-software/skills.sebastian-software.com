[← Sebastian Software Skills](../../README.md)

# Metro English

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Make professional English sound like a smart teammate wrote it quickly but
carefully: direct, natural, warm enough, and free of corporate or AI varnish.**

Metro English rewrites German or stiff English into relaxed US metropolitan
team language for Slack, GitHub, Linear, pull requests, async updates, and
internal communication. The target is polished casual with a little startup
energy, not slang and not manufactured friendliness.

## What It Changes

- removes ceremony, filler, inflated transitions, and AI-shaped phrasing
- uses direct verbs, natural contractions, and varied sentence rhythm
- makes requests and disagreement clear without becoming cold
- preserves useful uncertainty and avoids fake confidence
- adapts tone to Slack, issue comments, PR reviews, async updates, and
  docs-adjacent notes
- translates German team messages by intent rather than word-for-word syntax

## Example Prompts

```text
Rewrite this German update as natural English for our US Slack channel.

Make this pull-request comment sound less formal and more human without
weakening the technical concern.

Remove the AI tone from this Linear comment and keep it concise.

Turn this blunt rejection into a clear teammate response that explains the real
blocker and the next useful step.
```

The skill includes before-and-after patterns for formal reviews, stiff Slack
updates, AI-ish issue comments, German team notes, and messages that became too
blunt. See [SKILL.md](SKILL.md) for the voice target, channel presets, rewrite
rules, and output format.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill metro-english
```

Or select it with DALO:

```sh
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian metro-english
dalo approve skill sebastian:metro-english
dalo sync
```

## Related Skills

- [PR Review](../pr-review/README.md) provides the complete technical and
  operational workflow around pull-request feedback.
- [LinkedIn Posts](../linkedin-posts/README.md) handles public professional posts
  with audience, format, and content goals.
- [Consultant Profile](../consultant-profile/README.md) creates the underlying
  profile narrative and claims before channel-specific rewriting.
- [Locale Typography](../locale-typography/README.md) applies punctuation,
  spacing, quotation, number, date, and currency conventions after rewriting.

## Scope

Metro English changes voice, rhythm, and clarity. It does not change facts,
technical meaning, commitments, established terminology, or durable house-style
decisions without explicit authority.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).
