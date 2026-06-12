# Auth and Web Security UX

Keep authentication, credential handling, and browser security policy separate from generic form design. Login flows are UI, but the source of truth is threat model, credential safety, recovery, and current platform guidance.

## Working Rules

- Treat passkeys and WebAuthn as security architecture plus product UX, not just form replacement.
- Design enrollment, fallback, recovery, device sync, and account-switching states deliberately.
- Use current OWASP, MDN, and browser guidance for concrete security headers and policies.
- Keep older explanatory security articles as context unless they match current header and browser behavior.

## Source-Backed Guidance

### www.smashingmagazine.com/2023/10/passkeys-explainer-future-password

- Things ID(s): `EQSwrzoCqtcV3cNsDbwiJy`
- Source: <https://www.smashingmagazine.com/2023/10/passkeys-explainer-future-password-less-authentication/>
- Decision: `primary`
- Target: `auth-security`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for auth-security: passkeys/WebAuthn concepts, public/private key authentication, domain-bound phishing resistance, authenticator/WebAuthn/CTAP model, attestation/assertion/challenge flow, public-key storage, and API flow; cross-reference forms-ux for login, fallback, account recovery, and device-sync UX.

### Passkeys: What the Heck and Why?

- Things ID(s): `FDLiaaQoUdiKS77TGNSrv6`
- Source: <https://css-tricks.com/passkeys-what-the-heck-and-why/>
- Decision: `secondary`
- Target: `auth-security`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for auth-security, linked to source 30 as technical supplement: API/code-oriented passkeys/WebAuthn explanation covering navigator.credentials.create/get, server challenge, PublicKeyCredential, attestation/assertion, clientDataJSON, origin/challenge validation, public-key storage, and signature verification; cross-reference forms-ux for login and recovery UX.

### Sichere Server durch Header

- Things ID(s): `GFfTZrYzLTvUKPhvfbtNzA`
- Source: <https://www.smashingmagazine.com/2017/04/secure-web-app-http-headers/>
- Decision: `secondary`
- Target: `web-security`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for web-security: useful historical/explanatory overview of security response headers such as HSTS, CSP, X-Frame-Options/frame-ancestors, X-Content-Type-Options, Referrer-Policy, cookie flags, and older headers; use as context only, because concrete rules must be based on current OWASP/MDN/scanner guidance due to header drift, deprecation, replacement, and context-specific policy tradeoffs.

