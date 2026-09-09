code_surface: openChart (witnessed encounter session, transcript segment, working differential, attestation, reconciliation-item and provenance-class DocTypes on the open_chart Frappe application; a dedicated streaming session service beside bench holding the live session, transcript stream and inference path; guarded `open_chart.api.v1` write surfaces for every durable chart mutation the session produces; voice-CPOE staging into the existing order composition path; the Flutter client's multi-device join, role resolution and private surfaces; no credential issuance, no production clinical authority, no retention or patient-visibility ruling on the unspoken layer)
target_release: live visit companion v1 — lands on a validator-green open_chart application in which a witnessed encounter session opens before the encounter, survives interruption by resume rather than restart, is hosted concurrently by a room-resident device and the practitioner's mobile, streams transcript and prompts, maintains a live working differential as a versioned chart object, stages verbally called-out orders into the existing order path, and files two independently signed records of the same visit with divergence recorded as a reconciliation item rather than merged
Status: draft
Source: staged topic `openChart:staging:live-visit-companion`, all six open questions dispositioned accepted by owner ruling 2026-08-26 (disposition round 1). See `supporting-docs/`.

## Why

openChart already owns substantial encounter-capture machinery and none of it is
present in the room while the encounter happens. Consent-gated ambient capture,
the ambient note review queue, sentence-level transcript provenance, the ambient
visit capture draft, consented mobile capture and the clinician video console are
all capture-then-queue: they record, a job runs, a draft appears afterwards.
Nothing streams, nothing prompts mid-visit, nothing stays resident across an
interruption, and nothing analyzes an order or a symptom at the moment it is
spoken. The result is a companion that documents a visit it did not attend.
Meanwhile the reasoning it should be assisting has no representation at all: the
problem list holds conclusions only, so there is no working differential to
reason against even if the companion were present.

The gap widens sharply once the practitioner may be a credentialed AI. If an AI
practitioner works a silent machine lane, the encounter stops being legible to the
patient and witnessable by anyone, and the chart's strongest available evidentiary
claim — that two independent actors attest to the same spoken visit — is lost
before it is ever built. openChart needs the encounter to be a live, witnessed,
verbal event that both practitioner kinds join on equal terms, with a companion in
the room that hears it, reasons over it as it unfolds, and signs what it heard.

## What Changes

- Add the **witnessed encounter session** as openChart's in-visit object: it opens
  before the encounter, stays open across interruptions, and resumes rather than
  restarts. Pre-visit prep runbook state, including its check-off provenance
  events, hands off into the session at open.
- Make the session **two-hosted**: a dedicated room-resident device and the
  practitioner's mobile capture into one session. Neither is the other's fallback;
  the session is the object and the devices are hosts of it.
- Replace the recording-then-draft lifecycle for in-visit workloads with a
  **streaming transcript surface and live prompting** bound to what is being said.
- Add the **working differential as a first-class versioned chart object** —
  competing candidates, evidence links, uncertainty, distinct from the problem
  list — maintained and displayed **live during the visit**, with heard symptoms
  shifting hypotheses in real time and called-out orders evaluated against it.
  Promotion from differential to problem-list conclusion stays an explicit signed
  practitioner decision.
- Fix the encounter protocol as **modality-equal and verbal-first**: both
  practitioner kinds speak to the patient and call orders aloud. There is no
  silent machine lane for the clinical encounter.
- Add **two-witness dual attestation**: the practitioner signs the chart as they
  said and heard it, and the companion independently produces and signs its own
  record of the same visit. **Divergence never blocks signing** — both records
  file and the discrepancy becomes a flagged reconciliation item reviewed after
  the visit.
- Add the **layered record**: each actor's unspoken portion (practitioner private
  reasoning or an AI reasoning trace; the companion's extended analysis) is part
  of the record in a **distinct provenance class**, with **exposure** and
  **reliance** tags captured contemporaneously on every element. Retention and
  patient visibility are deferred to the named legal-research work item.
- Route the companion's ask-and-correct agency in patient visits through the
  **private channel by default**; audible companion speech to the room is reserved
  for conferences or an explicit practitioner invitation. **Private-channel
  prompts are part of the record**, in the same class as the unspoken portions and
  carrying the same tags.
- Add **voice-CPOE**: verbal call-outs stage orders in real time into the existing
  order composition path. A human practitioner confirms by signature; an AI
  practitioner's call-out carries order intent under its credential.
- Make consent **live**: revocation stops capture forward from the moment it is
  given, content already captured is retained under the consent that covered it,
  and the transition itself is logged as a session event.
- Make sessions **split-surface**: one Flutter client runs on several devices per
  session and every instance resolves its role at join — common-to-room or
  private-to-practitioner. Private surfaces carry a second screen and private
  audio for a human practitioner and a private comms channel for an AI
  practitioner, including a robot-embodied one.
- Instantiate **case conferences as the same session type** with N practitioners:
  notes surfaced as the meeting proceeds with review-back links to related chart
  items, a live mind-map/graph of the meeting's subjects, an actively
  participating companion, and every attending practitioner signing under their
  credential.
- Introduce a **dedicated streaming session service beside bench** holding the
  session, transcript stream and inference path, writing into openChart only
  through guarded `api.v1`-style surfaces. rq stays unchanged for post-visit jobs.
- **Restate, never delete**, the in-visit assumptions this supersedes: doc-039's
  Recording → Processing → Draft Ready batch lifecycle, aic-048's async-job
  latency and fallback policy, and aic-003 / mob-020's episodic capture framing.
- Excluded: retention or patient-visibility rulings on the unspoken layer, the
  legal matter workspace (openPractice's), external-organization participant
  identity and consult-package exchange, knowledge-connector sourcing for the
  differential, and any grant of clinical authority — which this change consumes
  from `practitioner-identity` and does not issue.

## Capabilities

### New Capabilities

- `live-visit-companion`: the witnessed encounter session and its lifecycle
  (open-before-encounter, interruption-survival, resume, runbook hand-off,
  multi-host); streaming transcript and live prompting; the live working
  differential as a versioned chart object; two-witness dual attestation and the
  reconciliation item; layered spoken and unspoken record classes with exposure
  and reliance tagging; live consent and forward-only revocation; voice-CPOE
  staging; split-surface device roles and the private channel; the conference
  encounter type; and the streaming session service's guarded write path.

### Modified Capabilities

None. `expanded-patient-intake` requirements are unchanged: they govern
patient-reported intake — identity with namespaced external identifiers,
versioned idempotent submissions, statement families, amendment history and the
guarded versioned API — and its authority boundary states that no intake,
statement, API response or extension event creates a prescription, diagnosis,
order, administration, recommendation or autonomous action. This change adds a
practitioner-side encounter surface beside that intake, writes through the same
guarded API discipline, and neither weakens that boundary nor grants intake any
new authority. The assumptions this change supersedes (doc-039, aic-048,
aic-003, mob-020) are brainstorm-stage catalog entries, not promoted specs.

## Impact

- **openChart:** new encounter-session, transcript-segment, working-differential,
  attestation, reconciliation-item, session-event and provenance-class records;
  exposure and reliance tags on companion output; voice-CPOE staging into the
  existing order composition path; new guarded `open_chart.api.v1` write surfaces
  for every durable mutation the session produces; migrations, permissions, audit
  and synthetic fixtures for all of it.
- **Infrastructure:** a **new runtime dimension**. Nothing in Frappe v15's worker
  model serves a persistent low-latency in-room session, so the streaming session
  service runs its own process lifecycle beside bench. The separation of runtime
  from write surface is the load-bearing part: low latency where it is needed,
  every durable chart mutation still on the single audited path the attestation
  and ledger guarantees depend on.
- **Flutter client:** multi-device join into one session, role resolution at join,
  role-aware rendering, private audio and second-screen surfaces, and the AI
  practitioner's private comms channel including robot embodiment.
- **Dependency on `practitioner-identity` (proposed, not promoted):** this change
  signs but issues no credentials. It consumes that capability's companion
  attesting credential, the AI practitioner's order-intent credential, the
  co-signature record, and the restatement of the human-gate predicate as
  *accountable credentialed practitioner*. Attestation and voice-CPOE tasks are
  blocked on it; session, transcript, differential and consent work are not.
- **Extends without replacing:** aic-004 review queue (post-visit work stays
  queued), aic-005 sentence-level transcript provenance (now over a streaming
  source and two attesting records), aic-013 and ord-008 (voice-CPOE stages into
  them), aic-015 gap nudges (become in-visit prompts), tel-002 video console (one
  host of a session, not a separate remote mode), car-054 care conference
  coordination (a witnessed encounter type carrying its agenda, attendance and
  dissent content).
- **`iax` gap:** a dual-operator UX contract — a human and an AI attesting or
  editing the same note concurrently, plus room-common versus practitioner-private
  surface rules — has no representation today; iax-022's key-phrase expander is
  the only adjacent in-visit interaction feature.
- **Legal research:** retention, patient visibility and discoverability of the
  unspoken layer are carried by the existing named legal-research work item. The
  tags are built now because exposure and reliance can only be recorded
  contemporaneously; the class decision is deliberately deferrable and the tagging
  is not.
- **Safety:** the companion is a witness, not an authority. It never blocks
  signing, never speaks to the room in a patient visit unless invited, holds no
  clinical decision-making, and every chart mutation it produces passes the
  guarded write surface under an accountable practitioner's authority.
