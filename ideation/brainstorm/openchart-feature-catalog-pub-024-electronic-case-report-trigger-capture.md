# Electronic Case Report Trigger Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures explainable electronic case-report triggers from accepted problem and laboratory context and routes candidates for governed reporting.
Topics: openchart-feature-catalog, public-health, frappe, ecr-trigger
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-024 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Trigger release sandbox** — Replay synthetic records against candidate trigger versions before activation.

## Focus

Versioned trigger detection and evidence capture, not autonomous case diagnosis or disclosure.

## Behavior

- Accepted coded problems or laboratory results are evaluated against the active jurisdiction trigger release.
- A trigger record identifies rule, source version, matching values, evaluation time, and jurisdiction.
- Outcomes are candidate, excluded, duplicate, indeterminate, promoted-to-report, and superseded.
- Missing demographics or ambiguous code mappings preserve an indeterminate candidate for review.
- Authorized users may disposition a trigger with reason but cannot alter source evidence.
- Rule changes create new evaluations and never rewrite prior trigger history.

## Frappe realization

- **DocTypes:** Add `OC eCR Trigger Release`, child rules, and immutable `OC eCR Trigger Event` linked to source Dynamic Links.
- **Workflow:** Govern rule releases through test and clinical review; route trigger candidates with Assignment Rules.
- **Hooks:** Enqueue evaluation after accepted condition/result events and deduplicate by source version plus rule release.
- **Surfaces:** Provide evidence drill-down, trigger worklist Query Report, and synthetic conformance Script Report.

## Boundaries

Owns: trigger rules, evaluations, and dispositions. Consumes: accepted problems, labs, jurisdiction, and rule content. Emits: case-report candidates. Does not own: diagnosis, external disclosure, or report completion.

## Open questions

- Which trigger content can be distributed openly and kept current by first-party releases?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
