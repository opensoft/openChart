# Insurance Card OCR Extraction — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Extracts reviewable payer, member, group, and plan candidates from insurance cards to reduce transcription errors.
Topics: openchart-feature-catalog, registration, frappe, insurance-card-ocr
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-025 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Payer-directory reconciliation** — Rank directory matches from extracted payer names and routing identifiers.

## Focus

Use OCR to propose structured coverage fields while requiring explicit human acceptance.

## Behavior

- OCR starts only for an authorized coverage-card record and runs as a background job.
- Candidate payer, member ID, group, plan, subscriber name, and service numbers retain field confidence.
- Reviewers compare each candidate with the image and existing coverage value.
- Ambiguous characters in identifiers are highlighted rather than normalized silently.
- Accepted fields create or amend coverage through guarded APIs with extraction provenance.
- Processing failures are retryable and redact member identifiers from operational logs.

## Frappe realization

- **DocTypes:** `OC Coverage Card Extraction` and child `OC Extracted Coverage Field` with candidate, confidence, target, and disposition.
- **Workflow:** Queued → Extracted → Review → Accepted, Partial, Rejected, or Failed.
- **Roles/permissions:** `OC Coverage Reviewer` confirms; integration role accesses only queued private files; others see status.
- **API/surfaces:** `open_chart.api.v1.registration.extract_coverage_card` and `.apply_coverage_extraction`; comparison page and OCR exception report.

## Boundaries

Owns: extracted coverage candidates and dispositions. Consumes: insurance-card images. Emits: confirmed coverage changes. Does not own: payer eligibility or benefit interpretation.

## Open questions

- Should payer-specific card templates be centrally curated or site-configured?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
