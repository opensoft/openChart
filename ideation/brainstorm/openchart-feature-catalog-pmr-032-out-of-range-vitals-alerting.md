# Out Of Range Vitals Alerting — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Evaluates accepted vital signs against context-aware thresholds and routes reviewable alerts without autonomous clinical action.
Topics: openchart-feature-catalog, medical-records, frappe, vital-alerts
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-032 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Repeat-measurement protocols** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

Explainable threshold alerts sensitive to age, setting, pregnancy context, method, and active target plans.

## Behavior

- Nurses, clinicians, and configured response teams open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are observation, threshold rule release, patient context, measurement method, alert recipient, and acknowledgement.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are new, acknowledged, escalated, resolved, invalid-measurement; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces a routed alert with evidence, acknowledgement, and resolution and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Missing context yields an indeterminate review flag rather than applying an unsafe generic threshold.

## Frappe realization

- **DocTypes:** Extend or compose `OC Vital Alert` and add `OC Vital Alert Evidence` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Vital Threshold Rule`, Table rows to `OC Vital Alert Evidence`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `new, acknowledged, escalated, resolved, invalid-measurement` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Vital%20Alert?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: explainable threshold alerts sensitive to age, setting, pregnancy context, method, and active target plans. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: a routed alert with evidence, acknowledgement, and resolution. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- Which alerts should interrupt data entry versus route asynchronously?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
