# Order Renewal And Reorder — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Creates a reviewable successor from an existing order while preserving the original record and rechecking current context.
Topics: openchart-feature-catalog, cpoe, frappe, order-renewal
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-023 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Changed-context summary** — Highlight patient, catalog, and policy changes since the prior order was signed.

## Focus

This feature isolates safe reuse of prior order content without cloning prior authority.

## Behavior

- An authorized clinician chooses Renew for continuity or Reorder for a new episode and receives a fresh draft.
- The draft identifies the source order but uses current catalog defaults, patient facts, privileges, and CDS rules.
- Changed, retired, or unavailable fields are highlighted and require correction.
- Prior indications and comments remain visible but are not silently attested as current.
- The clinician explicitly reviews and signs the successor; no expiration event renews automatically.
- The source and successor remain linked in an immutable lifecycle chain.

## Frappe realization

- **DocTypes:** submittable `OC Clinical Order` stores predecessor, relationship_type, copied_fields JSON, and current provenance.
- **Workflow:** source remains Completed/Stopped/Discontinued; successor starts Draft → Pending Signature → Active.
- **Roles/permissions:** current order-class and privilege rules govern successor creation regardless of source access.
- **Hooks/API/surface:** whitelisted `prepare_successor` allowlists copied fields; `validate` and `on_submit` rerun all current checks; timeline displays the chain.

## Boundaries

Owns: successor preparation and lineage. Consumes: prior order plus current policy and patient context. Emits: unsigned successor draft. Does not own: automatic continuity decisions.

## Open questions

- Which historical fields should be visible but never copied into a successor?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Order Duration And Auto-Stop](openchart-feature-catalog-ord-022-order-duration-and-auto-stop.md)
