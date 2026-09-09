# Guarantor Relationship Management — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records who accepts financial responsibility for a patient and the evidence, scope, and dates of that relationship.
Topics: openchart-feature-catalog, registration, frappe, guarantor-relationships
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-014 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **External revenue-cycle handoff** — Export a purpose-limited guarantor snapshot to an authorized billing application.

## Focus

Represent guarantor authority in registration without making openChart the owner of balances or claims.

## Behavior

- Staff select the patient, a related person, or an organization as guarantor.
- The record captures relationship, responsibility scope, priority, effective dates, and attestation source.
- A minor can have multiple guarantors with explicit priority or shared responsibility.
- Conflicting active primary guarantors require supervisor review.
- Ending responsibility preserves the historic relationship used by prior registrations.
- Guarantor status does not automatically grant chart access, consent authority, or clinical disclosure.

## Frappe realization

- **DocTypes:** `OC Guarantor Relationship` with Dynamic Link guarantor, patient, scope, priority, validity, attestation, and status.
- **Workflow:** Draft → Pending Attestation → Active → Ended or Disputed.
- **Roles/permissions:** `OC Registration Clerk` prepares; `OC Registration Supervisor` resolves conflicts; financial fields at permlevel 1.
- **API/surfaces:** `open_chart.api.v1.registration.upsert_guarantor`; intake panel, relationship timeline, and guarded integration endpoint.

## Boundaries

Owns: guarantor identity and responsibility relationship. Consumes: related-person or organization identity and attestation. Emits: dated guarantor snapshot. Does not own: billing accounts, claims, or collections.

## Open questions

- What evidence is sufficient to activate a non-patient guarantor remotely?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
