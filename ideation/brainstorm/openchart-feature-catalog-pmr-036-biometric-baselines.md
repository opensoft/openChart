# Biometric Baselines — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets clinicians define effective-dated baseline ranges from selected observations for individualized comparison.
Topics: openchart-feature-catalog, medical-records, frappe, biometric-baselines
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-036 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Baseline drift review** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

A clinician-authored reference baseline separate from population thresholds and treatment targets.

## Behavior

- Clinicians open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are observation type, selected measurements, calculation window, baseline value or range, method, rationale, and effective dates.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are draft, active, superseded, retired; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces a source-traceable baseline displayed on trends and exposes unresolved items in list filters rather than hiding them.
- Edge handling: A baseline never suppresses extreme-value safety review and cannot be derived from rejected observations.

## Frappe realization

- **DocTypes:** Extend or compose `OC Biometric Baseline` and add `OC Baseline Source Observation` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Observation Code`, Table rows to `OC Baseline Source Observation`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `draft, active, superseded, retired` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Biometric%20Baseline?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: a clinician-authored reference baseline separate from population thresholds and treatment targets. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: a source-traceable baseline displayed on trends. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- When should the system suggest baseline review without autonomously changing it?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
