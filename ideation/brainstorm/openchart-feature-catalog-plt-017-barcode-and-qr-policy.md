# Barcode And QR Policy — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Configures approved barcode and QR symbologies, payload contracts, labels, and verification rules by use case.
Topics: openchart-feature-catalog, platform, frappe, barcode-qr
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-017 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Scanner compatibility suite** — Test generated symbols against registered device profiles before rollout.

## Focus

This feature isolates code-generation policy so labels and documents encode stable, minimum-necessary identifiers rather than ad hoc text.

## Behavior

- Administrators define a use case, symbology, payload schema, dimensions, error correction, human-readable text, and expiry behavior.
- Policies are scoped by site, DocType, and output format with explicit precedence.
- Preview uses synthetic identifiers and checks maximum payload length and print density.
- Policies move through Draft, Review, Active, Retired, and Superseded states.
- Raw sensitive identifiers and credentials are prohibited; resolvable tokens must be signed, scoped, and expiring where appropriate.
- Scan verification reports invalid, expired, or unknown codes without exposing the underlying record to unauthorized users.

## Frappe realization

- **DocTypes:** `OC Code Generation Policy` stores use case, barcode field type or QR renderer, payload JSON schema, scopes, dimensions, and status.
- **Hooks/API:** `open_chart.api.v1.platform.generate_code` validates authority and policy; a whitelisted resolver enforces token scope and expiry.
- **Surface:** policy preview embeds generated symbols in approved Print Formats and tests synthetic scanner inputs.
- **Permissions:** Platform Configuration Administrator manages policy; ordinary users generate codes only through permitted business actions.

## Boundaries

Owns: symbol and payload policy plus code rendering. Consumes: stable identifiers, print context, and signing service. Emits: barcode or QR images and verification outcomes. Does not own: source record identity or scanner hardware.

## Open questions

- Which use cases require offline-verifiable signed payloads rather than online lookup tokens?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Print Format Designer](openchart-feature-catalog-plt-016-print-format-designer.md) · [Document Numbering Series Administration](openchart-feature-catalog-plt-042-document-numbering-series-administration.md)
