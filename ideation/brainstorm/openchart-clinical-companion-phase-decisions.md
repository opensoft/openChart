# Clinical Companion Phase Decisions — Brainstorm

Status: brainstorm
Kind: report
Summary: decision record from the issue-by-issue discussion of the clinical-companion feature review, capturing the product owner's direction on each pillar gap and the boundary cleanup, as input to the next phase (staging and OpenSpec proposals).
Topics: openchart-clinical-companion, phase-decisions, gap-analysis
Repository context: openChart — Frappe v15 native EMR; discussion outcomes recorded 2026-08-25 against the findings in the clinical-companion feature review
Captured: 2026-08-25

## How to read this

Each section closes one issue from
[Clinical Companion Feature Review](openchart-clinical-companion-feature-review.md):
the finding in one line, the direction decided in discussion, and any
constraints or open questions the owner attached. Sections are appended
as the discussion proceeds; an issue without a section is not yet
discussed.

## Decisions

<!-- Appended one issue at a time during the review discussion. -->

### Issue 1 — P1 Pre-visit preparation

**Finding (one line):** best-covered pillar (aic-007, aic-016, doc-037/038/040,
pmr-050, car-022, pub-005, mob-006), but preparation only reaches what is
already in the local chart.

**Direction decided:** build the **pre-visit prep runbook** — a chart-reading
AI produces one canonical assessment of what the practitioner must know for
this visit (important items, each cited to chart sources), rendered at two
bandwidths for the two practitioner kinds:

- **Human practitioner:** a short, concise, prioritized runbook UI. Each item
  supports **check off** or **explain**; the UI presents the important items
  (importance determined by the chart AI) and the human doc drills in for
  details. Explain yields summary basics broken into sections, each section
  drillable further so the doc can refresh their knowledge on that issue.
- **AI practitioner:** the same canonical artifact at full fidelity, loaded
  instantly as a fast graph — no pacing, no summarization loss.

**Design consequences recorded:**
- One artifact, two renderings — human and AI doctors prepare from the same
  determination of "what matters"; conciseness is a rendering concern, not a
  different analysis.
- P1 is its own surface (runbook precedes the visit); runbook state hands off
  into the P2 in-visit session rather than P1 being merely P2's opening state.
- Runbook check-offs are first-class provenance events — durable evidence of
  preparation that feeds the P4 medico-legal pillar.
- Merges/extends existing seeds aic-007 + aic-016; the graph rendering and the
  dual-rendering contract are new; the sectioned knowledge-refresh drill-down
  is new.

**Open questions attached:**
- Does Explain drill-down draw on chart facts only, or also external medical
  knowledge (guidelines, literature)? The latter depends on the R4 knowledge
  connectors packet.
- On-demand outside-record retrieval before a visit (the P1 gap in the review)
  was not resolved — deferred, not rejected.

### Issue 2 — P2 Always-on in-visit companion

**Finding (one line):** capture machinery exists (doc-039, mob-020, tel-002,
aic-003/004/005) but everything is capture-then-queue; nothing streams, prompts
mid-visit, or stays resident in the room.

**Direction decided:**
- **Live transcript and live prompting, always on in the room** — not
  fast-draft-at-visit-end. The streaming path replaces aic-048's
  async-jobs assumption for in-visit workloads.
- **Two hosts, one session:** a dedicated room-resident device AND the
  doctor's mobile, capturing into the same encounter session.
- **Real-time order and symptom analysis:** orders and symptoms are analyzed
  as they are heard — spoken by the patient, called out verbally by the
  practitioner, or noted — for human and AI practitioners alike.

**The two-witness encounter record (core architecture decided):**
- The encounter protocol is **modality-equal and verbal-first**: an AI doctor
  speaks to the patient and calls out orders aloud exactly like a human
  doctor. No silent machine lane for the clinical encounter itself; the visit
  stays legible to the patient and witnessable by the companion.
- **Dual attestation:** the practitioner (human or AI) signs the chart as they
  said/heard it; the openChart ambient companion independently captures the
  same visit and signs its own record. The AI practitioner's own record is
  compared against the companion's record.
- **Layered record:** beyond the spoken/witnessed layer, each actor keeps a
  more detailed unspoken portion — the practitioner's private reasoning (for
  an AI doctor, its reasoning trace) and the companion's extended analysis.

**Design consequences recorded:**
- The companion becomes an attesting actor, not passive tooling — it signs.
- Practitioner-vs-companion discrepancy becomes a first-class reconciliation
  event surface.
- Dual attestation directly strengthens P4: the spoken layer of the chart is
  corroborated by two independent signers.
- Voice-CPOE: verbal order call-outs stage orders in real time; a human
  practitioner confirms by signature, an AI practitioner's call-out carries
  intent under its credential (P7 dependency).

**Open questions attached:**
- Adjudication when practitioner and companion records disagree — who
  resolves, and whether disagreement blocks chart signing.
- Legal/record class of the unspoken detailed portions: retention,
  discoverability in a malpractice matter, patient visibility (P4 interplay).
- Whether the companion signs under its own openXwallet credential (leaning
  yes — a credentialed witness) or as a system attestation (P7 dependency).

### Issue 3 — P3 Case collaboration

**Finding (one line):** correct fragments exist (car-054 conference record with
dissent, car-023/028/031 referrals and e-consults, msg-028, img-040) but no
case assembly, no second-opinion flow, no exchange representation, no AI
participants.

**Direction decided:**
- **Conferences reuse the P2 companion architecture** — a case conference is
  another witnessed encounter type with N practitioners: always-on capture,
  live prompting, dual attestation.
- The companion **surfaces important notes as the meeting happens**, with a
  simple way for a human to review back to related chart items, and a **live
  mind-map / graph view of the meeting's subjects** in the UI.
- The companion is an **active participant**: it may ask questions of the
  meeting and correct other members.
- **Split-surface session topology:** one Flutter client runs on several
  devices per session and each instance knows its role — common view to the
  room, or private to a practitioner. A human practitioner gets a private
  second mobile UI screen and private audio; an AI practitioner (on a mobile
  device or in a robot body) gets a private comms channel from openChart.
- **AI doctors join as full peers** — presenting, dissenting, signing the
  conference record under their credential. Ultimate goal stated: MedxFactory
  as a team of AIs that, as a council or a single gateway AI, is itself the
  state-licensed practitioner. openChart plans for full peer from the start.
- **Internal and external conferences**, with full teleconference ability
  native to both the companion and the AI doctor; the AI doctor is expected
  to be mobile (robot embodiment).

**Design consequences recorded:**
- The practitioner model must support a **composite practitioner** — a
  council of AIs behind one gateway identity/credential (P7: how signature
  and liability resolve inside the collective).
- Flutter is the client framework; sessions are multi-device with role-aware
  rendering (room-common vs practitioner-private).
- Teleconference (and robot presence) becomes part of the companion platform,
  not a bolt-on telehealth module.
- P1's runbook pattern generalizes to a pre-meeting **case packet** (imaging,
  timeline, prior workup, the specific question) — assembly for N doctors.

**Open questions attached:**
- Does the companion's ask/correct agency extend into patient visits (P2),
  and how is it moderated in front of the patient?
- Composite practitioner: does the gateway sign alone or do council members
  co-sign; internal dissent within the council as record content?
- Identity and trust for external participants (human or AI) from other
  organizations; consult-package exchange in `int` still undesigned.
- Are private-channel prompts to a practitioner part of the encounter record
  (same class as the unspoken detailed portions from Issue 2)?

### Issue 4 — P4 Medico-legal support

**Finding (one line):** the corpus has the strongest evidentiary substrate
(sec-021/022/046, dms-040, doc-028/029/069, msg-005/006/023) but nothing
defense-shaped — no matter workspace, no cross-domain sealed package, no
who-knew-what-when reconstruction.

**Direction decided:**
- **Ownership boundary:** legal-defense features (matter workspace, counsel
  collaboration) belong to **openPractice's legal portion**, linked to
  openChart. openChart must carry and expose everything openPractice will
  later use for defense — sealed cross-domain evidence packages, timelines,
  attestations — through the integration seam. (Revises the review's R7:
  openChart owns evidence generation and export, openPractice owns the
  matter workspace.)
- **Companion attends all legal meetings**, with:
  - a provable **off-the-record mode** — nothing counsel rules off the record
    may be stored; off-record segments never reach durable storage;
  - **redact and correct** abilities on the record;
  - **attorney-client privilege engineered in** — a named legal-research work
    item; privilege rules vary by state (e.g., third party in the room), and
    whether the companion or an AI practitioner counts as a
    privilege-destroying third party must be answered per jurisdiction.
- **Audience: defense-side only** — the practice and its practitioners, not
  plaintiff tooling.
- **Reasoning-evidence rule:** the companion makes no decisions; only the
  practitioner does. The evidence packet therefore includes only the
  companion data the practitioner actually **used in decision-making**. For
  an AI practitioner's internal reasoning chain, decision-relevant elements
  are identified by **contemporaneous tagging during reasoning** — key
  elements are tagged as the reasoning happens, never reconstructed after.
- Working assumption to verify by legal research: a doctor's case/patient
  notes are discoverable, and companion notes are therefore discoverable too.

**Design consequences recorded:**
- Redaction must coexist with the append-only hash-chained ledger — content
  removal without breaking chain verifiability (tombstone-style), with the
  on/off-record transitions themselves logged even when content is not.
- "Used in decision-making" becomes a first-class provenance tag on
  companion outputs (runbook check-offs from Issue 1 and private-channel
  prompt consumption from Issues 2–3 feed it).
- The reasoning-tagging framework is general AI-evidence infrastructure:
  also needed later by the omnigent layer for treatment simulations (which
  protect the system, not the practitioner — separate problem, shared
  framework; forward pointer only).

**Open questions attached:**
- Legal research: does "used in decision-making" survive as a discovery
  scope line, given that surfaced-but-ignored companion output is the target
  of failure-to-heed claims? The tagging framework should capture *exposure*
  as well as *reliance* so counsel can decide later.
- The redaction model's exact mechanics against sec-022-style chain
  integrity.
- Per-state privilege matrix: when does companion presence, AI-practitioner
  presence, or multi-party attendance break privilege?

### Issue 5 — P5 Patient diagnostic research

**Finding (one line):** zero coverage — no hypothesis object (the pmr problem
list holds conclusions only), no workup-strategy comparison (lab-027 and
ord-012 don't reason over a differential), no external knowledge connectors,
no similar-patient evidence.

**Direction decided:**
- **The working differential becomes a first-class chart object**: competing
  candidate diagnoses with evidence links and uncertainty, versioned across
  encounters, distinct from the problem list, shared between practitioner and
  companion.
- **It is live during the visit**: the companion maintains and displays the
  differential as the encounter unfolds — symptoms heard shift hypotheses in
  real time — rather than differential work being a between-visit desk
  activity.

**Design consequences recorded:**
- The live differential is the anchor for Issue 2's real-time analysis:
  orders called out during the visit are evaluated against the active
  differential, and the companion can suggest discriminating
  questions/exams.
- The differential object is the clinical home for the AI practitioner's
  evolving reasoning about the patient (the longitudinal-state gap from
  Issue 2) and the spine of Issue 4's tagged reasoning evidence.
- Hypothesis-vs-conclusion separation preserves the problem list's meaning:
  promotion from working differential to problem-list conclusion is an
  explicit, signed practitioner decision.

**Open questions attached:**
- Knowledge-source priority for the next phase (literature/guidelines, drug
  reference, clinical-trial matching, own-cohort similar-patient evidence
  over anl-032/033) — not yet decided.
- Patient-facing visibility of the working differential (what does the
  patient see of hypotheses that are later ruled out?).

### Issue 6 — P6 Treatment plan research and creation

**Finding (one line):** the authoring spine exists (car-001–005, ord-013–016)
but there is no therapeutic-option research, no response tracking against the
plan, no outcome feedback, and no link to the patient-side loop.

**Direction decided:**
- **Working treatment options is a first-class object on the same pattern as
  the differential** (Issue 5): competing options held with evidence and
  uncertainty, live-discussable during the visit; the committed option
  becomes the signed versioned plan.
- **Treatment research and plan definition use the openXdox ideation
  dashboard** — the lens, the wheel, and the engineering-research machinery
  map onto medical research and treatment. openChart provides the seam by
  which an openXdox-researched plan lands as a versioned openChart plan.
- **Omnigent is in scope from day one**, in two roles: generating treatment
  options during research, and running simulations to explain results when
  actuals deviate. (The owner's initial "simulations later" was superseded by
  the explicit day-one scope answer in the same discussion.)
- **Response tracking flows primarily through the HealthLinc patient app into
  openChart.** HealthLinc also tracks adherence/compliance.
- **Deviation triage order:** adherence first ("was the plan followed?"),
  then omnigent simulation ("why doesn't the data fit despite adherence?").
- **Loud practitioner notification on deviation** — to AI or human doctor —
  via dashboard messages, SMS, email, phone calls, and notices in the
  doctor-side HealthLinc app.

**Design consequences recorded:**
- Plans must carry an **expected-response envelope** (expected ranges over
  time) for out-of-range detection to be computable; its source (omnigent
  simulation, literature, cohort evidence) is part of plan research.
- P8's "patient companion app" is **HealthLinc** — the R8 packet becomes a
  HealthLinc integration contract, not a new app build.
- A **doctor-side HealthLinc app** exists in the plan and is not yet named.

**Open questions attached:**
- Name for the doctor-side HealthLinc app.
- Notification escalation thresholds (what earns a phone call vs a dashboard
  message) and alert-fatigue policy.
- The openXdox↔openChart integration contract (how lens/wheel research
  artifacts map to plan objects).

### Issue 7 — P7 AI practitioner and openXwallet (partially recorded; credential mechanics pending openXwallet review)

**Finding (one line):** zero coverage and a structural contradiction (aic-036
encodes *human* as the gate predicate; ~575 entries forbid autonomous clinical
action), while the governance machinery (aic-022/023/026-028/033/043/044/046,
plt-005/043/044) transfers almost intact once the predicate becomes
*accountable credentialed practitioner*.

**Direction decided so far:**
- **openXwallet is existing capability, not a fresh design**: it lives today
  as features in openXfactory (the xFactory repo), is already used by
  MedxFactory, and will become its own repo-level project later. openChart
  adopts it rather than inventing a parallel credential system. A review of
  the current openXwallet feature set was commissioned before finalizing
  credential mechanics.
- **Scope enforcement is a soft block with graduated zones.** The AI is
  notified when it enters the grey zone. Zones quantify distance from the
  *license* boundary (it should be hard or impossible to leave the AI's
  *expertise*; the state license is the binding edge):
  - **Green** — well within the boundary.
  - **Yellow** — near the boundary, from the inside.
  - **Red** — near the boundary, from the outside.
  - **Black** — well outside the boundary; shutdown.
  This implies quantified scope metrics (distance-to-boundary must be
  computable) — a named design problem.
- **Transition period (pre-licensure):** run as if licensed, but **no orders
  take effect without signoff from a human medical director / managing
  physician**.
- **Environment split:** in QA testing, no signoff is required and the system
  pretends to hold the full practice license. On flip to production, a
  license number must be entered for the AI, **tied to a serial
  number/release of MedxFactory** — probably the **major release**, so minor
  updates do not require a new license (to be explored).

**Open questions attached:**
- **Licensed-identity continuity:** how do we prove the AI we licensed is the
  AI currently practicing — what counts as "the same practitioner" across
  model updates, and where is the major/minor line that triggers
  re-licensure?
- Zone quantification: what metric places an intended action in
  green/yellow/red/black, and who calibrates it per jurisdiction?
- ~~Patient consent/disclosure of AI treatment~~ — **decided**: consent to AI
  treatment is **one-time and revocable**, not per-encounter. Rationale: for
  at least the first year it will be clear to the patient that the
  practitioner is an AI, so per-visit notification is unnecessary. Riders:
  define what revocation triggers operationally (handoff to a human
  practitioner mid-course of care), and legal-research check that no target
  state mandates per-encounter AI disclosure regardless of obviousness.
- ~~Credential attestation contents, issuance, verification, revocation~~ —
  **resolved after the openXwallet review** (see below).

**openXwallet review outcome (recorded):** openXwallet is a ratified contract
family in openxFactory (contract-v1.31, 2026-08-07) — schemas, canonical
validator, CI, one live holder (a council with holder_class `agent`, the
council-wallet precedent). No runtime/issuance service yet. Identity is
**composition** (sha256 over declared components: model_version,
prompt_contract, tool_manifest, policy_version, parameters,
retrieval_corpus); authority travels as **monotonically narrowing grants**
(scope.acts/objects, expiry, revocation through derivation, checked at
exercise); proof of possession required. Binding doctrines inherited: a
wallet identifier is never a subject identifier (the AI physician keeps its
own practitioner identity in openChart), and every domain must remain
operable with no wallet at all. openChart adopts openXwallet vocabulary
(holder classes person/practitioner/organisation/agent; authority tiers
attest/request/act/act_unsupervised; wallet states active/suspended/revoked)
rather than inventing parallel terms.

**Credential decisions (closing Issue 7):**
- **openChart drives the new practitioner profile family** over the neutral
  openXwallet core — the sanctioned extension path — adding
  specialty/expertise attestation, state-license-number binding, the zone
  model, and a co-signature record kind.
- **License-vs-release posture: strict-revoke + fast reissue.** openXwallet's
  any-composition-change-revokes rule is kept; changes classified *minor* get
  fast, automatic re-issuance (the license persists; the wallet re-attests).
  Maximally defensible to a state board. Open design detail: which
  composition components are license-relevant (e.g., does a retrieval_corpus
  update — new medical literature — touch the license at all?).
- **Supervision tier mapping confirmed:** pre-licensure grants cap at `act`
  (human medical director / managing physician approval before apply);
  post-licensure `act_unsupervised`; QA runs `act_unsupervised` against
  synthetic data only. A co-signature record kind is added via the
  practitioner profile family.
- **Zones live in openChart's enforcement layer**, not the wallet: the wallet
  carries the scope; openChart computes green/yellow/red/black distance per
  intended action.
- **Third-party (court / state board) verification: deferred** to when
  openXwallet becomes its own repo-level project.
- Flag carried forward: MedxFactory's wallet brainstorms currently forbid
  agent-owned order signing — the same human-gate predicate to restate there
  as in the openChart catalog.

### Issue 8 — P8 Patient-side app integration (HealthLinc)

**Finding (one line):** the catalog has portal fragments (eng-036/037/038/039,
mob-029, pmr-021, phr-046) but no patient app, no plan-push contract, and no
composed adherence loop.

**Direction decided:**
- **The patient app is HealthLinc**, spanning **pre, during, and post visit**.
  It is the **first** app, not the only one: the openChart API is open and
  standards-compliant so third-party patient apps can join the same contract.
- **HealthLinc's own AI stack**, with a deliberate agency split:
  - a **companion** — structured, predefined tasks, records and structure;
    the openChart companion pattern mapped to the patient role. Its limits
    are deferred.
  - a **medical advisor AI licensed at nurse level** and a **medical research
    helper** — NOT task-bounded, but passing an **output safety check**; both
    exist partly to keep patients off uncensored internet AI producing
    unqualified research (named as the hardest patient-safety surface).
  - the advisor/researcher **outline every interaction for storage with the
    companion, noted for the next visit** — patient-side AI conversations
    become inputs to the practitioner's next prep runbook (closes into P1).
- **Chart-ward telemetry (to openChart via the intake discipline, as
  provenance-classed patient-reported/device statements):** compliance
  tracking plus field medical telemetry — pictures of food consumed, exercise
  amount, sleep and wake times, bowel movements, pills taken when and with or
  without food, BP, CGM connector, temperature, etc.
- **openPractice split confirmed from the patient side:** HealthLinc routes
  scheduling, bill pay, past-record requests, and administrative status to
  openPractice; openChart receives only the clinical loop.

**Design consequences recorded:**
- The **nurse-level AI is a second consumer of the P7 practitioner profile
  family** at nurse license scope — profile family, zones, and supervision
  tiers must support multiple license levels, with escalation to the treating
  practitioner as the boundary crossing.
- Patient-ward contract carries the versioned plan as actionable tasks and
  med schedules, plus education, visit-prep asks, and post-visit summaries
  (per the pre/during/post-visit scope).

**Open questions attached:**
- Output-safety-check design for the non-task-bounded nurse/researcher AIs.
- Companion limits in HealthLinc (explicitly deferred).
- Escalation contract between HealthLinc's nurse-level AI and the treating
  practitioner in openChart (when advice crosses into practice).

### Issue 9 — Boundary cleanup

**Finding (one line):** ~250 of 1,115 features sit in excluded territory
(billing, scheduling, HR/workforce, practice ops, supply chain); the
revenue-cycle strategy doc is a direct violation, and the
business-and-exchange synthesis welds revenue cycle to interoperability.

**Direction decided:**
- **Move, with overlap allowed.** The revenue-cycle strategy doc and the
  clearly openPractice-owned feature docs move to openPractice's ideation,
  leaving stub links behind. Overlap is legitimate: an atomic that is truly
  part of openChart may live in **both** repos.
- **The split rule for scheduling-flavored features:** booking/scheduling
  machinery (slots, cascades, calendars, the follow-up *appointment*) is
  openPractice; **pure clinical follow-up intent** (the recall's clinical
  reason, care-pathway sequences, the visit-start signal the companion
  consumes) stays in openChart, re-filed under car/tel. Applies to the sch
  clinical residue (sch-017/019/026/030/031/037/039/043/049 and kin).
- **Timing:** the cleanup is part of the next phase's work (owner answered
  "yes" to inclusion; if background-only was meant, adjust here).

## Next phase (closing summary)

The R1–R8 agenda from the feature review, as reshaped by these decisions:

- **R1 practitioner identity** → the **openXwallet practitioner profile
  family**, driven by openChart: specialty attestation, state-license
  binding (strict-revoke + fast minor reissue), co-signature record kind,
  zone model (green/yellow/red/black computed in openChart), supervision
  tiers mapped (act pre-licensure with medical-director signoff,
  act_unsupervised post-licensure, QA synthetic-only). Second consumer:
  HealthLinc's nurse-level AI.
- **R2 live visit companion** → live transcript + prompting, always on;
  room device + doctor mobile; two-witness dual-attested encounter record;
  modality-equal verbal protocol; split-surface Flutter sessions
  (room-common vs practitioner-private); voice-CPOE with real-time analysis
  against the live differential.
- **R3 diagnostic reasoning** → the working differential as a first-class,
  live-during-visit chart object; treatment options follow the same pattern
  (from R5).
- **R4 knowledge connectors** → needed by P1 Explain drill-down, P5, and
  HealthLinc's research helper; source priority still undecided.
- **R5 treatment-plan research bench** → research in the **openXdox
  ideation dashboard** (lens/wheel mapping); **omnigent from day one**
  (option generation + deviation explanation); expected-response envelope
  on every plan; loud multi-channel deviation notification.
- **R6 case collaboration** → conferences reuse the companion (witnessed
  encounter type); AI docs as full peers; live mind-map/graph UI; companion
  may ask and correct; internal + external with native teleconference.
- **R7 medico-legal** → matter workspace moves to **openPractice**;
  openChart owns the evidence substrate: cross-domain sealed packages,
  who-knew-what-when timelines, off-record mode, redact/correct,
  contemporaneous reasoning tagging (exposure and reliance), privilege
  engineering with state-by-state legal research.
- **R8 patient loop** → the **HealthLinc integration contract** (open,
  standards-compliant; HealthLinc is the first app): plan push, telemetry
  and adherence return, patient-side AI interaction outlines feeding the
  next prep runbook.
- **Boundary cleanup** (this issue) rides along in the next phase.

Cross-cutting frameworks named during discussion: the AI reasoning-evidence
tagging framework (shared with omnigent simulations), the prep-runbook
pattern (visit prep → case packets → patient visit-prep), and the
one-artifact-two-renderings principle (human-concise vs AI-full-graph).

Sequencing of the packets was not decided in this discussion.
