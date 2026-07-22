# Routing and Selective Installation

Read this reference only when the task needs a specialist route, spans several
owners, or the preferred owner may not be installed.

## Ownership Map

| Primary need | Authoritative first-party owner | Handoff focus |
| --- | --- | --- |
| Repository investigation, audit, prioritization, or implementation plan | `codebase-improvement` | Evidence, leverage, scope, and executable next move |
| Browser-facing product work | `effective-web` | UX, implementation, accessibility, performance, and browser evidence |
| Non-frontend test design or regression evidence | `software-testing` | Observable risk, suitable test boundary, and discrimination |
| Technical documentation | `tech-docs` | Audience, repository-native surface, examples, and verification |
| Dependency update | `smart-dependency-updater` | Ecosystem context, upstream research, compatibility, and validation |
| Pull-request review or review follow-through | `pr-review` | Impact-led findings, thread state, CI, and merge judgment |
| System boundary or evolutionary architecture | `software-architecture` | Drivers, quality scenarios, tradeoffs, operability, and migration |
| Durable cross-functional decision | `decision-records` | Repository-native ADR lifecycle and drift control |
| Port or compatibility migration | `port-codebases` | Behavior contract, parity evidence, execution profile, and handoff |
| Product, design, legal, locale, or communication concern | Matching existing owner | Domain outcome and evidence without expanding orchestration |

The orchestrator selects and sequences owners. Each owner controls its own
analysis, implementation guidance, evidence standard, and domain boundaries.

## Combine Owners Deliberately

1. Select the minimum owner set that covers the accepted outcome.
2. Order dependencies explicitly. For example, settle architecture before
   documenting it; reproduce a defect before implementing its regression guard;
   adapt a dependency before verifying affected docs.
3. Give each owner only the artifacts and questions it needs. Do not ask every
   owner to review the whole task.
4. Reconcile overlapping outputs at the orchestration layer. Do not let one
   owner silently broaden another owner's scope.

## Selective-Install Contract

When an optional owner is unavailable:

1. Continue to honor repository instructions, user authority, evidence, and
   handoff requirements; these belong to the orchestrator.
2. Disclose the missing owner when its absence materially reduces confidence or
   depth. Do not turn every missing optional skill into noise.
3. Use a narrow, repository-led fallback when the work is low-risk and normal
   engineering reasoning is sufficient. Reuse local commands, patterns, tests,
   and documentation.
4. Ask for installation, a domain decision, or a focused handoff when the
   missing expertise is necessary for a high-risk or specialist claim.
5. Never recreate a condensed specialist handbook, invent unavailable tool
   behavior, or install a skill without authority.

Describe reduced depth in the final handoff, including what evidence still
supports the result and which domain-specific review remains useful.
