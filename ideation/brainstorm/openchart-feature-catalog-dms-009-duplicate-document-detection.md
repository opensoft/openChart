# Duplicate Document Detection — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Warns reviewers about exact and likely duplicate uploads while preserving explicit decisions and distinct source provenance.
Topics: openchart-feature-catalog, documents, frappe, duplicate-detection
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-009 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Near-duplicate page comparison** — Highlight added, removed, or changed pages before a reviewer decides whether records differ materially.

## Focus

This feature isolates duplicate detection at ingest without silently discarding clinically relevant variants.

## Behavior

- Upload computes a cryptographic file checksum and normalized-content fingerprint before acceptance.
- Exact checksum matches within permitted scope produce a blocking duplicate review rather than a second silent chart copy.
- Similar text, image, date, source, and page-count signals produce non-blocking likely-duplicate candidates with reasons.
- A reviewer may link to the existing document, accept as a distinct record, or reject the new upload.
- Distinct acceptance requires a reason such as different source, annotation, signature, or page set.
- Cross-patient candidates reveal no content unless the reviewer has access to both patients and an identity-review role.
- Every candidate, decision, algorithm version, and threshold is retained for audit and tuning.

## Frappe realization

- **DocTypes:** `OC Duplicate Document Review` (incoming_version, state, detector_version, decision, reason) with child `OC Duplicate Candidate` (candidate_version, match_type, score, evidence JSON).
- **Hooks/jobs:** `open_chart.documents.on_file` computes SHA-256 synchronously and enqueues normalized fingerprint comparison through RQ after malware clearance.
- **Workflow:** Screening → Review Required → Resolved, with Unique, Linked Duplicate, Accepted Variant, and Rejected outcomes.
- **Roles/permissions:** Document Indexer resolves same-patient candidates; Patient Identity Reviewer handles authorized cross-patient evidence; detector integration role cannot decide.
- **Surfaces:** Desk comparison dialog, preview thumbnails, and a detector-quality Script Report expose explainable evidence.

## Boundaries

Owns: duplicate candidates, evidence, and reviewer disposition. Consumes: file checksums, approved OCR fingerprints, and permitted metadata. Emits: deduplication decision or accepted-variant reason. Does not own: patient merge, document supersession, or content deletion.

## Open questions

- Which near-duplicate thresholds should vary by document class and scan quality?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Document Version History With Supersession](openchart-feature-catalog-dms-010-document-version-history-with-supersession.md)
