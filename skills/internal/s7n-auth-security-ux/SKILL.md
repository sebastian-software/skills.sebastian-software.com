---
name: s7n-auth-security-ux
description: |
  Authentication UX, security-sensitive web flows, passkeys, password forms, session timeout, permission prompts, browser security constraints, and user-facing security decisions. Use when implementing login, signup, account recovery, 2FA, passkeys, permission requests, or security messaging in frontend UI.
license: MIT
metadata:
  author: sebastian-software
  version: "1.0"
---

# S7N Auth & Security UX

Use this skill for user-facing security flows where clarity, trust, and browser constraints matter.

## Workflow

1. Identify the security goal, user risk, attacker-relevant surface, and recovery path.
2. Make the safe path the easiest path without hiding important consequences.
3. Use browser-native capabilities for credentials, autocomplete, permissions, and secure context requirements.
4. Explain interruptions only when the user needs to decide or recover.
5. Verify accessibility, password manager compatibility, and failure states.

## Rules

- Do not block password managers or paste unless there is a documented security requirement.
- Recovery flows are part of auth UX, not an afterthought.
- Security copy should be precise, calm, and free of vague reassurance.
- Permission prompts need context before the browser prompt appears.
- Avoid leaking sensitive state through overly specific public error messages.

## References

- [references/34-auth-web-security.md](references/34-auth-web-security.md) - auth UX, browser security, and sensitive frontend flow rules.
