# Insurance Coverage Intake — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures patient-reported coverage records with dates, payer identity, order, and provenance for downstream administrative use.
Topics: openchart-feature-catalog, registration, frappe, coverage-intake
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-023 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Coverage coordination preview** — Explain apparent primary, secondary, and tertiary ordering before handoff.

## Focus

Record insurance coverage facts at registration without performing eligibility or claims functions.

## Behavior

- Staff add payer, plan, member identifier, group, coverage type, order, and effective dates.
- Member identifiers are masked in routine displays and searchable only through guarded exact match.
- Multiple active coverages are allowed with explicit coordination order and unknown-order state.
- Missing payer directory matches can be held as unverified free text for worklist resolution.
- Expired coverage remains historically linked to the registrations where it was presented.
- Acceptance records whether data was patient-reported, card-derived, imported, or staff-confirmed.

## Frappe realization

- **DocTypes:** `OC Patient Coverage` with payer link, plan, masked member ID, encrypted value, group, type, order, validity, and source.
- **Workflow:** Draft → Review Pending → Active, Unverified, or Rejected → Expired or Superseded.
- **Roles/permissions:** `OC Registration Clerk` captures; `OC Coverage Reviewer` resolves; identifiers use permlevel 2 and field masking.
- **API/surfaces:** `open_chart.api.v1.registration.upsert_coverage`; registration coverage grid, patient summary card, and unresolved-payer report.

## Boundaries

Owns: patient-reported coverage registration facts. Consumes: payer directory and source evidence. Emits: dated coverage snapshot. Does not own: eligibility, claims, benefits, or financial estimates.

## Open questions

- Which identifier fields require encryption in addition to Frappe private-field controls?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
