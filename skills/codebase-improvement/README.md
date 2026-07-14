[← Sebastian Software Skills](../../README.md)

# Codebase Improvement

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Turn repository uncertainty into a small set of well-supported improvements
and an executable next move.**

Codebase Improvement helps agents audit, prioritize, plan, reconcile, simplify,
and improve software repositories. It favors repository evidence and leverage
over generic best-practice inventories, producing fewer findings that a team
can actually act on.

## Operating Modes

- **Audit:** inspect read-only and return vetted findings.
- **Focused audit:** investigate one risk category, package, flow, or branch
  delta.
- **Plan:** make a requested improvement executable.
- **Review plan:** test an existing plan against current code and conventions.
- **Reconcile:** classify recorded work as done, stale, blocked, superseded, or
  still valuable.
- **Improve:** implement the agreed scope and verify it proportionately.

## What It Can Find

The workflow can examine correctness, security, performance, testing,
architecture, dependencies, documentation, developer experience, unnecessary
complexity, and stale improvement work. Findings include concrete evidence,
impact, confidence, scope, and a practical correction instead of vague advice.

## Example Prompts

```text
Audit this repository and rank the five highest-leverage improvements with
evidence from the current code.

Review this implementation plan against the repository and repair anything
stale, underspecified, or inconsistent with local conventions.

Find accidental complexity in this package and simplify only what the evidence
justifies.

Reconcile these old improvement issues: which are complete, obsolete,
duplicated, blocked, or still worth doing?
```

See [SKILL.md](SKILL.md) for the evidence model, artifact boundaries, safety
rules, and detailed workflow.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill codebase-improvement
```

Or select it with DALO:

```sh
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian codebase-improvement
dalo approve skill sebastian:codebase-improvement
dalo sync
```

## Related Skills

- [PR Review](../pr-review/README.md) handles review and maintenance of specific
  GitHub pull requests.
- [Smart Dependency Updater](../smart-dependency-updater/README.md) handles a
  dependency-update portfolio end to end.
- [Port Codebases](../port-codebases/README.md) manages deliberate migrations
  across languages, runtimes, frameworks, platforms, or major APIs.
- [Decision Records](../decision-records/README.md) preserves durable choices;
  audit findings and delivery plans remain separate artifacts.

## Scope

This is not a license to edit a repository during an audit-only request, publish
issues without authority, or produce a long speculative backlog. PR-only review
and dependency-update-only work should use the narrower skills above.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).
