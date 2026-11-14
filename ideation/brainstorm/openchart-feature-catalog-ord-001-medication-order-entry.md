# Medication Order Entry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures complete medication orders with structured dose, route, frequency, indication, and dispensing instructions.
Topics: openchart-feature-catalog, cpoe, frappe, medication-orders
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-001 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Dose calculator handoff** — Prefill a reviewable dose from weight or body-surface inputs without placing the order autonomously.

## Focus

This feature isolates clinician entry of a medication order as a complete, reviewable clinical instruction.

## Behavior

- Authorized prescribers select a medication concept and enter dose, unit, route, frequency, indication, start time, duration, and dispense details.
- Required fields vary by formulation and inpatient versus discharge context.
- The composer displays allergy, interaction, formulary, and dose guidance before signature.
- Draft orders may be edited; signed orders become immutable accepted records and corrections use succession.
- Missing units, impossible schedules, or inactive concepts block signing with field-specific errors.
- Every CDS suggestion remains optional until the prescriber explicitly accepts and signs it.

## Frappe realization

- **DocTypes:** submittable `OC Clinical Order` with naming series `ORD-.YYYY.-`, order_class `Medication`, patient, encounter, concept, dose, route, schedule, indication, provenance, and supersedes fields; child `OC Medication Instruction` holds dispense details.
- **Workflow:** Draft → Pending Signature → Active, with Reject and succession-based Amend actions; submission creates the accepted order.
- **Roles/permissions:** `OC Prescriber` creates and submits; `OC Pharmacist` reads and clarifies; permlevel 1 protects provenance and signature fields.
- **Hooks/API/surface:** `validate` normalizes units, `doc_events.on_submit` fires registered CDS rules, and guarded `open_chart.api.v1.orders.submit` plus `/api/resource/OC Clinical Order` filtered reads back the medication composer.

## Boundaries

Owns: medication-order intent and instructions. Consumes: patient context, medication terminology, privileges, and CDS responses. Emits: a signed medication order. Does not own: dispensing or administration.

## Open questions

- Which medication terminology and unit profiles are mandatory for the first release?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Order-Time Alert Orchestration](openchart-feature-catalog-ord-048-order-time-alert-orchestration.md)
