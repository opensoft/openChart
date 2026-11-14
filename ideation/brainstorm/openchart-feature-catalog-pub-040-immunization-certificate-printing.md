# Immunization Certificate Printing — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Produces signed, versioned immunization certificates and yellow-card-style records from selected verified history.
Topics: openchart-feature-catalog, public-health, frappe, immunization-certificate
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-040 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Tamper-evident verification** — Add a privacy-preserving signature and revocation lookup to issued certificates.

## Focus

A portable, as-of immunization record with selected doses, source labels, issuer identity, and artifact provenance.

## Behavior

- Authorized users select certificate format, purpose, recipient, language, as-of date, and included dose history.
- Unverified, invalid, or disputed doses are excluded by default and require explicit policy-approved labeling to include.
- The preview shows product/CVX, dates, lot details when appropriate, source, and issuer attestation.
- Issuance records signer, template version, source record versions, disclosure authority, and artifact digest.
- Later corrections do not alter the issued file; users revoke and issue a successor certificate.
- Missing mandatory fields block issuance and identify the exact history items needing review.

## Frappe realization

- **DocTypes:** Add submittable `OC Immunization Certificate` with selected-dose child rows, source digests, signer, recipient, purpose, expiry, and revocation fields.
- **Workflow:** Use prepared, signer-review, issued, revoked, expired, and superseded states.
- **Permissions:** Clinical staff prepare; `OC Clinician` or `OC Authorized Immunization Signer` issues; portal access follows patient/proxy authority.
- **Surfaces:** Provide versioned Jinja Print Formats for standard and yellow-card layouts, PDF generation, QR hooks, and audited download API.

## Boundaries

Owns: certificate snapshot, issuance, and revocation. Consumes: verified immunization history, consent, template, and signer authority. Emits: portable certificate artifacts. Does not own: destination acceptance rules or identity credentials.

## Open questions

- Which international certificate layouts and signatures can be implemented without proprietary content?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
