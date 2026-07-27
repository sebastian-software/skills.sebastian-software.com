---
name: apple-platform-design
description: >-
  Design, adapt, and review native Apple-platform experiences for iOS and
  iPadOS, with purposeful adaptations for macOS, watchOS, and visionOS. Use for
  native navigation, windows or spatial scenes, touch, keyboard, pointer, Apple
  Pencil, Digital Crown, eyes-and-hands input, Dynamic Type, VoiceOver, reduced
  motion, permissions, notifications, system integrations, cross-platform
  behavior, and deployment-target fallbacks. Verify changing platform
  capabilities and requirements against current official Apple guidance and
  documentation at runtime.
---

# Apple Platform Design

Turn one product intent into native experiences that preserve the same outcome
without pretending every Apple platform is a differently sized iPhone. Start
with iOS and iPadOS when they are the primary products, then adapt only the
valuable flows for the distinct context, window model, input, and attention
pattern of each additional platform.

## Workflow

1. Establish the supported matrix:
   - target platforms, devices, orientations, window or space modes
   - minimum deployment versions and required hardware
   - primary tasks, usage context, attention span, and continuity needs
   - input methods, accessibility settings, permissions, and offline states
   - supplied evidence, assumptions, implementation constraints, and non-goals
2. Separate the shared product outcome and information model from the
   platform-specific presentation. Do not infer that a shared codebase requires
   identical hierarchy, density, navigation, or controls.
3. Read [Apple design foundations](references/apple-design-foundations.md) for
   hierarchy, system conventions, adaptive layout, navigation, feedback,
   content priority, and state behavior.
4. Read [Platform adaptation](references/platform-adaptation.md) when a flow
   spans form factors or needs iPad windows, Mac desktop behavior, Watch
   glanceability, or visionOS windows, volumes, or immersive spaces.
5. Read [Accessibility and input](references/accessibility-and-input.md) for
   Dynamic Type or the current platform equivalent, VoiceOver, reduced motion,
   keyboard, pointer, Pencil, Crown, switch, voice, and spatial input.
6. Read [System integration and review](references/system-integration-and-review.md)
   for permissions, notifications, system surfaces, availability, deployment
   targets, fallbacks, and the device review matrix.
7. For any capability, API, component behavior, platform support claim,
   entitlement, or review requirement that may have changed, consult current
   official Apple design and developer documentation during the task. Record
   the checked platform, OS version, deployment target, date, and resulting
   decision in the working deliverable; do not create a source archive in this
   skill.
8. Produce a shared flow plus explicit platform deltas. Preserve the core task
   when a newer capability is unavailable; gate enhancement, not access to the
   product outcome.
9. Review realistic content and state across supported sizes, windows, inputs,
   accessibility settings, permission states, interruptions, and OS versions.
   Report what was exercised on hardware, simulator, preview, or inspection and
   keep unverified behavior visible.

## Operating Rules

- Prefer system components, semantic styles, and platform conventions before
  custom controls. Customize only for a product need that survives
  accessibility, input, localization, and state review.
- Keep navigation proportional to the platform and task. Preserve user
  orientation, restoration, selection, and deep-link destination across size
  and window changes.
- Design iPad as a flexible workspace, not a stretched phone. Account for
  freely changing window size and concurrent input methods without depending
  on one orientation or full-screen canvas.
- Design Mac adaptations for resizable windows, keyboard and pointer precision,
  menus, commands, file or document conventions where relevant, and long-lived
  work. Do not ship touch-sized duplication as desktop adaptation.
- Keep Watch flows glanceable, timely, and independently useful. Move deep
  authoring or prolonged attention to a more suitable platform.
- Start visionOS standard tasks in familiar windows. Add depth, volume, or
  immersion only when it materially improves the outcome, and protect visual
  comfort, physical safety, privacy, and non-spatial alternatives.
- Make every important action reachable without a single gesture or input
  mode. Hover, color, sound, motion, precise pointing, gaze, or drag alone
  cannot carry essential meaning or access.
- Ask for permission in context after explaining the immediate user benefit.
  Treat denied, restricted, limited, unavailable, and later-revoked access as
  ordinary states with a useful continuation.
- Send notifications only for timely user value, with consent and private
  lock-screen content. Never use repeated prompts or notifications to coerce
  engagement.
- Never claim accessibility, hardware support, API availability, or platform
  compliance from a static mockup or simulator-only happy path.

## Default Deliverable

Return the smallest decision-ready package containing:

1. platform and deployment-target matrix with facts, assumptions, and unknowns;
2. shared product outcome, objects, state, and primary flow;
3. navigation, window or space, layout, and input model for each target;
4. accessibility behavior and permission or notification state handling;
5. system integrations with their user value and non-integrated fallback;
6. availability guards and fallback behavior for older supported versions;
7. review matrix covering devices, sizes, inputs, settings, states, and evidence;
8. unresolved implementation, policy, hardware, or operational risks.

## Routing Boundaries

- Use `product-management` for audience, product strategy, business viability,
  outcomes, scope, prioritization, and release decisions.
- Use `product-design` for research synthesis, problem framing, object and
  interaction modeling, and prototypes before the Apple-platform expression is
  the primary decision. Return here for native adaptation and review.
- Use `effective-web` when the target is a browser experience, responsive web
  app, or website rather than a native Apple-platform surface.
- Use `software-architecture` for overall system boundaries, data ownership,
  service contracts, and operational architecture. General Swift architecture,
  framework selection, package structure, and concurrency implementation are
  outside this skill's design scope.
- Use `software-testing` for focused non-UI domain, service, persistence, and
  integration test evidence. This skill defines the native experience matrix
  and accessibility behavior but does not own a general native UI test stack.
- Use `decision-records` when a durable cross-platform design decision and its
  reopening conditions need to survive the current delivery.
- Signing, provisioning, certificates, notarization, release automation, App
  Store submission, commerce policy, and store operations remain outside this
  skill. Verify them with the appropriate current official requirements and
  qualified ownership.
