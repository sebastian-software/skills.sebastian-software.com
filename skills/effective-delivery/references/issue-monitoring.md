# Monitoring

Apply these rules when creating or waking a recurring issue-queue monitor:

1. Reuse a single automation and include the repository, tracker/project, cadence,
   active issue/PR, branch/worktree, and last observed head/check state in its
   prompt or durable state.
2. Prevent overlapping runs: reconcile the current agent/worktree/PR before
   dispatching another implementation agent.
3. Prioritize regressions on owned PRs over new queue items.
4. Auto-fix only reproducible, issue-scoped, branch-local problems. Escalate
   ambiguous requirements, security-sensitive policy decisions, destructive
   migrations, missing credentials, external outages, and unrelated failures.
5. Stay quiet when nothing changed. Notify the user for a new claim, pushed fix,
   ready-state transition, material blocker, or tracker/authentication failure.
6. Stop or pause immediately when requested and update or delete the recurring
   automation so it cannot continue firing.
