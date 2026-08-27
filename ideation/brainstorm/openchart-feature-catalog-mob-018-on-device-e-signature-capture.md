# On-Device E-Signature Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures an attributable on-device signature ceremony bound to a specific document version, signer role, disclosure, and consent context.
Topics: openchart-feature-catalog, mobile-devices, frappe, e-signature
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-018 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Witness co-sign ceremony** — Capture a separately authenticated witness attestation where policy requires it.

## Focus

This entry isolates signature intent and evidence rather than equating a drawn mark with identity or legal validity.

## Behavior

- The signer reviews the exact document version, required disclosure, signer capacity, and alternatives before signing.
- Staff select patient, representative, clinician, or witness capacity and record identity-verification method.
- The device captures a mark or typed acknowledgement plus explicit intent, time, actor, and document digest.
- Material document change invalidates the ceremony and requires a new signature.
- Declined, unable, interrupted, expired, and completed outcomes remain distinct.
- Offline signing is disabled unless a policy-issued document package and ceremony expiry permit it.
- A completed signature is immutable; correction creates succession evidence rather than replacing history.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create submittable `OC Signature Ceremony` with document Dynamic Link, digest, signer, capacity, disclosure version, verification method, outcome, and successor.
- **Workflow and roles:** Prepared → Presented → Signed/Declined/Unable/Expired/Voided; presenter, signer proxy, witness, and compliance reviewer permissions are separate.
- **API and auth:** Token-authenticated `open_chart.api.v1.mobile.signature.prepare` and `complete` verify current digest and use idempotent guarded submission.
- **Realtime and jobs:** Websocket events update ceremony status; server-side RQ jobs render signed copies, expire packages, and notify accountable reviewers.
- **Files and surfaces:** Signature marks and rendered copies use private Frappe file attachment APIs, digest binding, restricted download, and versioned Print Formats.

## Boundaries

Owns: ceremony, intent, signature evidence, and document binding. Consumes: identity verification, document version, capacity, and disclosure. Emits: immutable signature record. Does not own: legal interpretation or biometric identity proof.

## Open questions

- Which document types permit offline ceremony packages and for how long?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
