# Shadow-Mode Deployment — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Runs candidate AI capabilities silently against eligible workflows so safety and utility can be measured before user exposure.
Topics: openchart-feature-catalog, clinical-ai, frappe, shadow-mode
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-024 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Counterfactual reviewer sample** — Let blinded reviewers score a bounded sample of shadow outputs without exposing them to end users.

## Focus

This feature isolates pre-activation production observation where outputs cannot influence care.

## Behavior

- An AI governor defines eligible sites, roles, workflows, sampling, duration, and metrics for a shadow deployment.
- Eligible events invoke the candidate asynchronously after the live workflow completes or from a nonblocking snapshot.
- Shadow outputs are hidden from clinical and patient surfaces and cannot create drafts, alerts, assignments, or actions.
- Metrics compare candidate outputs with eventual human outcomes only under approved analysis rules.
- Operators can pause immediately and inspect errors, latency, cost, and stratified performance.
- Promotion requires a separate governed decision with evaluation and fairness evidence.

## Frappe realization

- **DocTypes:** `OC AI Shadow Deployment` stores capability, component versions, scopes, sampling, metrics, dates, and evidence Links; results link to nonclinical artifacts.
- **Workflow:** Draft → Approved → Scheduled → Running → Paused/Completed/Terminated.
- **Roles/permissions:** `OC AI Governor` approves; clinicians do not see patient-level shadow outputs; auditors receive controlled access.
- **Hooks/jobs/reports:** doc_events enqueue sampled snapshots to a shadow rq queue; no clinical write credentials; Dashboard Charts and Script Reports show aggregate performance.

## Boundaries

Owns: silent production evaluation scope and telemetry. Consumes: approved candidate and eligible event snapshots. Emits: non-user-facing evidence. Does not own: activation or any clinical action.

## Open questions

- Which outcome linkages are valid without introducing hindsight bias into shadow evaluation?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Per-Site And Per-Role Enablement](openchart-feature-catalog-aic-025-per-site-per-role-enablement.md)
