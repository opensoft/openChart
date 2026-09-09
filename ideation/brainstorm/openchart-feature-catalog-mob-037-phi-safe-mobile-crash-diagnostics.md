# PHI-Safe Mobile Crash Diagnostics — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Collects opt-in mobile crash and diagnostic evidence through deterministic PHI scrubbing, bounded retention, and support-controlled access.
Topics: openchart-feature-catalog, mobile-devices, frappe, crash-diagnostics
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-037 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Synthetic replay capsule** — Reconstruct app state with generated identifiers and payload shapes rather than patient data.

## Focus

This entry isolates useful diagnostics while treating logs, screenshots, breadcrumbs, and memory state as potentially sensitive.

## Behavior

- The app captures build, platform, exception, safe route name, resource pressure, and bounded breadcrumbs under published policy.
- Patient names, identifiers, free text, message bodies, file names, URLs, tokens, coordinates, and raw request bodies are excluded or scrubbed.
- Users may preview and add a description before submitting a support bundle.
- Screenshots, memory dumps, and database copies are disabled by default and require explicit governed escalation.
- Every bundle records scrubber version, detected-field counts, consent basis, retention, and access history.
- Offline bundles remain encrypted and can be discarded before upload.
- Scrubber failure blocks transmission rather than sending an unsanitized bundle.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Mobile Diagnostic Bundle` and `OC Diagnostic Scrub Policy` with build, fingerprint, scrubber, counts, state, retention, reporter, and provider reference.
- **Workflow and roles:** Local → Scrubbing → Submitted → Triaged → Resolved/Rejected/Expired; `OC Mobile Support` sees scrubbed data and security approves exceptional artifacts.
- **API and auth:** Token-authenticated `open_chart.api.v1.mobile.diagnostics.init` and `complete` validate scrub results; third-party provider callbacks use signed methods.
- **Realtime and jobs:** Websocket receipts report acceptance; server-side RQ jobs rescan, deduplicate, route, aggregate, and delete expired bundles.
- **Files and surfaces:** Bundles use encrypted private Frappe file attachment APIs with malware scanning and download audit; Desk reports expose fingerprints and trends, not PHI.

## Boundaries

Owns: diagnostic capture contract, scrub evidence, bundle lifecycle, and support access. Consumes: app failures and device telemetry. Emits: minimized support evidence. Does not own: third-party crash service behavior or clinical records.

## Open questions

- Is any third-party crash platform acceptable, or must all bundles terminate in openChart-controlled storage?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
