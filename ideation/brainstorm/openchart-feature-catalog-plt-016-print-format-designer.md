# Print Format Designer — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets administrators design, test, approve, and version printable document formats using governed Frappe-native tools.
Topics: openchart-feature-catalog, platform, frappe, print-format-design
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-016 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Representative output regression set** — Compare rendered synthetic PDFs before a format version is promoted.

## Focus

This feature isolates low-code output layout while preserving source-record semantics, permissions, and accepted-version provenance.

## Behavior

- Print administrators select an allowlisted DocType, page settings, published letterhead, fields, labels, and approved variables.
- Builder mode supports drag-and-drop layouts; advanced Jinja mode is restricted to reviewed template authors.
- Preview renders synthetic records across empty, long-text, multi-page, and translated cases.
- Formats move through Draft, Review, Published, Retired, and Superseded states.
- Publishing validates field permissions and prevents hidden or sensitive values from bypassing the requesting user's access.
- Rendering errors return a safe message and correlation ID while retaining the selected format version for diagnosis.

## Frappe realization

- **DocTypes:** native Print Format is wrapped by `OC Print Format Release` with target DocType, version, letterhead Link, test cases, state, and digest.
- **Surface:** extend Frappe Print Format Builder and Jinja preview with permission simulation and PDF snapshots.
- **Permissions:** Print Designer authors; Print Approver publishes; runtime rendering retains source DocType permissions.
- **Promotion:** approved Print Format records and releases export as fixtures; incompatible changes use patches with rollback snapshots.

## Boundaries

Owns: printable layout versions and release evidence. Consumes: permitted fields, branding, translations, and variables. Emits: native Print Formats and PDFs. Does not own: source record values, legal signature authority, or delivery.

## Open questions

- Which regulated outputs require immutable format retention beyond ordinary version history?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Site Letterhead And Branding](openchart-feature-catalog-plt-015-site-letterhead-and-branding.md) · [Barcode And QR Policy](openchart-feature-catalog-plt-017-barcode-and-qr-policy.md)
