# Accessibility and Input

Use this reference when reviewing text scaling, VoiceOver, motion, contrast,
focus, keyboard, pointer, touch, Pencil, Crown, switch, voice, or spatial input.
Treat accessibility as interaction behavior across states, not a visual
checklist.

## Define Semantic Structure

For every meaningful element, specify:

- role, concise accessible name, current value, and state;
- reading and focus order that follows the task;
- available actions, including custom and adjustable actions;
- grouping that preserves useful context without creating noisy repetition;
- announcements for consequential asynchronous changes; and
- error association, required state, and recovery instruction.

Do not encode type, state, or action only in an icon, location, color, sound,
animation, or visual grouping. Hide decorative elements from the accessibility
tree and keep useful content out of inaccessible drawings.

## Design for VoiceOver and Alternatives

Walk the complete task with the current platform's VoiceOver behavior:

1. Enter from each supported deep link or restored state.
2. Navigate in a logical order without sight.
3. Identify controls before activating them.
4. Change adjustable values and perform reorder, reveal, delete, or custom
   actions without a spatial gesture.
5. Hear validation, progress, completion, and errors at the right moment.
6. Escape modal or spatial contexts and return to the prior location.

Never prescribe a gesture as the only path. Provide visible and semantic
alternatives for drag, swipe, hover, Pencil, Crown, gaze, or direct spatial
manipulation.

## Support Text and Content Scaling

Use semantic text styles and flexible layout. On platforms that currently
support Dynamic Type, test the full supported range including accessibility
sizes. On platforms with different text-size or zoom behavior, verify the
current official mechanism and provide equivalent legibility rather than
claiming unsupported behavior.

- Reflow before truncating essential text.
- Let controls grow or rearrange with their labels.
- Avoid fixed-height containers around user-facing text.
- Preserve reading order when columns stack or controls move.
- Make meaningful icons scale where platform behavior calls for it.
- Test localized, long, bold, and mixed-content text.

Do not reduce a person's selected text size to protect a screenshot layout.

## Respect Motion and Sensory Preferences

Observe the current reduced-motion setting. Remove or replace parallax, depth
simulation, large translations, rapid zoom, autoplay, and unnecessary spatial
movement that can cause discomfort.

When motion conveys hierarchy or state, preserve the meaning with a lower-motion
transition, fade, highlight, or immediate state change. Keep controls available
when animation is disabled. Do not rely on sound or haptics for essential
information, and respect relevant contrast, transparency, differentiation,
caption, and audio-description needs.

## Support the Platform's Inputs

### Touch and Pencil

- Make targets forgiving and separated; verify current platform guidance rather
  than freezing one universal metric.
- Keep common actions reachable and prevent edge gestures from colliding with
  system behavior.
- Use Pencil for precision, drawing, annotation, or handwriting where it adds
  value; preserve a touch, keyboard, or control alternative for essential work.

### Keyboard and Pointer

- Provide logical focus order, visible focus, activation, escape, and standard
  text-editing behavior.
- Add shortcuts for frequent commands without making discovery depend on
  memorization.
- Use pointer and hover feedback as enhancement; do not hide required actions
  until hover.
- Distinguish focus, selection, activation, and current navigation location.

### Crown, Voice, Switch, Eyes, and Hands

- Map the Digital Crown to continuous or navigational adjustment with clear
  state and a touch alternative where appropriate.
- Give voice and switch users semantic, stable targets and non-time-critical
  completion paths.
- In visionOS, make gaze targets forgiving but never infer identity, intent, or
  consent merely from where a person looks.
- Support indirect eyes-and-hands interaction in a relaxed posture and avoid
  requiring prolonged direct manipulation or precise reach.

## Verify with an Evidence Matrix

For every supported platform and critical flow, record:

- device or simulator and OS version;
- window size, orientation, and relevant display context;
- text size, VoiceOver, reduced motion, contrast, and other relevant settings;
- touch, keyboard, pointer, Pencil, Crown, voice, switch, or spatial input used;
- result, defect, evidence artifact, and untested gap.

Use simulators and previews for breadth, then use representative hardware for
input, ergonomics, haptics, audio, camera or sensors, performance, comfort, and
other behavior simulation cannot establish.
