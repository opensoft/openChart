# Sensitive Document Encryption at Rest — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Enforces class-aware encryption and key-policy evidence for sensitive document files and derivatives stored by Frappe.
Topics: openchart-feature-catalog, documents, frappe, storage-encryption
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-019 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Cryptographic policy dashboard** — Show key version, algorithm, storage class, and rotation status without revealing protected content.

## Focus

This feature isolates verifiable at-rest protection beyond ordinary private-file URL controls.

## Behavior

- A Security Administrator maps governed document classes to storage encryption profiles and effective dates.
- Upload is accepted only when the storage adapter returns required encryption and key-version evidence.
- Originals, OCR intermediates, thumbnails, renditions, exports, and backups inherit or exceed the source class profile.
- Decryption occurs only through an authorized application request after patient and class ACL checks.
- Missing evidence, disabled keys, unexpected plaintext replicas, or policy drift quarantines the file and alerts Security Operations.
- Key rotation rewraps or re-encrypts content through tracked jobs without changing the document checksum semantics unexpectedly.
- Audit records key identifiers and outcomes but never stores key material or decrypted content.

## Frappe realization

- **DocTypes:** `OC Document Encryption Profile` (class, adapter, algorithm, key_alias, rotation_days) and `OC File Encryption Evidence` linked one-to-one with private File versions.
- **Hooks/jobs:** `open_chart.documents.on_file` validates adapter evidence before release; scheduler_events verify samples and enqueue key-rotation work through a KMS connector.
- **Roles/permissions:** Security Administrator manages profiles; Security Auditor reads evidence; document users cannot access key metadata beyond protected status.
- **API/storage:** Frappe file manager delegates byte storage to an encrypted adapter; whitelisted download streams only after ACL and evidence checks.
- **Surfaces:** Security dashboard, failed-evidence report, and restricted rotation queue; no decrypted file is written to public File storage.

## Boundaries

Owns: encryption policy mapping, evidence, access-time enforcement, and rotation tracking. Consumes: document class, File, KMS, and storage adapter receipts. Emits: protected-file status and security alerts. Does not own: KMS keys, host disk encryption, or patient access policy.

## Open questions

- Which checksum should identify plaintext clinical content versus encrypted storage objects during rotation?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Checksum Integrity Verification Jobs](openchart-feature-catalog-dms-020-checksum-integrity-verification-jobs.md)
