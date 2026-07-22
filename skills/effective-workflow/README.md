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

## Distillation Contract

The pinned external `effective-flow` from the separately managed DALO
`effective-flow` catalog exposes 17 public workflow tools and 15 internal worker
contracts. This first-party skill keeps the portable coordination ideas without
copying that product's command system, state, setup, or specialist manuals.

| Current capability surface | Decision | First-party treatment |
| --- | --- | --- |
| `investigate` and clarification gates | Keep as orchestration | Preserve read-only diagnosis and resolve only implementation-blocking ambiguity. |
| `apply`, `build`, `fix`, `refactor`, `docs`, and `iterate` | Keep as orchestration | Select a natural-language change route and sequence understand, change, verify, and deliver. |
| `commit` and `pr` completion | Keep as orchestration | Use host-native delivery only within explicit authority. |
| `maintain` dependency mechanics | Delegate to an existing owner | Let `smart-dependency-updater` own research, adaptation, grouping, and validation. |
| Code, UI, Node.js, Rust, test, docs, and review workers | Delegate to existing owners | Route to the matching first-party skill instead of maintaining parallel worker manuals. |
| Standalone `review` and plan review | Delegate to existing owners | Use `pr-review`, `codebase-improvement`, `software-testing`, and other domain owners by scope. |
| `plan`, `open-plans`, and `plan-issue` stores and tracker conventions | Evaluate separately | Reuse repository-native issues and plans; add no mandatory plan directory or labels. |
| Fixed worker registry, automatic worktrees, and completion modes | Evaluate separately | Use host capabilities situationally when available and authorized. |
| `setup`, `cleanup`, `version`, configuration ADR, hidden memory, counters, locks, and migrations | Leave external | Require no special project setup or private operating system. |

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

## Relationship to the Richer Workflow Product

The external `effective-flow` from the separately managed DALO `effective-flow`
catalog remains the feature-rich choice for teams that want its command catalog,
configuration, internal workers, tracker conventions, worktree automation, and
project state. Effective Workflow is the portable first-party choice for teams
that want repository-native orchestration with no setup. The catalog sources use
different skill slots and are not interchangeable implementations.

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
- [Tech Docs](../tech-docs/README.md) owns documentation craft and verification.
- [Smart Dependency Updater](../smart-dependency-updater/README.md) owns
  dependency research, adaptation, grouping, and validation.
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
