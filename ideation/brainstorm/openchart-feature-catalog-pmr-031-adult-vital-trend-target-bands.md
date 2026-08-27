# Adult Vital Trend Charts With Target Bands — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Charts longitudinal adult vital signs against clinician-defined or policy-derived target bands.
Topics: openchart-feature-catalog, medical-records, frappe, adult-vital-trends
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-031 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Event annotations on trends** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

An interactive trend view that separates measured values from contextual targets.

## Behavior

- Clinicians, nurses, and patients with portal access open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are accepted observations, date range, aggregation choice, target-band source, and display units.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are current, historical, target-changed; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces filterable trend charts with source-labeled target bands and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Target changes are effective-dated and never recolor historical periods as though the prior target did not exist.

## Frappe realization

- **DocTypes:** Extend or compose `OC Vital Target Plan` and add `OC Vital Target Band` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Observation Code`, Table rows to `OC Vital Target Band`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `current, historical, target-changed` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Vital%20Target%20Plan?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: an interactive trend view that separates measured values from contextual targets. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: filterable trend charts with source-labeled target bands. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- May patients define personal display goals distinct from clinician-authored targets?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
