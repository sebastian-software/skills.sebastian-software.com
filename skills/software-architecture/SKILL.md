---
name: software-architecture
description: >-
  Assess, design, review, and evolve general software architecture with
  explicit system boundaries, responsibilities, data and integration contracts,
  quality attributes, operational concerns, and migration paths. Use when a
  user asks for software or system architecture, architecture options or
  review, service or module boundaries, monolith versus service decisions,
  scalability, reliability, deployability, operational readiness, or a
  cross-cutting technical direction. Apply Twelve-Factor practices where they
  fit a long-running service; do not use for frontend-only architecture,
  codebase audit-only work, implementation plans, or recording an already-made
  decision when a narrower skill applies.
---

# Software Architecture

Turn a product and delivery problem into a system direction that can be built,
operated, and changed safely. Prefer a small, evidenced design over named
patterns, diagrams, or distributed components without a clear driver.

## Choose the Mode

- **Assess:** map an existing system and report verified architectural risks,
  strengths, and unknowns without editing it.
- **Design:** compare viable options and recommend the smallest architecture
  that meets stated quality attributes and constraints.
- **Review:** test a proposal, ADR, or implementation plan against the current
  system, operational reality, and delivery path.
- **Evolve:** define an incremental migration, compatibility period, rollback
  conditions, and evidence gates for an approved direction.

Respect the user's authority. Do not change source, infrastructure, cloud
resources, secrets, deployments, or decision records during an assessment or
design request unless explicitly asked.

## Workflow

1. Discover the product goal, users, critical flows, scale or latency needs,
   compliance and data constraints, team ownership, delivery constraints, and
   the consequences of failure. Read scoped instructions, repository docs,
   manifests, deployment and CI configuration, runbooks, observability setup,
   representative entry points, tests, and accepted ADRs before judging.
2. State the decision scope and evidence limits. Separate facts observed in the
   system from assumptions, forecasts, and open questions. Do not invent load,
   availability, recovery, regulatory, budget, or ownership requirements.
3. Read [Architecture foundations](references/architecture-foundations.md) to
   map responsibilities, boundaries, interfaces, data ownership, quality
   scenarios, and viable options. Keep diagrams proportional: a concise
   component map or sequence may clarify a consequential relationship; it is
   not a deliverable by default.
4. Read [Operability and Twelve-Factor practices](references/operability-and-twelve-factor.md)
   when the system is a service, API, worker, scheduled process, or deployment
   change. Treat the factors as operational design prompts, not a checklist
   that mandates containers, microservices, or a cloud vendor.
5. For each serious option, name the changed boundaries and contracts, the
   operational model, benefits, costs, failure modes, security implications,
   migration path, and how the important claims will be verified. Reject an
   option that solves an imagined scale problem while increasing actual
   coupling, latency, cost, or support burden.
6. Recommend one direction with explicit tradeoffs, deferred choices, and the
   next smallest reversible step. Create or update an ADR only when the choice
   is durable and the user authorizes that artifact; use `decision-records` for
   its repository convention and lifecycle.
7. For an approved evolution, sequence delivery around stable seams: establish
   observability and tests, introduce compatible contracts, migrate one flow or
   consumer at a time, measure, remove the old path, and verify the intended
   quality attributes. Set a removal owner and gate for every temporary bridge.

## Deliverables

Return the smallest artifact that makes the next decision or delivery step
clear. A useful architecture recommendation normally contains:

- context, constraints, observed system shape, and open questions;
- the recommended boundaries, responsibilities, data ownership, and contracts;
- quality scenarios and operational expectations that drove the choice;
- considered alternatives and concrete tradeoffs;
- a migration or delivery sequence, compatibility and rollback conditions; and
- verification signals, including what would cause the direction to be revised.

Keep exact topology, ports, endpoint values, environment values, credentials,
and runbook commands in their owning code, configuration, or runbooks. Never
place secrets or personal data in an architecture artifact.

## Operating Rules

- Start from the simplest deployable shape. A modular monolith is a valid
  default when it meets the product and operational needs; introduce a service
  boundary only for a concrete independent scaling, reliability, security,
  ownership, lifecycle, or technology reason.
- Make ownership singular. One component or service owns each mutable business
  fact; other components receive a contract, projection, or explicit write
  protocol rather than sharing its storage by accident.
- Design contracts for failure: timeouts, retries, idempotency, ordering,
  partial completion, degraded behavior, and compatibility are part of the
  architecture when a flow crosses a process or network boundary.
- Distinguish architecture from implementation preference. A framework, queue,
  database, or pattern is a means, not the decision unless its properties are
  the durable tradeoff.
- Keep security architecture specific to a threat and trust boundary. Escalate
  specialist security, privacy, compliance, capacity, cost, or incident
  decisions when the available evidence cannot establish a safe direction.
- Treat observability, deployment, data recovery, and rollback as design
  concerns for consequential flows, not post-launch chores.

## Routing Boundaries

- Route repository-wide audit findings, prioritization, and executable delivery
  plans to `codebase-improvement`.
- Route durable choices, ADR format, supersession, and drift control to
  `decision-records`.
- Route behavior-preserving language, framework, runtime, or platform ports to
  `port-codebases`.
- Route frontend CSS, React, rendering, component, and interface architecture
  to `effective-web`.
- Route a specific pull request's review, feedback, or CI recovery to
  `pr-review`.

Use this skill when the system-level direction itself needs reasoning; use the
narrower skill once the question becomes its specialized execution work.
