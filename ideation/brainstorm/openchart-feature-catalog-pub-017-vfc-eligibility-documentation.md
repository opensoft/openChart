# VFC Eligibility Documentation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Determines and records time-bounded Vaccines for Children eligibility with evidence, reason category, and administration-time snapshot.
Topics: openchart-feature-catalog, public-health, frappe, vfc-eligibility
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-017 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Eligibility recertification queue** — Flag expiring or incomplete eligibility before vaccination visits.

## Focus

A reviewable program-eligibility determination separate from insurance coverage and clinical need.

## Behavior

- Authorized staff assess age, program reason category, supporting evidence, effective period, and assessor.
- Results are eligible, not-eligible, indeterminate, or pending-evidence with explanation.
- The administration records an immutable eligibility snapshot and funding source used at that time.
- Changes create a successor determination and do not rewrite prior funded administrations.
- Missing evidence may permit a policy-defined pending state but cannot silently become eligible.
- Users outside vaccine-program roles see only the minimum eligibility status needed for workflow.

## Frappe realization

- **DocTypes:** Add submittable `OC VFC Eligibility Determination` with evidence Attach, category, dates, predecessor, and assessor fields.
- **Workflow:** Use draft, pending-evidence, accepted, superseded, expired, and entered-in-error states.
- **Permissions:** Entry for `OC Vaccine Program User`, acceptance for `OC Vaccine Program Manager`, and protected evidence at permlevel 1.
- **Hooks and surfaces:** Validate age/effective dates, snapshot on administration submit, and provide recertification Query Reports and Quick Entry.

## Boundaries

Owns: VFC eligibility determinations and snapshots. Consumes: demographics, evidence, and program policy. Emits: funding eligibility context. Does not own: insurance adjudication, billing, or vaccine clinical eligibility.

## Open questions

- Which pending-evidence exceptions are permissible in each program jurisdiction?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
