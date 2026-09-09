# Discrete Genomic Variant Result Return — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Stores source-attributed genomic variants and interpretations discretely so reviewed pharmacogenomic workflows can consume them.
Topics: openchart-feature-catalog, laboratory, frappe, genomic-results
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-025 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Discrete Genomic Variant Result Return assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates discrete genomic variant representation as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Molecular Lab Reviewer supplies assay, genome build, gene, variant nomenclature, zygosity, interpretation, classification, evidence date, source report, and laboratory.
- The system produces immutable variant observations with interpretation-version provenance and exposes its current state to permitted users.
- The governed lifecycle is Received → Normalization Review → Filed → Reinterpreted by Successor; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Unmapped nomenclature, conflicting classifications, and revised interpretations remain distinct and trigger review rather than silent replacement.

## Frappe realization

- **DocTypes:** `OC Genomic Variant Result` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Received → Normalization Review → Filed → Reinterpreted by Successor; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Molecular Lab Reviewer` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.discrete_genomic_variant_results` is the supported write method, with allowlisted `/api/resource/OC%20Genomic%20Variant%20Result` reads and a Desk worklist or report.

## Boundaries

Owns: discrete genomic variant representation. Consumes: genomic reports, terminology, reference builds, and reviewer evidence. Emits: immutable variant observations with interpretation-version provenance. Does not own: drug selection, dosage changes, or autonomous pharmacogenomic decisions.

## Open questions

- Which organization-level policy values and exception thresholds for discrete genomic variant result return must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
