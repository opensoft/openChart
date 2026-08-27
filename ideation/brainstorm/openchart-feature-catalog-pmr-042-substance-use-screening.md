# Substance Use Screening — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures coded non-tobacco substance use, route, frequency, recency, screening responses, and patient-reported provenance.
Topics: openchart-feature-catalog, medical-records, frappe, substance-screening
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-042 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Consent-scoped referral prompts** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

A privacy-aware, nonjudgmental screening record distinct from confirmed substance-related diagnoses.

## Behavior

- Patients and specifically authorized clinical staff open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are substance category, use status, route, frequency, last use, instrument responses, reporter, consent, and privacy flags.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are complete, incomplete, declined, restricted, amended; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces a permission-aware screening summary and history and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Restricted responses honor role and user permissions and are not exposed through generic chart summaries.

## Frappe realization

- **DocTypes:** Extend or compose `OC Social History Statement` and add `OC Substance Use Detail` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Substance Use Code`, Table rows to `OC Substance Use Detail`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `complete, incomplete, declined, restricted, amended` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Social%20History%20Statement?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: a privacy-aware, nonjudgmental screening record distinct from confirmed substance-related diagnoses. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: a permission-aware screening summary and history. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- Should individual substance categories support separately restricted visibility?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
