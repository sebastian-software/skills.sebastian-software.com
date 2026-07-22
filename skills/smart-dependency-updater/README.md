[← Sebastian Software Skills](../../README.md)

# Smart Dependency Updater

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Turn dependency selection and maintenance into researched, validated, and
review-ready engineering changes.**

Smart Dependency Updater goes beyond mechanical version bumps. It researches
new dependency choices and upstream changes, respects local compatibility and
lockfile ownership, groups related updates into coherent delivery units,
assesses the local impact, adopts useful APIs when justified, validates the
result, and explains the work where reviewers need it: in the pull request.

## Default Outcome

The skill prepares every viable dependency group as a focused, review-ready
delivery unit. When the request includes publishing or an orchestrating caller
grants delivery authority, each group becomes a pushed, ready-for-review pull
request; otherwise the run stops at local branches plus a delivery proposal.
Each group documents:

- why the versions belong together
- which upstream changes matter to this codebase
- what local code or configuration changed
- which tests, builds, audits, and behavior checks ran
- what risk remains and which groups were deferred

## Use It When

- selecting or introducing a new external package, crate, action, image, or SDK
- updating direct dependencies across a repository or workspace
- replacing noisy bot-generated update streams with intentional groups
- handling major-version migrations with local adaptations
- evaluating whether new package capabilities simplify existing code
- creating several dependency PRs in isolated worktrees
- explaining why a security or maintenance update is safe to merge

## Example Prompts

```text
Choose and add a stable HTTP client that fits this repository's runtime and
package-manager constraints. Keep the manifest and lockfile consistent.

Update this repository's dependencies and open one ready PR per coherent group.

Replace the current Dependabot backlog with a researched update portfolio and
defer only groups that have a concrete blocker.

Upgrade this framework major version, adapt our code to the relevant upstream
changes, and document the risk and validation in the PR.

Check whether the new dependency APIs let us remove any workarounds while doing
the update.
```

See [SKILL.md](SKILL.md) for grouping heuristics, research requirements,
worktree orchestration, validation, local adoption, and PR structure.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill smart-dependency-updater
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian smart-dependency-updater
dalo approve skill sebastian:smart-dependency-updater
dalo sync
```

## Related Skills

- [PR Review](../pr-review/README.md) maintains the resulting pull requests and
  responds to reviewer feedback.
- [Codebase Improvement](../codebase-improvement/README.md) handles broader
  modernization opportunities that are not dependency-update work.
- [Port Codebases](../port-codebases/README.md) is the better fit when an update
  becomes a deliberate language, runtime, framework, or platform migration.
- [Decision Records](../decision-records/README.md) captures durable dependency
  or platform choices when the rationale must survive the update.
- [Software Validation](../software-validation/README.md) executes established
  repository gates; this skill owns dependency-specific compatibility research
  and validation scope.

## Scope

The skill does not force unsafe upgrades through failing checks or hide blocked
groups behind a green summary. A focused dependency introduction does not trigger
a repository-wide update inventory. Planning-only, draft, local-only, or
single-group outcomes remain available when the user asks for that narrower
scope, and a caller's narrower delivery authority always overrides the default
delivery contract.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
