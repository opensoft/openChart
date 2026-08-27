# AI Follow-up Recommendation Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents model-generated follow-up recommendation candidates for clinician acceptance, editing, rejection, and provenance-preserving conversion into report text only.
Topics: openchart-feature-catalog, imaging, frappe, ai-follow-up-suggestions
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-039 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Guideline comparison panel** — Show the recommendation candidate beside approved evidence references and known applicability gaps.

## Focus

This feature isolates AI-assisted recommendation drafting from the human decision that creates a clinical obligation.

## Behavior

- A model may propose follow-up modality, interval, rationale, finding linkage, guideline reference, and applicability caveats.
- Suggestions remain in a quarantined panel and never create registry, recall, scheduling, or communication records.
- The radiologist reviews source finding, patient context, evidence citation, model version, and confidence before disposition.
- Acceptance copies reviewed text and structured values into the report draft with provenance; editing preserves both versions.
- Rejected or ignored candidates remain available for governed quality analysis without appearing clinically accepted.
- Model unavailability or invalid provenance does not block reporting or suppress human-authored recommendations.

## Frappe realization

- **DocTypes:** child `OC AI Follow Up Suggestion` under `OC Imaging AI Run` with finding Link, interval, modality, rationale, evidence, caveats, and disposition.
- **Roles/permissions:** radiologists alone accept clinical content; model operators inspect technical runs without patient-wide report authority.
- **API/surfaces:** report form action copies selected fields only after server permission and context validation; no background hook creates downstream tasks.
- **Audit/reports:** accepted and rejected outputs retain model provenance; aggregate Script Report supports safety review with access controls.

## Boundaries

Owns: AI recommendation candidate, provenance, and human disposition. Consumes: report findings, approved context, and model output. Emits: reviewed report-draft content only. Does not own: recommendation acceptance, registry creation, scheduling, notification, or autonomous action.

## Open questions

- What evidence and context minimum is required before a recommendation candidate may be shown?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
