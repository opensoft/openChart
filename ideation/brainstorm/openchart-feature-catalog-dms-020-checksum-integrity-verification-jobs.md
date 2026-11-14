# Checksum Integrity Verification Jobs — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Recomputes and reconciles file and manifest checksums on a governed schedule to detect corruption, loss, or unauthorized change.
Topics: openchart-feature-catalog, documents, frappe, integrity-verification
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-020 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Replica repair orchestration** — Restore a corrupt object from a verified replica only after an authorized integrity decision.

## Focus

This feature isolates continuous integrity evidence for originals, derivatives, packets, and manifests.

## Behavior

- A Storage Auditor defines verification cadence and sampling policy by document class and storage tier.
- Scheduled jobs stream file bytes from storage and compare computed checksums with immutable version records.
- Manifests are also checked for missing files, unexpected files, page-order drift, and derivative lineage breaks.
- A match appends verification evidence without changing the clinical document.
- A mismatch immediately marks the object Integrity Suspect, blocks ordinary download, and opens an incident.
- Retry distinguishes transient storage failure from confirmed checksum mismatch and preserves every attempt.
- Repair or false-positive closure requires an authorized reason, source replica evidence, and post-action verification.

## Frappe realization

- **DocTypes:** `OC Integrity Verification Run` (scope, policy, state, counts) with child `OC Integrity Check Result` (File, expected_checksum, observed_checksum, outcome, error) and `OC File Integrity Incident`.
- **Jobs:** scheduler_events enqueue bounded RQ batches; jobs use storage streaming and idempotency keys, with realtime progress and retry classification.
- **Roles/permissions:** Storage Auditor configures and reviews; Security Operations resolves incidents; ordinary document roles see availability status only.
- **Hooks/API:** `open_chart.documents.on_file` establishes baseline checksums; download methods deny Integrity Suspect objects unless break-glass policy authorizes forensic access.
- **Surfaces:** Integrity dashboard, mismatch alerts, trend chart, and signed verification report Print Format.

## Boundaries

Owns: verification policy, runs, comparisons, incident state, and repair evidence. Consumes: immutable expected checksums and storage bytes. Emits: integrity status and alerts. Does not own: storage replication, encryption keys, or automatic repair authority.

## Open questions

- What sampling and full-scan cadence balances evidence strength, storage cost, and operational load?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Sensitive Document Encryption at Rest](openchart-feature-catalog-dms-019-sensitive-document-encryption-at-rest.md)
