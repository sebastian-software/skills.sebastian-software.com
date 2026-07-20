# ADR-0001: Distill Effective Flow and retire the standalone system

- Status: accepted
- Date: 2026-07-20
- Deciders: Sebastian Software skills maintainers
- Supersedes: —
- Superseded by: —

## Context

[Effective Flow](https://github.com/sebastian-software/effective-flow) is a
standalone, private repository that packages a broad software-delivery workflow
for Claude Code and Codex. Its audited `origin/develop` revision
[`1cdd053`](https://github.com/sebastian-software/effective-flow/tree/1cdd0533c13ddcd9b2bf4205e2ddfecf152dc923)
contains a router, 23 public and internal tools, 13 custom workers, 27 shared
instruction fragments, target-project state and configuration, a
source-to-distribution compiler, separate harness outputs, a generated delivery
branch, release archives, and a custom installer.

Several parts contain useful practice, including PR-feedback handling,
technical documentation, testing, diagnosis, planning, and backend/runtime
review. The system also delegates substantial domain judgment to skills already
maintained in this collection. Preserving Effective Flow wholesale would make
its self-created packaging and lifecycle constraints part of this collection
without evidence that users need the umbrella system or identical internal
worker layouts across harnesses.

Issue [#104](https://github.com/sebastian-software/skills.sebastian-software.com/issues/104)
therefore asks for an evidence-led distillation and retirement path rather than
an integration of the existing package.

## Decision

We treat Effective Flow as **source material**, not as a package or architecture
to import.

We will selectively distill only capabilities that:

1. are independently valuable outside Effective Flow;
2. have a clear first-party owner or establish a well-evidenced gap;
3. can be named by their concrete user outcome;
4. preserve repository and caller authority;
5. work as directly installable, inspectable skill source; and
6. can be evaluated and maintained without the standalone runtime.

When an existing skill owns the domain, useful Effective Flow guidance is
merged into that owner. A new skill is considered only through a separate,
narrow issue with its own scope and evidence. Compatibility code may remain as
a temporary adapter for existing consumers or artifacts, but is not a permanent
capability.

### Umbrella orchestration

No umbrella orchestration skill is justified now, and no successor named
`effective-flow` is assumed.

End-to-end implementation, validation, Git operations, worktree use, and
provider calls are normal agent workflow unless evidence identifies a specific
cross-skill orchestration problem that hosts and narrow skills cannot solve.
After the candidate capabilities are distilled and used, we may reconsider a
small orchestration layer. The default outcome remains that no umbrella
successor is needed.

### Naming

`Effective Flow`, `Firmo`, and `sf-plugin` are historical system names. They may
appear in audit, migration, and retirement documentation, but new or extended
public skills use descriptive, portable names based on user-visible outcomes.

Existing owners retain their names, for example `pr-review`,
`codebase-improvement`, and `smart-dependency-updater`. Candidate names such as
`technical-documentation` or `software-testing` are evaluated in their own
issues and are not accepted merely by this ADR.

### Portability target

The target is the collection's existing direct-source contract:

```text
skills/<descriptive-name>/
├── README.md
├── SKILL.md
├── agents/openai.yaml
├── evals/evals.json
├── references/
└── scripts/
```

Only files needed by a concrete skill are present. `SKILL.md` and its focused
references are the portable interface. Skills install from this repository's
normal default branch through DALO, the skills CLI, or another Agent
Skills-compatible manager.

The target does not require:

- generated Claude and Codex variants;
- fixed model, tool, color, reasoning, or sandbox declarations for a worker
  fleet;
- a source-to-distribution compiler;
- a generated delivery branch;
- a standalone release archive or version command;
- a custom global installer;
- a shared Effective Flow configuration; or
- hidden cross-skill runtime state.

Native delegation may be used opportunistically when a host supports it.
Equivalent internal worker topology across hosts is not a product requirement.

### Migration phases

1. **Freeze and inventory.** Use the
   [capability inventory](../audits/effective-flow-capability-inventory.md) as
   the baseline and avoid adding standalone machinery while replacements are
   evaluated.
2. **Distill independently valuable capabilities.** Work one narrow issue at a
   time. Existing follow-ups [#105](https://github.com/sebastian-software/skills.sebastian-software.com/issues/105),
   [#106](https://github.com/sebastian-software/skills.sebastian-software.com/issues/106),
   and [#107](https://github.com/sebastian-software/skills.sebastian-software.com/issues/107)
   remain independently reviewable scopes; this ADR neither bundles nor
   automatically approves their implementations.
3. **Redirect consumers.** Replace actual Effective Flow dependencies with
   accepted existing or new owners. Use bounded adapters for valuable plans,
   findings, issue state, or configuration that must survive the transition.
4. **Deprecate the standalone system.** Stop recommending and releasing the
   umbrella entry point once required outcomes are available directly. Publish
   migration and uninstall guidance before removing compatibility.
5. **Clean up.** After an announced support window and a consumer check, remove
   custom workers, compiler, generated branch, release/installer machinery,
   branded labels and runtime state, and temporary adapters. Archive the
   external repository when it is no longer an active dependency.

Progress is successive: a phase advances only when the relevant replacement is
usable, evaluated, directly installable, and mapped to known consumers. We do
not implement all candidate capabilities in parallel simply to complete the
retirement.

## Decision drivers

- The collection is directly installable from GitHub and intentionally contains
  no installer, generated distribution tree, or vendored external collection.
- A public skill needs independent user value, not just a role inside another
  orchestration system.
- The audited system's platform split is primarily caused by its fixed custom
  workers and command syntax, not by a requirement of portable skills.
- Existing first-party skills already own much of the substantive domain
  guidance.
- Hidden state, custom labels, branch policy, and mutation authority reduce
  portability and make removal costly.
- The source shows documentation drift between its current setup/configuration
  implementation and user guide, demonstrating ongoing coordination cost.
- A staged retirement must preserve valuable user artifacts and avoid a
  disruptive all-at-once replacement.

## Considered options

### Chosen: selective distillation followed by staged retirement

This keeps useful practice, protects existing consumers during migration, and
lets each capability earn its place in the collection.

### Rejected: import Effective Flow wholesale

This would preserve the compiler, dual distributions, custom workers, installer,
configuration, state, and delivery lifecycle before proving that the umbrella
system is valuable. It would also reverse this collection's direct-source and
first-party ownership model.

### Rejected: rewrite Effective Flow as a direct umbrella skill immediately

Removing the compiler would improve installation, but the resulting router
would still bundle unrelated capabilities and assume that an umbrella workflow
is needed. The narrower ownership decisions must come first.

### Rejected: delete the external system immediately

Existing consumers, plans, review reports, tracker artifacts, and setup state
have not yet been inventoried. Immediate deletion would trade architectural
simplicity for avoidable migration risk.

### Deferred: a small orchestration skill after distillation

This remains possible only if observed use after the narrow migrations exposes
a repeatable gap that cannot be solved by host behavior or existing owners.
There is no placeholder name, implementation, or commitment for it.

## Consequences

- Issue #104 produces decision and inventory artifacts, not a new skill.
- #105–#107 remain separately reviewable and may be changed or rejected without
  reopening this decision.
- Existing skills may gain small, evidence-backed rules from Effective Flow
  without adopting its brand or lifecycle.
- Some Effective Flow features will disappear because they are ordinary agent
  behavior, duplicate an owner, or exist only to support the standalone system.
- Temporary migration adapters add short-term work, but their removal condition
  is explicit.
- Existing consumers must be identified before final deprecation; this ADR does
  not claim that there are none.
- The external repository remains read-only source material during collection
  work and is changed only through an explicitly scoped retirement task.

## Validation and review triggers

Alignment is checked by keeping the inventory disposition current through new
ADRs rather than rewriting this accepted record, reviewing each candidate
against the collection's authoring and evaluation standards, and verifying
direct installation from the normal default branch.

Create a superseding ADR if any of these become true:

- measured use shows an umbrella orchestrator provides material value that host
  behavior and narrow skills cannot provide;
- a target harness requires generated artifacts for otherwise portable skill
  behavior;
- a distilled capability needs shared persistent runtime state;
- active consumers cannot migrate through the staged plan;
- standard skill managers cannot deliver an accepted capability safely; or
- ownership boundaries in the capability inventory materially change.

## References

- [Effective Flow capability inventory](../audits/effective-flow-capability-inventory.md)
- [Issue #104](https://github.com/sebastian-software/skills.sebastian-software.com/issues/104)
- [Effective Flow source](https://github.com/sebastian-software/effective-flow)
- [Skill authoring guide](../authoring-skills.md)
- [DALO setup](../dalo.md)
