# Prescription Review And Signing — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents the complete prescription, safety findings, authority context, and destination for an accountable human signature before transmission.
Topics: openchart-feature-catalog, eprescribing, frappe, prescription-signing
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-010 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Batch review without batch signature** — A queue could streamline comparison while requiring an explicit signature act for each prescription.

## Focus

This feature isolates the ordinary, non-EPCS signing checkpoint. It makes the prescriber's reviewed facts and unresolved warnings visible at the exact moment authority is applied.

## Behavior

- The review screen freezes patient, medication, SIG, quantity, refills, indication, pharmacy, and benefit context into one preview.
- It lists safety checks with severity, evidence freshness, disposition, and any documented overrides.
- The system revalidates prescriber license scope, organization authority, patient identity, and destination immediately before signature.
- Material changes after review invalidate prior acknowledgements and require a fresh review.
- One deliberate signature action submits the prescription; unattended or delegated signing is prohibited.
- A signed digest, actor, authentication context, timestamp, and content version become immutable audit evidence.

## Frappe realization

- **DocTypes:** Submittable `OC Prescription` stores review snapshot, content digest, signer, signed time, and linked safety dispositions.
- **Workflow:** Draft → Clinical Review → Ready to Sign → Signed; only the signing transition sets docstatus 1 through a guarded API.
- **Roles/API:** `OC Prescriber` receives transition permission; `open_chart.api.v1.prescriptions.sign` revalidates authority and idempotency.
- **Surfaces/hooks:** A full-page Desk review, server `before_submit` validation, and immutable Version/audit events support accountable signing.

## Boundaries

Owns: human review and signature evidence. Consumes: prescription draft, authority, safety findings, and pharmacy choice. Emits: submitted prescription ready for routing. Does not own: authentication enrollment, EPCS ceremony, or autonomous approval.

## Open questions

- Which changes are material enough to invalidate prior safety acknowledgements?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [EPCS Two-Factor Signing Ceremony](openchart-feature-catalog-phr-011-epcs-two-factor-signing-ceremony.md)
