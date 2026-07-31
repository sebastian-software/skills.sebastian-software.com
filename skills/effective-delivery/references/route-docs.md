# Route: Technical Documentation

Make documentation a trustworthy interface to the product or software. Help the
intended reader complete a real task, understand the relevant contract, and
recover from likely failures without inventing behavior or imposing a foreign
docs system.

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
     [Guides and READMEs](guides-and-readmes.md).
   - API, CLI, configuration, or migration documentation: read
     [Interfaces and Migrations](interfaces-and-migrations.md).
   - JSDoc, TSDoc, rustdoc, docstrings, or explanatory comments: read
     [Code Documentation](code-documentation.md).
   - ASD-STE100, Simplified Technical English, STE, controlled English,
     international maintenance text, or an STE conformance review: read
     [Simplified Technical English](simplified-technical-english.md) together
     with the reference for the owning documentation surface.
   - tekom, rule-based writing, controlled or standardized German,
     translation-oriented German, or a German technical-language review: read
     [Controlled Technical German](controlled-technical-german.md) together
     with the reference for the owning documentation surface.
   - Any task with commands, code samples, generated references, links, or docs
     tooling: read [Examples and Verification](examples-and-verification.md).
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
- Apply a controlled-language profile only when the user, project, or governing
  documentation contract requires it. Name the selected standard, guide,
  edition, and project profile. Distinguish informed editing from a verified
  review.
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

## Cross-links

- Repository-wide documentation audits, gap prioritization, and broader
  improvement planning are the Audit route; return here for the selected
  documentation work.
- Execution-only requests for existing docs builds, doctests, link checks,
  generated-reference checks, examples, or combined repository gates are the
  Validation route. Keep documentation authoring and evidence design here.
- Browser-interface copy and frontend implementation concerns belong to
  `effective-web` when the browser experience is primary.
- Locale-specific punctuation and formatting, and natural professional English
  for team communication, belong to `effective-writing`. That discipline does
  not own documentation architecture or technical correctness, and when
  ASD-STE100 governs, its controlled vocabulary and writing rules take
  precedence over natural voice preferences.
- Marketing positioning and campaign copy belong to `effective-marketing`. A
  root README may contain technical onboarding owned here and product
  positioning owned there.
- System direction and unresolved architectural choices belong to
  `effective-engineering`, and durable accepted decisions to
  `effective-product`. Document their results here only after the underlying
  direction is known.

Use this route for the craft and verification of technical documentation, not as
an orchestration, approval, commit, worktree, or delivery system.
