[← Sebastian Software Skills](../../README.md)

# Social Content

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Turn real ideas, evidence, and authored perspective into credible,
platform-native social content without posting the same generic copy
everywhere.**

Social Content helps agents write and adapt posts for X or Twitter, Threads,
Bluesky, Instagram, Mastodon, and multi-platform campaigns. It preserves the
speaker's strongest wording, separates authored voice from quoted material,
checks available content history for repeated angles, and treats platform
mechanics as volatile rather than folklore.

## What It Can Deliver

- original posts, replies, quote posts, threads, captions, and resource shares
- product, project, educational, announcement, and event content
- evidence-backed social content series and cross-platform calendars
- three materially different finished directions when the angle is open
- platform-native adaptations of one verified source or idea
- social excerpts and discussion prompts from articles, talks, and case studies
- voice matching from authorized authored examples
- content-history checks for repeated hooks, claims, stories, proof, and endings
- visual, carousel, and short-video concepts with accessibility notes

## Example Prompts

```text
Turn these project notes into three different X posts. Keep my strongest line
and do not invent results.

Adapt this article into platform-native versions for X, Threads, Bluesky, and
Instagram. Preserve the same evidence, but do not just shorten one master post.

Study these authorized examples of my posts and replies, then rewrite this draft
in my voice without copying signature phrases or manufacturing quirks.

Check our recent published content for this hook, claim, anecdote, and proof
point before proposing a fresh angle.

Write a concise reply that adds one useful implementation constraint without
turning into a sales pitch.
```

See [SKILL.md](SKILL.md) for the workflow, evidence rules, format selection,
platform adaptation, and routing boundaries.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill create-social-content
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian create-social-content
dalo approve skill sebastian:create-social-content
dalo sync
```

## Related Skills

- [LinkedIn Posts](../linkedin-posts/README.md) owns LinkedIn-only ideas,
  calendars, formats, documents, and post writing; Social Content coordinates a
  shared brief when LinkedIn is one part of a multi-platform deliverable.
- [LinkedIn Social Selling](../linkedin-social-selling/README.md) establishes
  LinkedIn positioning, buyer context, relationships, offers, funnels, and
  pipeline; Social Content consumes its approved content brief.
- [Nonfiction Writing](../nonfiction-writing/README.md) creates the standalone
  article, newsletter, case study, or other long-form source before it is
  adapted socially.
- [Product Marketing](../product-marketing/README.md) establishes positioning,
  messages, proof, launch choices, and claim boundaries before channel
  expression.
- [Consultant Profile](../consultant-profile/README.md) supplies professional
  positioning, project evidence, and permission-sensitive client context.
- [Decision Records](../decision-records/README.md) preserves durable choices
  about audience relationship, voice, tone, terminology, claims, and channel
  exceptions.
- [Locale Typography](../locale-typography/README.md) applies the final
  locale-specific punctuation and visible-prose conventions.
- [Web Legal Compliance](../web-legal-compliance/README.md) researches current
  advertising, endorsement, testimonial, privacy, and disclosure constraints
  when they materially affect publication.

## Scope

The skill creates and reviews social content. It does not invent personal
experience, customer evidence, quotations, metrics, product behavior, or
results. It does not own long-form writing, product positioning, LinkedIn
acquisition strategy, or account actions such as publishing, scheduling,
liking, following, or direct messaging.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
