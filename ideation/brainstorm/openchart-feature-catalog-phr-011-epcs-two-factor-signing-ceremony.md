# EPCS Two-Factor Signing Ceremony — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Applies a controlled-substance-specific two-factor signing ceremony with authority, content, and authentication evidence bound to one prescription.
Topics: openchart-feature-catalog, eprescribing, frappe, epcs
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-011 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Authenticator assurance dashboard** — Compliance staff could monitor expiring, revoked, or weak authenticator enrollments without accessing clinical content.

## Focus

This feature isolates the high-assurance signature ceremony for controlled substances. It binds two distinct factors and the exact prescription digest while prohibiting background or delegated signing.

## Behavior

- The system detects that the medication schedule requires EPCS and routes to the dedicated ceremony.
- The prescriber reviews the full controlled-substance prescription and affirmatively confirms readiness to sign.
- A second factor from an approved authenticator is challenged in the same bounded session.
- License, DEA authority, schedule scope, enrollment status, and authenticator status are rechecked at signing time.
- Failure, timeout, factor replay, or content change aborts the ceremony without submitting or transmitting the prescription.
- Success stores tamper-evident factor class, assurance result, actor, timestamp, content digest, and authorization evidence without storing secrets.

## Frappe realization

- **DocTypes:** `OC EPCS Signing Event` is append-only and links submitted `OC Prescription`, authority snapshots, factor metadata, nonce, and digest.
- **Workflow/API:** `OC Prescription` enters EPCS Review → Factor Challenge → Signed; a guarded whitelisted method coordinates the ceremony and rejects generic submit.
- **Roles/permissions:** Only enrolled `OC EPCS Prescriber` users may transition; compliance roles can inspect assurance evidence at restricted permlevels.
- **Hooks/security:** `before_submit` enforces a fresh successful event, session-bound challenge state, replay prevention, and structured security logging.

## Boundaries

Owns: EPCS signature ceremony and assurance evidence. Consumes: identity proofing, credentials, authenticator, prescription digest, and schedule. Emits: legally accountable signature evidence. Does not own: authenticator secrets, DEA policy, or prescription clinical choice.

## Open questions

- Which authenticator types and assurance levels will each jurisdiction and network accept?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Prescriber Identity-Proofing Enrollment](openchart-feature-catalog-phr-012-prescriber-identity-proofing-enrollment.md)
