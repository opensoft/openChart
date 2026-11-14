# Staged: Live visit companion

Status: staged
Kind: capability-proposal
Summary: openChart's ambient companion becomes a resident, always-on participant
in the clinical encounter rather than a recorder that hands work to a queue. A
witnessed session stays open in the room across a dedicated room device and the
practitioner's mobile, streaming transcript, prompts, and real-time order and
symptom analysis against a live working differential. The protocol is
modality-equal and verbal-first — an AI practitioner speaks to the patient and
calls out orders aloud like a human one — and the visit produces a two-witness
record: the practitioner signs as they said and heard it, the companion
independently captures and signs its own. Case conferences reuse the architecture
as another witnessed encounter type with N practitioners.
Topics: openchart-clinical-companion, live-visit-companion, ambient-documentation, two-witness-record
Repository context: openChart — Frappe v15 native EMR; openChart owns the companion capability; Flutter client spans room devices and practitioner mobiles; the practitioner may be human or a credentialed AI (see the practitioner-identity staged topic)
Staging ID: openChart:staging:live-visit-companion
Captured: 2026-08-26
Source: owner discussion 2026-08-25/26 recorded in the clinical-companion phase-decisions document ([../../brainstorm/openchart-clinical-companion-phase-decisions.md](../../brainstorm/openchart-clinical-companion-phase-decisions.md)), closing Issues 2, 3, and 5 of the clinical-companion feature review ([../../brainstorm/openchart-clinical-companion-feature-review.md](../../brainstorm/openchart-clinical-companion-feature-review.md))
Target capabilities: ADDED `live-visit-companion` (always-on witnessed encounter sessions: live transcript, live prompting, two-witness attestation, live differential)

## Last proposal attempt (round-trip provenance)

<!-- Stays "none yet" until this topic first reaches proposal. On DEMOTE,
     replace every field below with the ACTUAL values from the demoted
     change — never re-blank them; that is the whole point of this slot. -->

Change ID: none yet
Raised: n/a
Status at demote: n/a
Demoted: n/a
Demote reason: n/a

## Claims

<!-- Settled context the open questions below should NOT reopen. -->

- **Live transcript and live prompting, always on in the room.** The in-visit
  surface streams; it is not fast-draft-at-visit-end. The catalog's
  capture-then-queue posture (doc-039, mob-020, aic-003/004/005) is the
  substrate, not the target shape.
- **Two hosts, one session.** A dedicated room-resident device and the
  practitioner's mobile capture into the same encounter session. Neither is a
  fallback for the other; the session is the object, the devices are hosts of it.
- **Real-time order and symptom analysis, anchored on the live working
  differential.** Orders and symptoms are analyzed as they are heard — patient-
  spoken, practitioner-called-out, or noted — for both practitioner kinds. The
  working differential is a first-class chart object (competing candidates,
  evidence links, uncertainty, versioned across encounters, distinct from the
  problem list), **live during the visit**: heard symptoms shift hypotheses in
  real time, and called-out orders are evaluated against it.
- **Modality-equal, verbal-first encounter protocol.** An AI practitioner speaks
  to the patient and calls out orders aloud exactly as a human one does. There is
  no silent machine lane for the clinical encounter: the visit stays legible to
  the patient and witnessable by the companion.
- **Two-witness dual attestation.** The practitioner (human or AI) signs the chart
  as they said and heard it; the openChart companion independently captures the
  same visit and signs its own record. An AI practitioner's own record is compared
  against the companion's.
- **Layered record.** Beyond the spoken/witnessed layer, each actor keeps a more
  detailed unspoken portion — the practitioner's private reasoning (for an AI
  practitioner, its reasoning trace) and the companion's extended analysis.
- **The companion is an attesting actor, not passive tooling.** It signs, so its
  disagreement with the practitioner's record is a first-class reconciliation
  event surface rather than a log anomaly.
- **Conferences reuse this architecture.** A case conference is another witnessed
  encounter type with N practitioners: always-on capture, live prompting, dual
  attestation. The companion surfaces notes as the meeting happens with
  review-back to related chart items, renders a live mind-map/graph of the
  meeting's subjects, and may ask questions of the meeting and correct members.
- **Split-surface Flutter sessions.** One Flutter client runs on several devices
  per session and each instance knows its role — common-to-room or
  private-to-practitioner. A human practitioner gets a private second mobile
  screen and private audio; an AI practitioner gets a private comms channel,
  including when embodied in a robot.
- **Runbook state hands off into the visit session.** The pre-visit prep runbook
  is its own surface preceding the visit, and passes its state — including
  check-offs, which are first-class provenance events — into the in-visit session,
  which is not merely the runbook's next screen.
- **Voice-CPOE.** Verbal order call-outs stage orders in real time; a human
  practitioner confirms by signature, and an AI practitioner's call-out carries
  intent under its credential.

## Why

<!-- xspec:candidate target=live-visit-companion -->
openChart already owns substantial encounter-capture machinery, and none of it is
present in the room while the encounter happens. Consent-gated ambient capture,
the ambient note review queue, sentence-level transcript provenance, the ambient
visit capture draft, consented mobile capture, and the clinician video console
are all capture-then-queue components: they record, a job runs, a draft appears
afterwards. Nothing streams, nothing prompts mid-visit, nothing stays resident in
the room across an interruption, and nothing analyzes an order or a symptom at
the moment it is spoken. The result is a companion that documents a visit it did
not attend. Meanwhile the clinical reasoning it should be assisting — the working
differential — has no representation at all: the problem list holds conclusions
only, so the companion has nothing to reason against even if it were present. The
gap widens sharply once the practitioner may be a credentialed AI. If an AI
practitioner works a silent machine lane, the encounter stops being legible to the
patient and witnessable by anyone, and the chart's strongest possible evidentiary
claim — that two independent actors attest to the same spoken visit — is lost
before it is ever built. openChart needs the encounter to be a live, witnessed,
verbal event that both practitioner kinds join on equal terms, with a companion in
the room that hears it, reasons over it as it unfolds, and signs what it heard.
<!-- /xspec:candidate -->

## What changes

<!-- xspec:candidate target=live-visit-companion -->
A new `live-visit-companion` capability introduces the **witnessed encounter
session** as openChart's in-visit object. A session opens before the encounter,
stays open across interruptions, and is hosted concurrently by a dedicated
room-resident device and the practitioner's mobile — one session, multiple hosts,
with resume rather than restart. Pre-visit prep runbook state, including its
check-off provenance events, hands off into the session at open.

The session streams. A live transcript surface replaces the recording-then-draft
lifecycle for in-visit workloads, and live prompting is bound to what is being
said: symptoms and orders are analyzed as they are heard and evaluated against the
**live working differential**, which this capability treats as a first-class,
versioned chart object maintained and displayed during the encounter. Verbal
call-outs stage orders in real time (voice-CPOE) into the existing order
composition path; a human practitioner confirms by signature, and an AI
practitioner's call-out carries order intent under its own credential.

The encounter protocol is fixed as **modality-equal and verbal-first**: both
practitioner kinds speak to the patient and call out orders aloud. Against that
spoken layer the capability defines **two-witness dual attestation** — the
practitioner signs the chart as they said and heard it, and the companion
independently produces and signs its own record of the same visit, with divergence
recorded as a reconciliation item rather than silently merged. Each actor
additionally keeps an **unspoken layer** (private reasoning or an AI reasoning
trace; the companion's extended analysis) in a distinct provenance class.

Sessions are **split-surface**. The Flutter client runs on several devices per
session and every instance resolves its role at join: common-to-room, or
private-to-practitioner. Private surfaces carry second-screen UI and private audio
for a human practitioner, and a private comms channel for an AI practitioner,
including a robot-embodied one. Private-channel prompts address one practitioner
and never render on the room-common surface.

**Case conferences instantiate the same session type** with N practitioners
instead of one patient encounter. The companion surfaces notes as the meeting
proceeds with review-back links to related chart items, renders a live
mind-map/graph of the meeting's subjects, and participates actively — asking
questions and correcting members — while every attending practitioner, human or
AI, signs the conference record under their credential.
<!-- /xspec:candidate -->

## Impact

<!-- xspec:candidate target=live-visit-companion -->
- Affected specs: `live-visit-companion` (ADDED — witnessed encounter session
  lifecycle, streaming transcript and prompting, two-witness dual attestation,
  layered spoken/unspoken record classes, live working differential binding,
  voice-CPOE staging, split-surface device roles, conference encounter type)
- Supersedes in-visit assumptions, not the features themselves: doc-039's
  Recording → Processing → Draft Ready batch lifecycle and aic-048's async-job
  latency and fallback policy stop describing the in-visit path, and aic-003 /
  mob-020's episodic capture framing becomes resident-session framing. Restated,
  not deleted — their consent, provenance, and mobile substrate carries forward.
- Extends without replacing: aic-004 review queue (post-visit work stays queued),
  aic-005 sentence-level transcript provenance (now over a streaming source and
  two attesting records), aic-013 and ord-008 (voice-CPOE stages into them),
  aic-015 gap nudges (become in-visit prompts), tel-002 video console (one host of
  a session, not a separate remote mode), car-054 care conference coordination
  (a witnessed encounter type carrying its agenda/attendance/dissent content).
- Touches `iax`: a **dual-operator UX contract** — a human and an AI editing or
  attesting the same note concurrently, plus room-common vs practitioner-private
  surface rules — has no representation today; iax-022's key-phrase expander is
  the only adjacent in-visit interaction feature.
- Depends on the **practitioner-identity** staged sibling for the credentials this
  capability signs with: the companion's attesting credential, the AI
  practitioner's order-intent credential, and the supervision tier gating whether
  a called-out order takes effect.
- Affected code: openChart Frappe v15 app (encounter session doctypes, order
  staging, differential object, attestation and provenance classes) and the
  Flutter client (multi-device join, role-aware rendering, private audio/comms).
- Infrastructure: introduces a **streaming inference path alongside Frappe's rq
  async model**. rq stays correct for post-visit jobs; nothing in Frappe v15's
  worker model serves a persistent low-latency in-room session, so this adds a
  runtime dimension the platform does not have.
<!-- /xspec:candidate -->

## Idea notes (pre-document, non-documented)

<!-- Free-form thoughts that have not earned a claim, a question, or a
     proposal line yet. Anyone — human or agent — may append. -->

- Room-device hardware posture is unexamined. "Dedicated room-resident device"
  could mean a fixed appliance, a wall panel, a docked tablet, or just the first
  Flutter instance to claim the room role — and the answer drives microphone
  quality, mid-visit network-drop behaviour, physical security of an always-
  listening exam-room device, and who provisions it. — Added-by: Claude Fable 5 · 2026-08-26
- The conference mind-map/graph may be the same graph object the AI practitioner
  loads in the P1 fast-graph runbook rendering, from another angle: the case as
  prepared vs as discussed. If so, the conference UI is a live view over an
  existing artifact, and one-artifact-two-renderings extends into the meeting.
  Worth testing before either is designed. — Added-by: Claude Fable 5 · 2026-08-26

## Conflicts

<!-- Honest tensions this topic has NOT resolved: with another staged
     topic, with a promoted spec, with itself. A conflict names something
     currently INCONSISTENT, even when the reconciliation is "defer,
     noted" — it is not the same thing as an open question. -->

- aic-048's inference latency and fallback policy assumes asynchronous jobs. This
  topic supersedes that for in-visit workloads, but aic-048 is not yet restated
  and still reads as governing policy for all inference — so the catalog answers
  "what happens when the model is slow in the room" with a queue-shaped answer
  this capability rejects. — Added-by: Claude Fable 5 · 2026-08-26
- doc-039's Recording → Processing → Draft Ready lifecycle directly contradicts
  always-on capture with a live transcript surface. Both descriptions of ambient
  visit capture stand in the corpus today, and doc-039 is the one written down as
  the documentation-side contract. — Added-by: Claude Fable 5 · 2026-08-26
- aic-003's episodic consent gate (consent obtained for a capture episode)
  conflicts with live, revocable, mid-encounter consent in a session that stays
  open across interruptions. Q4 proposes semantics the entry as written does not
  accommodate. — Added-by: Claude Fable 5 · 2026-08-26
- The catalog-wide human-gate boilerplate — roughly 575 entries forbidding
  autonomous clinical action, with aic-036 encoding *human* as the gate predicate
  — is inconsistent with a companion that signs its own record as an attesting
  actor, and with an AI practitioner whose call-out carries order intent. A
  **shared conflict with the practitioner-identity staged topic**, which owns the
  predicate restatement (accountable credentialed practitioner): this topic cannot
  resolve it alone and is blocked by it. — Added-by: Claude Fable 5 · 2026-08-26

## Open questions

<!-- The section read most closely. Every question gets all four
     sub-fields below, in this order, even when the answer feels
     obvious — "obvious" is exactly when a wrong disposition ships
     silently. -->

### Q1. When the practitioner's record and the companion's record disagree, who adjudicates, and does the disagreement block chart signing?

Context: Dual attestation makes divergence detectable for the first time, so the
system must say what divergence *does*. The companion is a witness with no
clinical authority; the practitioner carries the license and the liability. But a
witness whose objection leaves no trace is worthless as corroboration, and a
witness who can halt care is a second decision-maker nobody credentialed.
Recommended answer: Disagreement never blocks signing. Both records file
independently, and the discrepancy is emitted as a flagged reconciliation item
reviewed after the visit by the practitioner, with escalation paths defined by the
practice rather than by the companion.
Explanation: Blocking would convert the witness into an authority over the
clinician at the moment care is being delivered — clinically unsafe and outside
anything the companion is credentialed for. Filing both records plus a durable
discrepancy flag preserves the full evidentiary value of two-witness attestation:
the disagreement is on the record, timestamped and attributable, without giving
the companion a veto. The reconciliation item is the accountability mechanism.
Disposition status: accepted — owner ruling 2026-08-26 (disposition round 1, recommendation stands)
Added-by: Claude Fable 5 · 2026-08-26

### Q2. What record class, retention period, and discoverability apply to the unspoken detailed portions (practitioner private reasoning, AI reasoning trace, companion extended analysis)?

Context: The layered record deliberately creates content never spoken to the
patient and never witnessed by the other actor. Whether it is part of the medical
record, how long it is kept, whether the patient may see it, and whether it is
discoverable in a malpractice matter are legal questions the Issue-4 legal-research
work item was created to answer, and they are not answered yet.
Recommended answer: Treat the unspoken portions as part of the record, held in a
**distinct provenance class** from the witnessed spoken layer, with retention and
patient-visibility deferred to the Issue-4 legal research — and capture
**exposure** and **reliance** tags on every element from day one regardless of
where that research lands.
Explanation: Building the unspoken layer outside the record and moving it in later
is not possible; building it inside with a distinct class and moving the retention
policy later is. The tags are the irreversible part: whether a companion output was
surfaced (exposure) and whether the practitioner acted on it (reliance) can only be
recorded contemporaneously, and failure-to-heed claims target precisely the
surfaced-but-ignored case. Deciding the legal class later is cheap; reconstructing
the tags later is impossible.
Disposition status: accepted — owner ruling 2026-08-26 (disposition round 1, recommendation stands)
Added-by: Claude Fable 5 · 2026-08-26

### Q3. Does the companion's ask-and-correct agency extend into patient visits, and how is it moderated in front of the patient?

Context: The agency was decided for conferences, where every participant is a
clinician. A patient visit has a lay participant present, and a companion that
audibly corrects the practitioner in front of the patient changes the encounter's
social and legal character — while a companion that stays silent about a real
error is the failure mode dual attestation exists to catch.
Recommended answer: During patient visits the agency operates through the
**private channel by default** — the companion prompts the practitioner on their
private surface and the correction reaches the room, if at all, through the
practitioner's own voice. Audible companion speech to the room is reserved for
conferences, or a patient visit where the practitioner explicitly invites it.
Explanation: This keeps the practitioner as the single voice of clinical authority
in front of the patient, which is what verbal-first is protecting, while still
guaranteeing the correction is delivered and — via Q2's exposure and reliance
tagging — provably delivered. The invitation escape hatch covers the practitioner
who wants the companion to address the room, without making that the default.
Disposition status: accepted — owner ruling 2026-08-26 (disposition round 1, recommendation stands)
Added-by: Claude Fable 5 · 2026-08-26

### Q4. What are the semantics of mid-encounter consent revocation in an always-on session?

Context: aic-003 gates capture on episode-level consent. An always-on session that
spans an entire visit and survives interruptions needs an answer for the patient
who withdraws consent partway through: what stops, what is deleted, and what the
chart says happened.
Recommended answer: Consent state is **live**. Revocation stops capture forward
from the moment it is given; content already captured is retained under the
consent that covered it at the time; and the consent transition itself is logged
as a session event even though no content is captured after it.
Explanation: Forward-only revocation is the only reading that is honest to the
patient (nothing further is recorded) and to the record (nothing lawfully captured
silently disappears, which would break both the append-only ledger posture and the
two-witness corroboration for the earlier part of the visit). Logging the
transition without content mirrors the off-the-record mechanism already decided for
legal meetings, giving the session one "capture stopped here" pattern, not two.
Disposition status: accepted — owner ruling 2026-08-26 (disposition round 1, recommendation stands)
Added-by: Claude Fable 5 · 2026-08-26

### Q5. Where does the streaming session runtime live relative to Frappe v15?

Context: Frappe's async model is rq workers — correct for post-visit jobs, wrong
for a persistent low-latency in-room session with streaming inference. openChart
is a Frappe-native EMR, so introducing a second runtime is a genuine architectural
commitment, not a library choice.
Recommended answer: A **dedicated streaming session service beside bench** — its
own process lifecycle, holding the live session, transcript stream, and inference
path — writing into openChart only through guarded api.v1-style surfaces. rq stays
in place for post-visit jobs unchanged.
Explanation: Putting the session inside the Frappe worker model means fighting rq's
job semantics for something that is not a job; putting chart writes inside the
streaming service means a second, unguarded write path into the record — untenable
for content that will be signed and attested. Separating the runtime from the write
surface gets low latency where it is needed while keeping every durable chart
mutation on the single audited path the attestation and ledger guarantees depend on.
Disposition status: accepted — owner ruling 2026-08-26 (disposition round 1, recommendation stands)
Added-by: Claude Fable 5 · 2026-08-26

### Q6. Are private-channel prompts to a practitioner part of the encounter record?

Context: If Q3's recommendation holds, the private channel becomes the main
delivery route for companion input during patient visits — which makes its record
status the difference between a documented and an undocumented influence on care.
The same question was raised for conferences in Issue 3.
Recommended answer: Yes — private-channel prompts are part of the record, in the
same class as the unspoken detailed portions from Q2, carrying exposure and
reliance tags.
Explanation: A prompt that changes what the practitioner says or orders has
influenced care, and contemporaneous tagging exists so that influence is captured
when it happens rather than reconstructed afterwards. Treating private prompts as a
separate, unrecorded channel would open a deliberate gap in the evidentiary
substrate exactly where failure-to-heed and reliance arguments concentrate. Sharing
Q2's class also means one retention decision covers both, rather than two that drift.
Disposition status: accepted — owner ruling 2026-08-26 (disposition round 1, recommendation stands)
Added-by: Claude Fable 5 · 2026-08-26

## Exit

This topic crosses the proposal gate when every open question above carries a
disposition other than `open`, and specifically when the streaming-architecture
recommendation in Q5 has an owner ruling — the runtime boundary shapes the
capability's requirements, not merely its implementation, so a proposal drafted
before that ruling would need rewriting rather than amending. The
practitioner-identity sibling's restatement of the human-gate predicate must also
be at least proposed, since this topic's attestation claims depend on credentials
it does not own.

Gate status 2026-08-26: all six questions dispositioned `accepted` (disposition round 1); the practitioner-identity sibling is proposed (`add-practitioner-identity`), satisfying the predicate-restatement condition.
