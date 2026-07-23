---
name: decision-records
description: >-
  Create, review, update, supersede, and audit Architecture Decision Records
  (ADRs) for durable project decisions. Use when a user asks for an ADR,
  decision log, architecture decision, design decision, communication or brand
  voice decision, or recorded rationale; when a cross-cutting technical,
  product, design, content, marketing, security, operational, or process choice
  must remain understandable across people, tools, and agent sessions; or when
  another skill identifies a decision whose undocumented rationale would
  otherwise drift. Preserve existing repository conventions and do not create
  skill-specific dot folders or private memory formats.
---

# Decision Records

Keep durable rationale in repository-owned Markdown that humans and different
tools can read. Treat an ADR as a shared project artifact, not as agent memory.

## Workflow

1. Discover the repository's decision convention before writing. Search for
   `docs/adr`, `docs/decisions`, `adr`, decision indexes, ADR templates, and
   contribution guidance. Read related accepted records and follow their
   filename, numbering, metadata, status vocabulary, lifecycle, and index
   conventions. Determine whether accepted records are immutable or whether the
   repository explicitly uses living records that are edited in place.
2. Decide whether the choice deserves an ADR. Record it when it is durable,
   cross-cutting, costly to reverse, contains real tradeoffs, or must coordinate
   multiple people, channels, components, services, or future sessions. Do not
   create an ADR for a local refactor, an easily reversible detail, a task log,
   or an exact value already owned by code or configuration. The narrow
   exception is a repository-declared living setup or configuration record that
   intentionally keeps related values and rationale together as one source of
   truth.
3. Choose the operation:
   - create a `proposed` record for an undecided choice;
   - create an `accepted` record for an agreed choice;
   - amend only non-semantic errors or explicitly mutable review evidence, such
     as a dated validation result in a field the record marks as updatable, when
     the repository uses the immutable lifecycle;
   - supersede an accepted decision when its rationale or outcome changes in the
     immutable lifecycle;
   - update the existing record in place when an explicitly declared living
     lifecycle makes that file the current decision;
   - mark a record `deprecated` when it no longer applies and has no successor.
4. Read [ADR format and lifecycle](references/adr-format.md), then write the
   smallest complete record. For language, brand, content, or marketing
   decisions, also read [Communication decisions](references/communication-decisions.md).
5. Connect the record to reality. Link related code, configuration, design
   tokens, editorial guidance, examples, tests, runbooks, or issues where the
   repository convention permits. Keep exact implementation values in their
   owning artifacts; the ADR explains why the durable direction exists.
6. Update the ADR index or navigation if one exists. Check links, numbering,
   status, supersession in both directions, and consistency with the implemented
   result before finishing.

## Default Convention

When the repository has no decision convention and the work genuinely needs
one, use `docs/adr/` with zero-padded Markdown filenames such as
`0001-use-postgresql-for-primary-storage.md`. Do not create `.decision-records`,
`.architecture`, `.design-memory`, `.brand-memory`, or another tool-specific
directory.

Use a lightweight MADR-style structure without requiring a generator or custom
schema. Plain Markdown is the interoperability contract. Preserve an existing
Nygard-, MADR-, or repository-specific structure instead of converting it merely
to match this skill.

The portable default is immutable after acceptance. A living or mutable
lifecycle is opt-in: use it only when the repository already declares it or the
user explicitly authorizes the convention after seeing the cheaper-read versus
weaker-audit-history tradeoff. Never silently turn an immutable ADR corpus into
living records.

## Operating Rules

- Read accepted ADRs as constraints, not suggestions. When requested work
  conflicts with one, surface the conflict before implementation and either
  follow the record or explicitly supersede it with authorization.
- Preserve history according to the declared lifecycle. In the immutable
  default, do not rewrite an accepted record so that an old decision appears
  never to have existed. In an explicit living lifecycle, keep the current file
  accurate, record its update date or change note when the convention supports
  one, and rely on repository history for earlier versions.
- Separate decision from enforcement: ADRs hold rationale; code, tokens,
  schemas, editorial guides, examples, policy, tests, and automation enforce
  the outcome. Only one declared living setup or configuration record may also
  carry the exact non-secret values it intentionally owns.
- Keep one decision per record by default. A living setup or configuration
  bundle may group values and rationale only when they form one operational
  source of truth and are expected to change together.
- State uncertainty and missing evidence. A `proposed` record may contain open
  questions; an `accepted` record must make the chosen direction unambiguous.
- Use concrete language and project nouns. Avoid ceremony, fictional consensus,
  and generic claims such as "best practice" without a project-specific driver.
- Never record secrets, personal data, credentials, or private incident details
  in a broadly readable ADR.

## Routing Boundaries

- Route repository-wide decision discovery, audit, and prioritization to
  `codebase-improvement`; use this skill once a durable decision needs a record.
- Route unresolved system direction to `software-architecture` before recording
  it here, and route implementation work to the skill that owns that surface.
