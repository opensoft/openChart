# Evidence Citations For CDS Rules — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Attaches versioned, reviewable evidence citations and applicability notes to CDS rule artifacts and user-facing guidance.
Topics: openchart-feature-catalog, cpoe, frappe, cds-evidence
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-061 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Citation freshness monitor** — Flag withdrawn, superseded, or overdue evidence for rule-owner review.

## Focus

This feature isolates the provenance bridge between a decision-support rule and its supporting evidence.

## Behavior

- Authors attach citation title, publisher, identifier or URL, publication date, accessed date, version, excerpt location, and applicability note.
- Reviewers can distinguish primary evidence, guideline, regulatory source, local policy, and expert consensus.
- At least one approved rationale source is mandatory for activation unless an exception is documented and approved.
- User-facing alerts expose concise citation labels and optional details without overwhelming the order composer.
- Citation updates create a successor rule review rather than rewriting active-version provenance.
- Broken links do not erase citation metadata and create stewardship tasks.

## Frappe realization

- **DocTypes:** `OC CDS Evidence Citation` with source_type, bibliographic fields, URL/identifier, version, applicability, status, checked_at, and provenance; rules link citations by child table.
- **Workflow:** Draft → Verified → Active → Superseded/Withdrawn.
- **Roles/permissions:** authors propose; `OC Evidence Reviewer` verifies; alert consumers read approved citation summaries.
- **Scheduler/API/surface:** scheduled link/freshness checks create review assignments; registry and alert APIs return citation metadata under allowlists.

## Boundaries

Owns: evidence citation metadata, verification, and freshness. Consumes: external publications and local policies. Emits: rule-linked rationale sources and review signals. Does not own: publication content or clinical endorsement.

## Open questions

- Which evidence-source changes require immediate rule suspension versus expedited review?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [CDS Rule Version And Provenance](openchart-feature-catalog-ord-046-cds-rule-version-and-provenance.md)
