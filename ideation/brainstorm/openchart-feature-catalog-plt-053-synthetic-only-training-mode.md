# Synthetic-only Training Mode — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Marks and enforces a site as training-only so records, integrations, communications, and exports accept synthetic identities exclusively.
Topics: openchart-feature-catalog, platform, frappe, training-mode
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-053 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Synthetic-data quality dashboard** — Check scenario diversity and referential integrity without weakening the real-data exclusion gate.

## Focus

This feature isolates an environment-level safety mode that prevents a training site from becoming a shadow clinical system.

## Behavior

- Platform operators set training mode only during site provisioning or an approved empty-site conversion.
- A persistent banner, hostname marker, print watermark, and API response header identify the site as non-production.
- Patient and related identifiers must satisfy synthetic fixture policy, including the `SYN-` discipline and prohibited real-data patterns.
- External messages route only to sinks or allowlisted test destinations; production integrations and credentials remain unavailable.
- Backup, export, print, and file actions retain training labels so artifacts cannot be mistaken for clinical records.
- Disabling training mode requires proof the site is empty and reprovisioned; it is never an ordinary toggle.

## Frappe realization

- **DocTypes:** Single `OC Environment Safety Profile` stores immutable mode, hostname, allowed endpoints, synthetic policy version, and provisioning evidence.
- **Hooks:** validate/before_save guards on patient and clinical DocTypes enforce synthetic identifiers; communication and integration adapters enforce sinks.
- **Client/surfaces:** boot info adds banners; Letter Head and Print Formats apply watermark; APIs add a training-mode header.
- **Permissions:** only Platform Operator may set mode through provisioning API; Site Administrator has read-only visibility.

## Boundaries

Owns: training-only environment invariant and guard evidence. Consumes: site mode, synthetic data policy, and endpoint allowlist. Emits: blocked writes, watermarks, and safe routes. Does not own: synthetic scenario generation or production de-identification.

## Open questions

- Which attachments can be reliably recognized as synthetic without inspecting sensitive content?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Training Sandbox Clone Generator](openchart-feature-catalog-plt-052-training-sandbox-clone-generator.md)
