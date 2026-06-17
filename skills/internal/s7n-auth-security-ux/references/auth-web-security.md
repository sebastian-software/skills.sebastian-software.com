# Auth and Web Security UX

Authentication is UI on the surface, but its source of truth is the threat model:
credential safety, phishing resistance, recovery, and current platform behavior.
Keep these concerns separate from generic form styling and decide them
deliberately.

## Passkeys and WebAuthn

Treat passkeys as the default modern credential and design them as product UX,
not just a password replacement.

- Offer passkeys as the primary path for new accounts; keep a password or email
  link only as fallback while adoption grows. Phishing resistance comes from the
  credential being bound to the origin, so never weaken that with a cross-domain
  workaround.
- Drive creation with `navigator.credentials.create()` and authentication with
  `navigator.credentials.get()`. The server issues a random challenge, and the
  client returns a `PublicKeyCredential`; verify the signature, origin, and
  challenge server-side before trusting an assertion. Never accept an assertion
  whose `clientDataJSON` origin or challenge does not match what the server
  issued.
- Prefer discoverable credentials (resident keys) with `autocomplete="webauthn"`
  on the username field so the browser can offer conditional UI ("passkey
  autofill") instead of forcing the user to type an identifier first.
- Design the full credential lifecycle, not only first login: enrollment,
  adding a second passkey, syncing across a provider, signing in on a new or
  borrowed device, and removing a lost authenticator. Each is a distinct screen
  with its own copy.
- Always provide a recovery path that does not require the original device.
  Passkeys remove password reset as a crutch, so recovery becomes a deliberate
  flow rather than an afterthought.

## Passwords and credential forms

When passwords remain (legacy, fallback, or shared accounts), keep them
manager-friendly.

- Use a single `type="password"` field with `autocomplete="current-password"`
  for login and `new-password` for signup. Do not split passwords across boxes
  or block paste — both break password managers and hurt accessibility.
- Let the browser and managers fill credentials: correct `type`, `name`,
  `autocomplete`, and a stable form structure matter more than custom widgets.
- Allow long passphrases and the full character set; validate against length and
  known-breach lists rather than composition rules that push users toward weak,
  predictable patterns.
- Offer a visible "show password" toggle with an accessible name and pressed
  state instead of masking that users cannot verify.

## Recovery, sessions, and re-authentication

- Treat account recovery as part of auth UX. Design what happens when the user
  loses the device, the email, or the second factor — and make the safe recovery
  path discoverable before the user is locked out.
- Match session lifetime to risk. Keep low-risk sessions long-lived; require
  fresh authentication (step-up) only for sensitive actions such as changing
  credentials, email, or payment details.
- On timeout, preserve the user's in-progress work and context where possible so
  re-authentication does not discard a half-finished task.

## Security response headers and secure context

These are the server-side guarantees the UI depends on; verify them with current
OWASP and MDN guidance rather than copying older header lists, which drift.

- Serve auth and any credentialed flow only over HTTPS in a secure context;
  WebAuthn and many platform capabilities require it.
- Send `Strict-Transport-Security` (HSTS) so the browser refuses downgrade.
- Define a `Content-Security-Policy` that constrains script sources; it is the
  primary defense against injected scripts stealing credentials or tokens.
- Use `frame-ancestors` in CSP (the modern replacement for `X-Frame-Options`) to
  prevent clickjacking of login and consent screens.
- Set `X-Content-Type-Options: nosniff` and a restrictive `Referrer-Policy` so
  URLs containing tokens or identifiers do not leak to third parties.
- Scope session cookies with `Secure`, `HttpOnly`, and an appropriate
  `SameSite` value; prefer short-lived tokens with rotation over long-lived
  bearer cookies.

## Permission prompts

- Give context before the browser's native prompt appears. Explain why the
  permission is needed and what the user gets, so the irreversible browser
  dialog is a confirmation, not a surprise.
- Request a permission at the moment of use, triggered by a clear user action,
  not on page load. A denied prompt is expensive to recover from.
- Design the denied and "ask again" states; never trap the user in a flow that
  only works if they accept.

## Security copy and error messaging

- Keep security copy precise and calm. Avoid vague reassurance ("your data is
  safe") and avoid alarming language that pushes users to disable protections.
- Do not leak sensitive state through overly specific public errors. Use a
  uniform "wrong email or password" rather than revealing which field was wrong,
  and do not confirm whether an account exists in public-facing flows.
- Reserve detailed, actionable messages for states the user can fix (expired
  code, locked account with a recovery link), and route security-relevant
  detail to logs, not the screen.

## Review checklist

- Is the safe path also the easiest path, without hiding consequences?
- Do passkey enrollment, fallback, recovery, and device-sync states all exist?
- Are credential forms compatible with password managers, autofill, and paste?
- Are server-side origin, challenge, and signature checks in place for WebAuthn?
- Do headers (HSTS, CSP with `frame-ancestors`, `nosniff`, referrer policy) and
  cookie flags match current OWASP/MDN guidance?
- Do permission prompts have in-product context and a designed denied state?
- Is public error copy free of account-existence and field-level leakage?
- Have keyboard and screen-reader flows been verified for every auth screen?
