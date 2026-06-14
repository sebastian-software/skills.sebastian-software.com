# Auth and Web Security UX

Keep authentication, credential handling, and browser security policy separate from generic form design. Login flows are UI, but the source of truth is threat model, credential safety, recovery, and current platform guidance.

## Working Rules

- Treat passkeys and WebAuthn as security architecture plus product UX, not just form replacement.
- Design enrollment, fallback, recovery, device sync, and account-switching states deliberately.
- Use current OWASP, MDN, and browser guidance for concrete security headers and policies.
- Keep older explanatory security articles as context unless they match current header and browser behavior.

## Additional Rules

- Passkeys/WebAuthn concepts, public/private key authentication, domain-bound phishing resistance, authenticator/WebAuthn/CTAP model, attestation/assertion/challenge flow, public-key storage, and API flow; connect to forms-ux for login, fallback, account recovery, and device-sync UX.
- API/code-oriented passkeys/WebAuthn explanation covering navigator.credentials.create/get, server challenge, PublicKeyCredential, attestation/assertion, clientDataJSON, origin/challenge validation, public-key storage, and signature verification; connect to forms-ux for login and recovery UX.
- Historical/explanatory overview of security response headers such as HSTS, CSP, X-Frame-Options/frame-ancestors, X-Content-Type-Options, Referrer-Policy, cookie flags, and older headers; use as context only, because concrete rules must be based on current OWASP/MDN/scanner guidance due to header drift, deprecation, replacement, and context-specific policy tradeoffs.
