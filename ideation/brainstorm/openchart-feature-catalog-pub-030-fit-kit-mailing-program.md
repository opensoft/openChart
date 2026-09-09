# FIT Kit Mailing Program — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Manages fecal immunochemical test kit enrollment, mailing, specimen return, result linkage, and nonreturn follow-up.
Topics: openchart-feature-catalog, public-health, frappe, fit-kit-program
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-030 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Return-label tracking** — Reconcile carrier events with specimen receipt while minimizing disclosed identity.

## Focus

Closed-loop operational handling of one mailed FIT kit from eligibility confirmation to result review.

## Behavior

- Program staff confirm a reviewed colorectal screening gap, mailing address, consent, and kit eligibility.
- Each kit records manufacturer, lot, expiry, unique identifier, mailed date, and return deadline.
- States are prepared, mailed, delivered, returned, unsuitable, resulted, nonreturned, cancelled, and closed.
- Returned specimens link to laboratory order and result without duplicating the result source of truth.
- Nonreturn reminders follow bounded cadence and communication preferences.
- Positive, indeterminate, or unsuitable results create accountable clinical follow-up tasks.

## Frappe realization

- **DocTypes:** Add `OC FIT Kit Episode` with kit identifiers, mailing events, order/result Links, reminders, and outcome.
- **Workflow:** Use operational states with assignments for nonreturn and clinical-result review.
- **Permissions:** Program users manage logistics; `OC Clinician` handles result disposition; addresses and results use separate permlevels.
- **Surfaces:** Provide barcode labels, mailing batches, Calendar/List views, nonreturn Query Report, and completion Dashboard Charts.

## Boundaries

Owns: kit logistics and program follow-up. Consumes: reviewed gap, address, consent, inventory identity, orders, and results. Emits: mailing events and tasks. Does not own: laboratory processing, diagnosis, or general shipping operations.

## Open questions

- Should kit stock reuse Frappe inventory or a purpose-specific clinical lot ledger?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
