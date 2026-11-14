# Pregnancy And Lactation Warnings — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents evidence-based pregnancy and lactation warnings using time-bounded patient context, uncertainty, and medication-specific guidance.
Topics: openchart-feature-catalog, eprescribing, frappe, reproductive-safety
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-033 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Shared-decision documentation prompt** — A reviewed counseling template could cite the warning evidence and patient preferences.

## Focus

This feature isolates reproductive safety review for prescribing. It avoids binary assumptions about pregnancy, sex, or feeding status and requires human confirmation when context is missing or sensitive.

## Behavior

- The engine checks candidate medications against effective pregnancy and lactation guidance.
- Patient context distinguishes confirmed, possible, not pregnant, unknown, postpartum, lactating, not lactating, and declined-to-answer where represented.
- Warnings show source, evidence version, gestational or postpartum applicability, and uncertainty.
- Missing or stale status prompts respectful review without forcing disclosure or inferring status from demographics alone.
- Severe findings require prescriber disposition and optional counseling or monitoring documentation.
- No warning automatically discontinues therapy, changes contraception, or modifies the prescription.

## Frappe realization

- **DocTypes:** `OC Reproductive Safety Rule` is versioned; safety evaluations link effective pregnancy-status records and preserve minimum necessary snapshots.
- **Permissions:** Sensitive context uses restricted permlevels and purpose-based access; prescribers disposition findings.
- **Hooks:** Candidate or status changes invalidate evaluations; `before_submit` enforces freshness policy.
- **Surfaces:** Privacy-aware warning card and evidence drawer avoid exposing sensitive status in broad list views.

## Boundaries

Owns: medication-to-reproductive-context warning and disposition. Consumes: time-bounded patient context and evidence rules. Emits: explainable findings and counseling prompts. Does not own: pregnancy determination, reproductive counseling, or autonomous therapy change.

## Open questions

- How should unknown or declined status affect hard-stop policy for high-risk medications?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Pharmacogenomic Drug-Gene Alerts](openchart-feature-catalog-phr-034-pharmacogenomic-drug-gene-alerts.md)
