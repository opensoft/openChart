# Virtual Encounter E-Prescribing Launch — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Launches a governed e-prescribing workflow from a virtual encounter with encounter, authority, and modality context.
Topics: openchart-feature-catalog, telehealth, frappe, virtual-e-prescribing
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-033 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Prescription status return** — Reconcile accepted, rejected, changed, or cancelled network outcomes into the encounter timeline.

## Focus

This feature isolates the virtual-encounter handoff into an approved prescribing service; it does not implement the prescribing network itself.

## Behavior

- An authorized prescriber starts the action from the active encounter and receives patient, medication, allergy, pharmacy, and encounter context.
- The launch verifies prescriber authority, patient identity, encounter state, jurisdiction, and any modality-sensitive policy.
- Clinical details are reviewed by the prescriber; no conversation or questionnaire answer creates a prescription autonomously.
- The adapter returns a correlation identifier and normalized status without copying credentials or sensitive network payloads into logs.
- Cancellation, failure, or incomplete signing leaves an explicit encounter event and no false indication that medication was sent.
- Successful completion links the resulting medication order or external reference to the encounter with provenance.

## Frappe realization

- **DocTypes:** `OC Prescribing Launch` stores encounter, prescriber, jurisdiction result, adapter, correlation ID, status, outcome reference, and timestamps.
- **API/adapters:** a whitelisted launch method issues a scoped context token to a configured partner; callbacks validate signatures and update normalized state idempotently.
- **Permissions/safety:** Prescriber role and provider user permissions gate launch; EPCS or network authentication remains in the prescribing boundary; no automated signing is allowed.

## Boundaries

Owns: encounter-context launch and returned status. Consumes: prescriber authority, chart context, and external prescribing adapter. Emits: linked prescription outcome. Does not own: drug network, EPCS ceremony, or pharmacy routing.

## Open questions

- Which virtual modalities or jurisdictions require additional prescribing attestations before partner launch?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
