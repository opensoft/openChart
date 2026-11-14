# Duplicate Therapy Alerts — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Identifies overlapping medication classes or duplicate diagnostic orders while distinguishing intentional combination therapy.
Topics: openchart-feature-catalog, cpoe, frappe, duplicate-therapy
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-051 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Episode-aware duplicate view** — Group pending, active, and recently completed orders by care episode.

## Focus

This feature isolates clinically meaningful duplication checks at order time.

## Behavior

- Rules compare a draft with active, pending, held, same-basket, and recent orders in configured windows.
- The alert displays the candidate duplicate, status, date, ordering context, and exact match rationale.
- Medication class, test code, anatomy, specimen, and care-setting logic vary by rule type.
- Known intentional combination patterns may downgrade severity only through governed exceptions.
- The clinician may cancel, proceed with coded rationale, or revise timing.
- A technical duplicate caused by replay is handled idempotently before clinical alerting.

## Frappe realization

- **DocTypes:** `OC CDS Rule` type Duplicate Therapy/Test with lookback, status scope, equivalence set, exceptions, owner, and provenance.
- **Roles/permissions:** clinical users see only comparison orders permitted in patient context; curators manage logic separately.
- **Hooks/API/surface:** basket preview and order `on_submit` query indexed patient/order fields; evaluations link compared order identifiers and versions.
- **Reports:** analytics distinguish overridden clinical duplicates from rejected idempotent submissions.

## Boundaries

Owns: duplication evaluation and alert. Consumes: draft and existing orders. Emits: comparison evidence and resolution. Does not own: idempotency or therapeutic appropriateness beyond registered rules.

## Open questions

- Which completed-order lookback windows should vary by test and care setting?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Dose Range Checking](openchart-feature-catalog-ord-052-dose-range-checking.md)
