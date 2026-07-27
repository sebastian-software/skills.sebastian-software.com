[← Sebastian Software Skills](../../README.md)

# Apple Platform Design

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Keep one product coherent across Apple platforms without flattening their
different windows, spaces, inputs, accessibility needs, and usage contexts.**

Apple Platform Design helps agents shape native iPhone and iPad experiences,
then make purposeful adaptations for Mac, Apple Watch, and Apple Vision Pro. It
connects navigation and layout with accessibility, permissions, notifications,
system integration, deployment targets, and verifiable fallback behavior.

## What It Can Deliver

- platform and deployment-target matrices
- native navigation, layout, window, and spatial-scene models
- explicit iPhone, iPad, Mac, Watch, and Vision Pro adaptations
- touch, keyboard, pointer, Pencil, Crown, voice, switch, and spatial input plans
- Dynamic Type, VoiceOver, reduced-motion, and focus behavior
- permission, notification, system-integration, and degraded-state designs
- device and accessibility review matrices with evidence gaps

## Use It When

Use this skill for a new native iOS or iPadOS experience, an iPhone interface
that must become a real iPad or Mac product, a concise Watch companion, a
visionOS adaptation, an accessibility review, or a feature that needs honest
behavior on older deployment targets.

## Example Prompts

```text
Turn this iPhone workflow into an iPad workspace that works in narrow and wide
windows with touch, keyboard, pointer, and Apple Pencil.

Review this native flow with accessibility text sizes, VoiceOver, reduced
motion, keyboard navigation, denied permissions, and interrupted state.

Adapt these two useful tasks for Apple Watch without copying the full phone
hierarchy or requiring the phone for every interaction.

This feature uses a newer platform capability but our deployment target is
older. Verify current official availability and design a meaningful fallback.

Decide whether this visionOS experience needs a window, volume, or immersive
space, and preserve comfort and a non-immersive path.
```

See [SKILL.md](SKILL.md) for the complete native design, adaptation,
accessibility, integration, and review workflow.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill apple-platform-design
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian apple-platform-design
dalo approve skill sebastian:apple-platform-design
dalo sync
```

## Related Skills

- [Product Design](../product-design/README.md) owns research synthesis, problem
  framing, interaction modeling, and prototypes before native platform
  adaptation becomes the central question.
- [Product Management](../product-management/README.md) decides audience,
  outcomes, viability, platform scope, prioritization, and release direction.
- [Effective Web](../effective-web/README.md) owns the browser counterpart,
  responsive web behavior, web accessibility, and frontend implementation.
- [Software Architecture](../software-architecture/README.md) owns system
  boundaries and operational architecture behind the native experience.
- [Decision Records](../decision-records/README.md) preserves consequential
  cross-platform design decisions and reopening conditions.

## Scope

This skill covers experience design and review for native Apple platforms. It
does not provide general Swift architecture, framework or package design,
signing, provisioning, notarization, App Store submission, release automation,
store operations, or legal and policy advice. Changing platform capabilities
and requirements must be checked against current official Apple documentation
during the task.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
