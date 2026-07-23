# Structure and Prototyping

Move from a product and interaction model toward a concrete experience while
keeping fidelity tied to the decision being tested. Structure should make the
system understandable; prototypes should expose uncertainty, not decorate it.

## Derive information architecture

Start from actors, objects, relationships, moments, permissions, and tasks.
Define:

- primary places and the purpose of each
- which objects appear there and at what density
- global, local, contextual, and utility navigation
- labels in the language people use and expect
- entry points from search, notifications, links, integrations, and return
- location, state, selection, filters, and unsaved work that must persist
- empty, first-use, loading, unavailable, error, and archived states

Test the model with representative finding and resumption tasks. A neat sitemap
is insufficient if people cannot predict where an object belongs, reach the
same object through a natural relationship, or recover their context after a
focused task.

Avoid using internal departments, database tables, or feature-team ownership as
the primary structure unless those concepts match the user's model. Preserve
multiple valid routes when the domain is genuinely relational rather than
forcing every task through a single hierarchy.

## Sketch breadth before depth

Use small, fast thumbnails to compare composition, hierarchy, navigation, and
interaction approaches. Keep content realistic enough to expose density and
priority. Generate materially different directions rather than minor styling
variants of the first idea.

Timebox several layouts for one context and use only enough marks to communicate
grouping and proportion. Let weak ideas become disposable evidence. Combine a
strong navigation treatment from one thumbnail with a better content layout
from another rather than treating every frame as an indivisible proposal. Move
between thumbnails and wireframes when a direction gains or loses credibility;
the work need not advance in one batch sequence.

For each direction check:

- what receives attention first and why
- where the person is, what they can do, and what changed
- how core objects and relationships are represented
- how an interruption, error, or alternative path changes the composition
- whether the environment supports exploration or intentionally narrows focus
- whether the design factors and visual character are already legible

Discard directions for explicit reasons and carry useful fragments forward.

## Use wireframes to specify behavior

Wireframes should make structure and interaction discussable without implying
finished visual design. Include real labels and representative content,
responsive changes, important states, action hierarchy, validation, feedback,
permissions, and recovery. Add concise annotations where behavior cannot be
inferred from the frame.

Cover enough key contexts before committing to a prototype that repeated
patterns, component needs, and inconsistencies can emerge. One polished frame
is weak evidence for a system that will require many states. Move back to broad
thumbnails when a wireframe exposes a layout problem, and zoom into a component
or interaction when that is the unresolved decision. Treat fidelity as a dial,
not a one-way stage gate.

For products shaped by user-created content, model a useful populated state
before designing onboarding and empty states. Then work backward: what actions,
tools, defaults, and guidance would let a person create that state? Starting
from emptiness can otherwise make the available controls, rather than the
desired outcome, define the product.

Do not use gray boxes as an excuse to postpone accessibility or content. Order,
landmarks, headings, labels, focus movement, target size, reading sequence, and
error association are structural decisions.

## Choose prototype fidelity by question

Name the question before choosing the medium:

| Question | Smallest useful artifact |
| --- | --- |
| Do people understand the concepts and labels? | object model, content sample, or rough structure |
| Can they find and resume the right place? | linked wireframes with realistic navigation and state |
| Does a risky interaction or transition make sense? | focused interactive prototype |
| Does responsive behavior survive real content? | coded slice or browser prototype |
| Does visual hierarchy, character, or motion communicate the intended quality? | high-fidelity visual or motion study |
| Does the end-to-end system work with real constraints? | thin production-like vertical slice |

Prototype the uncertain part and enough surrounding context for it to be
credible. Avoid building every screen at high fidelity when the decision
depends on one model, transition, or state change.

`product-design` owns the decision-grade question, fidelity choice, realistic
task, and evaluation plan. When the uncertainty is specifically browser layout,
responsive behavior, input, or implementation under already accepted intent,
use the optional `effective-web` skill. Its bounded browser protocol means:
build the smallest representative browser slice, record whether to `Discard`,
`Rebuild`, or `Productionize` it, and carry that conclusion back into the design
brief and prototype findings; do not leave a parallel browser artifact.

Start in the environment and viewport most representative of the intended use;
add other sizes when they answer a real layout or behavior question. Move into
the browser or target runtime when responsiveness, drag and drop, input,
performance, or platform behavior would only be simulated in a design tool.
The prototype medium must not conceal the uncertainty it is meant to resolve.

Use linked screens as an interaction sketch: they can test navigation,
information architecture, broad sequencing, and whether people recognize the
next place to act. They cannot substantiate claims about typing, validation,
loading, drag and drop, animation, or other behavior they do not reproduce.
State those omissions in the test plan and avoid interpreting workarounds as
participant difficulty with the intended product.

## Test realistic situations

Define tasks from research situations and desired progress, not instructions
that reveal the interface. Include realistic content, existing state, time
pressure or interruptions where relevant, and at least one non-happy path.

Observe comprehension, prediction, action, hesitation, recovery, and the
participant's explanation of what changed. Distinguish:

- observed behavior and quotes
- facilitator intervention
- interpretation and severity
- design hypothesis
- decision or follow-up question

Do not call a concept validated because participants completed a scripted path
after coaching. Revisit the object, language, or causal model when the same
misunderstanding appears across screens.

## Explore visual character in context

Name two to four qualities the experience should communicate and connect each
to the audience, purpose, and design brief. Avoid generic mood words that cannot
help distinguish a decision. Also name qualities that would send the wrong
signal.

This exploration precedes or feeds the optional `effective-web` skill's compact
Design Read and Decide Before Styling contract: record what the direction should
communicate, the evidence for it, and the decision that must precede styling.
`product-design` compares materially different experience directions;
`effective-web` carries the accepted direction into browser structure and
implementation constraints, then checks persistence and drift when later work
would erode that direction.

Gather references purposefully. Annotate the exact typography, color behavior,
shape language, spacing, imagery, icon treatment, depth, motion, or content tone
that communicates the intended quality. A folder of attractive screenshots is
not yet a design direction.

Build a small representative slice containing real content, a core object, a
primary action, and important state. Explore two or more coordinated visual
directions on that same slice so the comparison is about character rather than
different functionality. For each direction:

- identify the visual idea or motif that anchors it
- repeat compatible qualities across type, controls, icons, containers, and
  feedback instead of styling each element independently
- make deviations intentional and semantic, not accidental inconsistency
- evaluate hierarchy, readability, accessibility, cultural interpretation,
  product fit, distinctiveness, and durability beyond a current trend
- record which qualities worked, which conflicted, and what evidence should
  decide between the directions

Turn the chosen qualities into provisional tokens, component rules, and clear
anti-examples. Keep them as study evidence until `effective-web` reconciles
them with accepted design-system, accessibility, responsive, and implementation
contracts. Persist durable choices through the repository's decision convention
or the optional `decision-records` skill: record the context, decision, and
consequences rather than allowing a prototype token set to become an
undocumented parallel system. The delivered direction must fit this product
rather than reproduce another product's composition.

## Increase craft deliberately

When structure and behavior are credible, use typography, color, spacing,
shape, imagery, sound, and motion to communicate hierarchy, state, character,
and causality. Visual character is part of the product environment; it should
support purpose and expectation rather than arrive as an interchangeable skin.

Bring provisional design tokens and reusable patterns into the prototype early
enough that systemic decisions remain cheap to change. Promote a repeated
pattern to a component when coordinated change matters, but keep the system
provisional while the underlying interaction is still being learned.

Test accessibility, localization, reduced-motion behavior, contrast, zoom,
content extremes, and input modes at the fidelity where those qualities become
real. Route browser implementation and detailed visual-system work to
`effective-web`.

## Prepare delivery as a model, not a gallery

Handoff should include:

- design decision and evidence behind the chosen direction
- object, relationship, navigation, state, and permission model
- representative screens across breakpoints and states
- interaction, feedback, motion, and recovery behavior
- content, accessibility, localization, and data assumptions
- tokens or component decisions that must remain consistent
- prototype findings, unresolved risks, and rejected alternatives
- slices or milestones that preserve a coherent end-to-end experience
- acceptance evidence and questions requiring design review during build

Stay involved through implementation. A polished file is not the experience;
the delivered system, content, behavior, performance, and recovery paths are.
