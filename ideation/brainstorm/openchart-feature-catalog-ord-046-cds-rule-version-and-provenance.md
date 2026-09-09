# CDS Rule Version And Provenance — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Preserves succession, source evidence, authorship, approvals, and exact runtime version for every CDS evaluation.
Topics: openchart-feature-catalog, cpoe, frappe, cds-provenance
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-046 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Historical replay manifest** — Package the exact rule, value sets, and synthetic inputs needed to reproduce an evaluation.

## Focus

This feature isolates immutable lineage and reproducibility of rule artifacts.

## Behavior

- Authors create successor versions instead of editing active rules in place.
- Each version records predecessor, change rationale, evidence citations, author, owner, reviewers, approval timestamps, and effective interval.
- A semantic diff shows changes to inputs, logic, outputs, severity, and message text.
- Runtime evaluations record exact rule version and referenced value-set versions.
- Withdrawal stops new evaluations while preserving previous evaluation records.
- Imported rule artifacts retain source organization and transformation provenance.

## Frappe realization

- **DocTypes:** `OC CDS Rule` uses stable logical_id plus immutable version and predecessor; `OC CDS Evaluation` links exact version and context digest.
- **Workflow:** successor Draft → Testing → Review → Active; active versions are read-only and succession-based.
- **Roles/permissions:** provenance fields are mandatory and permlevel 2; only publishers set effective intervals.
- **Hooks/API/surface:** `before_save` computes diff/digest, `validate` rejects lineage gaps, and Script Reports show version and evidence history.

## Boundaries

Owns: rule succession and reproducibility metadata. Consumes: authored logic, evidence, and approvals. Emits: immutable evaluable versions. Does not own: clinical truth or runtime orchestration.

## Open questions

- How should shared terminology value-set versions be pinned across rule succession?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Evidence Citations For CDS Rules](openchart-feature-catalog-ord-061-evidence-citations-for-cds-rules.md)
