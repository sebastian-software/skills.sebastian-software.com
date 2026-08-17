version: 1.0.0
topics: documentation, source-of-truth, maintenance, context

# Documentation Truth Contract

Apply this contract whenever a task creates, changes, reviews, or removes
documentation, comments, agent instructions, plans, specifications, examples,
or repository maps. Domain guidance still decides the document's craft and
audience. User, project, regulatory, and host instructions still decide what is
required and what may be changed.

## Give Each Claim One Owning Artifact

Identify the source that owns a claim before documenting it. Different kinds of
truth can have different owners:

- Executed behavior belongs in code and configuration; tests, types, schemas,
  generated help, and executable examples prove or expose that behavior.
- Product requirements, external contracts, and regulated specifications may
  be authoritative artifacts of their own. Preserve their identity and trace
  them to implementation and verification where the project requires it.
- Durable rationale and rejected alternatives belong in the repository's
  decision-record convention.
- Domain terms belong in one glossary or domain model used by the code and its
  readers.
- Operational procedures and recovery steps belong in the established runbook
  closest to the owned service and its automation.
- Navigation belongs in a short map that links to those owners.

Do not use “the code is the only truth” as a reason to erase requirements,
safety obligations, contractual behavior, or rationale that code cannot own.
The goal is one owner per claim, not one artifact type for every claim.

## Do Not Build a Prose Shadow of the Code

Do not add Markdown that narrates modules, functions, types, flags, defaults, or
control flow already expressed by the current implementation unless a defined
reader task needs a stable abstraction over those details.

Prefer improving names, types, boundaries, tests, schemas, generated reference,
or executable examples when they can make the contract discoverable and
checkable. Keep agent instructions focused on decisions, boundaries, commands,
and non-obvious repository conventions; do not turn them into a file-by-file
tour that must be updated after every refactor.

## Make New Documentation Earn Its Maintenance Cost

Before adding a document or section:

1. Name its reader and the task, decision, or recovery path it enables.
2. Find the existing owning artifact for every material claim.
3. Explain what the proposed documentation contributes that its owner cannot:
   navigation, rationale, domain language, task sequence, safety, recovery, or
   a required traceability link.
4. Link to or generate from an owner instead of copying it. If duplication is
   unavoidable, keep it narrow and define how drift is detected.
5. Update an existing canonical surface before creating a parallel hierarchy.
6. If no reader job, distinct contribution, or credible maintenance path
   remains, do not add the documentation.

Temporary plans and investigation notes must follow the repository's existing
convention and must not quietly become permanent architecture memory.

## Reduce Existing Documentation Creep Safely

Audit claims, not file counts. Compare a document's material statements with
their current owners, then classify each surface as:

- **Keep:** it owns useful rationale, vocabulary, requirements, safety,
  onboarding, migration, operation, or recovery knowledge.
- **Link:** another artifact owns the claim and this surface only needs to
  guide the reader there.
- **Generate:** the material is a mechanical projection of code, schemas, help,
  or another machine-readable owner.
- **Move:** the content is useful but sits far from the contract it qualifies.
- **Update or remove:** it duplicates, contradicts, or no longer serves a real
  reader task.

When change authority is present, remove or supersede conflicting copies in the
same focused change. During answer-only or diagnosis-only work, report the
conflict and smallest credible correction without mutating the repository.

Do not delete material merely because it is prose. Preserve required
requirements, ADRs, glossaries, safety contracts, runbooks, migration paths,
and concise onboarding maps unless their owning contract has genuinely moved or
expired.

## Verify the Result

- Check every retained behavioral claim against its owning implementation,
  interface, requirement, or decision.
- Run established docs builds, link checks, doctests, generated-reference
  checks, and executable examples that apply.
- Confirm the change leaves one discoverable owner for each affected claim and
  no newly conflicting copy.
- Report what became the source of truth, what documentation was added, linked,
  generated, moved, updated, or removed, and what remains unverified.
