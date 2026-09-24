---
name: effective-project-conventions
description: >-
  Discover, decide, create, and update a repository's shared working conventions.
  Use when asked to establish project standards for language, branches, pull
  requests, merge behavior, checks, reviewers, or review bots, or to make those
  standards visible to coding agents through AGENTS.md. Not for carrying out a
  delivery, changing forge protections, or configuring one agent product.
---

# Effective Project Conventions

Establish a short, human-readable working agreement that people and coding
agents can use without this skill or another workflow installed. Inspect the
project before proposing rules. Distinguish what is enforced, what the project
has decided, what the repository merely suggests, and what remains unknown.

## Route by Intent

| User intent | Read |
| --- | --- |
| Discover, propose, create, update, or audit shared project standards | [Project Conventions](references/route-project-conventions.md) |

The route covers discovery, evidence, conflicts, the output contract, and safe
updates. For a narrow question, read only the relevant section.

## Workflow

1. Determine whether the user wants a read-only assessment, a proposal, or
   files created or updated. An instruction to set up the project authorizes
   writing the agreement and its short AGENTS.md pointer; a request to propose
   or assess alone does not.
2. Discover existing project guidance and applicable repository or forge rules.
   Read only sources needed for the requested surfaces. Inspect forge settings
   only when access is available and the question needs them.
3. Show the proposed values with their sources and state: enforced, decided,
   proposed, or open. Resolve genuine conflicts with the user or keep the
   affected value open. Do not promote a
   pattern in code, a default branch, a CI job, or a bot comment into binding
   policy without corroboration.
4. Use an existing project convention document when one exists. Otherwise use
   a short Markdown agreement under `docs/project-conventions.md`. Keep values,
   evidence, and a little rationale together. Add or propose a brief binding
   pointer in AGENTS.md; do not copy the value table into it.
5. When writing is authorized, preserve unrelated content, re-read each target
   immediately before editing, check containment and symlinks, and stop if a
   source or target changed in a way that affects the proposal. Report created
   or revised paths and unresolved decisions.

## Routing Boundaries

- `effective-delivery` executes repository changes, PRs, checks, reviews, and
  merges. This skill records their project-level rules; it never changes forge
  protections, triggers a bot, or merges a change on the strength of a policy.
- `effective-product` owns the craft and lifecycle of Architecture Decision
  Records. This skill can use a project-declared living setup record, but it
  does not impose an ADR format or alter an accepted decision silently.
- Product UI, CLI, and error-message language follows the product's localization
  policy, not the working language for code comments or agent chat.
- Do not invent organizational authority, required checks, reviewer identities,
  credentials, or secrets. A missing source or inaccessible forge is an unknown
  state to report, not permission to guess.
