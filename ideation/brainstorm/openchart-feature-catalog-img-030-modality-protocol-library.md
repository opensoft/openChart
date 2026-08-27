# Modality Protocol Library — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Maintains versioned imaging protocols by modality, study, facility, equipment class, patient factors, and approval lifecycle.
Topics: openchart-feature-catalog, imaging, frappe, protocol-library
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-030 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Protocol diff review** — Compare proposed and active versions with affected order and preparation rules.

## Focus

This feature isolates governed protocol content reused by assignment, performance, safety, and reporting workflows.

## Behavior

- Protocol managers define modality, study, anatomy, contrast, acquisition guidance, preparation, safety prerequisites, and applicability.
- Each published version has an effective period, owning facility, approvers, evidence references, and superseded version.
- Draft changes do not affect active orders or protocol assignments.
- Publication validates conflicting applicability and requires authorized approval.
- Existing assignments retain their selected version; reprotocoling is an explicit clinical action.
- Retired protocols remain readable for historical records but cannot be newly selected.

## Frappe realization

- **DocTypes:** `OC Imaging Protocol` and submittable `OC Imaging Protocol Version` with child steps, safety requirements, contrast plan, and applicability rules.
- **Workflow:** Draft → Clinical Review → Approved → Active → Retired.
- **Roles/permissions:** protocol managers draft; modality leads and radiologists approve; technologists read active versions.
- **Hooks/API/surfaces:** `validate` detects overlap; effective-date scheduler activates approved versions; Query Report shows coverage gaps and expiring versions.

## Boundaries

Owns: protocol definitions, versions, applicability, and approval. Consumes: study and equipment catalogs plus evidence references. Emits: selectable protocol and readiness requirements. Does not own: scanner configuration or patient-specific assignment.

## Open questions

- How should facility-specific overrides inherit from organization-wide protocols without obscuring differences?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
