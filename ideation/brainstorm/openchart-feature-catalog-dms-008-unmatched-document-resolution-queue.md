# Unmatched-document Resolution Queue — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Holds documents without a safe patient match in a restricted queue until an authorized reviewer resolves or rejects the association.
Topics: openchart-feature-catalog, documents, frappe, unmatched-resolution
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-008 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Sender clarification request** — Generate a minimum-necessary inquiry when source identifiers cannot resolve the patient.

## Focus

This feature isolates safe exception handling for documents whose patient identity is absent, ambiguous, or contradictory.

## Behavior

- Any ingest path creates an unmatched case when no single patient association meets policy.
- Patient Identity Reviewers see source identifiers, candidate patients, conflict reasons, and the original document in a restricted workspace.
- Reviewers may link an existing patient, register an approved external identifier, return to sender, or reject as non-patient material.
- Creating a new patient from the queue is never implicit and requires the governed registration workflow.
- Candidate searches and viewed records are audited because they expose identity information.
- Cases remain quarantined from the clinical chart and ordinary full-text search until resolved.
- Resolution records evidence and reviewer; reopening creates a new decision event rather than erasing the prior one.

## Frappe realization

- **DocTypes:** `OC Unmatched Document Case` (source_file, source_identifiers JSON, reason, state, resolved_patient, resolution_basis) with child `OC Patient Match Candidate`.
- **Workflow:** Unmatched → Investigating → Resolved, with Clarification Requested, Returned, and Rejected states.
- **Roles/permissions:** Patient Identity Reviewer has permlevel 1 access to identifiers; ordinary document users cannot list cases or source Files.
- **API/surfaces:** Guarded `open_chart.api.v1.documents.resolve_unmatched` requires reason and evidence; a Desk workspace provides candidate comparison and an aging Script Report.
- **Hooks:** `open_chart.documents.on_file` enforces quarantine attachment targets until the case reaches Resolved.

## Boundaries

Owns: unmatched case, candidate evidence, quarantine, and resolution decision. Consumes: source identifiers and patient-search projection. Emits: verified patient association or terminal rejection. Does not own: patient merge, patient registration, or OCR extraction.

## Open questions

- What evidence threshold permits linking when external records contain stale demographics?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [OCR-assisted Indexing Suggestions](openchart-feature-catalog-dms-006-ocr-assisted-indexing-suggestions.md)
