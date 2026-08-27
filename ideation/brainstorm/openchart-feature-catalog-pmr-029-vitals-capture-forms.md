# Vitals Capture Forms — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides configurable forms for recording blood pressure, pulse, temperature, respiration, oxygen saturation, height, weight, and related observations.
Topics: openchart-feature-catalog, medical-records, frappe, vitals-capture
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-029 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Specialty-specific vital bundles** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

Fast structured vital-sign entry with units, method, position, encounter, and provenance.

## Behavior

- Nurses, medical assistants, clinicians, and authorized patients open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are patient, encounter, observation type, value, unit, time, method, body site or position, device, and recorder.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are draft, accepted, amended, entered-in-error; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces a grouped vital-sign panel and discrete observations and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Implausible values require confirmation or correction but remain distinguishable from clinically extreme valid values.

## Frappe realization

- **DocTypes:** Extend or compose `OC Observation Statement` and add `OC Vital Component` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Observation Code`, Table rows to `OC Vital Component`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `draft, accepted, amended, entered-in-error` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Observation%20Statement?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: fast structured vital-sign entry with units, method, position, encounter, and provenance. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: a grouped vital-sign panel and discrete observations. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- Which vital bundles should ship as defaults for ambulatory, pediatric, and inpatient contexts?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
