# Accessibility Testing and Evidence

Treat WCAG conformance as a necessary baseline, not proof that people can use
the experience. Combine cheap automated checks with task-based manual evidence,
and match the depth of testing to the consequence of failure.

## Define the claim before testing

Separate these questions:

- **Conformance:** Does the implementation meet the selected WCAG version,
  level, and scope?
- **Technical interoperability:** Do browsers and assistive technologies expose
  the intended role, name, state, relationships, focus, and announcements?
- **Usability:** Can the target users discover, understand, complete, recover
  from, and repeat the task efficiently?

A passing scanner addresses only a subset of the first question. A technically
conforming interface can still be confusing, exhausting, or practically
unusable. Record which claim the evidence supports instead of calling the whole
experience accessible after one green result.

## Use a layered evidence strategy

Run the cheapest useful checks early, then add human and assistive-technology
testing where automation cannot decide intent:

1. **Static and component checks:** HTML validity, lint rules, accessible-name
   assertions, component contracts, axe-style rules, and known-state stories.
2. **Keyboard tasks:** natural focus order, visible focus, no traps, full
   operation, Escape paths, skip mechanisms, and focus recovery.
3. **Accessibility-tree inspection:** computed role, name, description, value,
   state, relationships, hidden content, and live-region boundaries.
4. **Rendered resilience:** 200% and 400% zoom, text-only resizing, narrow
   reflow, forced colors, contrast, reduced motion, orientation, and pointer
   alternatives.
5. **Representative assistive technology:** screen reader plus browser, speech
   input, magnification, switch or other input where the product and risk call
   for it.
6. **Disabled-user usability:** representative people completing realistic
   tasks, especially for consequential, unfamiliar, or domain-specific flows.

Automate deterministic regressions, but keep manual checks for reading order,
meaningful alternatives, focus judgment, announcement quality, error recovery,
and whether the interface makes sense as a whole.

## Test tasks, not pages

Write short scripts around user outcomes:

- identify the current location and primary action;
- navigate repeated content and reach the main region;
- complete and correct a form without losing entered values;
- open, operate, and close overlays and disclosures;
- understand loading, success, changed results, and failure;
- resume after an interruption or validation error;
- complete the task at high zoom and without a pointer.

For each task, define the start state, required data, expected focus/state
transitions, success evidence, and recovery route. Include empty, partial,
loading, error, and permission states instead of testing only the happy path.

## Inspect the accessibility tree diagnostically

Use browser accessibility tools to answer concrete questions:

- Is the correct element exposed with the intended role?
- Does the computed name come from the intended visible source?
- Is secondary help a description rather than part of an unwieldy name?
- Are expanded, selected, checked, pressed, invalid, disabled, busy, current,
  and modal states accurate?
- Are relationships such as label, description, ownership, and control targets
  intact after conditional rendering?
- Are visually hidden, inert, or collapsed descendants exposed only when they
  should be?

The tree is a diagnostic model, not a substitute for assistive-technology
testing. Browsers and platform APIs can map the same DOM differently, and a
correct-looking tree does not prove that interaction or announcements work.

## Choose representative pairings

- Select screen-reader/browser combinations from the supported product
  environment and current user evidence, not from personal habit alone.
- Include at least one primary desktop pairing for complex or consequential
  flows, and add mobile when the product is materially used there.
- Record browser, operating system, assistive-technology version, input method,
  viewport/zoom, locale, and test date so findings can be reproduced.
- Do not require identical speech across combinations. Require equivalent
  understanding and operation.
- Re-test support-sensitive patterns such as live regions, custom comboboxes,
  grids, drag-and-drop, `aria-describedby`, `aria-controls`, and modal focus
  instead of assuming standards text guarantees behavior.

## Use standards and examples correctly

- Apply the product's declared WCAG target precisely; do not invent failures
  from team conventions such as requiring exactly one `h1`.
- Treat WAI-ARIA Authoring Practices examples as educational pattern references,
  not production-ready components. Adapt styling, responsiveness, localization,
  error handling, state restoration, and tested platform support.
- Prefer native elements even when a custom example appears to satisfy the ARIA
  pattern. Native controls bring platform behavior that an example may omit.
- Track advisory usability findings separately from conformance failures, while
  still prioritizing both by user impact and task criticality.

## Triage and prevent recurrence

For each finding, record:

- affected user and task;
- observed result and expected result;
- environment and reproduction steps;
- conformance criterion when applicable;
- severity based on blocked task, lost information, frequency, reach, and
  availability of a workaround;
- owning component, primitive, content rule, or process;
- regression coverage and verification needed for closure.

Fix systemic causes in shared primitives, design-system contracts, authoring
guidance, or acceptance criteria rather than repeatedly patching pages. Block
release for failures that prevent essential or legally consequential tasks;
avoid letting a raw scanner count substitute for impact-based triage.

## Minimum review evidence

Before calling a changed interactive flow accessible, capture at least:

- relevant automated checks and their scope;
- keyboard completion of the affected tasks;
- accessibility-tree inspection of changed controls and states;
- zoom/reflow and relevant user-preference modes;
- a representative screen-reader/browser pass for custom, dynamic, or
  consequential behavior;
- known limitations, untested combinations, and follow-up ownership.
