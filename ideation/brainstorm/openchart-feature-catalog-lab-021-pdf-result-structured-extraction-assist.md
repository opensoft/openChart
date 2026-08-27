# PDF Result Structured Extraction Assist — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Extracts candidate observations from laboratory PDFs for human verification while keeping the source document authoritative and attached.
Topics: openchart-feature-catalog, laboratory, frappe, document-extraction
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-021 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **PDF Result Structured Extraction Assist assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates assistive extraction and reviewer decisions as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Lab Result Filer supplies source PDF, page regions, extracted labels, values, units, ranges, confidence, and patient-match candidates.
- The system produces a review queue of source-linked structured candidates and exposes its current state to permitted users.
- The governed lifecycle is Uploaded → Extracted → Human Review → Accepted, Corrected, or Rejected; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Low confidence, ambiguous patient identity, handwritten content, and conflicting values require explicit correction or rejection.

## Frappe realization

- **DocTypes:** `OC Lab Extraction Review` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Uploaded → Extracted → Human Review → Accepted, Corrected, or Rejected; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Lab Result Filer` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.pdf_result_structured_extraction_assist` is the supported write method, with allowlisted `/api/resource/OC%20Lab%20Extraction%20Review` reads and a Desk worklist or report.

## Boundaries

Owns: assistive extraction and reviewer decisions. Consumes: PDF attachments, OCR service outputs, terminology, and patient identity. Emits: a review queue of source-linked structured candidates. Does not own: autonomous chart filing or treating extracted text as verified truth.

## Open questions

- Which organization-level policy values and exception thresholds for pdf result structured extraction assist must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
