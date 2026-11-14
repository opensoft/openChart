# VXU Registry Submission — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Builds and transmits idempotent outbound immunization submissions to managed state-registry connectors.
Topics: openchart-feature-catalog, public-health, frappe, vxu-submission
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-010 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Managed connector conformance suite** — Continuously test first-party state profiles against synthetic payloads.

## Focus

Reliable outbound VXU-style submission from accepted local events through first-party managed connector profiles.

## Behavior

- Accepted reportable administrations create one submission candidate per applicable registry target.
- An exchange user reviews validation status, destination, event version, and consent basis before release when policy requires.
- States are pending, validated, queued, sent, acknowledged, rejected, retrying, and cancelled.
- Payload generation records profile version, message control ID, source record version, and content digest.
- Retries reuse the logical event identity and prevent accidental duplicate submissions.
- Unsupported required data blocks transmission and lists field-level remediation without mutating the clinical event.

## Frappe realization

- **DocTypes:** Add `OC Registry Submission` and protected `OC Registry Payload Artifact` linked to administration, target, profile version, digest, and correlation IDs.
- **Workflow:** Use validation and release states with optional approval by `OC Registry Exchange User`; accepted clinical records remain immutable.
- **Jobs:** Generate and transmit in rq workers with bounded retry, encrypted secrets outside documents, and structured PHI-safe logs.
- **API and surfaces:** Add guarded enqueue/retry/cancel methods, a registry exchange workspace, and Query Reports for pending and rejected submissions.

## Boundaries

Owns: outbound message lifecycle and evidence. Consumes: accepted immunizations, consent, target, and format profile. Emits: registry payloads and delivery status. Does not own: clinical event content or registry adjudication.

## Open questions

- Which state connectors can openChart operate and update as first-party supported services?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
