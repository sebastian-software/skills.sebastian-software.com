[← Sebastian Software Skills](../../README.md)

# Software Architecture

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Turn an architectural question into a system direction that remains
buildable, operable, and reversible.**

Software Architecture helps agents assess, design, review, and evolve software
systems. It makes boundaries, data and integration contracts, operational
requirements, quality attributes, tradeoffs, and migration paths explicit
without mistaking diagrams or fashionable patterns for a decision.

## What It Can Deliver

- evidence-led system and boundary assessments
- architecture options with concrete quality-attribute tradeoffs
- service, module, data ownership, and integration contract directions
- operational design using relevant Twelve-Factor practices
- incremental migration, compatibility, rollback, and removal plans
- durable decision inputs ready for the repository's ADR convention

## Use It When

Use this skill for system-level questions: whether a boundary should be a
module or service; how data ownership, events, retries, and failure behavior
should work; what operational model makes a service reliable; or how to evolve
an existing architecture without a risky rewrite.

The Twelve-Factor App methodology is an important input for deployable SaaS
services, especially configuration, dependencies, release separation,
stateless processes, observability, and lifecycle handling. It does not by
itself decide the domain model or service topology.

## Example Prompts

```text
Assess whether this modular monolith should extract its report-generation
workflow, using our current failure and scaling evidence.

Design the data ownership and retry-safe integration between billing and order
fulfilment. Explain the tradeoffs and the migration sequence.

Review this architecture proposal for deployability, observability, graceful
shutdown, and production configuration before we implement it.

Use Twelve-Factor principles to identify which parts of this worker deployment
are unsafe, and recommend only the changes justified by the system.
```

See [SKILL.md](SKILL.md) for the workflow, operating rules, and routing
boundaries.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill software-architecture
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian software-architecture
dalo approve skill sebastian:software-architecture
dalo sync
```

## Related Skills

- [Decision Records](../decision-records/README.md) records a durable accepted
  architecture direction and its rationale.
- [Codebase Improvement](../codebase-improvement/README.md) investigates
  observed repository behavior, prioritizes improvements, and turns approved
  work into delivery plans; this skill owns unresolved system direction.
- [Port Codebases](../port-codebases/README.md) manages behavior-preserving
  migrations across languages, runtimes, frameworks, and platforms.
- [Effective Web](../effective-web/README.md) owns frontend and React
  architecture detail.

## Scope

This skill does not replace specialist security, privacy, compliance, capacity,
cost, or incident work. It does not authorize changes to source, infrastructure,
cloud resources, secrets, deployments, or ADRs during an assessment-only
request.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
