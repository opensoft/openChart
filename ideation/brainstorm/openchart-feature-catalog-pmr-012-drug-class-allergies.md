# Drug Class Allergies — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records allergies against medication classes and evaluates candidate drugs against governed class membership.
Topics: openchart-feature-catalog, medical-records, frappe, drug-class-allergy
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-012 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Cross-reactivity review support** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

Class-level allergy representation without expanding it into unsupported ingredient-specific assertions.

## Behavior

- Clinicians and pharmacists open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are allergy statement, drug-class code, terminology release, exceptions, and verification provenance.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are unverified, confirmed, inactive; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces class allergy badges and explainable medication-match results and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Class membership changes are release-versioned and never retroactively alter the original assertion.

## Frappe realization

- **DocTypes:** Extend or compose `OC Allergy Statement` and add `OC Allergy Class Exception` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Medication Class Code`, Table rows to `OC Allergy Class Exception`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `unverified, confirmed, inactive` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Allergy%20Statement?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: class-level allergy representation without expanding it into unsupported ingredient-specific assertions. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: class allergy badges and explainable medication-match results. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- Which class hierarchies are clinically safe for alert matching at each site?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
