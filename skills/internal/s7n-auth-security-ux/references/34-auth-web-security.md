# Auth and Web Security UX

Keep authentication, credential handling, and browser security policy separate from generic form design. Login flows are UI, but the source of truth is threat model, credential safety, recovery, and current platform guidance.

## Working Rules

- Treat passkeys and WebAuthn as security architecture plus product UX, not just form replacement.
- Design enrollment, fallback, recovery, device sync, and account-switching states deliberately.
- Use current OWASP, MDN, and browser guidance for concrete security headers and policies.
- Keep older explanatory security articles as context unless they match current header and browser behavior.
- Meet WCAG 2.2 Accessible Authentication requirements: avoid cognitive-function tests as the only login path, and support copy/paste, password managers, passkeys, and recovery alternatives.
- Keep authentication errors useful without leaking account existence, credential validity, or security posture to attackers.

## Accessible Authentication

Authentication must work for users who cannot memorize, transcribe, solve puzzles, or perform complex gestures under time pressure.

- Allow password managers and paste in username, password, one-time-code, and recovery-code fields unless a documented risk outweighs the accessibility and security benefit.
- Use `autocomplete` tokens such as `username`, `current-password`, `new-password`, and `one-time-code` accurately.
- Support passkeys/WebAuthn as a lower-friction option, but provide recovery and account-switching paths for device loss, shared devices, and unsynced authenticators.
- Avoid CAPTCHA or puzzle-only authentication. If abuse prevention is needed, provide accessible alternatives and server-side risk controls.
- Keep OTP entry tolerant: allow paste, accept spaces/hyphens where reasonable, auto-advance only when it does not trap correction, and expose one text-field fallback for split-code UIs.
- Make timeouts visible, extendable where safe, and recoverable without losing entered data.

## Security-Sensitive Copy

- Use calm, precise error messages: "We could not sign you in with those details" is safer than confirming whether the email exists.
- Tell users what changed after security-sensitive actions: password changed, passkey added, session revoked, recovery email sent.
- Warn before irreversible or high-risk actions, but prefer recovery/undo for reversible account settings changes.
- Do not display secrets, tokens, backup codes, or full identifiers after the first safe reveal. Provide copy/download flows with explicit user action.

## Browser Security UX Checks

- Secure-context-only features need a graceful fallback or clear environment requirement.
- Permission prompts should follow user intent and explanatory UI, not appear on page load.
- Session expiration should preserve unsaved work when possible and return users to the interrupted task.
- Cross-origin embeds, downloads, clipboard, camera, microphone, geolocation, and payment flows need browser-policy checks before UI promises are made.

## Additional Rules

- Passkeys/WebAuthn concepts, public/private key authentication, domain-bound phishing resistance, authenticator/WebAuthn/CTAP model, attestation/assertion/challenge flow, public-key storage, and API flow; connect to forms-ux for login, fallback, account recovery, and device-sync UX.
- API/code-oriented passkeys/WebAuthn explanation covering navigator.credentials.create/get, server challenge, PublicKeyCredential, attestation/assertion, clientDataJSON, origin/challenge validation, public-key storage, and signature verification; connect to forms-ux for login and recovery UX.
- Historical/explanatory overview of security response headers such as HSTS, CSP, X-Frame-Options/frame-ancestors, X-Content-Type-Options, Referrer-Policy, cookie flags, and older headers; use as context only, because concrete rules must be based on current OWASP/MDN/scanner guidance due to header drift, deprecation, replacement, and context-specific policy tradeoffs.
