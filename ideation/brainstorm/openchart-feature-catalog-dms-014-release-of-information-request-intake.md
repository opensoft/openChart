# Release-of-information Request Intake — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures and validates requests for patient records with requester authority, scope, purpose, dates, due basis, and identity evidence.
Topics: openchart-feature-catalog, documents, frappe, roi-intake
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-014 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Portal authorization intake** — Let patients submit scoped requests and identity evidence through a secure Web Form.

## Focus

This feature isolates governed intake and authorization review before any record selection or disclosure occurs.

## Behavior

- A patient, proxy, legal requester, or staff member submits requester identity, recipient, purpose, scope, date range, format, and delivery preference.
- Intake records the authority basis and attaches authorization, subpoena, court order, or identity evidence as applicable.
- A Release Specialist validates patient match, requester authority, signature, scope, expiration, and statutory due date.
- Deficient requests enter Clarification Required with specific missing items and paused or continuing deadline basis.
- Approved requests freeze a versioned fulfillment scope; denied or withdrawn requests retain reason and notice evidence.
- Sensitive classes may require segment-specific authorization or Privacy Officer review.
- Intake never exposes records or promises completeness before fulfillment review.

## Frappe realization

- **DocTypes:** `OC ROI Request` (naming series `OCROI-.YYYY.-.#####`, patient, requester_type, authority_basis, scope JSON, due_at, delivery_method, state) with child evidence and requested-class rows.
- **Files/forms:** Private File attachments hold authorization evidence through `open_chart.documents.on_file`; a Frappe Web Form supports patient intake with guarded upload tokens.
- **Workflow:** Received → Identity Review → Authorization Review → Approved, with Clarification Required, Denied, Withdrawn, and Cancelled states.
- **Roles/permissions:** Release Specialist processes; Privacy Officer approves exceptions; Patient user can view own portal request; legal evidence uses permlevel 2.
- **API/surfaces:** `open_chart.api.v1.documents.submit_roi_request`; Desk ROI workspace, SLA Number Cards, and request acknowledgment Print Format.

## Boundaries

Owns: request identity, authority evidence, scope, due basis, and intake disposition. Consumes: patient/proxy identity and policy. Emits: approved versioned fulfillment scope. Does not own: document selection, legal interpretation, payment, or delivery channel operation.

## Open questions

- Which due-date rules are configurable by jurisdiction and request authority type?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [ROI Fulfillment Packet Assembly](openchart-feature-catalog-dms-015-roi-fulfillment-packet-assembly.md)
