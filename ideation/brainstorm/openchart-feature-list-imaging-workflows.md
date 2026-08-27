# Imaging Workflows — Brainstorm

Status: brainstorm
Kind: report
Summary: openChart should own imaging orders, results routing with follow-up accountability, and PACS-neutral viewer integration — including AI finding-flag surfacing — rather than pretending to be a PACS like nobody does, but unlike OpenEMR leaving follow-up closure to chance.
Topics: openchart-feature-list, imaging, competitive-research
Repository context: openChart — Frappe-native EMR foundation; feature research versus the OpenEMR baseline and the enterprise big-3 (Epic, Oracle Health, MEDITECH Expanse)
Captured: 2026-08-23

## Possible feats

- **Imaging order class with protocol context** — modality, contrast, prep instructions, and clinical question captured at order time.
- **Result routing with critical-finding tracking** — radiology reports route to ordering clinician pools; critical findings carry acknowledgment and follow-up obligations inside the orders accountability loop.
- **PACS-neutral viewer integration** — zero-footprint DICOM viewing via standard connections (OpenEMR already bundles a DICOM viewer; extend rather than replace).
- **AI finding extraction surfacing** — machine-extracted findings/follow-up recommendations presented as suggestions with provenance, never auto-actions (Epic imaging-AI interaction pattern).
- **Follow-up registry** — incidental-finding tracking (pulmonary nodules pattern) ensuring recommendations become completed care.

## Focus

How does openChart close the imaging loop — order to interpretation to acknowledged, actionable result — without building a PACS?

## Current state: OpenEMR baseline

OpenEMR includes procedure orders covering imaging, results filing into charts, a bundled DICOM image viewer, medical-image/document storage, pending-procedure reports, and ordered-procedure statistics. Radiology-specific workflow depth (modality worklists, protocol management, critical-result acknowledgment, follow-up registries) is absent; external PACS/RIS integration is custom-interface territory.

Sources: open-emr.org Features wiki; Modules catalog.

## Enterprise gap candidates

- Epic Radiant handles radiology ordering/results/routing integrated with In Basket follow-up; public EHI/AI-interaction structures show imaging-finding extraction and radiology follow-up AI use; Epic connects to external PACS rather than replacing them.
- Oracle carries RadNet heritage (scheduling, modality coordination, reporting) and drafts imaging orders from ambient conversation via Clinical AI Agent; positions enterprise imaging across radiology/cardiovascular contexts.
- MEDITECH integrates Imaging and Documentation Management with surgical/anesthesia interfaces and device connectivity around diagnostics.
- Common enterprise thread: imaging results are worked objects with ownership and follow-up, not filed PDFs.

## Proposed feature set for openChart

Parity floor: imaging procedure orders, report/result storage, embedded DICOM viewer. Adopted gaps: structured order protocol fields; critical-finding acknowledgment tied to the Result Accountability object from orders-and-cds; incidental-finding follow-up registry with due dates and escalation; viewer integrations via DICOMweb/OHIF-class zero-footprint embeds; AI finding-extraction suggestions rendered with model provenance and explicit non-action defaults. Twist: the follow-up registry publishes completion metrics to analytics-and-population-health — closing loops becomes measurable safety performance.

## Interfaces and boundaries

Consumes: order context from orders-and-cds, encounter/document context from clinical-documentation, external images/reports via interoperability exchange. Emits: finalized reports to longitudinal record, follow-up tasks to staff queues, loop-completion metrics to analytics. Owns imaging-order state and follow-up registry; explicitly does not own PACS archive/modality hardware.

## Alternatives and tensions

Bundling a full open-source viewer (OHIF) vs thin integration changes maintenance surface. AI finding extraction vendors vary in quality; pluggable interface keeps openChart honest. Deep radiology operations (technologist worklists) may exceed ambulatory launch scope while hospital buyers expect it.

## Open questions

- Which viewer integration ships first — OHIF embed or vendor-neutral link-out standard?
- Are critical-result acknowledgment rules jurisdiction-configurable at launch?
- Does incidental-finding registry content start oncology-only?

## Relationships

Clustered in [Synthesis: Clinical Core](openchart-feature-list-synthesis-clinical-core.md). Adjacent: [Clinical Orders And Decision Support](openchart-feature-list-orders-and-cds.md), [Labs And Diagnostics](openchart-feature-list-labs-and-diagnostics.md).
