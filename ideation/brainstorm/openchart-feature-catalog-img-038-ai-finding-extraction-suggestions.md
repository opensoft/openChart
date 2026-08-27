# AI Finding-extraction Suggestions — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Surfaces model-generated candidate imaging findings beside source evidence with provenance, confidence, human disposition, and no autonomous chart action.
Topics: openchart-feature-catalog, imaging, frappe, ai-finding-extraction
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-038 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Suggestion calibration dashboard** — Compare accepted, edited, rejected, and missed suggestions by model version and study cohort.

## Focus

This feature isolates assistive extraction from images or report text while a qualified human remains the sole clinical author.

## Behavior

- A configured model run produces candidate finding text, location, attributes, source references, confidence, and limitations.
- The interface labels suggestions as unverified and separates them from clinician-authored report content.
- The radiologist may accept, edit, reject, or ignore each candidate; no candidate enters the report automatically.
- Every disposition records user, time, original output, resulting text, model, version, inputs, and execution source.
- Missing provenance, unsupported study type, stale model output, or patient mismatch prevents presentation.
- Model failure never blocks ordinary reporting and creates no orders, alerts, diagnoses, or follow-up records.

## Frappe realization

- **DocTypes:** `OC Imaging AI Run` and child `OC AI Finding Suggestion` store model provenance, input references, output, confidence, limitations, and disposition.
- **Workflow:** Requested → Processing → Available → Reviewed, with Failed, Invalidated, and Withdrawn states.
- **Roles/permissions:** integrations create runs; radiologists review; model administrators manage registrations but cannot accept findings.
- **API/jobs/surfaces:** RQ invokes approved adapter; report workspace displays a quarantined suggestion pane; guarded accept action copies reviewed text with provenance.

## Boundaries

Owns: AI-run provenance, candidate suggestions, and human dispositions. Consumes: authorized image or report references and model output. Emits: reviewed text candidates and quality data. Does not own: autonomous interpretation, report signature, alerts, diagnoses, or actions.

## Open questions

- Which source-reference granularity is required for a suggestion to be reviewable and auditable?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
