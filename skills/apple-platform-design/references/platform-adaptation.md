# Platform Adaptation

Use this reference when one product spans iOS, iPadOS, macOS, watchOS, or
visionOS. Preserve shared outcomes and state while adapting hierarchy, density,
window or space behavior, inputs, and attention.

## iPhone and iOS

Prioritize the primary task and content in a compact, mobile context. Expect
touch, virtual keyboard, interruptions, short or extended sessions, changing
orientation where supported, and one-handed use where relevant.

- Keep primary actions discoverable and comfortably reachable.
- Limit simultaneous chrome without hiding consequential state.
- Preserve a predictable back path and state restoration.
- Request personal data or sensors only for an immediate feature benefit.
- Use system integrations when they shorten a real task, not to decorate the
  app with platform features.

Do not assume every iPhone size, orientation, input, or accessibility setting
provides the same available space.

## iPad and iPadOS

Treat iPad as a flexible workspace. People may hold it, place it on a stand,
resize its window, work beside other apps, and combine touch, Pencil, keyboard,
pointer, and voice.

- Design continuously from narrow to wide windows.
- Use additional width to expose useful context, selection, detail, inspectors,
  or tools instead of stretching line lengths and controls.
- Preserve task and selection as columns collapse or expand.
- Support keyboard navigation, shortcuts, pointer feedback, context menus, drag
  and drop, and Pencil only where each improves the task.
- Let multiple windows represent meaningful independent documents or work
  contexts; define creation, restoration, identity, and close behavior.

Never require landscape, full screen, or one multitasking arrangement unless a
verified hardware or safety constraint makes it unavoidable.

## Mac and macOS

Design for long-lived work, high information density, resizable and overlapping
windows, multiple displays, keyboard and pointer precision, inactive state, and
system command conventions.

- Give windows meaningful identity, restoration, minimum useful size, and
  sensible behavior across displays.
- Put broadly applicable commands in discoverable menus and provide conventional
  keyboard shortcuts.
- Use toolbars, sidebars, inspectors, context menus, selection, and file or
  document behavior when they fit the product model.
- Support keyboard-only operation and distinguish focus from selection.
- Adapt spacing and control density to desktop expectations instead of
  preserving touch-first scale everywhere.

A shared framework or Catalyst foundation can reduce implementation work, but
it does not prove the experience behaves like a Mac app.

## Apple Watch and watchOS

Choose a small set of timely, glanceable, independently valuable tasks.
Interactions may happen while a person is moving and often last less than a
minute.

- Surface essential state immediately.
- Keep hierarchy shallow and actions focused.
- Use the Digital Crown, notifications, complications, and other current system
  surfaces only when they improve quick access or control.
- Preserve legibility and tap confidence with realistic wrist context.
- Offer a useful failure and offline state without requiring the paired phone
  for every core Watch task.

Move deep browsing, prolonged authoring, dense comparison, and complex
configuration to a more suitable platform while preserving continuity.

## Apple Vision Pro and visionOS

Start conventional UI work in a standard window in the shared space. Choose a
volume, portal, or immersive space only when spatial representation or
immersion materially changes the outcome.

- Use the minimum level of immersion needed for the moment.
- Keep content within a comfortable field of view and avoid unnecessary head,
  arm, or body movement.
- Support relaxed indirect eyes-and-hands interaction and alternatives to
  precise gaze or direct reach.
- Maintain a stable visual reference and a reduced-motion path.
- Preserve privacy around surroundings, nearby people, and potentially visible
  content.
- Provide windowed or otherwise non-immersive access to essential tasks.

Do not turn a conventional settings, account, form, or list task into a spatial
spectacle. Do not require standing, walking, extended reach, or full immersion
without a necessary and verified use case.

## Create a Delta Matrix

For each primary flow, record:

| Decision | Shared outcome | iPhone | iPad | Mac | Watch | Vision |
| --- | --- | --- | --- | --- | --- | --- |
| Entry and continuation | | | | | | |
| Hierarchy and navigation | | | | | | |
| Window or space | | | | | | |
| Primary and alternate input | | | | | | |
| Accessibility behavior | | | | | | |
| System integration | | | | | | |
| Fallback or omission | | | | | | |

Include only supported targets. An honest omission is better than a token
companion that cannot complete a valuable task.
