[← Sebastian Software Skills](../../README.md)

# Issue Autopilot

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Turn an unspecified live issue queue into ranked, isolated, review-ready work
without taking over explicitly named tickets or merging pull requests.**

Issue Autopilot discovers the repository's authoritative GitHub or Linear queue,
applies ownership and actionability gates, ranks eligible work, selects the next
target, delegates its implementation in an isolated worktree, and keeps the
resulting PR's readiness state synchronized. Its activation boundary is deliberately
narrow: choosing a named issue is ordinary targeted delivery, not queue automation.

## Default Outcome

In triage mode, the skill returns a compact evidence-based queue without changing
tracker or repository state. In run mode, it selects and advances exactly one
actionable issue at a time. In monitor mode, it reconciles queue-owned PRs before
checking for newly opened, reopened, or changed issues and stays quiet when nothing
material changed.

Every mutating run keeps implementation isolated, preserves other people's work,
opens or updates a reviewable PR, and treats `ready-to-merge` as a reversible derived
flag rather than permission to merge.

## Use It When

- finding and fixing the next or highest-priority eligible issue
- processing an assigned or unassigned backlog without preselecting ticket IDs
- monitoring incoming issues and queue-owned CI or review feedback
- ranking a live issue set without claiming or implementing anything
- continuing an issue or PR demonstrably claimed by an earlier Autopilot run

## Example Prompts

```text
Find the highest-priority unassigned issue in this repository and fix it.

Work through my assigned open issues one at a time and keep each PR review-ready.

Monitor incoming bug reports every 15 minutes and take the next actionable one.

Triage the current project backlog, but do not change tracker or repository state.
```

Requests such as `Fix GitHub issue #123`, `Implement LIN-42`, or `Review PR #9`
remain targeted workflows and must not activate this queue workflow.

See [SKILL.md](SKILL.md) for the activation gate, ownership rules, ranking,
delegation, monitoring, and reversible ready-state contract.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill issue-autopilot
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian issue-autopilot
dalo approve skill sebastian:issue-autopilot
dalo sync
```

## Related Skills

- [Effective Workflow](../effective-workflow/README.md) owns a specifically named
  software change after Issue Autopilot's activation gate rejects queue mode.
- [PR Review](../pr-review/README.md) owns standalone review and maintenance of an
  explicitly named PR that was not created by the active queue.
- [Metro English](../metro-english/README.md) shapes the team-facing issue, PR, and
  review communication after the technical substance is settled.
- [Software Validation](../software-validation/README.md) executes established
  repository gates when the selected issue needs broader validation depth.

## Scope

Issue Autopilot never expands a named issue, issue URL, exact title, finite ticket
list, or unrelated PR into a backlog run. It does not take work assigned only to
another active human, invent tracker ownership, merge PRs, modify production data,
or auto-fix ambiguous and security-sensitive policy decisions. Queue monitoring is
real only when the environment provides a configured recurring mechanism.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
