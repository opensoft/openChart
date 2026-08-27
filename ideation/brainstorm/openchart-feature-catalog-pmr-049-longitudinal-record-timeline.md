# Longitudinal Record Timeline — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents problems, allergies, medications, vitals, devices, and histories on a provenance-aware patient timeline.
Topics: openchart-feature-catalog, medical-records, frappe, record-timeline
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-049 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Episode clustering** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

A read-only temporal composition of effective clinical records without becoming their source of truth.

## Behavior

- Clinicians, nurses, pharmacists, and authorized patients open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are patient, date range, record-family filters, effective events, source filters, and permission context.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are current-view, filtered-view, exported-view; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces an interactive timeline with drill-through to authoritative records and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Restricted records and superseded versions follow permissions and explicit display controls rather than disappearing without explanation.

## Frappe realization

- **DocTypes:** Extend or compose `OC Clinical Timeline View` and add `OC Timeline View Preference` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Clinical Record Family`, Table rows to `OC Timeline View Preference`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `current-view, filtered-view, exported-view` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Clinical%20Timeline%20View?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: a read-only temporal composition of effective clinical records without becoming their source of truth. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: an interactive timeline with drill-through to authoritative records. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- How should uncertain dates be positioned without implying false chronological precision?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
