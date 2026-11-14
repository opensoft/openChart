# PDMP One-Tap Lookup — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Launches or retrieves a state-selected prescription drug monitoring report with purpose, user, patient, and retrieval evidence logged.
Topics: openchart-feature-catalog, eprescribing, frappe, pdmp
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-014 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Multi-state lookup bundle** — Authorized users could request several relevant jurisdictions while retaining separate consent and access evidence.

## Focus

This feature isolates human-initiated PDMP access at prescribing time. It supports state choice and retrieval logging without copying more sensitive report content than policy permits.

## Behavior

- The prescriber invokes PDMP lookup from the patient or prescription context and selects an applicable state when not deterministic.
- The system confirms user authority, patient match, purpose of use, consent or legal basis, and required encounter context.
- The adapter opens single sign-on or retrieves a report according to state capability.
- Access outcome, jurisdiction, requester, purpose, patient identifiers used, timestamps, and external correlation are logged.
- Failed or ambiguous patient matching blocks result association and directs the user to a safe retry or manual process.
- Any displayed report remains read-only, source-labeled, freshness-dated, and subordinate to prescriber judgment.

## Frappe realization

- **DocTypes:** `OC PDMP Retrieval` stores jurisdiction, purpose, minimum patient query snapshot, status, external reference, timestamps, and restricted result reference.
- **Roles/API:** `OC PDMP Authorized Prescriber` uses a guarded whitelisted method; permission checks include User Permissions and purpose-of-use policy.
- **Surfaces:** A one-tap prescription action, state selector, restricted report viewer, and compliance Query Report expose access appropriately.
- **Hooks/security:** Structured audit events record every attempt; sensitive payloads use short retention or external references according to site policy.

## Boundaries

Owns: lookup initiation, state selection, and retrieval audit. Consumes: PDMP adapter, patient identity, prescriber authority, and legal basis. Emits: read-only report reference and access evidence. Does not own: PDMP data or clinical interpretation.

## Open questions

- What result retention model satisfies state restrictions while supporting defensible clinical documentation?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [EPCS Two-Factor Signing Ceremony](openchart-feature-catalog-phr-011-epcs-two-factor-signing-ceremony.md)
