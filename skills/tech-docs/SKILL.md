---
name: tech-docs
description: >-
  Design, write, update, and verify technical documentation for software users
  and contributors, including READMEs, setup and task guides, API and CLI
  references, migration notes, JSDoc, TSDoc, rustdoc, explanatory code
  comments, and executable examples. Use when asked to create or improve
  technical docs, document a public interface or migration, align documentation
  with implementation, or validate docs against repository conventions. Do not
  use for general marketing copy; route repository-wide documentation audits
  and prioritization to codebase-improvement.
---

# Tech Docs

Make documentation a trustworthy interface to the software. Help the intended
reader complete a real task, understand the relevant contract, and recover from
likely failures without inventing behavior or imposing a foreign docs system.

## Workflow

1. Discover the repository before choosing a document shape. Read scoped agent
   instructions, existing READMEs and docs, navigation and generator config,
   contribution guidance, terminology, language, implementation, tests, and
   repository-native validation commands relevant to the requested surface.
2. Define the documentation job: audience, task or decision, entry point,
   prerequisites, expected result, likely failure paths, and the interface or
   behavior that is the source of truth. Ask only for gaps that cannot be
   resolved from the repository.
3. Choose the narrowest owning surface and read its reference:
   - README, setup, task, conceptual, or contributor guide: read
     [Guides and READMEs](references/guides-and-readmes.md).
   - API, CLI, configuration, or migration documentation: read
     [Interfaces and Migrations](references/interfaces-and-migrations.md).
   - JSDoc, TSDoc, rustdoc, docstrings, or explanatory comments: read
     [Code Documentation](references/code-documentation.md).
   - Any task with commands, code samples, generated references, links, or docs
     tooling: read [Examples and Verification](references/examples-and-verification.md).
4. Write at the closest stable source of truth. Update connected navigation,
   indexes, examples, and references only when the changed contract requires it.
   Link to an existing owner instead of duplicating material that will drift.
5. Verify with the repository's own tools. Run the relevant docs build, lint,
   link check, doctest, typecheck, example test, generated-reference check, or
   local smoke test. Never claim a check ran when it did not.
6. Report the reader-facing improvement, files changed, checks run, and any
   remaining evidence gap or intentional limitation.

## Operating Rules

- Preserve established language, terminology, information architecture,
  generator, formatting, and contribution conventions unless the task is to
  change them or evidence shows they are failing readers.
- Derive commands, flags, defaults, configuration keys, types, responses,
  errors, version requirements, and migration steps from current code and
  tests. Treat uncertain behavior as a question, not documentation.
- Lead with the supported path a reader should take. Add alternatives only when
  the choice changes compatibility, safety, cost, or outcome.
- Prefer task completion and progressive disclosure over exhaustive prose.
  Keep quick-start material short and route advanced concerns to focused pages.
- Document contracts, constraints, side effects, failure behavior, recovery,
  and non-obvious rationale. Do not paraphrase signatures or narrate obvious
  code merely to increase coverage.
- Keep examples minimal but complete enough to copy, adapt, and verify. Do not
  hide prerequisites or replace required behavior with convenient pseudocode.
- Preserve secrets and production safety. Use explicit placeholders, safe test
  data, and non-destructive environments; never publish credentials or suggest
  a production mutation merely to prove an example.
- Keep facts in their owning artifacts. Do not create a parallel documentation
  inventory, audit ledger, or mandatory docs hierarchy when the repository does
  not already use one.

## Routing Boundaries

- Route repository-wide documentation audits, gap prioritization, and broader
  improvement planning to `codebase-improvement`; return here for the selected
  documentation work.
- Route execution-only requests for existing docs builds, doctests, link checks,
  generated-reference checks, examples, or combined repository gates to
  `software-validation`. Keep documentation authoring and evidence design here.
- Route browser-interface copy and frontend implementation concerns to
  `effective-web` when the browser experience is primary.
- Route locale-specific punctuation and formatting to `locale-typography`.
- Use `metro-english` for natural professional English when requested; it does
  not own documentation architecture or technical correctness.
- Keep marketing positioning and campaign copy outside this skill. A root
  README may contain technical onboarding owned here and product positioning
  owned elsewhere.
- Route system direction and unresolved architectural choices to
  `software-architecture`, and durable accepted decisions to `decision-records`.
  Document their results here only after the underlying direction is known.

Use this skill for the craft and verification of technical documentation, not
as an orchestration, approval, commit, worktree, or delivery system.
