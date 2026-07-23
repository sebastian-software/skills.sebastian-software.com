[← Sebastian Software Skills](../../README.md)

# Effective Workflow

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Take software work from an unclear request to a verified, review-ready handoff.**

Effective Workflow is the collection's lightweight software-delivery
orchestrator. It connects understanding, change, verification, and delivery
while existing first-party skills retain authority over frontend work, tests,
documentation, dependencies, architecture, ports, decisions, and PR review.

## What It Can Deliver

- a clear route from an ambiguous request to the smallest suitable workflow
- a strict boundary between read-only diagnosis, authorized implementation,
  and external delivery actions
- repository-native plans, tests, documentation, Git conventions, and handoffs
- before-and-after evidence for refactors and regression evidence for bug fixes
- selective coordination of only the specialist skills the current task needs
- capability- and cost-aware routing across available models and agents instead
  of assuming one model should own every stage
- compact delegation receipts that preserve exact evidence without returning a
  transcript of every search or tool call
- bounded delegation topologies that never silently weaken read-only access,
  worktree isolation, or tool limits
- an honest completion report covering evidence, skipped checks, delivery state,
  and remaining risk

## Use It When

Use this skill for end-to-end repository work: fixing a bug through regression
proof, implementing a feature from an unclear brief, coordinating a dependency
update with code and docs, carrying a refactor through baseline comparison, or
leaving a mixed change ready for review and authorized delivery.

Use a specialist skill directly when the work is already narrow and no broader
sequencing is needed.

## Example Prompts

```text
Take this bug from diagnosis through a minimal fix, regression evidence, and a
review-ready handoff. Do not push or open a PR.

Implement issue #42 using the repository's existing plan and conventions. Run
the relevant checks, review the final diff, then commit and open a PR.

Refactor this parser without changing behavior. Establish a focused baseline,
compare it after the change, and report any checks you could not run.

Update this dependency and any affected code or docs. Use only the specialist
skills that are installed and disclose any reduced-depth fallback.
```

See [SKILL.md](SKILL.md) for the four-stage workflow and its authority model.

## Design Contract

| Concern | First-party treatment |
| --- | --- |
| Diagnosis and clarification | Preserve read-only diagnosis and resolve only choices that block a safe next step. |
| Implementation intent | Use natural-language routes and sequence understand, change, verify, and deliver only as far as the task needs. |
| Specialist judgment | Delegate frontend, testing, validation, documentation, dependency, review, architecture, decision, and port depth to their owners. Use a disclosed repository-led fallback where no language specialist exists. |
| Delegation | Match model capability to judgment and execution risk; give bounded owners explicit authority, deliberate execution topology, and compact result contracts without weakening isolation or evidence to save cost. |
| Mixed repositories | Route each affected domain independently; distinguish product code, tooling, documentation, generated output, and vendored content before delegating. |
| Plans and progress | Reuse repository-native issues, plans, branches, commits, CI, and pull requests instead of creating a parallel workflow store. |
| Delivery | Use host-native Git and forge capabilities only within explicit authority. |
| Runtime footprint | Add no fixed command vocabulary, worker registry, setup wizard, private state, counters, locks, migrations, or automatic tracker mutations. |

## Size and Duplication Budget

- `SKILL.md`: fewer than 200 lines
- runtime references: at most two, each fewer than 120 lines and linked directly
  from `SKILL.md`
- specialist routes: selection rule plus handoff, never a second implementation
  or review handbook
- project footprint: no scripts, setup wizard, config, hidden state, generated
  distribution, fixed roles, or skill-specific tracker schema

Crossing a budget requires a design review that first tries delegation or
removal. The runtime references are intentionally split between
[routing and selective installation](references/routing-and-fallbacks.md) and
[evidence and delivery](references/evidence-and-delivery.md), so an agent loads
only the current decision surface.

## Selective Installation

Effective Workflow remains useful when optional first-party owners are absent.
It follows the repository, discloses a material loss of specialist depth, and
uses a narrow fallback for low-risk work. It asks for installation or a focused
handoff when a high-risk claim needs unavailable expertise. It never embeds a
replacement handbook or installs another skill without authority.

The complete fallback contract is in
[routing and selective installation](references/routing-and-fallbacks.md).

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-workflow
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian effective-workflow
dalo approve skill sebastian:effective-workflow
dalo sync
```

## Related Skills

- [Codebase Improvement](../codebase-improvement/README.md) owns repository
  investigation with a read-only diagnosis boundary, audit quality,
  prioritization, and executable plans.
- [Effective Web](../effective-web/README.md) owns browser-facing design,
  implementation, accessibility, performance, and frontend verification.
- [Software Testing](../software-testing/README.md) owns focused non-frontend
  test design and regression evidence.
- [Software Validation](../software-validation/README.md) discovers and executes
  established repository checks and reports explicit evidence gaps.
- [Tech Docs](../tech-docs/README.md) owns documentation craft and verification.
- [Smart Dependency Updater](../smart-dependency-updater/README.md) owns
  dependency selection, introduction, update research, adaptation, grouping,
  and validation.
- [PR Review](../pr-review/README.md) owns impact-led PR review, feedback
  resolution, CI recovery, and merge judgment.
- [Software Architecture](../software-architecture/README.md), [Decision
  Records](../decision-records/README.md), and [Port
  Codebases](../port-codebases/README.md) own their specialist decisions and
  evidence while this skill sequences the wider task.

## Scope

This skill owns coordination, authority boundaries, evidence selection, and the
completion handoff. It does not own specialist technical judgment, require a
fixed phase for every task, create internal project state, or mutate Git,
pull-request, tracker, deployment, or release state without user authority and
host capability.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
