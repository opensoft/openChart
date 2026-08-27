# Clinical Documentation And Ambient Capture — Brainstorm

Status: brainstorm
Kind: report
Summary: openChart can beat OpenEMR's documentation by pairing a structured discrete-data form engine with governed ambient capture and AI chart search over unstructured history, where OpenEMR offers only manual notes and paid add-ons.
Topics: openchart-feature-list, clinical-documentation, competitive-research
Repository context: openChart — Frappe-native EMR foundation; feature research versus the OpenEMR baseline and the enterprise big-3 (Epic, Oracle Health, MEDITECH Expanse)
Captured: 2026-08-23

## Possible feats

- **Governed ambient documentation** — conversation capture drafts the note for clinician review-before-sign, with transcript-to-note provenance linkage.
- **AI chart search over messy history** — search and summarize across structured data, scanned documents, faxes, and legacy imports, Expanse Navigator style.
- **Role-specific drafting** — separate draft behaviors for physicians, nurses (handoff/SBAR), and ED staff.
- **Contextual patient timeline** — visit-type-aware presentation that adapts what the clinician sees first.
- **Structured form engine v2** — discrete observations from forms (PowerForms/LBF successor) so every capture is coded, queryable data, not free text.

## Focus

What must openChart's clinical documentation domain deliver so clinicians document faster than in OpenEMR while producing more structured, provenance-bearing data than any of the three enterprise leaders require of their own stacks?

## Current state: OpenEMR baseline

OpenEMR ships encounter creation, SOAP notes, problem lists, vitals and growth charts, medication/allergy records, the Layout-Based Forms engine for custom forms, Nation Notes WYSIWYG editing, e-signature, form profiles/templates, and social-screening forms. Its 2022 official usability report recorded a System Usability Scale score of 55, with complaints about navigation complexity, cumbersome data entry, and inconsistent controls. Clinical AI exists only as two optional paid modules (~$65/month each): an AI Chart Summary and a Chrome-only voice-to-text tool. There is no native ambient capture, no AI search over scanned/faxed/unstructured history.

Sources: open-emr.org Features wiki; OpenEMR Usability Report (2022); Release Features wiki; OpenEMR Modules catalog.

## Enterprise gap candidates

- Epic Art / Oracle Health Clinical AI Agent / MEDITECH ambient listening all draft notes from conversation for review-before-sign; Epic extends drafting to nursing end-of-shift notes and In Basket message replies.
- MEDITECH Expanse Navigator searches structured and unstructured chart material (scans, faxes, handwritten notes, abbreviations, misspellings) and ranks/summarizes results inside the chart.
- Oracle PowerForms/Dynamic Documentation emphasize discrete, coded capture over narrative; Epic SmartText manages reusable text blocks as structured content.
- Oracle's new cloud EHR presents a context-filtered patient timeline adapting to clinician behavior and visit type.
- KLAS reports Epic's AI drafting outcomes vary materially by workflow and configuration — an opening for a cleaner, governed implementation.

## Proposed feature set for openChart

Parity floor: encounters, structured notes, problem lists, vitals, custom form engine with discrete-field capture, templates, e-signature. Adopted gaps: pluggable ambient capture service producing review-before-sign drafts with transcript linkage; chart-wide semantic search spanning document attachments and imported records; nurse handoff generation; contextual timeline view. Twist: every AI-drafted artifact carries model/version, source-transcript reference, reviewer identity, and amendment history as first-class fields — governance the incumbents bolt on later.

## Interfaces and boundaries

Consumes: encounter context from orders-and-cds, medication/allergy lists from pharmacy-and-eprescribing, imported outside records via interoperability, attachment text via platform document services. Emits: signed notes and discrete observations to analytics-and-population-health and revenue-cycle (documentation-driven charge hints). Owns the note lifecycle (draft → reviewed → signed → amended); does not own orders or billing codes.

## Alternatives and tensions

Ambient capture could be a thin integration with third-party scribes (Abridge/Suki pattern) instead of native plumbing — faster to ship, weaker provenance and margin. Deep structured capture raises documentation friction that ambient text lowers; both are needed but pull UX in opposite directions. Full AI search requires ingesting unstructured attachments, which expands PHI surface area.

## Open questions

- Build versus integrate ambient capture: partner-first (Suki/Dragon pattern) or first-party pipeline?
- How much structured-capture enforcement survives contact with real clinician workflows?
- Does AI chart search run on-device, in-cluster, or via external embedding services — and what does each cost the security posture?

## Relationships

Clustered in [Synthesis: Clinical Core](openchart-feature-list-synthesis-clinical-core.md). Adjacent: [Clinical Orders And Decision Support](openchart-feature-list-orders-and-cds.md), [Clinical AI And Governance](openchart-feature-list-clinical-ai.md), [Platform, Security And Deployment](openchart-feature-list-platform-and-security.md).
