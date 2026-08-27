# Imaging Order Entry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures imaging requests with modality, anatomy, laterality, contrast, urgency, and a clinically answerable indication.
Topics: openchart-feature-catalog, cpoe, frappe, imaging-orders
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-003 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Protocol recommendation preview** — Let radiology propose a protocol for ordering-clinician approval.

## Focus

This feature isolates safe, complete diagnostic-imaging order capture.

## Behavior

- The ordering clinician selects modality, body site, laterality, contrast plan, urgency, and clinical question.
- Contrast orders require relevant allergy, renal-status, and pregnancy-context review when applicable.
- The composer warns when anatomy or laterality conflicts with the selected procedure.
- Prior comparable studies are shown without automatically suppressing the new order.
- Radiology may request clarification while preserving the original signed wording.
- Unanswered mandatory safety questions block signature and identify the missing evidence.

## Frappe realization

- **DocTypes:** submittable `OC Clinical Order` with order_class `Imaging`; child `OC Imaging Instruction` stores modality, anatomy, laterality, contrast, and safety responses.
- **Workflow:** Draft → Pending Signature → Active → Clarification Requested → In Fulfillment → Completed.
- **Roles/permissions:** `OC Ordering Clinician` submits; `OC Imaging Staff` updates fulfillment and clarification fields but cannot rewrite intent.
- **Hooks/API/surface:** `validate` enforces anatomy fields, `on_submit` invokes CDS, and class/status REST filters plus an Imaging Orders Desk workspace expose worklists.

## Boundaries

Owns: imaging-order intent and safety answers. Consumes: imaging catalog, prior studies, allergies, and labs. Emits: protocol-ready request. Does not own: image acquisition or interpretation.

## Open questions

- Which contrast-risk questions are organization-configurable versus fixed?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Renal Dose Adjustment Guidance](openchart-feature-catalog-ord-058-renal-dose-adjustment-guidance.md)
