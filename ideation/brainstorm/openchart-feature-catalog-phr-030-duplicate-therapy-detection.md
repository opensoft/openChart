# Duplicate-Therapy Detection — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Detects ingredient, product, and therapeutic-class duplication between a candidate prescription and the patient's medication context.
Topics: openchart-feature-catalog, eprescribing, frappe, duplicate-therapy
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-030 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Intent-aware overlap review** — Replacement, taper, bridge, and combination intents could reduce noise while retaining deliberate overlap evidence.

## Focus

This feature isolates duplicate-therapy review from broader interaction checking. It explains exact and class-level overlap and requires the prescriber to identify intended versus unintended duplication.

## Behavior

- The engine compares candidate ingredients and therapeutic classes with active, PRN, and recently discontinued medications.
- Findings distinguish exact product, same ingredient, ingredient combination, therapeutic class, and overlapping transition.
- Start/stop dates, taper plans, care setting, and documented replacement intent refine presentation.
- Missing dates or coding make uncertainty visible instead of suppressing a finding.
- The prescriber marks intended combination, replacement, taper overlap, data error, or changes the draft.
- No finding automatically discontinues an existing medication or alters the candidate prescription.

## Frappe realization

- **DocTypes:** `OC Prescription Safety Finding` records duplicate type, related statement/prescription, temporal evidence, severity, and disposition.
- **Hooks:** Medication or date changes trigger deterministic reevaluation; signed prescriptions snapshot related record versions.
- **Permissions:** Prescribers resolve findings; data-quality issues can be assigned to medication reconciliation roles.
- **Surfaces:** Overlap timeline, comparison card, disposition dialog, and unresolved-duplication report support review.

## Boundaries

Owns: duplicate-therapy detection and prescribing disposition. Consumes: candidate prescription, medication statements, prescription history, and class terminology. Emits: overlap findings and reconciliation tasks. Does not own: medication-list correction or automatic discontinuation.

## Open questions

- What temporal window should count recently discontinued therapy for each medication class?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Drug-Drug Interaction Checking](openchart-feature-catalog-phr-028-drug-drug-interaction-checking.md)
