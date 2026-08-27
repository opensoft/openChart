# Clinical Alert Override Documentation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures accountable, severity-aware prescriber dispositions for overridable medication safety findings without weakening non-overridable controls.
Topics: openchart-feature-catalog, eprescribing, frappe, alert-overrides
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-035 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Alert-governance feedback report** — Safety committees could review de-identified override patterns by rule and reason.

## Focus

This feature isolates the human disposition record shared across interaction, allergy, dose, organ, reproductive, and pharmacogenomic findings. It distinguishes acknowledge, override, resolve, and unable-to-evaluate outcomes.

## Behavior

- Each alert presents severity, evidence, source data, policy, and allowed actions before disposition.
- Non-overridable findings offer correction or escalation but no hidden bypass.
- Overridable findings require a coded reason, narrative when policy requires it, signer, and timestamp.
- Monitoring, counseling, consultation, or follow-up commitments can create assigned tasks with due dates.
- Material prescription or patient-context changes invalidate prior dispositions and rerun the check.
- Governance reports aggregate patterns without feeding autonomous clinical actions or exposing unnecessary patient detail.

## Frappe realization

- **DocTypes:** `OC Safety Finding Disposition` links finding, actor, reason code, narrative, follow-up tasks, prescription digest, and policy version.
- **Workflow:** Open → Reviewed → Resolved/Overridden/Escalated; immutable submitted dispositions are superseded when context changes.
- **Roles:** Prescribers disposition clinical alerts; safety officers review aggregate reports but cannot alter signed decisions.
- **Surfaces/hooks:** Standard override dialog, `before_submit` completeness checks, Assignment Rules, and Script Reports support accountable use.

## Boundaries

Owns: alert disposition, override evidence, and follow-up commitment. Consumes: safety findings and site policy. Emits: signed decisions, tasks, and aggregate governance data. Does not own: rule content, clinical choice, or bypass of mandatory controls.

## Open questions

- Which override reason sets should be shared across alert types versus specialized?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Drug-Drug Interaction Checking](openchart-feature-catalog-phr-028-drug-drug-interaction-checking.md)
