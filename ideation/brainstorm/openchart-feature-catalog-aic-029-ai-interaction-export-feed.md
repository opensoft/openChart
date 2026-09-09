# AI Interaction Export Feed — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Exports machine-readable AI interactions, provenance, review, and action-boundary events for audit and oversight systems.
Topics: openchart-feature-catalog, clinical-ai, frappe, audit-export
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-029 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Regulator-ready evidence package** — Produce a signed bounded export for a capability, incident, time range, and site.

## Focus

This feature isolates a portable audit feed comparable across models and capabilities.

## Behavior

- Authorized auditors select site, capability, actor, patient, incident, artifact, or time range within purpose-limited permissions.
- Export records invocation, model and prompt versions, source manifests, output digest or payload policy, confidence, human disposition, edits, escalation, and destination links.
- Events are ordered, uniquely identified, schema-versioned, and include correction or retraction references.
- PHI fields follow export purpose, minimum-necessary policy, and recipient authorization.
- Large exports run asynchronously with manifest, row counts, checksums, and failure report.
- Export never implies that a generated artifact was clinically accepted.

## Frappe realization

- **DocTypes:** `OC AI Audit Export` stores filters, purpose, authorization, schema version, status, manifest, checksum, Attach output, and requester.
- **Workflow:** Requested → Privacy Review → Approved → Generating → Available/Failed/Expired.
- **Roles/permissions:** `OC AI Auditor` requests; `OC Privacy Reviewer` approves PHI-bearing exports; download URLs expire.
- **Jobs/API:** rq streams JSONL/NDJSON; `open_chart.api.v1.ai.exports` supports request and status; `on_submit` freezes manifest and logs download events.

## Boundaries

Owns: portable AI audit-event projection and export evidence. Consumes: invocation, artifact, review, policy, and incident records. Emits: authorized machine-readable feed. Does not own: source systems or recipient compliance.

## Open questions

- Which interoperable event vocabulary should be adopted without losing openChart-specific human-gate semantics?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Prompt And Context Audit Capture](openchart-feature-catalog-aic-021-prompt-context-audit-capture.md)
