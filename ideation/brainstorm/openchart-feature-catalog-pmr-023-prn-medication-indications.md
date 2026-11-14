# PRN Medication Indications — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures why and under what limits an as-needed medication is reportedly used.
Topics: openchart-feature-catalog, medical-records, frappe, prn-indications
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-023 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **PRN use diary linkage** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

Structured PRN indication and limits attached to an as-needed medication statement.

## Behavior

- Clinicians, nurses, pharmacists, patients, and caregivers open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are medication statement, coded indication, patient wording, minimum interval, maximum use, and effective dates.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are reported, reviewed, inactive; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces an indication-aware as-needed medication card and exposes unresolved items in list filters rather than hiding them.
- Edge handling: A PRN status without a known indication remains explicit and is queued for clarification rather than guessed.

## Frappe realization

- **DocTypes:** Extend or compose `OC Medication Statement` and add `OC PRN Indication` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Clinical Condition Code`, Table rows to `OC PRN Indication`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `reported, reviewed, inactive` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Medication%20Statement?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: structured prn indication and limits attached to an as-needed medication statement. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: an indication-aware as-needed medication card. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- Which maximum-use fields are safe to capture as reports rather than instructions?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
