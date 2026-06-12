# Auth and Web Security UX

Keep authentication, credential handling, and browser security policy separate from generic form design. Login flows are UI, but the source of truth is threat model, credential safety, recovery, and current platform guidance.

## Working Rules

- Treat passkeys and WebAuthn as security architecture plus product UX, not just form replacement.
- Design enrollment, fallback, recovery, device sync, and account-switching states deliberately.
- Use current OWASP, MDN, and browser guidance for concrete security headers and policies.
- Keep older explanatory security articles as context unless they match current header and browser behavior.

## Source-Backed Guidance

