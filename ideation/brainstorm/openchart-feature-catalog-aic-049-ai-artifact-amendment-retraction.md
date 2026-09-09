# AI Artifact Amendment And Retraction — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Corrects, supersedes, or retracts AI artifacts while preserving lineage to any human-accepted destination records.
Topics: openchart-feature-catalog, clinical-ai, frappe, artifact-corrections
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-049 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Downstream impact checklist** — Route destination-specific review when a retracted artifact contributed to accepted content.

## Focus

This feature isolates post-generation correction without rewriting audit history or silently changing accepted clinical records.

## Behavior

- Authorized reviewers can mark an artifact erroneous, superseded, withdrawn by provider, stale, or retracted with reason and evidence.
- Correction creates an immutable event or successor; original output, review, and destination links remain readable to auditors.
- Unaccepted artifacts become unavailable for promotion immediately.
- Accepted destination records receive an impact-review task but are amended only by their ordinary qualified authority.
- Users viewing a linked artifact see current correction status and successor.
- Bulk provider withdrawals require scoped impact enumeration and incident linkage.

## Frappe realization

- **DocTypes:** `OC AI Artifact Correction` stores artifact, correction type, reason, evidence, successor, incident, destinations, reviewer, and effective time.
- **Workflow:** Proposed → Impact Review → Approved → Applied → Closed; urgent retraction may apply first and require retrospective review.
- **Roles/permissions:** `OC AI Reviewer` proposes; `OC AI Governor` approves bulk/provider corrections; destination owners receive assignments.
- **Hooks/jobs/surfaces:** artifact hooks deny promotion when corrected; rq traces destinations; timeline banners, Notifications, and Script Report show unresolved impacts.

## Boundaries

Owns: artifact correction state and impact routing. Consumes: artifact lineage, provider notices, incidents, and reviewer evidence. Emits: retraction/successor status and human review tasks. Does not own: silent amendment of accepted clinical records.

## Open questions

- Which urgent safety conditions permit immediate retraction before full impact review?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [AI Artifact Registry](openchart-feature-catalog-aic-001-ai-artifact-registry.md)
