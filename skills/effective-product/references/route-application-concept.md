# Route: Application Concept

Use this route when the requested outcome is a concept for a **new application**
or a deep review of such a concept before implementation planning. A feature
request, research question, or isolated scope decision stays on its narrower
Product route. Do not turn a concept into an implementation plan.

## Read the relevant product guidance

- [Discovery and Evidence Review](route-discovery.md) and
  [Product decision contract](product-decision-contract.md) for the problem,
  audience, evidence, and consequential assumptions.
- [Scope, Quality, and Shipping](route-scope-and-shipping.md) for the smallest
  coherent first version, non-goals, and quality bar.
- [Solution Modeling and Prototyping](route-design-modeling.md) when the
  application needs objects, flows, or interaction alternatives to make its
  solution understandable.
- [Decision Records](route-decisions.md) only to judge whether a durable choice
  merits a later ADR. Creating a concept does not create an ADR.

Load only the links needed for the current concept. Bring in
`effective-engineering` for consequential system or data feasibility and
`effective-web` for browser experience or browser-specific obligations; keep
their detailed designs out of the concept.

## Develop the first concept

Read the user's idea, existing product evidence, and any applicable project
brief or repository context. An empty repository is a valid starting point.
Clarify only missing choices that change the application's purpose, primary
users, central use cases, hard constraints, or explicit exclusions. Label what
remains unknown rather than holding a broad discovery interview or inventing
customer evidence.

Produce a complete but deliberately shallow concept covering:

1. The problem and desired progress for a named target audience; distinguish
   observations, stakeholder claims, commitments, and assumptions.
2. Two or three central use cases and the solution idea that connects them.
3. The smallest coherent first version, its critical quality bar, and explicit
   non-goals.
4. A coarse technical direction: platform, likely integration or data needs,
   and constraints, with rationale and uncertainty. Name candidate approaches
   without specifying interfaces, schemas, code, or an implementation sequence.
5. Material product, feasibility, trust, privacy, or security risks and open
   questions whose answers could change the direction.

Use the project's existing concept format if one exists. Otherwise return the
concept in clear Markdown; save it only when the user asks or the project
convention requires it. Keep the whole artifact in the project's chosen
language. Do not add a work breakdown, schedule, plan file, status marker, or
tool-specific invocation to this first version.

Before handing it over, check that every area above has a meaningful answer,
non-goals constrain the first version, evidence and assumptions are visibly
different, and a reader can decide whether this is the application they want.
An honest open question is better than a fabricated answer.

## Review the concept in depth

Start with the actual concept and its evidence. Compare its claims **with each
other** before adding new criteria: do the audience, problem, use cases,
solution, first-version scope, non-goals, and technical direction describe the
same application? Then examine product fit, coherent scope and quality,
feasibility, data and trust boundaries, material risks, and the evidence behind
consequential claims. A demanding technical or browser question belongs with
the matching discipline above; name the unresolved dependency in the concept.

Classify each material finding by what it needs:

- **Direct correction:** a supported, uncontroversial omission or
  contradiction. Correct a supplied, editable concept during its deep review
  unless the user asked for read-only feedback, and report what changed.
- **Direction decision:** materially different viable paths. Present their
  consequences and a reasoned recommendation; do not choose on the user's
  behalf when the choice changes the product promise, scope, or risk.
- **Open blocker:** missing evidence, feasibility, or a deferred decision that
  prevents a responsible recommendation. State the precise question and what
  would close it; keep it visible even when other sections are improved.

Recheck the revised concept for internal consistency. Recommend proceeding to
implementation planning only when no material contradiction or blocking open
point remains. A deferred blocker cannot appear elsewhere as a decided
implementation choice. When the concept is viable, add a **coarse handoff** of
ordered work packages: each package has a goal, completion criterion, and
dependencies. Mark any durable decision that may merit an ADR with one-line
rationale. These packages frame later plans; do not write plan or ADR files
unless separately requested.

Report the recommendation, corrections, decisions still needed, blockers, and
the next useful package or evidence step. Keep small, clear concepts small;
depth is for finding consequential gaps, not filling every possible template.
