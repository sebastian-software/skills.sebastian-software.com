# Things Intake Snapshot: 2026-06-10

This snapshot records the first broad tagging pass from Things into the skill
archive review process.

## Scope

- Source: local Things database
- Included: open, non-trashed tasks containing `http`
- Deduplicated open URLs seen during extraction: 5,325
- Intake threshold: heuristic score `>= 4`
- Things action: tagged matching tasks with `Skill Archive`,
  `Skill Archive Intake`, and one broad category tag.
- Important: these are **not reviewed sources** yet.

## Tagged Intake Counts

| Things category tag    |     Tasks |
| ---------------------- | --------: |
| `Skill: JS Tooling`    |       535 |
| `Skill: Frontend UI`   |       401 |
| `Skill: Testing`       |        21 |
| `Skill: AI Agents`     |        21 |
| `Skill: Performance`   |        12 |
| `Skill: Knowledge`     |        11 |
| `Skill: Visual Assets` |         6 |
| `Skill: Backend Cloud` |         3 |
| `Skill: Security`      |         2 |
| `Skill: Marketing`     |         2 |
| **Total**              | **1,014** |

## Interpretation

The first classifier over-selects old JavaScript/tooling links because GitHub
and package/tool names are common in Things. Treat `Skill: JS Tooling` as an
intake queue that needs aggressive pruning. Prefer reviewing smaller clusters
with clear skill potential:

1. `Skill: Testing`
2. `Skill: Performance`
3. `Skill: AI Agents`
4. `Skill: Visual Assets`
5. high-authority `Skill: Frontend UI`

## Next Review Pass

Start with `Skill: Testing` because the cluster is small enough to review
manually and already points to a coherent potential skill:

- Vitest Browser Mode / visual regression
- Playwright screenshots
- Storybook testing
- CI baselines and screenshot update workflows
- flake control

For each reviewed source, create a source card or append the source to a cluster
brief before changing any skill.

## Progress Log

### 2026-06-10

Completed first final-action pass:

| Cluster brief                              | Items completed in Things | Candidate | Deferred | Rejected |
| ------------------------------------------ | ------------------------: | --------: | -------: | -------: |
| `clusters/testing.md`                      |                        21 |        18 |        2 |        1 |
| `clusters/performance-security-backend.md` |                        17 |         9 |        5 |        3 |
| `clusters/ai-visual-knowledge.md`          |                        38 |        14 |       10 |       14 |
| `clusters/marketing-misclassified.md`      |                         2 |         1 |        1 |        0 |
| `clusters/js-tooling-01.md`                |                        50 |         4 |       15 |       31 |
| `clusters/frontend-ui-01.md`               |                        50 |        29 |        7 |       14 |
| `clusters/js-tooling-02.md`                |                        50 |         0 |       19 |       31 |
| **Total**                                  |                   **228** |    **75** |   **59** |   **94** |

Policy correction after user clarification:

- `clusters/github-project-reclassification.md` moved 9 GitHub repository,
  README, or PR sources from `Skill Archive Candidate` to
  `Skill Archive Deferred`.
- GitHub projects remain interesting, but are now tracked in
  `github-projects/github-project-matrix.csv` instead of the skill-candidate
  stream.
- GitHub-hosted articles/blog posts can still remain candidates when the source
  is article-like rather than a project repository.

Corrected decision totals:

| Items completed in Things | Candidate | Deferred | Rejected |
| ------------------------: | --------: | -------: | -------: |
|                       228 |        66 |       68 |       94 |

Additional batch:

| Cluster brief                | Items completed in Things | Candidate | Deferred | Rejected |
| ---------------------------- | ------------------------: | --------: | -------: | -------: |
| `clusters/js-tooling-03.md`  |                        50 |         0 |       41 |        9 |
| `clusters/js-tooling-04.md`  |                        50 |         1 |       32 |       17 |
| `clusters/js-tooling-05.md`  |                        50 |         0 |       42 |        8 |
| `clusters/frontend-ui-02.md` |                        50 |        31 |        8 |       11 |
| `clusters/js-tooling-06.md`  |                        50 |         0 |       44 |        6 |
| `clusters/js-tooling-07.md`  |                        50 |         0 |       41 |        9 |
| `clusters/frontend-ui-03.md` |                        50 |        11 |       23 |       16 |
| `clusters/js-tooling-08.md`  |                        50 |         1 |       28 |       21 |
| `clusters/frontend-ui-04.md` |                        50 |         9 |       23 |       18 |
| `clusters/js-tooling-09.md`  |                        50 |         2 |       15 |       33 |
| `clusters/js-tooling-10.md`  |                        50 |         0 |       31 |       19 |
| `clusters/frontend-ui-05.md` |                        50 |        23 |       12 |       15 |
| `clusters/js-tooling-11.md`  |                        35 |         3 |       17 |       15 |
| `clusters/frontend-ui-06.md` |                        50 |        14 |       14 |       22 |
| `clusters/frontend-ui-09.md` |                         1 |         0 |        1 |        0 |
| `clusters/frontend-ui-07.md` |                        50 |        29 |        7 |       14 |
| `clusters/frontend-ui-08.md` |                        50 |        31 |       13 |        6 |

Current corrected totals:

| Items completed in Things | Candidate | Deferred | Rejected |
| ------------------------: | --------: | -------: | -------: |
|                     1,014 |       221 |      460 |      333 |

Applied Things changes:

- added `Skill Archive Reviewed`
- added final decision tag
- removed `Skill Archive Intake`
- marked each handled task complete

Verification after latest actions:

- 1,014/1,014 handled cluster rows have `status=completed`
- 0/1,014 handled cluster rows still have `Skill Archive Intake`
- 1,014/1,014 handled cluster rows have `Skill Archive Reviewed`
- Raw cluster decisions contain 230 candidate rows, but 9 early GitHub
  repository/README/PR candidates were later reclassified to deferred according
  to the GitHub-project policy. The final Things decision tags are therefore
  221 candidate, 460 deferred, and 333 rejected.
- Candidate GitHub repository URL check leaves 5 article- or guide-backed
  exceptions, not plain project picks: `Priority Plus Navigation mit JS`
  includes the CSS-Tricks article; `defaultIsBad` is TypeScript Book prose;
  `PostCSS Plugin fuer ChromaJS` includes the Vis4 color-scale article; and the
  two ReactWG RSC entries are guide-like working-group discussions.

Remaining open intake after latest verification:

| Things category tag | Open intake tasks |
| ------------------- | ----------------: |
| **Total**           |             **0** |
