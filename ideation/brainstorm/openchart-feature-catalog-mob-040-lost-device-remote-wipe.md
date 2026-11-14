# Lost Device Remote Wipe — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Revokes a lost mobile installation and drives verifiable destruction of local keys, caches, attachments, sessions, and notification state.
Topics: openchart-feature-catalog, mobile-devices, frappe, remote-wipe
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-040 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Pending-work recovery escrow** — Preserve encrypted authored intents for governed server recovery before local key destruction where feasible.

## Focus

This capability isolates wipe command lifecycle, server revocation, local cleanup, acknowledgement, and unresolved offline risk.

## Behavior

- A user or authorized administrator marks an enrollment lost, stolen, reassigned, or compromised with reason and effective time.
- The server immediately revokes tokens, cache manifests, notification routing, file grants, and device trust.
- Push and websocket channels carry an opaque wipe generation; every subsequent API response repeats it until acknowledged.
- The app destroys account keys, cached records, staged attachments, message previews, session state, and safe-to-delete drafts.
- Pending authored work follows explicit recover, quarantine, or destroy policy and never transfers to a new user silently.
- A wipe receipt records categories cleared, app build, device time, and server time without listing patient data.
- Devices that never reconnect remain Unconfirmed, with residual-risk review rather than a false success claim.

## Frappe realization

- **DocTypes:** Create `OC Mobile Wipe Command` and `OC Mobile Wipe Receipt` with enrollment, generation, reason, requester, scope, state, issued/acknowledged times, and residual-risk outcome.
- **Workflow and roles:** Requested → Issued → Acknowledged/Unconfirmed/Failed → Closed; users wipe own devices, while `OC Security Administrator` handles compromise and closure.
- **API and auth:** Revocation endpoints under `open_chart.api.v1.mobile.wipe` use TLS REST token auth where still valid and signed device proof for receipts; all APIs check active wipe generation.
- **Realtime and jobs:** Send wipe through websocket and generic push; server-side RQ jobs retry, revoke dependent grants, age unconfirmed cases, and notify reviewers.
- **Files and surfaces:** All device-specific Frappe private file attachment grants are revoked; recovery escrow, if enabled, remains server-side encrypted and restricted, with a Security Desk report.

## Boundaries

Owns: openChart revocation, wipe command, receipt, and residual-risk state. Consumes: enrollment, push channel, MDM signal, and pending-work policy. Emits: revoked access and cleanup evidence. Does not own: physical recovery, OS factory reset, or proof of destruction on a permanently offline device.

## Open questions

- Which pending clinical drafts may be escrowed without weakening device-loss containment?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
