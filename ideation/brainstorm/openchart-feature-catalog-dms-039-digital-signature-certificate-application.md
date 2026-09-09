# Digital Signature Certificate Application — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Applies an authorized signer certificate to a finalized PDF and preserves signature intent, certificate chain, timestamp, validation, and revocation evidence.
Topics: openchart-feature-catalog, documents, frappe, pdf-signature
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-039 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Long-term validation package** — Embed or retain timestamp and revocation evidence needed to validate signatures after certificate expiry.

## Focus

This feature isolates cryptographic signing of an immutable exported PDF; it does not equate login identity with certificate authority automatically.

## Behavior

- An authorized signer opens a finalized PDF, reviews its checksum and purpose, and explicitly confirms signing intent.
- The system verifies signer role, certificate binding, validity period, permitted purpose, and document state.
- A signing service applies the certificate and trusted timestamp without exposing private key material to Frappe.
- The signed output is a new immutable File linked to the exact unsigned checksum and signature request.
- Validation stores certificate chain, signature coverage, timestamp, algorithms, and revocation-check result.
- Expired, revoked, mismatched, weak, unavailable, or partially covering signatures fail with specific status.
- Any content change after signing invalidates that output and requires a new version and signature request.

## Frappe realization

- **DocTypes:** `OC PDF Signature Request` (source_file, checksum, signer, purpose, certificate_alias, state) and `OC PDF Signature Evidence` (signed_file, chain JSON, timestamp, validation_result, revocation_checked_at).
- **Workflow:** Draft → Signer Review → Signing → Validated, with Declined, Failed, Invalid, and Superseded states.
- **Roles/permissions:** Certificate Signer acts only for bound purposes; Certificate Administrator manages aliases, not private keys; Auditor reads evidence.
- **API/jobs:** Guarded intent method plus RQ call to HSM/remote signing adapter; callbacks are signed and idempotent.
- **Surfaces:** PDF preview, certificate summary, validation badge, verification Print Format, and scheduled revocation recheck report.

## Boundaries

Owns: signature request, intent evidence, signed-output linkage, and validation record. Consumes: finalized PDF, signer authority, certificate service, and timestamp service. Emits: signed PDF and verification evidence. Does not own: private keys, certificate issuance, document authorship, or legal sufficiency determination.

## Open questions

- Which signature profiles and trusted timestamp authorities are required for initial jurisdictions and use cases?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Chain-of-custody Legal Export](openchart-feature-catalog-dms-040-chain-of-custody-legal-export.md)
