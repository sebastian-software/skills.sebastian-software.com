[← Sebastian Software Skills](../../README.md)

# Effective Project Conventions

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Make a repository's working standards clear to people and coding agents.**

This skill discovers how a project actually works, distinguishes enforced
rules from observed habits, and creates or updates a short, readable agreement.
It covers working language, branches, pull requests, merges, checks, and
reviewers. It can propose or add a concise AGENTS.md instruction that points to
the agreement. It works without Effective Flow or another workflow installed.

## What It Can Deliver

- an evidence-backed inventory of existing project standards and conflicts
- a compact Markdown agreement with sources, rationale, and open decisions
- a binding AGENTS.md pointer that avoids a second copy of configuration values
- a report of which delivery and review rules are actually enforced by the
  forge, when that information is accessible

## Example Prompts

```text
Set up project conventions from this repository. Check the existing guidance,
CI, and GitHub rules, create a readable agreement, and point AGENTS.md to it.

Our team writes plans in German and code comments in English. Propose the
smallest update to our project standards; do not edit files yet.

Audit our documented PR, merge, and review-bot rules against what GitHub
currently enforces. Show conflicts and unknowns without changing settings.
```

See [SKILL.md](SKILL.md) for the workflow and boundaries.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-project-conventions
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian effective-project-conventions
dalo approve skill sebastian:effective-project-conventions
dalo sync
```

## Related Disciplines

- [Effective Delivery](../effective-delivery/README.md) performs repository
  changes and PR, validation, review, and merge work under these conventions.
- [Effective Product](../effective-product/README.md) owns durable ADR craft
  when a project decision needs its own record.

## Scope

The skill records project working agreements. It does not install agent tools,
change forge protections or CI, trigger review bots, or grant permission to
publish or merge a particular change. It marks missing evidence as unknown and
never writes secrets into a shared document.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
