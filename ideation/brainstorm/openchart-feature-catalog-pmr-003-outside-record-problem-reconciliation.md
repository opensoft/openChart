# Outside Record Problem Reconciliation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets clinicians compare imported outside problems with the local list and accept, reject, map, or defer each candidate.
Topics: openchart-feature-catalog, medical-records, frappe, problem-reconciliation
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-003 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Selective auto-suggested matching** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

Item-by-item reconciliation that preserves source provenance and local clinical authority.

## Behavior

- Clinicians and designated reconciliation staff open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are outside document reference, candidate wording and code, local matches, source date, and reconciliation note.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are unreviewed, matched, accepted, rejected, deferred; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces a signed reconciliation result and any authorized successor condition statements and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Conflicting candidates stay side-by-side and cannot silently replace a locally confirmed condition.

## Frappe realization

- **DocTypes:** Extend or compose `OC Problem Reconciliation` and add `OC Problem Reconciliation Item` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Reconciliation Disposition`, Table rows to `OC Problem Reconciliation Item`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `unreviewed, matched, accepted, rejected, deferred` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Problem%20Reconciliation?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: item-by-item reconciliation that preserves source provenance and local clinical authority. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: a signed reconciliation result and any authorized successor condition statements. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- When may a trusted source pre-populate a recommended disposition without auto-accepting it?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
