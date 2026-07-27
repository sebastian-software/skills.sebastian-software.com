# System Integration and Review

Use this reference for permissions, notifications, widgets or other system
surfaces, availability, deployment targets, fallbacks, and final review.

## Request Permission in Context

Before requesting access:

1. Confirm the feature needs the data or capability now.
2. Minimize scope, duration, precision, and retained data.
3. Explain the immediate user benefit in plain language.
4. Trigger the system request from the action that needs it.
5. Define behavior for not determined, allowed, limited, restricted, denied,
   unavailable, and later-revoked states where the capability exposes them.
6. Offer a useful manual, deferred, or reduced-capability path.

Do not bundle unrelated requests at first launch, imitate the system prompt,
mislead people about consequences, or repeatedly block the product after
decline. Link to system settings only when a person intentionally retries a
feature and changing access is the appropriate next step.

Treat permission copy, privacy manifests, usage descriptions, entitlements, and
platform policies as version-sensitive. Verify current official requirements
for the exact capability and target before implementation or approval.

## Design Trustworthy Notifications

Use a notification when information is timely, personally valuable, and useful
outside the app.

- Ask for consent in context after the benefit is understandable.
- Keep title and body concise and actionable.
- Avoid sensitive details that can appear on a lock screen or shared display.
- Provide meaningful actions only when they can complete safely from the
  notification context.
- Avoid duplicate, generic, nagging, or task-list notifications.
- Handle foreground delivery without repeating what the visible interface
  already communicates.
- Respect system settings, focus modes, delivery decisions, and revocation.

Define the source event, deduplication, timing, expiry, deep-link destination,
authorization state, and in-app equivalent. A notification cannot be the only
way to discover durable information.

## Select System Integrations by Value

Consider current platform surfaces such as widgets, complications, shortcuts,
search, sharing, drag and drop, handoff or continuity, live activities, menu
commands, document handling, or spatial scenes only when they reduce effort or
keep important state available in context.

For each integration, state:

- user outcome and entry context;
- data freshness, privacy, and authentication behavior;
- deep-link and state-restoration destination;
- unavailable, offline, signed-out, and stale behavior;
- platform and deployment availability; and
- a path to the same important outcome without the integration.

Do not add a system surface merely to claim platform completeness.

## Verify Availability and Fallbacks

Never infer support from the SDK compiling on the development machine.

1. Inspect every target's actual minimum deployment version and hardware scope.
2. Check current official Apple documentation for the API, component,
   capability, framework, and entitlement.
3. Separate compile-time SDK availability, runtime OS availability, device
   support, authorization, entitlement, account state, and service reachability.
4. Gate the enhancement at the correct boundary.
5. Design a fallback that preserves the core outcome, data integrity, and
   understandable state.
6. Build and launch the oldest supported target, exercise the unavailable path,
   and verify restoration, accessibility, localization, and analytics behavior.

Do not write a version number from memory. Do not make an optional enhancement
a hidden increase in the minimum supported OS. If no meaningful fallback
exists, make the higher deployment requirement an explicit product decision
owned by `product-management`.

## Run the Review Matrix

Cover the smallest matrix that can establish the claims:

- every supported platform and minimum deployment version;
- compact, intermediate, and expansive windows where applicable;
- portrait and landscape where supported;
- light, dark, elevated, transparent, or spatial appearances where applicable;
- default and accessibility text sizes or current platform equivalent;
- VoiceOver, reduced motion, keyboard-only, pointer, touch, and platform inputs;
- first run, returning, signed out, offline, denied permission, interrupted,
  loading, empty, stale, error, recovery, and completed state;
- realistic long localized content and sensitive-content contexts; and
- representative hardware for behavior a simulator cannot establish.

Record the environment and evidence for every pass. Do not collapse inspection,
preview, simulator, automated test, and hardware observation into one
“verified” label.

## Stop or Escalate

Stop approval when:

- current official support or requirements remain unverified;
- the fallback loses the core outcome or corrupts state;
- an essential action has no accessible alternative;
- a permission denial makes unrelated product value unusable;
- a Watch or Vision experience creates avoidable physical, motion, attention,
  or privacy risk;
- signing, entitlements, distribution, store policy, or specialist legal and
  security questions determine feasibility.

Return the unresolved decision to its owner instead of disguising it as a
design detail.
