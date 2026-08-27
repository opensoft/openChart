# Submission History And Receipts — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Maintains an immutable archive of quality submissions, manifests, transport events, acknowledgments, receipts, and final disposition.
Topics: openchart-feature-catalog, quality-reporting, frappe, submission-history
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-032 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Receipt reconciliation dashboard** — Flag released packages lacking acknowledgment by the expected response time.

## Focus

End-to-end evidence of what was released, by whom, through which channel, and how the destination responded.

## Behavior

- Every released package creates a submission record with period, program, entity, artifact manifest, checksum, approver, and destination.
- Transport events record attempted, sent, delivered, rejected, acknowledged, accepted, and unknown states with source timestamps.
- Receipts are attached or parsed with provenance and correlated by identifiers rather than filename alone.
- Duplicate events are idempotent while conflicting acknowledgments create a reconciliation issue.
- Users can search by program, period, TIN, provider, package, external tracking ID, or disposition.
- Archived artifacts are read-only, access-audited, retention-governed, and integrity-checked.
- Missing acknowledgments or rejection deadlines create assigned follow-up items.

## Frappe realization

- **DocTypes:** Add `OC Quality Submission`, `OC Submission Transport Event`, and `OC Submission Receipt` with package Links, identifiers, timestamps, Attach, checksums, status, and correlation evidence.
- **Workflow:** Use prepared, released, in-transit, acknowledged, accepted, rejected, reconciliation, and archived states.
- **API and jobs:** Provide guarded event/receipt ingestion, idempotency keys, scheduled acknowledgment checks, and PHI-safe logs.
- **Surfaces:** Deliver submission timeline, history Script Report, receipt reconciliation queue, and archive Print Format.

## Boundaries

Owns: local submission, transport, receipt, disposition, and integrity history. Consumes: released packages and destination responses. Emits: reconciliation tasks and durable receipts. Does not own: external portal behavior, transport infrastructure, or regulator acceptance criteria.

## Open questions

- What retention periods and storage tiers apply to patient-level submission artifacts?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
