# Structured Social History — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures living situation, occupation, education, relationships, activity, nutrition, safety, and other social context as effective-dated statements.
Topics: openchart-feature-catalog, medical-records, frappe, social-history
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-044 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Configurable social-needs instruments** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

Modular social-history assertions with provenance and privacy controls rather than one mutable narrative blob.

## Behavior

- Patients, caregivers, clinicians, social workers, and intake staff open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are topic code, coded value, patient wording, effective interval, reporter, verification status, and privacy flags.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are reported, reviewed, inactive, restricted, entered-in-error; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces a topic-grouped longitudinal social history and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Sensitive topics can be restricted independently and declined answers never become negative findings.

## Frappe realization

- **DocTypes:** Extend or compose `OC Social History Statement` and add `OC Social History Attribute` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Social History Topic`, Table rows to `OC Social History Attribute`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `reported, reviewed, inactive, restricted, entered-in-error` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Social%20History%20Statement?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: modular social-history assertions with provenance and privacy controls rather than one mutable narrative blob. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: a topic-grouped longitudinal social history. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- Which topics belong in core openChart versus locally configured extensions?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
