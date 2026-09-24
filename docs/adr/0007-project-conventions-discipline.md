# ADR 0007: Add Project Conventions as a Separate Discipline

- Status: Accepted
- Date: 2026-09-24
- Issue: [#253](https://github.com/sebastian-software/skills.sebastian-software.com/issues/253)

## Context

[ADR 0004](0004-effective-disciplines.md) consolidated the collection into six
broad disciplines to avoid overlapping triggers and duplicated guidance.
Those disciplines cover product decisions and repository delivery, but none
owns the independent outcome of discovering and documenting a project's
working standards across people, agents, repository files, and forge rules.
Effective Flow has a project-setup ADR, but a reusable convention method must
work without its configuration keys or installation.

## Decision

Add `effective-project-conventions` as a seventh, independently installable
discipline. It discovers the project's existing language, delivery, validation,
and review standards; distinguishes explicit decisions, observed patterns,
verified enforcement, and open questions; and creates or revises one readable
agreement with a short AGENTS.md pointer when requested.

The skill does not operate the delivery workflow, change forge settings, or
own ADR craft. Those remain with `effective-delivery`, the forge, and
`effective-product` respectively. Its first version uses an existing project
convention document when possible, otherwise `docs/project-conventions.md`.
It does not prescribe a universal machine-readable schema. A downstream
workflow may translate established values into its own configuration.

## Alternatives Considered

- **Put the method in `effective-delivery`.** Rejected because establishing a
  cross-tool working agreement is independently requestable and also applies
  before repository delivery work begins. The new skill's trigger is setting
  project standards; Delivery's trigger remains executing repository work.
- **Make Effective Flow setup the standard.** Rejected because its ADR schema,
  runtime defaults, and lifecycle are particular to that workflow.
- **Create a universal structured configuration file.** Rejected for the first
  version because the relevant formats and enforcing systems are separate;
  a new schema would duplicate their values without making them authoritative.

## Consequences

The public inventory, activation matrix, README, and site now describe seven
skills. The new trigger competes with repository audit and ADR requests, so
positive and negative activation scenarios must be reviewed. The agreement is
readable to humans and can be linked from AGENTS.md; forge rules remain the
authority for what is technically enforced. Revisit the split if real use shows
that convention setup is mostly inseparable from Delivery rather than an
independent task.
