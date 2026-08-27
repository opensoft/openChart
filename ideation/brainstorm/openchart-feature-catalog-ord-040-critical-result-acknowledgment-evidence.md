# Critical Result Acknowledgment Evidence — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures verifiable recipient identity, communication channel, read-back, timestamp, and disposition for critical results.
Topics: openchart-feature-catalog, cpoe, frappe, critical-results
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-040 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Critical communication timer** — Display elapsed time from finalization through contact and acknowledgment.

## Focus

This feature isolates heightened evidence required for critical-result communication.

## Behavior

- A critical classification starts a policy-defined timer and identifies qualified recipients.
- Communicating staff record contacted person, identity verification, channel, contact time, result read-back, and response.
- Portal delivery, message opening, or voicemail alone cannot satisfy critical acknowledgment unless policy explicitly permits it.
- The qualified recipient confirms clinical acknowledgment separately from communicator documentation.
- Failed contact attempts retain evidence and advance escalation.
- Corrections to a critical result create new communication obligations when policy requires.

## Frappe realization

- **DocTypes:** submitted `OC Critical Result Communication` with accountability, attempt number, recipient, verification method, channel, read_back, timestamps, and outcome.
- **Workflow:** Contact Required → Attempted → Communicated → Clinically Acknowledged or Escalated.
- **Roles/permissions:** result communicators record attempts; qualified clinicians acknowledge; evidence is immutable at permlevel 2.
- **Hooks/API/surface:** result critical flag creates the task on submit; guarded methods record attempts; scheduler drives tier deadlines and REST critical worklists.

## Boundaries

Owns: critical communication and acknowledgment evidence. Consumes: critical classification, result version, and recipients. Emits: verified acknowledgment or escalation. Does not own: critical-threshold definition.

## Open questions

- Which channels and identity checks meet policy for each critical-result class?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Result Escalation Ladder](openchart-feature-catalog-ord-038-result-escalation-ladder.md)
