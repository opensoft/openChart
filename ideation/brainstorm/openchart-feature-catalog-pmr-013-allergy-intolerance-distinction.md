# Allergy Versus Intolerance Distinction — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Separates immune-mediated allergy, non-allergic intolerance, adverse effect, and unknown assertions while preserving patient language.
Topics: openchart-feature-catalog, medical-records, frappe, allergy-intolerance
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-013 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Patient education prompts** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

A clinically meaningful assertion type that avoids presenting every unwanted effect as a true allergy.

## Behavior

- Clinicians, nurses, and pharmacists open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are substance, assertion type, patient wording, manifestation, certainty, and reviewer rationale.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are unknown, allergy, intolerance, adverse-effect; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces a visibly classified safety record and immutable reclassification history and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Reclassification creates a successor and keeps prior alert behavior traceable to its effective period.

## Frappe realization

- **DocTypes:** Extend or compose `OC Allergy Statement` and add `OC Allergy Classification History` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Allergy Assertion Type`, Table rows to `OC Allergy Classification History`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `unknown, allergy, intolerance, adverse-effect` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Allergy%20Statement?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: a clinically meaningful assertion type that avoids presenting every unwanted effect as a true allergy. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: a visibly classified safety record and immutable reclassification history. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- Should unknown assertions alert like allergies until reviewed, and at what interruptiveness?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
