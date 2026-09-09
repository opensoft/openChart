# Kiosk Registration Flow — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides a privacy-preserving shared-device registration flow that returns submitted information to staff review and reliably clears each session.
Topics: openchart-feature-catalog, registration, frappe, kiosk-registration
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-043 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Assisted-mode handoff** — Let a patient summon authorized staff without leaving sensitive responses visible.

## Focus

Adapt registration intake to a shared, unattended device with stronger session and privacy constraints.

## Behavior

- A patient begins using a single-use code, QR token, or staff-issued session that reveals no other patient data.
- Large controls, timeout warnings, accessibility options, and language selection support independent use.
- The flow allows document and photo capture only after purpose notice and confirmation.
- Timeout, cancellation, submission, or browser restart clears local data and invalidates the kiosk token.
- A privacy screen masks sensitive fields and prevents back-navigation into the previous session.
- Submission enters the staff review queue and does not mark arrival or alter the chart unless configured hooks succeed.

## Frappe realization

- **DocTypes:** `OC Kiosk Session` with token digest, kiosk_device, facility, intake, expiry, state, and cleanup confirmation.
- **Workflow:** Issued → Active → Submitted, Timed Out, Canceled, or Failed → Purged.
- **Roles/permissions:** Guest methods are token-scoped; `OC Registration Clerk` issues sessions; `OC Kiosk Administrator` manages device registrations.
- **API/surfaces:** `www/kiosk-registration` and `open_chart.api.v1.registration.start_kiosk_session`; kiosk-mode CSS, no-cache headers, and worklist receipt.

## Boundaries

Owns: shared-device session security and kiosk intake channel. Consumes: one-time authorization and registration schema. Emits: reviewable intake and cleanup audit. Does not own: check-in status or identity acceptance.

## Open questions

- What offline fallback is safe when a kiosk loses connectivity mid-session?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
