# Apple Design Foundations

Use this reference when shaping the shared native experience, hierarchy,
navigation, layout, state, feedback, or use of system conventions.

## Start from the Outcome

Describe the primary task without naming a screen or component. Then map:

- people, objects, relationships, permissions, and consequential state;
- entry points, interruptions, restoration, and completion;
- content priority and secondary actions;
- device context, attention, posture, and likely duration; and
- platform evidence, assumptions, and unresolved constraints.

Preserve this model across platforms. Adapt the visible hierarchy and
interaction to the platform instead of copying coordinates or control chrome.

## Prefer Familiar System Behavior

Start with system-provided controls, materials, typography, symbols, sheets,
menus, selection, feedback, and navigation patterns. They carry platform
behavior, accessibility semantics, input support, localization, and future
adaptation that custom replicas must rebuild.

Customize only when the standard behavior cannot express a material product
need. For every custom control, specify:

- semantic role, name, value, state, and available actions;
- focus, hover, pressed, selected, disabled, loading, and error behavior;
- keyboard, pointer, touch, voice, switch, and assistive access;
- text scaling, localization, contrast, and reduced-motion behavior; and
- how it remains recognizable after platform appearance changes.

Do not use visual novelty as the only reason to discard native behavior.

## Build Adaptive Hierarchy

Design around content priority and available space:

1. Identify what must remain visible to understand the current state.
2. Decide what can move into a secondary column, inspector, toolbar, menu, or
   detail destination.
3. Preserve selection and task context as width or window mode changes.
4. Define narrow, intermediate, and wide behavior from actual supported
   windows, not device-name assumptions.
5. Test long localized strings, accessibility sizes, empty and error states,
   keyboard presence, and system overlays.

Respect safe areas and system-owned regions. Do not freeze layout to one
resolution, orientation, full-screen size, or screenshot.

## Choose Navigation from the Information Model

- Use a stack when people move through a focused hierarchy or task and need a
  predictable back path.
- Use top-level destinations when areas are peers and people switch frequently.
- Use a sidebar or multi-column structure when persistent selection and context
  improve larger or resizable workspaces.
- Use search, commands, menus, shortcuts, or deep links as complementary entry
  paths where the platform and task warrant them.
- Use modality for a bounded decision or temporary task, not as the default
  container for deep navigation.

Keep destination identity stable across forms. A deep link should resolve to
the same object or task even if one platform shows a pushed detail, another a
selected column, and another a separate window.

## Make State Legible and Recoverable

Show loading, empty, offline, stale, permission-denied, partial, success, and
failure states in the interface that owns the task. Keep the last useful state
when safe, and distinguish unavailable actions from actions that are still
working.

For destructive or costly actions:

- make consequence and scope clear before commitment;
- prefer undo or recovery when feasible;
- preserve selection and context after completion;
- avoid surprise changes caused by a gesture with no visible alternative; and
- make cross-device or background progress explicit.

Use haptics, sound, animation, color, and material as supporting feedback.
Essential confirmation and status must remain perceivable without any one of
them.

## Verify Volatile Guidance

Before asserting a specific component, metric, API, platform behavior, or
support matrix:

1. Check current official Apple Human Interface Guidelines.
2. Check current official developer documentation for the exact platform and
   deployment range.
3. Inspect the project's configured deployment targets and SDK.
4. Record the date, relevant version, decision, and unverified conditions in
   the task artifact.

Do not preserve copied documentation, screenshots, source lists, or version
tables inside the skill. Keep the resulting design rule and verification need.
