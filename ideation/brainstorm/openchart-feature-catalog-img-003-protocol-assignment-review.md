# Protocol Assignment Review — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Converts an accepted imaging order into a reviewed modality protocol while preserving the order's original clinical intent.
Topics: openchart-feature-catalog, imaging, frappe, protocol-assignment
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-003 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Protocol exception analytics** — Identify studies that repeatedly require deviations from catalog defaults.

## Focus

This feature isolates human protocol selection, modification, approval, and clarification before performance.

## Behavior

- Eligible orders enter a protocoling queue with clinical question, safety data, priors, and requested study.
- A credentialed radiologist or delegated protocoling role selects a versioned protocol and contrast plan.
- Deviations from defaults require a reason and retain both default and selected values.
- Missing information moves the case to Clarification Requested and identifies the responsible party.
- Approved protocols become read-only instructions for scheduling and technologist worklists.
- Reprotocoling after scheduling records impact and never silently overwrites an accepted protocol.

## Frappe realization

- **DocTypes:** `OC Imaging Protocol Assignment` links order and `OC Imaging Protocol Version`, with deviation reason, contrast plan, and approver.
- **Workflow:** Pending Review → Clarification Requested → Approved → Superseded or Cancelled.
- **Roles/permissions:** `OC Radiologist` approves; `OC Protocoling Technologist` drafts where delegated; facility user permissions constrain queues.
- **Hooks/API/surfaces:** `on_submit` emits readiness events; `open_chart.api.v1.imaging.assign_protocol` guards changes; Kanban and Assignment Rules route pending cases.

## Boundaries

Owns: protocol selection and approval evidence. Consumes: order, safety, and protocol-library data. Emits: approved performance instructions. Does not own: acquisition device configuration or the order's clinical intent.

## Open questions

- Which protocols may be approved by delegated technologists versus a radiologist?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
