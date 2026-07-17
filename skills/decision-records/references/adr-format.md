# ADR Format and Lifecycle

Use this reference when creating, reviewing, superseding, or auditing a decision
record. Prefer the repository's existing format when it has one.

## Contents

- [Portable Default](#portable-default)
- [Lifecycle Modes](#lifecycle-modes)
- [Status and History](#status-and-history)
- [Identity and Migration](#identity-and-migration)
- [What Belongs Where](#what-belongs-where)
- [Audit Checklist](#audit-checklist)

## Portable Default

```md
# ADR-0042: Use a dense product register for the operations console

- Status: accepted
- Date: 2026-07-14
- Deciders: Product and frontend team
- Supersedes: ADR-0017
- Superseded by: —

## Context

Describe the concrete problem, affected people and systems, constraints, and
the forces that make a durable decision necessary.

## Decision

State the chosen direction in present tense. Make the scope and boundaries
clear enough that implementation and review can test alignment.

## Decision drivers

- Driver with project-specific evidence
- Constraint or quality attribute that materially shaped the choice

## Considered options

### Chosen option

Explain why it fits.

### Rejected option

Explain the meaningful tradeoff, not a straw man.

## Consequences

- Positive result
- Cost, limitation, migration work, or new responsibility

## Validation and review triggers

Explain how alignment is checked and which future events should reopen the
decision.

## References

- Related issue, code, research, design, runbook, or superseded ADR
```

Only `Context`, `Decision`, and `Consequences` are essential in an established
minimal format. Include drivers, options, validation, and references when they
preserve reasoning that would otherwise be lost. Omit empty ceremonial sections.

## Lifecycle Modes

Use the repository's declared lifecycle. When none exists, use the immutable
default.

### Immutable default

An accepted record is a historical artifact. When its decision changes, create
and link a successor rather than replacing the accepted text. This costs an
extra lookup when decisions evolve, but it keeps the audit trail readable
without relying on Git history.

### Living records

A living record is an explicit opt-in convention in which one file always
contains the current decision. Semantic edits after acceptance are allowed, and
readers do not walk a supersession chain. This reduces lookup and context cost
but weakens the in-document audit trail because earlier states live primarily
in repository history.

Before creating or updating a living record, confirm that the repository
declares:

- the living or mutable lifecycle;
- its filename identity and location;
- its status vocabulary;
- whether the record includes an update date or short change note;
- any narrow records allowed to own configuration values.

When introducing the convention, state this tradeoff and get authorization.
Do not infer living mode merely because one accepted file has been edited in
the past. Once authorized, edit the current file in place, keep its current
decision and consequences unambiguous, and update its date or change note when
the convention defines one.

## Status and History

Use the repository's vocabulary when defined, including localized values such
as `Aktiv`, `Abgelöst`, or `Nicht umgesetzt`. Map each value to its lifecycle
meaning before editing; do not normalize a repository's terms merely to match
this reference. Otherwise:

- `proposed`: under discussion; semantic edits are allowed.
- `accepted`: current project decision; preserve its historical text.
- `rejected`: considered but not adopted.
- `deprecated`: no longer applicable and has no direct successor.
- `superseded`: replaced by another ADR; link the successor.

In the immutable default, only update evidence that the record explicitly
identifies as mutable, such as a dated validation result or review outcome. Do
not use that exception to alter the accepted decision, context, rationale, or
original consequences.

When an immutable decision changes:

1. Create a new proposed ADR referencing the old one.
2. Explain which assumptions or drivers changed.
3. Accept the new ADR through the project's normal decision process.
4. Mark the old ADR superseded and link the new record.
5. Update indexes, code references, and enforcement artifacts.

Do not use Git history as the only supersession record. Readers should discover
the current decision from the ADR corpus itself. This rule does not apply to an
explicit living lifecycle: there, the current file is the discovery mechanism
and Git history intentionally carries earlier versions.

## Identity and Migration

Follow the repository's identity scheme. The portable default uses zero-padded
numbers because they provide stable ordering, but a living convention may use a
stable numberless slug such as `project-setup.md` when one file always represents
the current decision.

Do not bulk-rename existing numbered ADRs merely to introduce numberless living
records. Keep old records readable, document which naming rule applies to new
records, and make indexes or discovery guidance cover both forms. If an existing
decision becomes living, define its stable current filename and link from the
old numbered record or index when that is needed for discovery; do not fabricate
a supersession chain the living convention intentionally avoids.

## What Belongs Where

| Artifact | Owns |
| --- | --- |
| ADR | Durable direction, rationale, tradeoffs, scope, and review triggers |
| Code or configuration | Exact executable behavior and values |
| Design tokens and components | Reusable visual and interaction decisions |
| Editorial or brand guide | Applied vocabulary, examples, and channel guidance |
| Tests and policy checks | Enforced invariants and drift detection |
| Issue or project plan | Delivery tasks, owners, sequencing, and temporary status |
| Runbook | Operational response and step-by-step procedures |

Keep exact values in code or configuration by default. A repository may declare
one narrowly scoped living setup or configuration record as the source of truth
for a cohesive table of non-secret values plus their rationale. Use that
exception only when the values belong together, are not already authoritatively
owned elsewhere, and readers benefit from one current tracked file. Keep
generated runtime state, credentials, personal data, and environment-specific
secrets out of the ADR.

For a design direction, record why the surface is product, brand, or
content-heavy; the intended audience and primary action; selected direction;
density, expression, motion, and depth constraints; rejected directions; and
review triggers. Keep exact colors, spacing values, component props, and motion
durations in the design system unless the value itself is the durable decision.

For a communication direction, record audience relationship, form of address,
voice, tone range, information density, vocabulary boundaries, channel
exceptions, rejected directions, and review triggers. Keep full copy libraries
and campaign drafts in their normal content artifacts.

## Audit Checklist

- Does every accepted record still describe implemented reality?
- Are competing accepted ADRs scoped or superseded explicitly?
- Can a new contributor find the current decision without reading Git history?
- Do status, dates, numbering, and index entries follow repository convention?
- Is the lifecycle explicit, and are living records actually current?
- Can numbered historical records and numberless living records both be found
  during a migration?
- Are consequences and review triggers observable rather than aspirational?
- Are implementation details duplicated in the ADR and already drifting?
- If a living setup record owns values, is that carve-out explicit, cohesive,
  non-secret, and free of a competing source of truth?
- Did a tool create a private dot-folder that should be migrated into the shared
  ADR corpus, design system, editorial guide, or project documentation?
