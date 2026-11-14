# Duplicate-Record Detection Assist — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Scores potential duplicate patient or clinical records and routes candidates to authorized human reconciliation queues.
Topics: openchart-feature-catalog, clinical-ai, frappe, duplicate-detection
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-017 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Feature contribution view** — Explain which matching fields raised or lowered a candidate score without revealing restricted values.

## Focus

This feature isolates machine-learning assistance for candidate detection while prohibiting silent merge or deletion.

## Behavior

- Authorized users or scheduled jobs scan a permitted record class for likely duplicate pairs.
- Candidates show score band, matching and conflicting attributes, model version, and source freshness.
- Reviewers mark Not Duplicate, Needs Evidence, Confirmed Candidate, or forward to an existing reconciliation workflow.
- No score merges identities, deletes records, or chooses the authoritative value.
- Protected or sensitive fields are masked according to reviewer permission.
- Model upgrades rescore in a new run and preserve prior dispositions.

## Frappe realization

- **DocTypes:** `OC AI Duplicate Candidate` stores dynamic record Links, score, explanation JSON, run, model, reviewer, and disposition.
- **Workflow:** Detected → Under Review → Not Duplicate/Needs Evidence/Confirmed Candidate → Reconciliation Handoff.
- **Roles/permissions:** `OC Identity Reviewer` handles patient candidates; domain record stewards handle nonidentity candidates.
- **Jobs/surfaces:** scheduler_events enqueue bounded scans; Script Report and review form show permission-filtered comparisons; handoff API never performs merge itself.

## Boundaries

Owns: duplicate likelihood and review disposition. Consumes: permitted matching attributes. Emits: human-reviewed reconciliation candidate. Does not own: identity merge, record deletion, or authority selection.

## Open questions

- Should confirmed false positives suppress only the pair or influence future evaluation sets?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Correction Feedback For Evaluation](openchart-feature-catalog-aic-037-correction-feedback-for-evaluation.md)
