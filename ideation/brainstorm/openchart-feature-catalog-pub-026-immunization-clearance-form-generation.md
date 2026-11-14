# Immunization Clearance Form Generation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Generates school, camp, or work clearance forms from a reviewed immunization-status snapshot and template-specific requirements.
Topics: openchart-feature-catalog, public-health, frappe, immunization-clearance
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-026 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Recipient verification QR** — Verify document identity and revocation state without exposing the full chart.

## Focus

Purpose-bound clearance documents that state evidence and limitations rather than overclaiming health status.

## Behavior

- Authorized users select purpose, recipient, jurisdiction template, relevant date, and permitted disclosures.
- The preview shows included doses, source/verification labels, schedule assessment, exemptions, and unresolved gaps.
- A clinician must approve any clearance conclusion; staff may prepare but not sign it.
- Generated output records source versions, template version, signer, as-of time, and disclosure authority.
- Changed records do not rewrite issued forms; users may revoke and issue a successor.
- Missing required evidence produces an incomplete form or blocks signature according to template policy.

## Frappe realization

- **DocTypes:** Add `OC Immunization Clearance` with purpose, recipient, consent, status snapshot, template version, signature, and revocation fields.
- **Workflow:** Use prepared, clinical-review, issued, revoked, expired, and superseded states.
- **Permissions:** Preparation for clinical staff, signature for `OC Clinician`, and release constrained by consent and patient User Permissions.
- **Surfaces:** Use versioned Jinja Print Formats, Letter Heads, PDF generation, and an audited portal download endpoint.

## Boundaries

Owns: clearance snapshot, conclusion, and issued artifact. Consumes: immunization history, schedule result, exemptions, and disclosure authority. Emits: purpose-specific forms. Does not own: recipient acceptance policy.

## Open questions

- Which standard forms permit electronic signatures and verification links?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
