# Synthesis: Imaging Workflows — Brainstorm

Status: brainstorm
Kind: reference
Summary: Connects imaging intent, readiness, performance, interpretation, image access, communication, follow-up, quality, and external-system exchange into a human-governed clinical workflow.
Topics: openchart-feature-catalog, imaging, frappe, synthesis
Repository context: openChart — Frappe v15 native EMR; Imaging Workflows domain synthesis
Captured: 2026-08-24

## Possible feats

- **Closed-loop imaging episode** — Provide one permissioned timeline from clinical question through accepted report, communication, and verified follow-up while PACS remains the image authority.

## Focus

This synthesis relates the 40 Imaging Workflows capabilities and their authority, identity, safety, provenance, and integration seams. openChart owns order, report, communication, and follow-up state; it integrates external scheduling, modalities, viewers, archives, readers, and billing systems without becoming a PACS.

## Members and their joints

### Intent, protocol, preparation, and scheduling

- [Imaging Order Entry](openchart-feature-catalog-img-001-imaging-order-entry.md) and [Mandatory Clinical Question](openchart-feature-catalog-img-002-mandatory-clinical-question.md) establish signed intent that can be interpreted and challenged without silent edits.
- [Protocol Assignment Review](openchart-feature-catalog-img-003-protocol-assignment-review.md) applies a patient-specific protocol selected from the [Modality Protocol Library](openchart-feature-catalog-img-030-modality-protocol-library.md).
- [Preparation Instruction Generation](openchart-feature-catalog-img-004-preparation-instruction-generation.md), [Imaging Scheduling Integration](openchart-feature-catalog-img-005-imaging-scheduling-integration.md), [Advanced Imaging Precertification Capture](openchart-feature-catalog-img-033-advanced-imaging-precertification.md), and [Repeat-due Imaging Recall](openchart-feature-catalog-img-034-repeat-due-imaging-recall.md) connect readiness to access without moving clinical authority into scheduling or payer systems.

The joint is a versioned readiness snapshot: a signed order supplies intent, protocol review supplies performance requirements, safety and authorization records supply bounded evidence, and scheduling consumes only the current approved projection. Any material upstream change invalidates affected downstream assumptions and opens visible reconciliation rather than rewriting history.

### Performance, safety, dose, and resources

- [Technologist Worklist](openchart-feature-catalog-img-006-technologist-worklist.md) coordinates ready work while [Imaging Performance Documentation](openchart-feature-catalog-img-007-imaging-performance-documentation.md) records what actually occurred.
- [Renal Contrast Safety Check](openchart-feature-catalog-img-023-renal-contrast-safety-check.md), [Pregnancy Screening Before Radiation Imaging](openchart-feature-catalog-img-024-pregnancy-screening-before-radiation.md), and [MRI Implant and Device Safety](openchart-feature-catalog-img-025-mri-implant-device-safety.md) produce episode-specific human-reviewed readiness states.
- [Study Radiation Dose Capture](openchart-feature-catalog-img-021-study-radiation-dose-capture.md) feeds the [Cumulative Radiation Exposure View](openchart-feature-catalog-img-022-cumulative-radiation-exposure-view.md) without collapsing unlike metrics into false precision.
- [Contrast Inventory Tracking](openchart-feature-catalog-img-031-contrast-inventory-tracking.md) links lot availability and consumption to the performed study, while [Imaging Charge Capture](openchart-feature-catalog-img-032-imaging-charge-capture.md) projects accepted clinical evidence to an external billing owner.

The joint is performed-fact authority: worklists and safety checks govern whether work may proceed, but the accepted performance record says what happened. Device and inventory data may assist capture; technologist reconciliation, provenance, and succession preserve clinical accountability.

### Image access, comparison, and outside studies

- [Zero-footprint DICOM Viewer Embed](openchart-feature-catalog-img-013-zero-footprint-dicom-viewer-embed.md) and [DICOMweb PACS Retrieval](openchart-feature-catalog-img-014-dicomweb-pacs-retrieval.md) provide secure standards-based access while pixels stay outside openChart.
- [Prior and Current Image Comparison](openchart-feature-catalog-img-015-prior-current-image-comparison.md), [Viewer Measurement Tools](openchart-feature-catalog-img-016-viewer-measurement-tools.md), and [Key Image and Note Linkage](openchart-feature-catalog-img-017-key-image-note-linkage.md) retain selected references and evidence that can survive the viewer session.
- [Outside DICOM Upload](openchart-feature-catalog-img-018-outside-dicom-upload.md), [Outside Imaging Patient Matching](openchart-feature-catalog-img-019-outside-imaging-patient-matching.md), and [Outside Report OCR-assisted Indexing](openchart-feature-catalog-img-020-outside-report-ocr-indexing.md) separate quarantine, identity decision, archive transfer, and report indexing.

The joint is verified reference identity: DICOM UIDs, accession identifiers, patient mappings, source systems, and immutable import manifests connect chart records to external pixels. Every launch or import revalidates patient authority, and ambiguous identity stops association rather than inviting a convenient match.

### Reporting, structured interpretation, and reader authority

- [Imaging Result Report Capture](openchart-feature-catalog-img-008-imaging-result-report-capture.md) is the report authority, supported by the [Imaging Report Template Library](openchart-feature-catalog-img-036-imaging-report-template-library.md) and [Structured Imaging Category Fields](openchart-feature-catalog-img-037-structured-imaging-category-fields.md).
- [Preliminary-to-Final Report Workflow](openchart-feature-catalog-img-009-preliminary-to-final-report-workflow.md) preserves wet-read or resident disclosure through attending attestation.
- [Multi-reader Imaging Consensus](openchart-feature-catalog-img-040-multi-reader-consensus.md) adds quorum, independent submissions, reconciliation, and final authority where a linear supervision path is insufficient.
- [Teleradiology Package Exchange](openchart-feature-catalog-img-035-teleradiology-package-exchange.md) carries minimum-necessary context and returned artifacts across organizational boundaries with explicit reconciliation.

The joint is attested interpretation lineage: templates and category schemas structure expression but do not author findings; preliminary, consensus, and external reads remain clearly labeled until the authorized final signer accepts a report version. Addenda and corrections create successors and renewed downstream obligations.

### Communication, findings, follow-up, and recall

- [Critical Finding Acknowledgment](openchart-feature-catalog-img-010-critical-finding-acknowledgment.md) handles urgent closed-loop acknowledgment, while [Radiology Communication Evidence](openchart-feature-catalog-img-027-radiology-communication-evidence.md) records ordinary report delivery outcomes.
- [Incidental Finding Registry](openchart-feature-catalog-img-011-incidental-finding-registry.md) turns an accepted recommendation into durable accountable demand.
- [Imaging Follow-up Completion and Escalation](openchart-feature-catalog-img-012-imaging-follow-up-completion-escalation.md) carries that demand through outreach, scheduling, reviewed evidence, escalation, and closure.

The joint is obligation identity: an accepted report version creates a delivery or follow-up obligation with a responsible human and due basis. Transmission, acknowledgment, appointment, performance, and verified completion remain distinct evidence states so dashboards cannot claim closure prematurely.

### Quality, education, metrics, and bounded AI assistance

- [Order-to-Report Turnaround Metrics](openchart-feature-catalog-img-026-order-to-report-turnaround-metrics.md) derives reproducible intervals from accepted events.
- [Radiology Peer Review Sampling](openchart-feature-catalog-img-028-radiology-peer-review-sampling.md) and [Teaching File Flagging](openchart-feature-catalog-img-029-teaching-file-flagging.md) create separately permissioned quality and education paths without changing clinical truth silently.
- [AI Finding-extraction Suggestions](openchart-feature-catalog-img-038-ai-finding-extraction-suggestions.md) and [AI Follow-up Recommendation Capture](openchart-feature-catalog-img-039-ai-follow-up-recommendation-capture.md) quarantine model output until a qualified clinician explicitly accepts, edits, or rejects it.

The joint is explainable secondary use: metrics, peer review, education, and AI evaluation reuse provenance-rich imaging events under narrower authority. None may amend a report, trigger patient action, or change clinical state without the separately authorized workflow that owns that decision.

## Frappe realization

- **Core model:** OC-prefixed order, protocol, safety, work, performance, report, communication, follow-up, external-reference, quality, and AI-run DocTypes use Links, child evidence rows, immutable source identifiers, and succession-based corrections.
- **Workflow and permissions:** Frappe Workflows expose explicit states; Ordering Clinician, Imaging Coordinator, Imaging Technologist, Radiologist, Safety Officer, Follow-up Coordinator, Quality Reviewer, Identity Reviewer, and integration roles combine DocPerms with patient and facility user permissions.
- **API and integration:** guarded `open_chart.api.v1.imaging` methods are the supported write surface; signed whitelisted callbacks, OAuth or token-scoped connectors, DICOMweb adapters, idempotency keys, and RQ jobs integrate scheduling, PACS, viewers, modalities, teleradiology, OCR, AI, and billing owners.
- **Surfaces:** Desk workspaces, List, Kanban, Calendar, Assignment Rules, Query/Script Reports, Number Cards, Dashboard Charts, patient timeline cards, portal pages, Print Formats, Notification Log, and websocket events provide role-specific projections.
- **Audit and safety:** accepted transitions record actor, source, correlation ID, policy or model version, evidence, and reason; sensitive screening and quality data use restricted permlevels and minimum-necessary views.
- **PACS boundary:** Frappe stores clinical workflow state, metadata, manifests, and durable references; external archives and zero-footprint viewers own pixel storage, rendering, image lifecycle, and acquisition-console behavior.

## Boundaries

Owns: imaging orders, protocol and safety decisions, performed-study documentation, reports, communications, follow-up obligations, external study references, and auditable operational state. Consumes: patient and encounter context, laboratory and device evidence, scheduling and payer outcomes, modality metadata, PACS and viewer services, external readers, and communication channels. Emits: schedulable demand, performance and result events, delivery evidence, follow-up tasks, quality measures, and bounded integration packages. Does not own: image acquisition consoles, PACS pixel archives, diagnostic rendering, billing or claims, payer adjudication, or autonomous AI-driven clinical action.

## Emergent behavior

Together, these features create an end-to-end but federated imaging episode: a specific clinical question becomes a governed protocol; preparation, safety, authorization, and scheduling establish readiness; technologists attest performance; external archives expose images through verified references; readers create provenance-rich preliminary, consensus, external, or final reports; communication turns accepted results into accountable delivery; and finding registries carry recommendations to verified completion. Shared episode and event identity lets corrections invalidate stale instructions, re-open delivery, refresh follow-up, and recompute measures without letting any integration silently become the clinical authority.

## Tensions to hold

- Fast access to images and outside media must not weaken patient matching, minimum-necessary disclosure, or the PACS boundary.
- Safety checks need strong blocking states, but urgent exceptions and incomplete evidence require explicit human authority rather than rigid automation.
- Structured reporting improves retrieval and follow-up, while category systems and templates must not crowd out nuanced narrative interpretation.
- Delivery, acknowledgment, scheduling, performance, and completion are operationally related but cannot be treated as interchangeable proof.
- Metrics and peer review need detailed provenance, yet their use for individual performance can distort behavior and requires separate governance.
- AI suggestions may reduce omission, but model output must remain quarantined, fully attributed, optional, and incapable of autonomous clinical action.

## Recombination opportunities

- Combine protocol assignment, safety checks, precertification, preparation, and scheduling state into a human-reviewed imaging readiness cockpit.
- Combine DICOMweb study references, comparison sessions, measurements, key images, templates, and structured fields into a portable reporting workspace independent of any one viewer.
- Combine accepted recommendations, delivery evidence, incidental registry entries, recalls, and completion evidence into a unified but type-preserving follow-up command center.
- Combine dose, contrast lot, performance deviation, peer review, and turnaround evidence into a quality program that explains source data and never modifies care automatically.
- Combine preliminary, consensus, and teleradiology workflows around one attestation model that keeps every disclosed version and authority transition visible.
- Combine AI dispositions, report corrections, and follow-up outcomes into controlled model evaluation datasets with consent, access, and provenance gates.

## Open questions

- What canonical imaging episode and event identifiers can bridge orders, external schedulers, modalities, PACS, viewers, reports, and follow-up without centralizing pixel data?
- Which safety, communication, and follow-up policies are organization-wide defaults versus facility- or modality-specific versions?
- Which DICOMweb, reporting, and teleradiology profiles form the minimum interoperable baseline for the first implementation?
- How should sensitive screening, quality-review, and AI-evaluation data be separated while remaining auditable from the clinical episode?
- Which report and recommendation changes automatically re-open downstream obligations, and which require explicit reviewer selection?

## Relationships

[openChart Feature Catalog](openchart-feature-catalog-overview.md)
