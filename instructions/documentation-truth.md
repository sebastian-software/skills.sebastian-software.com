version: 1.1.0
topics: documentation, source-of-truth, maintenance, context

# Documentation Truth Contract

Apply when working on documentation, comments, agent instructions, plans,
specifications, examples, or repository maps. User, host, project, and regulatory
requirements determine what may change.

## Give Each Claim One Owner

| Claim | Owning artifact |
| --- | --- |
| Executed behavior, flags, defaults | Code/configuration, exposed by types, schemas, generated help, tests, or executable examples |
| Requirements and external contracts | Approved requirements/specifications, traced to implementation where required |
| Durable rationale and rejected alternatives | The repository's decision records |
| Domain meaning | One glossary or domain model |
| Operational recovery | The service's verified runbook |
| Navigation | A short map linking to those owners |

Code cannot replace rationale, domain meaning, requirements, or recovery
sequencing. Preserve those when they serve a distinct reader task.

## Keep Documentation Useful and Maintainable

Before adding prose, identify the reader's task and the contribution the owning
artifact cannot make. Update the canonical surface first. Link to or generate
mechanical inventories instead of copying them; when a duplicate is required,
keep it narrow and define how drift is detected.

Do not narrate every module, function, type, flag, or control path in a parallel
Markdown hierarchy. Prefer discoverable names, contracts, generated references,
and executable examples. Agent instructions should record non-obvious
conventions and conditional pointers, not mandate a full repository tour before
every edit.

Keep temporary plans in the project's existing convention. Do not turn session
notes into permanent architecture memory.

## Audit and Reduce Existing Prose

Compare affected claims with their owners. Keep useful rationale, vocabulary,
requirements, onboarding, migration, and recovery guidance. Link or generate
mechanical projections, move misplaced knowledge, and update or remove
conflicting, redundant, or obsolete copies when the request authorizes changes.
Read-only audits return findings without modifying files.

Audit claims rather than deleting to meet a file-count target. Required
traceability, accepted ADR history, safety contracts, and runbooks remain useful
even when implementation details can be read in code.

Verify changed behavioral claims and examples against their owners, check
changed links, and run applicable repository documentation checks. Report the
new owner only where it changed and disclose material verification gaps; a small
edit does not need a full documentation inventory or report template.
