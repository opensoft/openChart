# Document Numbering Series Administration — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Governs collision-safe, site-aware naming series for administrative and clinical document identities.
Topics: openchart-feature-catalog, platform, frappe, naming-series
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-042 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Series capacity forecast** — Warn before a numeric width or annual range is exhausted.

## Focus

This feature isolates Frappe naming-series policy while preserving stable OC identifiers and preventing administrators from renumbering accepted records.

## Behavior

- Platform administrators define an allowlisted DocType, prefix pattern, site or location scope, date tokens, counter width, and effective dates.
- Preview generates synthetic examples and checks collisions against active and retired series.
- Policies move through Draft, Review, Active, Frozen, Retired, and Superseded states.
- Counter allocation is transactional and never reuses a number after failed or cancelled business processing where audit requires uniqueness.
- Existing document names are immutable; a policy change applies only to future records and records the effective boundary.
- Exhaustion or invalid scope fails creation with a clear administrator alert rather than falling back to an unknown series.

## Frappe realization

- **DocTypes:** `OC Naming Series Policy` stores target DocType, pattern, scopes, width, dates, state, and last allocation evidence.
- **Integration:** controlled `autoname` hooks resolve an active policy and use Frappe naming series locking for `OC <Thing>` documents.
- **Permissions:** Naming Series Administrator authors; Platform Approver activates or freezes; ordinary users cannot select arbitrary series.
- **Surface:** preview, collision report, utilization Number Cards, and exhaustion alerts appear in Platform Configuration workspace.

## Boundaries

Owns: naming policy and future identifier allocation. Consumes: DocType, site, location, and current counters. Emits: stable unique document names and allocation evidence. Does not own: external identifiers or record meaning.

## Open questions

- Which document identifiers must remain globally unique across independently operated sites?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Barcode And QR Policy](openchart-feature-catalog-plt-017-barcode-and-qr-policy.md)
