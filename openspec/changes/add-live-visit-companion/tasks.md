## 1. Session Foundation And Provenance Classes

- [ ] 1.1 Add the Witnessed Encounter Session DocType with encounter type, subject, participants, lifecycle state (`open`, `active`, `interrupted`, `resumed`, `closed`), consent state and audit provenance, plus migrations.
- [ ] 1.2 Add the Session Event record (open, interruption, resume, close, consent transition, companion invitation) as the session's append-only event log.
- [ ] 1.3 Implement resume-not-restart: a rejoin attaches to the same session identity, loss of every host moves the session to `interrupted` rather than `closed`, and no second session is created for one encounter.
- [ ] 1.4 Add multi-host attachment with per-host provenance, and prove no host is defined as the other's fallback (a mobile-only session is fully valid).
- [ ] 1.5 Define the provenance-class attribute on every record element: witnessed spoken layer versus unspoken class, as a first-class field rather than a side table.
- [ ] 1.6 Implement exposure and reliance tags on companion output, written contemporaneously, with a refusal on any post-close tag write.
- [ ] 1.7 Make retention period and patient visibility attributes of the unspoken class so the deferred legal ruling applies without relocating content; record the named legal-research work item as the owner of that ruling.
- [ ] 1.8 Add permissions, audit behavior and synthetic fixtures for session, session event and provenance-class records.

## 2. Streaming Session Service And Guarded Write Path

- [ ] 2.1 Stand up the dedicated streaming session service beside bench with its own process lifecycle, holding live session, transcript stream and inference path.
- [ ] 2.2 Add the guarded `open_chart.api.v1`-style write surfaces the session needs: transcript segment commit, differential version, staged order, attestation, reconciliation item, session event — each carrying subject, tenant, purpose and role context.
- [ ] 2.3 Give the streaming service no direct write path to chart storage and no database credentials of its own; verify the controller guards refuse its unguarded writes exactly as any other.
- [ ] 2.4 Define and implement commit granularity and the maximum in-flight window a service crash may lose; record the chosen granularity.
- [ ] 2.5 Make committed session state authoritative over the service's in-flight state, with a defined reconciliation on reconnect.
- [ ] 2.6 Confirm rq continues to serve post-visit jobs unchanged (draft generation, review queue, reconciliation-item processing) with no change to that path.
- [ ] 2.7 Keep session-layer decisions (role resolution, consent evaluation, class assignment, divergence detection) in pure functions the bench-free validator can exercise without a Frappe site.

## 3. Live Consent

- [ ] 3.1 Implement live session consent evaluated continuously for the session's duration, replacing per-episode evaluation on the in-visit path.
- [ ] 3.2 Implement forward-only revocation: capture stops at the moment of revocation, the session stays open, and no prior content is deleted, redacted or invalidated.
- [ ] 3.3 Log the consent transition as a session event even though no content is captured after it, and support re-consent later in the same session with the uncaptured interval evident from the events.
- [ ] 3.4 Refuse any retroactive deletion of pre-revocation content justified by the revocation.

## 4. Live Transcript And Prompting

- [ ] 4.1 Add the Transcript Segment record with host provenance, timing, session reference and provenance class, committed durably during the session.
- [ ] 4.2 Implement multi-host transcript reconciliation into one ordered stream, with the reconciliation recorded and unreconcilable segments retaining both readings.
- [ ] 4.3 Deliver the live transcript to the session's surfaces during the encounter, replacing the batch draft lifecycle for in-visit content.
- [ ] 4.4 Implement live prompting bound to session content, with every prompt carrying its transcript anchor and session.
- [ ] 4.5 Implement private-by-default prompt delivery for patient encounters, the explicit practitioner invitation that permits audible companion speech (logged as a session event), and refusal of uninvited audible speech.
- [ ] 4.6 Record private-channel prompts in the unspoken provenance class with exposure and reliance tags, and refuse any unrecorded delivery path.
- [ ] 4.7 Verify a session that terminates abnormally retains every segment committed before termination.

## 5. Working Differential And Real-Time Analysis

- [ ] 5.1 Add the Working Differential DocType: competing candidates, evidence links, stated uncertainty, versioned across encounters, addressable independently of the problem list.
- [ ] 5.2 Implement in-visit revision as new versions (never overwrite), so the version in force at any timestamp is retrievable.
- [ ] 5.3 Implement real-time symptom and order analysis against the active differential version, identical for human and AI practitioners, with the evaluated version referenced on every result.
- [ ] 5.4 Implement the signed promotion path to the problem list: deciding practitioner, time, source differential version and signature, as a recorded act.
- [ ] 5.5 Refuse automatic promotion from confidence or evidence accumulation, and refuse companion-initiated promotion.
- [ ] 5.6 Enforce hypothesis-versus-conclusion separation so no surface represents a differential candidate as a conclusion.

## 6. Flutter Multi-Device Sessions And Private Surfaces

- [ ] 6.1 Implement Flutter multi-device join into one session with role resolution at join (`common-to-room` / `private-to-practitioner`), never derived from device registration or device type.
- [ ] 6.2 Implement role-aware rendering, including the private second screen and private audio for a human practitioner.
- [ ] 6.3 Implement the AI practitioner's private comms channel, including robot embodiment, while its clinical speech stays audible in the room.
- [ ] 6.4 Enforce at the session layer that private content addressed to one practitioner never renders or sounds on any common-to-room surface.
- [ ] 6.5 Implement the pre-visit runbook hand-off at session open: canonical item set plus check-off provenance events, transferred as an explicit recorded hand-off, with check-off provenance durable even when no session opens.
- [ ] 6.6 Verify the same device resolves different roles in different sessions with no reconfiguration.

## 7. Dual Attestation And Reconciliation

- [ ] 7.1 **BLOCKED on `add-practitioner-identity`** — bind the companion's attestation to its witness credential; until that capability lands, produce and sign the companion record under the interim path and refuse to claim credentialed attestation.
- [ ] 7.2 Add the Attestation record: one session, one attesting actor, one signed record, with the practitioner's and companion's attestations independently addressable and never merged.
- [ ] 7.3 Mark the companion's attestation as a witness holding no clinical decision-making authority.
- [ ] 7.4 Implement comparison of an AI practitioner's own record against the companion's record for the same session.
- [ ] 7.5 Implement divergence detection and the Reconciliation Item: session, diverging content, time, lifecycle state, practitioner review after the visit.
- [ ] 7.6 Guarantee divergence never blocks, delays or invalidates signing, and that the companion can neither escalate nor veto on its own authority.
- [ ] 7.7 Keep unreviewed reconciliation items visibly open rather than auto-closed, with practice-defined escalation paths configurable outside the companion.
- [ ] 7.8 Refuse any merge of the practitioner's and companion's records.

## 8. Voice-CPOE Order Staging

- [ ] 8.1 Stage verbal call-outs into the existing order composition path (aic-013, ord-008), carrying transcript segment, differential version and session — no parallel voice-order store.
- [ ] 8.2 Implement human-practitioner confirmation by signature before a staged order takes effect.
- [ ] 8.3 **BLOCKED on `add-practitioner-identity`** — carry an AI practitioner's order intent under its own credential, subject to that credential's supervision tier and staged-order co-signature rules.
- [ ] 8.4 Refuse a staged order from an AI call-out with no valid credential rather than substituting another authority.
- [ ] 8.5 Enforce modality-equal, verbal-first: refuse any silent clinical lane through which an AI practitioner issues an order without an audible call-out.
- [ ] 8.6 Refuse any order creation that bypasses the existing order composition path.

## 9. Conference Encounter Type

- [ ] 9.1 Instantiate the conference as the same witnessed encounter session type with N practitioners, parameterising participation rules by encounter type rather than forking the session.
- [ ] 9.2 Permit audible companion participation (asking questions, correcting members) in conference sessions as a type-level condition.
- [ ] 9.3 Implement in-meeting note surfacing with review-back links resolving to related chart items.
- [ ] 9.4 Implement the live mind-map/graph rendering of the meeting's subjects.
- [ ] 9.5 **BLOCKED on `add-practitioner-identity`** — have every attending practitioner, human or AI, sign the conference record under their own credential.
- [ ] 9.6 Carry dissent as conference record content rather than a separate unlinked object, absorbing car-054's agenda, attendance and dissent content into the session.

## 10. Catalog Restatement (Documentation)

- [ ] 10.1 Restate doc-039's Recording → Processing → Draft Ready lifecycle as the batch path for non-resident capture, with its consent and provenance substrate carried forward unchanged.
- [ ] 10.2 Restate aic-048's async-job latency and fallback policy as governing post-visit inference only, and name the streaming path's own latency and degradation behaviour for in-room inference.
- [ ] 10.3 Restate aic-003's episodic consent gate as live session consent, leaving the consent record, its parties and its provenance unchanged.
- [ ] 10.4 Restate mob-020's episodic mobile capture as one host of a witnessed encounter session.
- [ ] 10.5 Record which adjacent entries were deliberately left unchanged and why — aic-004 review queue, aic-005 transcript provenance, aic-013 / ord-008 order path, aic-015 gap nudges, tel-002 video console, car-054 conference coordination.
- [ ] 10.6 Record the `iax` gap: no dual-operator UX contract exists for a human and an AI attesting the same note concurrently, nor for room-common versus practitioner-private surface rules.
- [ ] 10.7 Record the dependency posture on `add-practitioner-identity` (proposed, not promoted) and the blocked tasks it gates, so the sequencing is auditable from the change itself.

## 11. Validation And Evidence

- [ ] 11.1 Add bench-free tests for session lifecycle and resume, role resolution, class assignment, live consent and forward-only revocation, differential versioning, and divergence detection; keep `make validate` green.
- [ ] 11.2 Add Docker-gated bench tests under `make validate-docker` for migrations, permissions, guarded-surface refusals, transcript commit durability and the signed promotion path.
- [ ] 11.3 Add negative tests for every refusal in the spec: second session for one encounter, merged attestations, companion blocking a signature, companion promotion, automatic promotion on confidence, retroactive deletion after revocation, post-close tag write, uninvited audible companion speech, private prompt on a room-common surface, unrecorded private delivery, silent AI clinical lane, AI call-out with no credential, parallel voice-order store, streaming-service direct write.
- [ ] 11.4 Add the two-witness scenario end to end: both records file, signing is unblocked, and a reconciliation item carries the divergence with a timestamp.
- [ ] 11.5 Add the abnormal-termination test proving every pre-termination transcript segment remains durable and attributable.
- [ ] 11.6 Publish the evidence bundle: synthetic-only fixtures, the guarded-write proof that the streaming service holds no direct path, the recorded commit granularity and worst-case in-flight loss window, and confirmation that this change grants no clinical authority and issues no credential.
- [ ] 11.7 Run `openspec validate add-live-visit-companion` and confirm every applyRequires artifact reports done.
