# ADR Format and Lifecycle

Use this reference when creating, reviewing, superseding, or auditing a decision
record. Prefer the repository's existing format when it has one.

## Contents

- [Portable Default](#portable-default)
- [Status and History](#status-and-history)
- [What Belongs Where](#what-belongs-where)
- [Audit Checklist](#audit-checklist)

## Portable Default

```md
# ADR-0042: Use a dense product register for the operations console

- Status: accepted
- Date: 2026-07-14
- Deciders: Product and frontend team
- Supersedes: ADR-0017

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

## Status and History

Use the repository's vocabulary when defined. Otherwise:

- `proposed`: under discussion; semantic edits are allowed.
- `accepted`: current project decision; preserve its historical text.
- `rejected`: considered but not adopted.
- `deprecated`: no longer applicable and has no direct successor.
- `superseded`: replaced by another ADR; link the successor.

When a decision changes:

1. Create a new proposed ADR referencing the old one.
2. Explain which assumptions or drivers changed.
3. Accept the new ADR through the project's normal decision process.
4. Mark the old ADR superseded and link the new record.
5. Update indexes, code references, and enforcement artifacts.

Do not use Git history as the only supersession record. Readers should discover
the current decision from the ADR corpus itself.

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
- Are consequences and review triggers observable rather than aspirational?
- Are implementation details duplicated in the ADR and already drifting?
- Did a tool create a private dot-folder that should be migrated into the shared
  ADR corpus, design system, editorial guide, or project documentation?
