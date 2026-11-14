# Template Variable Dictionary — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Publishes typed, permission-aware variables for notifications, print formats, help content, and release tours.
Topics: openchart-feature-catalog, platform, frappe, template-variables
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-037 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Variable usage impact map** — List every published asset affected by a proposed variable change.

## Focus

This feature isolates a shared variable contract so low-code templates do not depend on undocumented field paths or unsafe context.

## Behavior

- Template administrators register a variable key, label, type, description, source resolver, allowed purposes, channels, and sensitivity.
- Variables move through Draft, Review, Published, Deprecated, Retired, and Superseded states.
- Preview returns synthetic values and explains availability by actor, record state, purpose, and channel.
- Publication rejects duplicate keys, unbounded HTML, unstable field paths, and resolvers that bypass permissions.
- Deprecated variables remain resolvable for pinned template versions while usage reports drive migration.
- Missing or unauthorized values produce an explicit render error or approved fallback, never an empty misleading clinical statement.

## Frappe realization

- **DocTypes:** `OC Template Variable` stores key, type, resolver registry key, purposes, channels, sensitivity, fallback policy, version, and state.
- **API:** server-side resolver registry returns typed values after source DocType and field-permission checks; arbitrary Jinja object traversal is blocked.
- **Surface:** dictionary browser shows examples, consumers, deprecations, and synthetic preview.
- **Hooks:** validation of Notification Templates, Print Formats, and content assets pins referenced variable versions.

## Boundaries

Owns: typed template variable contracts and resolver governance. Consumes: permitted document context and synthetic examples. Emits: permission-checked render values. Does not own: templates, source records, or recipient selection.

## Open questions

- Should variable versions be pinned individually or inherited from each published template release?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Notification Template Editor](openchart-feature-catalog-plt-014-notification-template-editor.md) · [Print Format Designer](openchart-feature-catalog-plt-016-print-format-designer.md)
