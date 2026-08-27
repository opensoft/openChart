# Dispensing Label Printing — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Generates pharmacist-reviewed dispensing labels with patient directions, product facts, warnings, and native barcode identifiers.
Topics: openchart-feature-catalog, eprescribing, frappe, dispensing-labels
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-042 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Accessible label variants** — Large-print, multilingual, pictogram, and low-literacy renditions could share one verified content snapshot.

## Focus

This feature isolates controlled label composition, preview, print, and reprint evidence. The label reflects a verified dispense and never becomes a substitute for the signed prescription record.

## Behavior

- Staff generate a label from a prepared dispense using patient, pharmacy, product, quantity, SIG, prescriber, date, and required warnings.
- The preview shows exact line wrapping, truncation checks, language, printer stock, and barcode content.
- A pharmacist verifies the label content against the dispense before first print.
- Native barcode fields encode only approved identifiers and avoid unnecessary patient information.
- Printer failure leaves the dispense in a recoverable label-pending state without duplicating the dispense.
- Reprints require a reason and record user, time, printer, template version, and copy count.

## Frappe realization

- **DocTypes:** `OC Dispensing Label` links `OC Dispense` and stores immutable content snapshot, barcode fields, template, language, print events, and status.
- **Workflow:** Draft Preview → Pharmacist Verified → Printed, with Failed and Reprint Review actions.
- **Surfaces:** Jinja Print Formats sized for label stock, PDF/print service integration, and native Frappe Barcode fields support rendering.
- **Permissions/hooks:** Pharmacists verify; technicians print approved labels; print callbacks and audit hooks capture outcomes.

## Boundaries

Owns: label rendition, verification, barcode content, and print history. Consumes: verified dispense, SIG, product, and pharmacy policy. Emits: physical label and audit events. Does not own: prescription authority or printer hardware behavior.

## Open questions

- Which label content and accessibility rules must be jurisdiction-specific?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [In-House Dispensary Dispensing Record](openchart-feature-catalog-phr-036-in-house-dispensary-dispensing-record.md)
