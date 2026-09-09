# Guardian and Custody Authority — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records verified guardianship and custody authority with scope, evidence, dates, and disputes for safe registration decisions.
Topics: openchart-feature-catalog, registration, frappe, guardianship
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-029 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Authority-expiry alerts** — Notify accountable staff before temporary orders or delegated authority lapse.

## Focus

Establish who has legally supported authority for a patient without deriving it from kinship alone.

## Behavior

- Staff link a related person and record authority type, scope, jurisdiction, effective dates, and evidence.
- Authority remains Pending until an authorized reviewer verifies the evidence.
- Conflicting active custody claims place a prominent dispute warning and block unsupported proxy changes.
- Scope distinguishes registration, treatment consent, records access, and other configured powers.
- Expired or revoked authority is excluded from current decisions but preserved in history.
- Emergency exceptions record the policy basis and never silently activate a guardian.

## Frappe realization

- **DocTypes:** `OC Patient Authority` with related_person, authority_type, scope table, jurisdiction, private evidence, validity, and dispute state.
- **Workflow:** Draft → Evidence Review → Active, Rejected, or Disputed → Expired, Revoked, or Superseded.
- **Roles/permissions:** `OC Registration Clerk` submits; `OC Authority Reviewer` verifies; evidence uses permlevel 2; clinical users see scoped outcome.
- **API/surfaces:** `open_chart.api.v1.registration.submit_patient_authority`; authority panel, dispute queue, and expiring-authority report.

## Boundaries

Owns: documented guardianship and custody authority. Consumes: related-person identity and evidence. Emits: purpose-scoped authority decisions. Does not own: court proceedings or portal proxy implementation.

## Open questions

- Which evidence categories require legal or privacy-officer review rather than registration supervision?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
