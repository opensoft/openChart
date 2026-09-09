# Synthesis: Documents Scanning And Printing — Brainstorm

Status: brainstorm
Kind: reference
Summary: Connects capture, OCR, identity, routing, storage, retrieval, release, templates, fax, printing, integrity, and legal evidence into a first-party human-governed document pipeline.
Topics: openchart-feature-catalog, documents, frappe, synthesis
Repository context: openChart — Frappe v15 native EMR; Documents Scanning Templates And Printing domain synthesis
Captured: 2026-08-24

## Possible feats

- **Closed-loop document episode** — Provide one permissioned timeline from external capture through human indexing, chart use, release, retention, and verifiable disposition.

## Focus

This synthesis relates the 40 Documents Scanning Templates And Printing capabilities around immutable File versions, explicit identity and authority decisions, asynchronous processing, controlled renditions, and auditable physical or external delivery. The differentiator is a coherent first-party pipeline: scanner, fax, OCR, routing, printing, and legal evidence remain governed openChart workflows rather than opaque optional modules.

## Members and their joints

### Capture, scanning, assembly, and migration intake

- [Typed Patient Document Attachment](openchart-feature-catalog-dms-001-typed-patient-document-attachment.md) establishes the accepted patient-document identity and required class, while [Clinician Quick-attach From Encounter](openchart-feature-catalog-dms-032-clinician-quick-attach-from-encounter.md) offers a bounded encounter shortcut into the same authority model.
- [Scanner Ingest Integration](openchart-feature-catalog-dms-002-scanner-ingest-integration.md), [Multi-page PDF Assembly](openchart-feature-catalog-dms-003-multi-page-pdf-assembly.md), and [Barcode Batch Auto-splitting](openchart-feature-catalog-dms-004-barcode-batch-auto-splitting.md) turn raw pages into reviewed bundle and PDF manifests without deciding patient identity automatically.
- [External Records Import Bundles](openchart-feature-catalog-dms-011-external-records-import-bundles.md) applies the same quarantine, checksum, item disposition, and provenance principles to prior-chart migration packages.
- [Duplicate Document Detection](openchart-feature-catalog-dms-009-duplicate-document-detection.md) compares incoming content before acceptance, and [Document Version History With Supersession](openchart-feature-catalog-dms-010-document-version-history-with-supersession.md) preserves distinct accepted variants and corrections without in-place overwrite.

The joint is a sealed acquisition manifest. Scanner pages, archive members, encounter uploads, and ordinary attachments all retain source identity and checksums while transformations produce explicit derivatives. Human acceptance advances only a reviewed artifact into the chart; retries, duplicate candidates, and corrections remain evidence rather than disappearing into the File store.

### OCR, identity, routing, search, and reconciliation

- [OCR Full-text Extraction](openchart-feature-catalog-dms-005-ocr-full-text-extraction.md) creates machine-labeled text and coordinates; [OCR-assisted Indexing Suggestions](openchart-feature-catalog-dms-006-ocr-assisted-indexing-suggestions.md) converts that evidence into patient, type, and date candidates requiring human disposition.
- [Unmatched-document Resolution Queue](openchart-feature-catalog-dms-008-unmatched-document-resolution-queue.md) isolates ambiguous identity, while [Department Document Routing Inbox](openchart-feature-catalog-dms-007-department-document-routing-inbox.md) starts accountable operational delivery only after identity and classification are safe.
- [Document Tagging and Saved Searches](openchart-feature-catalog-dms-033-document-tagging-and-saved-searches.md) supplies governed facets and reusable queries to [ACL-filtered Full-text Document Search](openchart-feature-catalog-dms-034-acl-filtered-full-text-document-search.md).
- [Expiry-dated Document Alerting](openchart-feature-catalog-dms-035-expiry-dated-document-alerting.md) turns class-specific validity into renewal work, and [Outside-record Diff View](openchart-feature-catalog-dms-036-outside-record-diff-view.md) sends source-grounded differences toward owning clinical reconciliation workflows.
- [Audited Bulk Document Reclassification](openchart-feature-catalog-dms-037-audited-bulk-document-reclassification.md) corrects selected metadata at scale through frozen plans, blockers, item outcomes, and compensating reversal.

The joint is reviewed interpretation rather than automated truth. OCR, matching, retrieval, and comparison may rank or align evidence, but only role-authorized decisions establish patient association, metadata, routing disposition, or a downstream reconciliation request. Search applies authorization before snippets or counts, preventing the index from becoming an alternate disclosure channel.

### Clinical media, consent evidence, and patient access

- [Clinical Media Library](openchart-feature-catalog-dms-012-clinical-media-library.md) manages originals and safe renditions for photos, audio, and video.
- [Consent Document Linkage](openchart-feature-catalog-dms-013-consent-document-linkage.md) connects an exact evidence version to the signed event that owns consent status and scope.
- [Patient Portal Document Downloads](openchart-feature-catalog-dms-031-patient-portal-document-downloads.md) exposes only explicitly released versions after access-time patient, proxy, consent, class, and integrity checks.
- [Watermarking Drafts and Confidential Classes](openchart-feature-catalog-dms-038-watermarking-drafts-and-confidential-classes.md) produces purpose- and recipient-aware derivatives while originals remain immutable.

The joint is access derived from current authority over immutable evidence. A media or document File does not grant access by existing; consent and release records identify the audience and scope, access-time checks account for revocation or supersession, and watermarked renditions preserve the exact source and policy version used.

### Release, retention, security, and legal custody

- [Release-of-information Request Intake](openchart-feature-catalog-dms-014-release-of-information-request-intake.md) validates requester authority and freezes approved scope; [ROI Fulfillment Packet Assembly](openchart-feature-catalog-dms-015-roi-fulfillment-packet-assembly.md) selects exact versions and seals a reviewed packet.
- [Disclosure Log Per Document](openchart-feature-catalog-dms-016-disclosure-log-per-document.md) records recipient, purpose, authority, item versions, attempts, and terminal delivery evidence.
- [Document Retention Schedule Enforcement](openchart-feature-catalog-dms-017-document-retention-schedule-enforcement.md) computes reviewable disposition, while [Legal Hold Override](openchart-feature-catalog-dms-018-legal-hold-override.md) supplies the higher-authority preservation block.
- [Sensitive Document Encryption at Rest](openchart-feature-catalog-dms-019-sensitive-document-encryption-at-rest.md) requires key-policy evidence, and [Checksum Integrity Verification Jobs](openchart-feature-catalog-dms-020-checksum-integrity-verification-jobs.md) continuously tests stored bytes and manifests against immutable expectations.
- [Digital Signature Certificate Application](openchart-feature-catalog-dms-039-digital-signature-certificate-application.md) binds signing intent and certificate validation to a finalized PDF; [Chain-of-custody Legal Export](openchart-feature-catalog-dms-040-chain-of-custody-legal-export.md) combines selected versions, provenance, signatures, manifests, and handoff receipts into verifiable evidence.

The joint is a preservation-and-disclosure ledger. Authorization fixes what may leave, packet assembly fixes which versions did leave, disclosure records explain where and how, integrity and encryption protect stored evidence, retention governs ordinary lifecycle, and legal hold can suspend disposition without rewriting policy. A legal export is therefore reproducible from authoritative versions and custody events rather than assembled ad hoc from mutable folders.

### Templates, generated forms, and high-volume correspondence

- [Template Letter Library](openchart-feature-catalog-dms-021-template-letter-library.md) governs wording, merge fields, Letter Heads, locale, approval, and effective versions.
- [Cohort Mail-merge Batch Letters](openchart-feature-catalog-dms-022-cohort-mail-merge-batch-letters.md) freezes recipients and source values, applies exclusions, and renders per-recipient outputs with a reconciled manifest.
- [Data-driven PDF Form Generation](openchart-feature-catalog-dms-030-data-driven-pdf-form-generation.md) maps allowlisted chart fields into versioned form templates and immutable patient-specific outputs.

The joint is reproducible rendering from an approved definition and frozen data snapshot. Templates cannot query arbitrary chart state, bulk generation cannot change cohort membership mid-run, and regenerated forms or letters become new outputs. Signatures, releases, printing, and disclosure attach to exact rendered checksums rather than an abstract current template.

### Fax, labels, wristbands, stocks, and physical output

- [Inbound Fax OCR Routing](openchart-feature-catalog-dms-023-inbound-fax-ocr-routing.md) brings provider receipts into the same quarantine and human indexing pipeline used by scanners.
- [Outbound Fax Delivery Tracking](openchart-feature-catalog-dms-024-outbound-fax-delivery-tracking.md) sends only sealed authorized artifacts, while [E-fax Cost Controls](openchart-feature-catalog-dms-025-e-fax-cost-controls.md) adds estimates, approvals, bounded retries, and actual-cost reconciliation without shrinking clinical scope.
- [Front-desk Print Queue Management](openchart-feature-catalog-dms-026-front-desk-print-queue-management.md) separates submission, release, printer outcome, collection, and reprint evidence.
- [Clinical Label Printing Engine](openchart-feature-catalog-dms-027-clinical-label-printing-engine.md) snapshots domain-owned values for specimen, address, and pharmacy labels; [Patient Wristband Printing Integration](openchart-feature-catalog-dms-028-patient-wristband-printing-integration.md) adds encounter identity confirmation, activation, replacement, and destruction lineage.
- [Envelope and Label Stock Templates](openchart-feature-catalog-dms-029-envelope-and-label-stock-templates.md) governs geometry, compatibility, calibration, and physical-layout versions shared by these output paths.

The joint is controlled materialization. Faxes, letters, forms, labels, and wristbands start from sealed bytes or value snapshots; destination, printer, stock, and release checks occur before output; provider and printer callbacks establish transport status; and reprints or retries remain separate attempts. Physical production never becomes authority for the source clinical or identity record.

## Frappe realization

- **Core model:** OC-prefixed patient-document, File-version, scan, OCR, indexing, routing, media, ROI, disclosure, retention, hold, template, fax, print, and export DocTypes use Links, Dynamic Links, child manifests, immutable checksums, and succession-based accepted corrections.
- **File layer:** The private Frappe file manager and `File` attachment patterns preserve originals and derived Files; File `after_insert`/`on_update` hooks route through `open_chart.documents.on_file` for quarantine, MIME, checksum, encryption, derivative-lineage, and attachment-target enforcement.
- **Workflow and permissions:** Frappe Workflows expose human review and terminal states; patient and facility User Permissions combine with Document Indexer, Patient Identity Reviewer, Health Information Manager, Privacy Officer, Records Administrator, Legal Hold Officer, Template Approver, Fax Triage, Print Operator, and integration roles using permlevels 0-2.
- **API and jobs:** Guarded `open_chart.api.v1.documents` methods are the supported write surface; signed connector callbacks, idempotency keys, and RQ background jobs handle scanner pages, OCR, archive extraction, PDF assembly, renditions, search indexing, fax, printing, checksums, and exports.
- **Surfaces:** Desk workspaces, List/Kanban/Calendar views, Assignment Rules, Notifications, Query/Script Reports, Number Cards, Dashboard Charts, patient timeline cards, `www/` portal pages, and realtime websocket events expose role-specific projections.
- **Print formats:** Governed Jinja Print Formats, Frappe Letter Heads, PDF generation, barcode/QR rendering, calibrated stock definitions, and packet cover/manifests support letters, forms, labels, wristbands, receipts, certificates, and chain-of-custody output.
- **Audit and safety:** Accepted transitions record actor, source, correlation ID, policy/template/engine version, evidence, reason, and exact File checksum; machine suggestions remain quarantined until human confirmation and cannot trigger autonomous clinical action.

## Boundaries

Owns: document and media attachment versions, capture sessions, OCR evidence, human indexing, routing, retrieval projections, release packets, disclosure records, retention/hold state, template/render outputs, fax evidence, print jobs, integrity checks, and custody exports. Consumes: patient and encounter identity, consent and proxy authority, clinical source facts, external scanners/OCR/fax/signing/storage/printer adapters, facility policy, and legal direction. Emits: accepted document events, accountable routes, permissioned downloads, sealed packets, delivery receipts, physical-output evidence, alerts, disposition instructions, and verifiable exports. Does not own: scanner or printer firmware, carrier networks, private keys, storage KMS, patient registration/merge, clinical fact authority, billing, legal advice, or autonomous interpretation and action.

## Emergent behavior

Together, these features create a provenance-preserving document episode from capture to final disposition. Every source enters quarantine; pages, archives, fax payloads, and media gain checksums and manifests; OCR and matching produce reviewable evidence; authorized humans establish patient, class, route, and release; immutable versions support search and chart access; approved templates materialize reproducible letters, forms, labels, wristbands, and packets; and disclosure, retention, holds, integrity, signatures, and custody records keep later use accountable. Because the same version and event identities cross these seams, a correction can invalidate stale routes or releases, a hold can block disposition, a failed checksum can block download, and a legal export can prove exactly which bytes moved without any connector becoming clinical authority.

## Tensions to hold

- Fast scanner, fax, quick-attach, and portal flows must not weaken patient matching, classification, malware quarantine, minimum-necessary access, or human acceptance.
- OCR and comparison improve retrieval and reconciliation, but machine-extracted text and candidates must remain labeled, attributed, reversible, and incapable of autonomous chart changes.
- Exact duplicate suppression reduces clutter, while near-duplicate variants, signatures, annotations, and source provenance may make superficially similar files distinct evidence.
- Broad full-text search and saved queries improve usability, but ACL filtering must occur before snippets, facets, counts, or timing can reveal hidden records.
- Templates and bulk output need operational efficiency, while frozen snapshots, per-recipient exclusions, destination confirmation, stock calibration, and reprint evidence prevent scale from hiding mistakes.
- Retention favors controlled disposition and cost reduction, whereas legal holds, active disclosures, integrity incidents, and unresolved authority require fail-closed preservation.
- Watermarks, encryption, and signatures strengthen control and evidence but do not replace consent, release authority, recipient verification, or sound custody procedure.

## Recombination opportunities

- Combine scanner sessions, barcode splitting, PDF assembly, OCR, indexing review, unmatched resolution, duplicate review, and department routing into a unified document-ingest cockpit.
- Combine accepted OCR, taxonomy, ACL-filtered search, validity dates, outside-record comparison, and routes into a permissioned records-review workspace that preserves source evidence.
- Combine ROI intake, packet selection, watermarking, signature, fax/portal delivery, disclosure logging, and custody events into one version-locked release command center.
- Combine retention, legal hold, encryption evidence, checksum verification, version history, and chain-of-custody export into a defensible records-preservation program.
- Combine Letter Heads, template versions, PDF field maps, stock geometry, render snapshots, print queue, and fax delivery into one controlled output service without flattening purpose-specific approvals.
- Combine label and wristband snapshot rules, barcode verification, printer calibration, activation, replacement, and destruction evidence into a shared physical-identity safety layer.

## Open questions

- What is the canonical document/version/event identifier model that can bridge File storage, OCR, search, routes, portal release, disclosure, printing, retention, and legal export?
- Which document classes and transformations require second-person review, local-only processing, special consent, delayed portal release, or recipient-specific watermarking?
- Which scanner, OCR, fax, search, signing, encrypted-storage, and printer adapter contracts form the minimum first-party interoperable baseline?
- How should plaintext clinical checksums, encrypted-object checksums, derivative checksums, and package signatures coexist through key rotation and format normalization?
- Which organization, facility, and jurisdiction policies control routing deadlines, validity alerts, retention, disclosure, fax cost, print release, and legal evidence?

## Relationships

[openChart Feature Catalog](openchart-feature-catalog-overview.md)
