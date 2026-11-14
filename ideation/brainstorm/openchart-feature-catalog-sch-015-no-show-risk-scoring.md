# No-show Risk Scoring — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Produces explainable no-show risk estimates for outreach prioritization without restricting patient access automatically.
Topics: openchart-feature-catalog, scheduling, frappe, no-show-risk
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-015 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Intervention evaluation** — Compare outreach outcomes without treating correlation as causation.

## Focus

This feature isolates advisory risk scoring and the safeguards around its operational use.

## Behavior

- Authorized staff see a risk band, score timestamp, model version, and top contributing factors.
- Scores may prioritize supportive outreach but never cancel, deny, delay, or overbook autonomously.
- Missing or stale inputs produce an unavailable state rather than a fabricated low score.
- Protected attributes and prohibited proxies are excluded according to approved governance.
- Staff can record whether outreach occurred and whether the appointment was attended.
- Model drift and subgroup performance are reviewable before a new model version is activated.

## Frappe realization

- **DocTypes:** `OC No Show Risk Assessment` with appointment, model_version, band, factors JSON, generated_at, and disposition.
- **Permissions:** Scheduling Outreach reads operational bands; Model Auditor reads evaluation details; patients do not receive internal scores by default.
- **Automation:** background jobs score eligible appointments; Dashboard Charts and Script Reports monitor calibration and outcomes.

## Boundaries

Owns: advisory attendance-risk evidence. Consumes: approved scheduling history and operational features. Emits: outreach priority. Does not own: booking eligibility or autonomous action.

## Open questions

- Which features and fairness thresholds are acceptable for production scoring?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Appointment Reminder Cadence](openchart-feature-catalog-sch-013-appointment-reminder-cadence.md)
