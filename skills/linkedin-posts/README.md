[← Sebastian Software Skills](../../README.md)

# LinkedIn Posts

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Find worthwhile LinkedIn ideas and turn them into specific, readable posts
for a defined audience, voice, and goal.**

LinkedIn Posts helps agents brainstorm, plan, and write professional content
without defaulting to generic hooks, recycled engagement formulas, or an
emoji-heavy imitation of “LinkedIn voice.” Its idea library contains 300 prompts
across 11 categories, loaded selectively for the current topic.

## What It Can Deliver

- focused post ideas for a topic, audience, or goal
- content pillars and balanced content mixes
- practical editorial calendars
- text posts, document/carousel concepts, polls, videos, and infographics
- hook and structure alternatives
- a finished post plus optional engagement and visual suggestions
- adaptations to an established personal or company voice

## Idea Coverage

The bundled idea library spans company and project updates, education,
engagement, industry insights, careers, lifestyle, networking, personal
stories, professional development, recognition, and tools. Prompts are treated
as discovery cues, not as copy to reproduce.

## Example Prompts

```text
Give me ten LinkedIn post ideas about lessons from modernizing a legacy
frontend. Avoid generic hot takes.

Turn these rough notes into a concise post for engineering leaders in my normal
voice.

Create a six-week content calendar that balances expertise, project evidence,
professional perspective, and conversation starters.

Rewrite this draft with a stronger opening and clearer rhythm without adding
fake vulnerability, invented results, or engagement bait.
```

See [SKILL.md](SKILL.md) for the idea routes, discovery questions, writing
principles, formats, cadence, and output structure.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill linkedin-posts
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian linkedin-posts
dalo approve skill sebastian:linkedin-posts
dalo sync
```

## Related Skills

- [LinkedIn Social Selling](../linkedin-social-selling/README.md) establishes
  the target buyer, offer, profile, network, funnel, and commercial context;
  LinkedIn Posts consumes that brief without duplicating the strategy.
- [Consultant Profile](../consultant-profile/README.md) supplies credible
  positioning, project evidence, and professional narrative.
- [Metro English](../metro-english/README.md) adapts drafts to a more natural,
  relaxed US professional voice where appropriate.
- [Decision Records](../decision-records/README.md) preserves durable audience,
  voice, terminology, claim, and channel decisions.

## Scope

The skill writes LinkedIn content; it does not invent personal experiences,
customer evidence, outcomes, opinions, or a commercial strategy that has not
been established. End-to-end acquisition work belongs in LinkedIn Social
Selling.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
