[← Sebastian Software Skills](../../README.md)

# Codebase Improvement

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Turn repository uncertainty into a supported explanation, a small set of
well-supported improvements, and one executable next move.**

Codebase Improvement helps agents audit, prioritize, plan, reconcile, simplify,
diagnose, and improve software repositories. It favors repository evidence and
leverage over generic best-practice inventories, producing fewer findings that
a team can actually act on.

## Operating Modes

- **Audit:** inspect read-only and return vetted findings.
- **Focused audit:** investigate one risk category, package, flow, or branch
  delta.
- **Investigation:** explain a defect or surprising behavior with competing
  hypotheses and a strict no-implementation boundary.
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

Investigate why token refresh intermittently returns 401. Compare plausible
causes, report what the evidence rules out, and stop before implementing.
```

See [SKILL.md](SKILL.md) for the evidence model, artifact boundaries, safety
rules, and detailed workflow.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill codebase-improvement
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian codebase-improvement
dalo approve skill sebastian:codebase-improvement
dalo sync
```

## Related Skills

- [Effective Workflow](../effective-workflow/README.md) coordinates an unclear
  software request through implementation, verification, and handoff; this
  skill owns its read-only repository diagnosis, prioritization, and planning
  depth.
- [PR Review](../pr-review/README.md) handles review and maintenance of specific
  GitHub pull requests, including PR-scoped diagnosis.
- [Smart Dependency Updater](../smart-dependency-updater/README.md) handles a
  dependency-update portfolio end to end.
- [Port Codebases](../port-codebases/README.md) manages deliberate migrations
  across languages, runtimes, frameworks, platforms, or major APIs.
- [Tech Docs](../tech-docs/README.md) handles selected technical-documentation
  craft and verification after an audit or diagnosis identifies a mismatch.
- [Decision Records](../decision-records/README.md) preserves durable choices;
  audit findings and delivery plans remain separate artifacts.
- [Effective Web](../effective-web/README.md) handles frontend-specific design,
  accessibility, performance, browser verification, and frontend-only diagnosis.
- [Software Testing](../software-testing/README.md) owns focused non-frontend
  test design, implementation, and test-suite diagnosis.
- [Software Validation](../software-validation/README.md) discovers and runs
  established repository checks after this skill selects an improvement or
  needs a current health baseline.
- [Software Architecture](../software-architecture/README.md) owns unresolved
  system direction exposed by an investigation.

## Scope

This is not a license to edit a repository during an audit-only request, publish
issues without authority, implement during diagnosis-only work, or produce a
long speculative backlog. PR-only review, focused test diagnosis,
frontend-only diagnosis, architecture-only decisions, and
dependency-update-only work should use the narrower skills above.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
