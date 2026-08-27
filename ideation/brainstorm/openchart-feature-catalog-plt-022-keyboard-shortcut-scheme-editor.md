# Keyboard Shortcut Scheme Editor — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Publishes accessible keyboard shortcut schemes with collision detection, scope controls, and user-visible discovery.
Topics: openchart-feature-catalog, platform, frappe, keyboard-shortcuts
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-022 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Assistive-technology compatibility profiles** — Exclude combinations known to conflict with screen readers or operating systems.

## Focus

This feature isolates shortcut configuration for navigation and safe commands while keeping consequential actions confirmable.

## Behavior

- Workspace designers map approved commands to key combinations by Desk page, role, device class, and locale.
- Validation detects duplicate, browser-reserved, operating-system-reserved, and accessibility-conflicting combinations.
- Preview displays the complete scheme and lets testers exercise commands without committing records.
- Schemes move through Draft, Review, Published, Retired, and Superseded states.
- Users can view shortcuts, temporarily disable a scheme, and choose an approved alternative where policy allows.
- Delete, sign, submit, cancel, and other consequential commands still require normal authorization and confirmation.

## Frappe realization

- **DocTypes:** `OC Shortcut Scheme` and child `OC Shortcut Binding` store command key, combination, scope, roles, locale, and state.
- **Client scripts:** a Desk boot payload loads effective bindings and dispatches only registered commands after context checks.
- **Permissions:** Workspace Designer manages schemes; Accessibility Reviewer approves conflicts and alternatives.
- **Surface:** a searchable shortcut overlay and test mode expose active and shadowed bindings.

## Boundaries

Owns: keyboard binding schemes and discovery. Consumes: registered UI commands, role, page context, and locale. Emits: approved client command bindings. Does not own: command authorization or browser behavior.

## Open questions

- Should personal remapping be supported, and how would support teams reproduce it?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Quick Entry Form Customization](openchart-feature-catalog-plt-021-quick-entry-form-customization.md)
