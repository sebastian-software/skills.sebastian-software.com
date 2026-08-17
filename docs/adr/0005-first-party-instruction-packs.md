# ADR 0005: Publish First-Party Instruction Packs Alongside Skills

- Status: Accepted
- Date: 2026-08-17

## Context

The collection has treated `skills/` as both its portable artifact format and
its repository boundary. That kept six disciplines independently installable,
but it also implied that standing cross-task guidance must be authored in a
separate agent-stack repository.

DALO now distinguishes two portable source assets:

- skills are selected capabilities that activate for a matching task;
- instruction packs are explicitly enabled standing conventions rendered into
  managed blocks in agent instruction files.

That distinction removes the need to choose between independent skills and
first-party global guidance. Content ownership and runtime activation can stay
separate: this repository can maintain a provider-neutral convention while
DALO and a downstream agent stack decide whether, where, and with what other
sources it becomes active.

## Decision

1. This repository owns two first-party agent-guidance asset types:
   independently installable discipline skills under `skills/` and optional
   instruction packs under `instructions/`.
2. A skill owns an outcome that a user can request independently and has a
   trigger, workflow, evidence standard, and routing boundary. An instruction
   pack owns a standing convention that should apply across otherwise unrelated
   tasks once explicitly enabled; it has no trigger and is not a seventh
   discipline.
3. Skills remain complete when installed alone. They may not require an
   instruction pack, assume that one is active, or weaken their own authority,
   safety, evidence, and completion rules because a pack repeats them globally.
4. Instruction packs are provider-neutral Markdown files named
   `instructions/<id>.md`. They declare a semantic version and coarse topics in
   the DALO-compatible header, remain concise enough for standing context, and
   have matching review scenarios under `instructions/evals/<id>.json`.
5. Discovering or updating a source never activates a pack. DALO or another
   compatible manager owns explicit enablement, target projection, provenance,
   managed-block updates, drift detection, and removal.
6. A downstream agent stack owns source selection, target selection,
   precedence, overlap decisions, cross-catalog routing, and stack-specific
   instructions. It may enable a pack from this source without copying or
   becoming the canonical author of that pack.
7. Public inventory reports skills, focused references, and instruction packs
   as separate counts. Instruction packs do not inflate the skill count.

## First Pack

`request-and-completion` defines the cross-task contract for interpreting
answer, diagnosis, change, and delivery authority; taking reversible in-scope
action without needless questions; completing every requested deliverable or
naming its exact terminal state; using concurrency only across independent
state; and reporting the outcome concisely.

It deliberately excludes model names, provider commands, automatic external
actions, and a universal ASD-STE100 requirement. Those are respectively runtime
selection, target projection, authority, and artifact-specific language
concerns rather than general completion behavior.

## Alternatives Considered

### Keep all instruction packs in the downstream agent stack

Rejected as a universal rule. Stack-specific routing and precedence still
belong there, but moving canonical first-party behavior there would make its
maintenance and provenance depend on one composition repository.

### Add a seventh skill for agent execution

Rejected. The behavior has no independent user outcome or reliable activation
trigger; it is intended to remain active across product, web, engineering,
delivery, writing, and marketing tasks.

### Copy the rules into all six skills

Rejected. It would duplicate a standing contract, drift across disciplines, and
still leave tasks with no selected first-party skill uncovered.

### Activate instruction packs automatically with a skill or source

Rejected. Standing instructions affect every task in the target agent and can
overlap with user, team, provider, or project policy. Activation must remain an
explicit, inspectable choice.

## Consequences

- The collection is a source of first-party agent guidance, not only a skill
  catalog, while the six-discipline architecture remains unchanged.
- Skills CLI users continue to install skills exactly as before. Instruction
  packs require DALO or another manager that supports explicit instruction-file
  projection.
- The public README, website, DALO guide, authoring guide, and validators must
  describe and count both asset types without presenting a pack as auto-active.
- Instruction changes require both schema validation and behavioral review
  against their matching scenarios.

## Review Triggers

Revisit this decision when an instruction pack develops an independently
requestable outcome, when a skill begins to depend on an active pack, when
target-specific variants can no longer share one canonical body, or when
repeated topic overlaps require a stronger precedence contract than DALO's
explicit activation and advisory overlap reporting provide.
