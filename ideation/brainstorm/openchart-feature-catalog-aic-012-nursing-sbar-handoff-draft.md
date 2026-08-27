# Nursing SBAR Handoff Draft — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Drafts a shift-specific SBAR handoff from current chart data for nurse verification before handoff use.
Topics: openchart-feature-catalog, clinical-ai, frappe, sbar-handoff
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-012 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Bedside confirmation mode** — Let incoming and outgoing nurses jointly attest reviewed handoff sections.

## Focus

This feature isolates Situation-Background-Assessment-Recommendation drafting for nursing shift transitions.

## Behavior

- An assigned nurse requests a handoff for a patient, care location, and shift boundary.
- The draft cites recent observations, administrations, orders, events, lines, precautions, and pending tasks.
- Recommendations are clearly labeled as source-derived instructions or generated prompts requiring nurse judgment.
- Outgoing nurses correct and attest the draft; incoming nurses can acknowledge receipt without accepting clinical responsibility for unverified content.
- Stale observations and missing feeds display conspicuous timestamps and gaps.
- The draft cannot administer medication, change orders, complete tasks, or update assessments.

## Frappe realization

- **DocTypes:** `OC AI Nursing Handoff` links patient, care episode, shifts, artifact, source snapshot, section attestations, and acknowledgments.
- **Workflow:** Requested → Pending Outgoing Review → Ready For Handoff → Acknowledged/Expired.
- **Roles/permissions:** assigned nursing teams use user permissions; nurse managers audit exceptions; AI service accounts cannot alter clinical source records.
- **Hooks/jobs/surfaces:** rq generation; shift scheduler may prequeue drafts; bedside Workspace and print format show SBAR, citations, freshness, and acknowledgment.

## Boundaries

Owns: SBAR draft and handoff review evidence. Consumes: permissioned nursing and clinical records. Emits: verified handoff artifact. Does not own: nursing assessment, task completion, orders, or staffing assignments.

## Open questions

- What freshness threshold should force regeneration before handoff acknowledgment?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Confidence-Threshold Routing](openchart-feature-catalog-aic-039-confidence-threshold-routing.md)
