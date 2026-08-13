[← Sebastian Software Skills](../../README.md)

# Effective Delivery

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Move an existing repository — and the team around it — forward safely.**

Effective Delivery is one of six disciplines in this collection. It owns the
lifecycle work around code that already exists: coordinating a vague request
into a verified handoff, auditing and diagnosing, porting across languages and
runtimes, reviewing and maintaining pull requests, researching and grouping
dependency updates, running the repository's own checks and reporting the
evidence honestly, writing documentation that matches the implementation,
operating a delegated live issue queue, and leading the people doing all of it.

It keeps authority levels distinct: analysis is not implementation,
implementation is not delivery, and an available tool is not permission to use
it.

It replaces the former `effective-workflow`, `codebase-improvement`,
`port-codebases`, `pr-review`, `smart-dependency-updater`, `software-validation`,
`tech-docs`, `issue-autopilot`, and `engineering-management` skills. See
[MIGRATION.md](../../MIGRATION.md) for the full mapping.

## Ten Routes

| Route | Owns |
| --- | --- |
| Workflow Orchestration | sequencing, authority, smallest sufficient change, handoff |
| Codebase Audit and Plans | audits, root-cause diagnosis, prioritization, plans |
| Behavior-Preserving Ports | migration contracts, parity evidence, shard execution |
| PR Review and Upkeep | review ladder, merge judgment, feedback, CI recovery |
| Review Provider Access | adapters, GitHub CLI recipes, caller-owned handoff |
| Issue Queue Autopilot | delegated queue discovery, ranking, isolated implementation, PR reconciliation, monitoring |
| Dependency Updates | portfolio grouping, changelog research, adoption, PRs |
| Repository Validation | command discovery, safe execution, honest result states |
| Technical Documentation | READMEs, references, migrations, rustdoc, controlled language |
| Engineering Leadership | responsibilities, delegation, meetings, cognitive load |

## What It Can Deliver

- read-only root-cause reports that separate symptom, reproduction, and cause
- repository audits with verified, ranked, evidence-backed findings
- executable implementation plans and backlog reconciliation
- migration contracts, equivalence oracles, and port execution profiles
- pull-request reviews that name the blocking risk and the optional suggestion
- dependency portfolios grouped by one reviewer question each
- evidence-ranked issue queues, isolated implementations, and reversible
  readiness state without merging PRs
- validation reports with explicit `PASSED`, `FAILED`, `SKIPPED`, and `TIMEOUT`
  states per category
- READMEs, task guides, API and CLI references, and migration notes derived from
  the implementation
- ASD-STE100 and controlled-technical-German documentation work
- management interventions that are reversible, owned, and reviewed

## Use It When

Use this discipline when the work operates on something that already exists: a
repository, a change, a pull request, a dependency graph, a documentation set, a
check surface, or a team's responsibilities.

## Example Prompts

```text
Why does this endpoint return stale data after a deploy? Read-only — trace it
and tell me the best-supported cause, not a fix.

Audit this repository and rank the five highest-leverage improvements with the
evidence for each.

Catch up on my review queue: decide what is merge-ready and leave the reviews.

Research our outdated dependencies, group the compatible ones, and prepare
focused upgrade PRs with reviewer-grade bodies.

Work through my unassigned issue queue one item at a time, keep queue-owned PRs
review-ready, and do not merge them.

Validate this branch. Tell me exactly which checks ran, which were skipped, and
what that leaves unproven.

Write the migration notes for this breaking API change from the actual
implementation and tests, not from the changelog.

Two teams both think they own deploys and nothing ships on Fridays. Diagnose the
system before proposing a reorg.
```

See [SKILL.md](SKILL.md) for the workflow, route table, operating rules, and
routing boundaries.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-delivery
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian effective-delivery
dalo approve skill sebastian:effective-delivery
dalo sync
```

## Related Disciplines

- [Effective Engineering](../effective-engineering/README.md) owns architecture,
  data models, TypeScript and Rust depth, test design, and benchmark
  methodology. This discipline runs the checks and reviews the PRs; that one
  designs the code and the test.
- [Effective Web](../effective-web/README.md) owns frontend implementation,
  frontend-only diagnosis, browser test design, and web compliance.
- [Effective Product](../effective-product/README.md) owns Architecture Decision
  Records and the product decisions a delivery question depends on.
- [Effective Writing](../effective-writing/README.md) owns natural team English,
  locale typography, and long-form editorial prose. Controlled-language
  documentation stays here.

## Scope

This discipline operates on existing repositories and teams. It does not design
new system architecture, data models, or tests; it does not implement browser
experiences; and it does not invent repository workflow, delivery authority, or
project policy that the host repository and the user have not established. It
never installs or upgrades tooling silently, never treats a green command as
proof of untested behavior, and stops for qualified People/HR, employment-law,
occupational-health, security, or crisis support when those concerns determine
the action.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
