# Long Term Medication Monitoring Plans — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Defines reviewable laboratory and clinical monitoring schedules associated with long-term medication use.
Topics: openchart-feature-catalog, medical-records, frappe, medication-monitoring
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-024 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Protocol templates by medication class** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

A monitoring plan linked to medication statements that creates due flags but no autonomous orders.

## Behavior

- Clinicians and pharmacists open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are medication, monitoring test code, cadence, start and end dates, responsible role, target, and rationale.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are draft, active, paused, completed, cancelled; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces a due-date schedule and explainable monitoring status and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Overdue or unavailable results create a review flag and never infer medication discontinuation.

## Frappe realization

- **DocTypes:** Extend or compose `OC Medication Monitoring Plan` and add `OC Monitoring Schedule Item` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Monitoring Test Code`, Table rows to `OC Monitoring Schedule Item`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `draft, active, paused, completed, cancelled` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Medication%20Monitoring%20Plan?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: a monitoring plan linked to medication statements that creates due flags but no autonomous orders. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: a due-date schedule and explainable monitoring status. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- Who owns plan maintenance when several clinicians share longitudinal care?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
