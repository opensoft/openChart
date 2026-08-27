# Pediatric Growth Percentiles — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Calculates and charts age- and sex-reference percentiles for pediatric height, weight, BMI, and head circumference.
Topics: openchart-feature-catalog, medical-records, frappe, pediatric-growth
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-030 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Preterm age adjustment** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

Versioned growth-reference calculations over accepted observations with transparent reference metadata.

## Behavior

- Pediatric clinicians, nurses, and caregivers open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are patient birth data, applicable sex parameter, measurement time, accepted observations, and growth-reference release.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are calculable, insufficient-data, out-of-range-age, superseded-reference; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces percentile values and an interactive growth chart and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Missing or conflicting demographic inputs suppress percentile calculation rather than guessing.

## Frappe realization

- **DocTypes:** Extend or compose `OC Growth Assessment` and add `OC Growth Percentile Result` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Growth Reference Release`, Table rows to `OC Growth Percentile Result`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `calculable, insufficient-data, out-of-range-age, superseded-reference` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Growth%20Assessment?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: versioned growth-reference calculations over accepted observations with transparent reference metadata. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: percentile values and an interactive growth chart. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- Which reference sets and demographic parameters should be configurable by jurisdiction?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
