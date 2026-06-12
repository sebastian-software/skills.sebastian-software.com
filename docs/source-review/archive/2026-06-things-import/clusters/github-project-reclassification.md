# Cluster Brief: GitHub Project Reclassification

Reviewed: 2026-06-10

## Scope

This is a policy-correction pass over already reviewed Things items. The user
clarified that GitHub projects are generally interesting, but not direct skill
sources. They should be tracked in the GitHub Project Matrix instead of staying
in the skill-candidate stream.

The exception is a GitHub-hosted article or blog post that is not a repository
or project page. Those remain eligible for source review as articles.

## Decision Rule

- GitHub repositories, package repos, old example repos, and PRs/issues are
  deferred to the GitHub Project Matrix unless the source is itself a durable
  explanatory article, official specification, or skill-source document.
- Package/project metadata belongs in
  `docs/source-review/github-projects/github-project-matrix.csv`.
- Skill candidates should primarily be articles, official docs, standards,
  high-quality implementation guides, or other explanatory sources.

## Reclassified Sources

| Source | Prior decision | New decision | Reason |
| --- | --- | --- | --- |
| `commander` plus archived `micro-starter` example | candidate | deferred | Useful CLI package/project context, but not article-like skill source material. |
| `vercel-labs/agent-skills/react-best-practices` | candidate | deferred | Interesting skill repository, better tracked in the GitHub matrix until intentionally reviewed as a skill-design source. |
| `package-browser-field-spec` | candidate | deferred | Specification-like repo, but still a GitHub project source; keep in matrix until paired with current bundler/package docs. |
| Remix PR #5040 | candidate | deferred | Useful architecture/testing clue, but a PR should not drive skill material without stronger article/docs support. |
| `browserslist` config README | candidate | deferred | Important ecosystem project, but project README belongs in matrix rather than the skill-candidate stream. |
| `jest-image-snapshot` duplicate tasks | candidate | deferred | Tool repo only; visual-testing guidance should use articles/official docs as primary sources. |
| `simple-icons` | candidate | deferred | Useful asset project, but package/project inventory rather than skill source material. |
| `serverless-express` | candidate | deferred | Useful migration tool, but project README should be matrix inventory until paired with broader serverless architecture docs. |

Not reclassified:

- `RFLZcQheZd1Q6c2QTBHMQT` (`github.com/blog/2112-delivering-octicons-with-svg`)
  is a GitHub blog article, not a project repository. It stays eligible as an
  article candidate.

## Things Actions

| Things ID | Decision | Final tag | Complete? | Reason |
| --- | --- | --- | --- | --- |
| `Kphjct798N8Uc4uzb7Xsxd` | deferred | `Skill Archive Deferred` | yes | CLI package/project context; track as GitHub/package inventory, not a direct skill source. |
| `A8TEDcF6ywEmEWw3anTeRD` | deferred | `Skill Archive Deferred` | yes | External skill repo is interesting but should be reviewed separately before becoming source material. |
| `XaHkH61SCxJGxW4NJ2Zb3m` | deferred | `Skill Archive Deferred` | yes | Spec-like GitHub repo; defer until paired with current package-resolution docs. |
| `3wf8NZ6yqE9sR3Yes8UJMd` | deferred | `Skill Archive Deferred` | yes | PR rationale is useful background, but not enough as primary skill source. |
| `Ep8hqkGP9d8GFQM4V8E8AW` | deferred | `Skill Archive Deferred` | yes | Browserslist project README belongs in the GitHub project matrix. |
| `KurSGZy9V8u4BzVbi3phmL` | deferred | `Skill Archive Deferred` | yes | Tool repo only; use stronger visual-testing docs/articles for skill material. |
| `Q3mLHe4EuCoNdPqnbtYdzo` | deferred | `Skill Archive Deferred` | yes | Duplicate tool repo; use stronger visual-testing docs/articles for skill material. |
| `Ya4p6mpMcbHQg284vzK93L` | deferred | `Skill Archive Deferred` | yes | Icon project inventory, not direct skill source material. |
| `DWqqDGNbSA1PTRD5W38Pw1` | deferred | `Skill Archive Deferred` | yes | Serverless tool repo; defer until paired with broader architecture docs. |
