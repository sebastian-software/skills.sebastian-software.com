[← Sebastian Software Skills](../../README.md)

# Port Codebases

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Move a codebase across languages, runtimes, frameworks, platforms, storage
engines, or major APIs without losing the behavior that made it valuable.**

Port Codebases treats a rewrite as a controlled behavior migration rather than
a fresh implementation with familiar names. It helps agents assess feasibility,
define equivalence, build a migration system, scale the work to available
resources, and protect the correctness signal until the new implementation is
ready to ship.

## What It Can Deliver

- a port-versus-alternatives feasibility assessment
- an explicit migration contract and equivalence oracle
- architecture and dependency maps for the source system
- a pilot slice that tests the riskiest assumptions early
- strangler, staged, or big-bang migration plans
- compiler-, fixture-, and differential-test-driven work queues
- resource-aware orchestration for one or many agents
- parity reports, cutover criteria, and decommissioning plans

## Use It When

Use this skill for deliberate behavior-preserving migrations: replacing a
language or runtime, moving between frameworks or platforms, changing a storage
engine, or crossing a major API boundary. It starts by testing whether a port is
actually justified and by identifying the evidence that can prove semantic
equivalence.

## Example Prompts

```text
Assess whether we should port this Node.js service to Rust or harden the current
implementation instead.

Design a staged React-to-Solid migration that preserves public behavior and
keeps both implementations comparable during the transition.

Build a differential-testing harness and use failures as the migration queue for
this Python-to-Go port.

Plan the cutover from this storage engine, including rollback, data validation,
and the conditions for retiring the old path.
```

See [SKILL.md](SKILL.md) for the migration contract, resource profiles,
evidence-driven loops, correctness gates, and shipping workflow.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill port-codebases
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian port-codebases
dalo approve skill sebastian:port-codebases
dalo sync
```

## Related Skills

- [Codebase Improvement](../codebase-improvement/README.md) determines whether
  targeted hardening or simplification is a better investment than a port.
- [Decision Records](../decision-records/README.md) preserves the migration
  choice, rejected alternatives, and cutover constraints.
- [PR Review](../pr-review/README.md) reviews and maintains the resulting pull
  requests during delivery.
- [Smart Dependency Updater](../smart-dependency-updater/README.md) handles
  ordinary package and API upgrades that do not justify a full port.

## Scope

This skill is not for ordinary dependency bumps, local refactors, or product
redesigns disguised as technical migrations. Architectural cleanup should wait
until parity unless the user explicitly accepts the combined risk.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
