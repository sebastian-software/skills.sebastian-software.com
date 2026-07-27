# Safe Legacy Change Strategy

Use this reference when the requested behavior sits in existing code with weak
tests, hidden coupling, unclear responsibilities, or expensive failure modes.
The goal is not to modernize the surrounding system. It is to make one
authorized change observable, bounded, and reviewable.

## Define the Change Before Touching Structure

Write a compact change statement:

- the requested behavior and affected user or system outcome;
- the input, event, or state that initiates it;
- the current result, including whether it is correct, unknown, or known wrong;
- the intended result;
- the failure impact and rollback constraint;
- the authority and scope of the requested change.

Do not use “legacy” as evidence that broad rewriting is justified. Age, style,
or missing tests do not prove incorrectness.

## 1. Find the Change Point and Effect Chain

Start from an observable entry point and trace only the path that can affect the
requested result:

1. locate the public or operational entry point;
2. follow data and control flow to the narrowest decision or state mutation;
3. record external effects, persistence, messages, clocks, randomness, and
   global state;
4. identify callers and consumers that depend on the current contract;
5. mark uncertainty where dynamic dispatch, configuration, or unavailable
   systems break the trace.

Prefer evidence from execution, focused logs, repository history, and current
callers over names or comments. Do not claim full impact coverage when the
trace has unobserved boundaries.

## 2. Choose an Observation Point

Pick the closest stable boundary where the relevant behavior can be observed:

- a public function result or error;
- a state transition;
- a persisted record;
- a message or integration request at a controlled boundary;
- a user-visible or operational outcome.

The observation must discriminate the behavior at risk. A broad green suite,
line coverage, or a test of an internal helper does not establish that the
effect chain is protected.

When no usable observation exists, identify the smallest bounded
instrumentation or seam needed. Do not add permanent logging of secrets or
personal data merely to make the path visible.

## 3. Choose the Smallest Seam

A seam is a place where the relevant dependency or effect can be observed or
controlled without changing the business behavior. Prefer, in order:

1. an existing public or package boundary;
2. an existing injectable dependency, interface, adapter, or clock;
3. a narrow extraction around one effect;
4. characterization at a higher stable boundary when internal extraction would
   be riskier.

Do not introduce a framework, generic abstraction, service split, repository
layer, or dependency-injection system for one test. A seam is justified by the
specific observation and risk it enables.

## 4. Characterize Relevant Current Behavior

Before changing behavior, capture only the cases needed to protect the effect
chain:

- the normal path closest to the requested change;
- consequential edge or error paths;
- caller-visible ordering, persistence, or retry behavior;
- any interaction whose absence is part of the contract.

Characterization evidence describes what the system does now. It does not
automatically endorse that behavior as correct. Route focused non-frontend test
design and implementation to `software-testing`; this owner supplies the change
path, risk, observation boundary, and distinguishing cases.

## 5. Mark Known-Wrong Behavior

When current behavior is a confirmed defect:

- label it explicitly as known wrong in the plan and test intent;
- cite the evidence and accepted desired behavior;
- avoid a misleading regression assertion that presents the defect as a
  permanent contract;
- if a temporary characterization is necessary for safe preparation, state
  when it must change or be removed;
- ensure the final behavior evidence fails for the old defect and passes for
  the correction.

Do not “preserve all existing behavior” as a blanket instruction. Preserve
relevant relied-upon behavior while changing the authorized defect.

## 6. Separate Preparation from Behavior

Use distinct reviewable steps:

### Preparatory change

- introduces the narrow seam or clarifies the change point;
- is intended to preserve observable behavior;
- is validated against the current characterization evidence;
- avoids unrelated cleanup and renaming churn.

### Behavior change

- alters the named rule or outcome;
- updates or adds evidence for the desired behavior;
- removes temporary expectations for known-wrong behavior;
- includes rollback or containment proportional to failure impact.

Keep these in separate commits or PRs when their risk, reviewers, rollback, or
evidence differ materially. A tiny local extraction and behavior fix may remain
in one PR when the diff is still independently reviewable, but describe the two
steps separately.

## 7. Verify the Complete Effect

Run the narrowest discriminating evidence first, then repository-native checks
for affected callers and integrations. Verify:

- the requested outcome changed;
- protected current behavior did not;
- known-wrong behavior is not accidentally frozen;
- side effects occur once and in the required order;
- failure, retry, concurrency, and rollback behavior where relevant;
- no generated, configuration, or migration state was omitted.

Do not turn a dual-write, concurrency, migration, or architectural concern into
a local refactor. Route focused test implementation to `software-testing`,
system direction to `software-architecture`, and a language/runtime/framework
port to `port-codebases`.

## Plan Shape

Return:

1. change statement and scope;
2. entry, change point, effect chain, and important unknowns;
3. observation point and smallest seam;
4. current behaviors to characterize, with known-wrong cases marked;
5. preparatory step separated from behavior step;
6. focused and repository-native verification;
7. rollback, stop conditions, and specialist handoffs.

Stop when the relevant path cannot be observed safely, the desired behavior is
not authorized or agreed, or the smallest credible change requires a new
architecture, port, security, infrastructure, or language specialization
outside the selected scope.
