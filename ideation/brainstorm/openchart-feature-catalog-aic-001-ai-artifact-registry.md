# AI Artifact Registry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Registers every AI output as a typed, provenance-bearing artifact that can be reviewed, traced, amended, and audited.
Topics: openchart-feature-catalog, clinical-ai, frappe, ai-artifacts
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-001 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Artifact lineage graph** — Visualize which source records, prompts, models, and human decisions produced a retained output.

## Focus

This feature isolates the durable object shared by all clinical AI capabilities without treating generated content as accepted clinical truth.

## Behavior

- Each generation creates a typed artifact with capability, model identifier and version, prompt-context digest, output, confidence, timestamps, and source links.
- States are Generated, In Review, Accepted, Rejected, Superseded, Retracted, or Expired.
- Reviewers can compare generated, edited, and accepted text while preserving every version.
- Acceptance records the responsible human, time, disposition, and destination record.
- An artifact cannot directly submit an order, diagnosis, message, or signed note.
- Missing model or context provenance fails generation closed and exposes an operator error.

## Frappe realization

- **DocTypes:** submittable `OC AI Artifact` with naming series `AIA-.YYYY.-.#####`, typed output JSON, confidence, model/version Links, context digest, source child table, and successor/retraction links.
- **Workflow:** Generated → In Review → Accepted/Rejected; Accepted → Superseded/Retracted through immutable event records.
- **Roles/permissions:** `OC AI User` reads assigned artifacts, `OC AI Reviewer` resolves them, and `OC AI Auditor` reads provenance at permlevel 1.
- **Hooks/API/surfaces:** `validate` requires provenance; guarded `open_chart.api.v1.ai.create_artifact` is the write surface; Desk list, timeline, and Script Report expose lineage and state.

## Boundaries

Owns: AI output identity, lifecycle, provenance, and review disposition. Consumes: source references, model metadata, prompt context, and reviewer decisions. Emits: traceable accepted or rejected artifacts. Does not own: destination clinical-record authority or autonomous action.

## Open questions

- Which artifact payloads require full text retention versus a digest plus destination snapshot?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Prompt And Context Audit Capture](openchart-feature-catalog-aic-021-prompt-context-audit-capture.md)
