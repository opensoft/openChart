# Prescription Print Report — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Produces a signed, tamper-evident prescription report when paper or PDF fallback is permitted and records every rendition.
Topics: openchart-feature-catalog, eprescribing, frappe, prescription-printing
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-051 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Verification QR** — A minimal QR code could resolve to an authenticated validity check without exposing prescription details publicly.

## Focus

This feature isolates human-readable prescription rendition and print control. Printing does not change electronic transmission status and is blocked where law or site policy forbids it.

## Behavior

- Authorized users choose an eligible signed prescription and a permitted print purpose.
- The report contains patient, prescriber, medication, SIG, quantity, refills, dates, identifiers, signature evidence, and required legal text.
- Controlled-substance, copy, watermark, security-paper, and jurisdiction rules are evaluated before rendering.
- Preview shows the exact template version and marks duplicate or informational copies appropriately.
- Each print or PDF generation records actor, purpose, time, copy number, template, and output digest.
- Revoked, cancelled, superseded, or already-transmitted prescriptions show status warnings and may be blocked by policy.

## Frappe realization

- **DocTypes:** `OC Prescription Rendition` stores purpose, template version, sequence, digest, output reference, and status against submitted `OC Prescription`.
- **Surfaces:** Governed Jinja Print Formats, Letter Heads, PDF generation, and printer integration render jurisdiction-specific reports.
- **Permissions/API:** Prescribers and delegated print roles use a guarded rendition method; direct generic print is overridden for this DocType.
- **Hooks:** Policy checks and structured audit events run before output; files inherit clinical retention and access controls.

## Boundaries

Owns: prescription rendition, policy check, and print audit. Consumes: signed prescription, jurisdiction policy, and template. Emits: controlled paper/PDF artifact. Does not own: pharmacy acceptance or legal validity outside configured policy.

## Open questions

- Which anti-tamper elements can be reliably supported across commodity printers?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Outbound Pharmacy Fax Fallback](openchart-feature-catalog-phr-052-outbound-pharmacy-fax-fallback.md)
