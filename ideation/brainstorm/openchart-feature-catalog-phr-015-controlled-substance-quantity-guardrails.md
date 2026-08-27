# Controlled-Substance Quantity Guardrails — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Checks controlled-substance quantity, day supply, dosage-form multipliers, refill limits, and written-versus-numeric agreement before signing.
Topics: openchart-feature-catalog, eprescribing, frappe, quantity-guardrails
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-015 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Jurisdiction rule simulation** — Governance users could test proposed quantity policies against synthetic prescriptions before activation.

## Focus

This feature isolates arithmetic and policy guardrails for controlled-substance quantities. It explains discrepancies and limits but never chooses or changes a clinical quantity automatically.

## Behavior

- The composer calculates expected quantity from dose, frequency, duration, package size, and dosage-form multiplier.
- It compares calculated, entered numeric, written-text, and network-rendered quantities.
- Schedule- and jurisdiction-specific refill, day-supply, and maximum rules are evaluated using an effective policy release.
- Disagreement, impossible fractions, package mismatch, or excess quantity blocks signing or requires a permitted documented override.
- The prescriber must explicitly correct or attest the final quantity; suggestions never mutate signed fields.
- Signed evidence stores inputs, calculation version, policy version, findings, and disposition.

## Frappe realization

- **DocTypes:** `OC Quantity Guardrail Policy` is versioned; `OC Prescription Safety Finding` stores calculations, severity, evidence, and override.
- **Client/server checks:** Client scripts preview arithmetic while server `validate` and `before_submit` perform authoritative evaluation.
- **Permissions:** Policy stewards publish rules; only `OC Prescriber` may disposition overridable findings.
- **Surfaces:** Composer comparison panel and governance Script Report expose calculation details and policy coverage.

## Boundaries

Owns: quantity consistency and configured policy evaluation. Consumes: structured SIG, package metadata, schedule, jurisdiction, and policy release. Emits: explainable findings and signed evidence. Does not own: clinical dose selection or legal advice.

## Open questions

- Which jurisdictional limits can be encoded as hard blocks versus advisory findings?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [DEA Schedule Display](openchart-feature-catalog-phr-016-dea-schedule-display.md)
