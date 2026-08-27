# Preparation Instruction Generation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Generates patient-specific imaging preparation instructions from the scheduled study, protocol, and safety requirements for human review and delivery.
Topics: openchart-feature-catalog, imaging, frappe, preparation-instructions
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-004 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Comprehension confirmation** — Record a patient's acknowledgment of high-impact preparation steps.

## Focus

This feature isolates governed preparation content and its patient-specific rendering.

## Behavior

- Approved protocol and appointment details select a versioned instruction template.
- Rules merge fasting, hydration, medication, arrival, clothing, transportation, and contrast directions.
- Staff review generated content before release when study policy requires it.
- Delivery records channel, language, template version, recipient, timestamp, and outcome.
- Rescheduling or reprotocoling marks obsolete instructions and generates a replacement when content changes.
- Missing translations or unresolved safety requirements create visible tasks rather than silently omitting guidance.

## Frappe realization

- **DocTypes:** `OC Imaging Preparation Plan` with child `OC Preparation Step`, template version Link, language, and delivery status.
- **Workflow:** Generated → Review Required → Approved → Delivered → Superseded.
- **Roles/permissions:** imaging coordinators approve; patients and proxies receive only authorized portal views; template managers edit source content.
- **Hooks/API/surfaces:** background jobs regenerate on governed events; Notification and Print Format surfaces deliver content; API returns the current approved plan.

## Boundaries

Owns: rendered preparation plan and delivery evidence. Consumes: protocol, appointment, language, consent, and safety state. Emits: patient instructions and unresolved-readiness tasks. Does not own: clinical medication management or transport fulfillment.

## Open questions

- Which preparation changes require direct staff contact instead of routine re-notification?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
