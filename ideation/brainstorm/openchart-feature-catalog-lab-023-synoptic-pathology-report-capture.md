# Synoptic Pathology Report Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures narrative and structured synoptic pathology sections with specimen-part lineage, sign-out, and amendment history.
Topics: openchart-feature-catalog, laboratory, frappe, pathology
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-023 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Synoptic Pathology Report Capture assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates pathology report composition and sign-out as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Pathologist supplies case, specimen parts, gross description, microscopic findings, diagnosis, synoptic template version, signers, and attachments.
- The system produces a signed pathology report with discrete sections and retained narrative and exposes its current state to permitted users.
- The governed lifecycle is Accessioned → In Process → Preliminary → Final → Addended or Amended; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Addenda and amended diagnoses create linked successors and notify affected recipients without overwriting prior sign-out.

## Frappe realization

- **DocTypes:** `OC Pathology Report` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Accessioned → In Process → Preliminary → Final → Addended or Amended; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Pathologist` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.synoptic_pathology_report_capture` is the supported write method, with allowlisted `/api/resource/OC%20Pathology%20Report` reads and a Desk worklist or report.

## Boundaries

Owns: pathology report composition and sign-out. Consumes: specimen accessions, approved templates, terminology, and signer credentials. Emits: a signed pathology report with discrete sections and retained narrative. Does not own: image analysis, staging authority, or downstream treatment planning.

## Open questions

- Which organization-level policy values and exception thresholds for synoptic pathology report capture must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
