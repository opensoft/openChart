"""The versioned intake API (T009; FR-003, FR-004, FR-006, FR-007, FR-008).

`open_chart.api.v1` is the ONE supported write surface. Every endpoint:

- enforces subject/tenant/purpose/role context BEFORE touching data
  (FR-007) — a missing submitter context or purpose reference refuses;
- delegates every decision to the pure functions in
  ``open_chart.intake.core`` (idempotency D5, identity FR-002,
  succession D4) so the bench-free validator exercises the same logic;
- writes under the guard flag the controllers demand — nothing else in
  the process may set it (brief D6).

Nothing here creates a prescription, diagnosis, order, administration,
recommendation, or autonomous action; events carry pointers, never new
clinical claims (FR-008).
"""

from __future__ import annotations

import json
from typing import Any, Mapping

try:
    import frappe
except ImportError:  # bench-free repo validation
    frappe = None

from open_chart.intake import core

FINDING_CONTEXT = "OC-CONTEXT-REQUIRED"
FINDING_IDEMPOTENCY = "OC-IDEMPOTENCY-DIVERGED"

SUBMISSION = "OC Intake Submission"
IDENTIFIER = "OC Patient External Identifier"


def whitelist(func):
    return frappe.whitelist()(func) if frappe else func


def _require_context(submitter_context: str, purpose_or_consent_ref: str) -> None:
    """FR-007: subject/tenant context and purpose travel with every write."""
    if not str(submitter_context or "").strip() or not str(purpose_or_consent_ref or "").strip():
        frappe.throw(
            f"{FINDING_CONTEXT}: submitter_context and purpose_or_consent_ref are required "
            "on every intake write (FR-007)"
        )
    frappe.only_for(("System Manager",), message=True)


def _payload(payload: Any) -> dict:
    return json.loads(payload) if isinstance(payload, str) else dict(payload)


def _existing_submissions(patient: str) -> list[dict]:
    """The patient's submissions with each one's stored content hash,
    recomputed from its statement rows — divergence is judged on stored
    content, never on a transcribed value."""
    rows = []
    for sub in frappe.get_all(
        SUBMISSION, filters={"patient": patient}, fields=["name", "patient", "idempotency_key"]
    ):
        rows.append({**sub, "content_hash": core.content_hash(_statement_rows(sub["name"]))})
    return rows


def _statement_rows(submission_name: str) -> list[dict]:
    census = core.load_census()
    rows: list[dict] = []
    for family_name, mapping in core.family_maps(census).items():
        fieldnames = ["name", "assertion_kind", *mapping["fields"].values()]
        for doc in frappe.get_all(
            mapping["doctype"], filters={"submission": submission_name}, fields=fieldnames
        ):
            fields = {k: v for k, v in doc.items() if k != "name" and v not in (None, "")}
            rows.append({"doctype": mapping["doctype"], "record_family": family_name, "fields": fields})
    return sorted(rows, key=lambda r: str((r.get("fields") or {}).get("source_entry_id")))


@whitelist
def submit(
    patient: str,
    contract_version: str,
    idempotency_key: str,
    payload,
    submitter_context: str,
    purpose_or_consent_ref: str,
):
    """Idempotent submit (FR-003/FR-004): replay returns the existing
    submission and creates NOTHING; divergence refuses loudly."""
    _require_context(submitter_context, purpose_or_consent_ref)
    body = _payload(payload)
    census = core.load_census()
    rows = core.build_rows(body, census)
    decision, existing_name = core.idempotency_decision(
        _existing_submissions(patient), patient, idempotency_key, core.content_hash(rows)
    )
    if decision == core.DECISION_REPLAY:
        return read_submission(existing_name)
    if decision == core.DECISION_DIVERGED:
        frappe.throw(
            f"{FINDING_IDEMPOTENCY}: idempotency key {idempotency_key!r} was already used by "
            f"{existing_name} with DIFFERENT content; a replay must be byte-identical (FR-004)"
        )
    frappe.flags.oc_api_write = True
    try:
        submission = frappe.get_doc(
            {
                "doctype": SUBMISSION,
                "patient": patient,
                "contract_version": contract_version,
                "submission_version": 1,
                "lifecycle_state": "accepted",
                "submitter_context": submitter_context,
                "purpose_or_consent_ref": purpose_or_consent_ref,
                "submitted_time": frappe.utils.now_datetime(),
                "provenance": f"submitted via open_chart.api.v1 by {frappe.session.user}",
                "idempotency_key": idempotency_key,
            }
        ).insert()
        for row in rows:
            frappe.get_doc(
                {"doctype": row["doctype"], "patient": patient, "submission": submission.name, **row["fields"]}
            ).insert()
    finally:
        frappe.flags.oc_api_write = False
    return read_submission(submission.name)


@whitelist
def amend(submission_name: str, payload, reason: str, submitter_context: str):
    """Succession amendment (FR-006; brief D4): a successor document is
    created, the prior transitions accepted -> amended, content stays."""
    prior = frappe.get_doc(SUBMISSION, submission_name)
    _require_context(submitter_context, prior.purpose_or_consent_ref)
    fields = core.successor_fields(
        prior.as_dict(), submitter_context, reason, frappe.utils.now_datetime()
    )
    census = core.load_census()
    rows = core.build_rows(_payload(payload), census)
    frappe.flags.oc_api_write = True
    try:
        successor = frappe.get_doc({"doctype": SUBMISSION, **fields}).insert()
        for row in rows:
            frappe.get_doc(
                {
                    "doctype": row["doctype"],
                    "patient": prior.patient,
                    "submission": successor.name,
                    **row["fields"],
                }
            ).insert()
        frappe.flags.oc_api_amend = True
        try:
            prior.lifecycle_state = "amended"
            prior.save()
        finally:
            frappe.flags.oc_api_amend = False
    finally:
        frappe.flags.oc_api_write = False
    return read_submission(successor.name)


@whitelist
def read_submission(submission_name: str) -> dict:
    """The read surface consumers (MedxEHR included) use — never tables."""
    submission = frappe.get_doc(SUBMISSION, submission_name)
    submission.check_permission("read")
    return {
        "submission": {
            "name": submission.name,
            "patient": submission.patient,
            "contract_version": submission.contract_version,
            "submission_version": submission.submission_version,
            "lifecycle_state": submission.lifecycle_state,
            "idempotency_key": submission.idempotency_key,
            "predecessor": submission.predecessor,
            "amendment_reason": submission.amendment_reason,
        },
        "rows": _statement_rows(submission.name),
    }


@whitelist
def register_external_identifier(
    patient: str, issuer_or_endpoint: str, namespace: str, value: str, provenance: str = ""
):
    """FR-002: conflict enters identity review — never a merge. The
    decision is core.identity_decision; the controller guard enforces
    the same rule against any path that slips past this endpoint."""
    frappe.only_for(("System Manager",), message=True)
    decision = core.identity_decision(
        frappe.get_all(IDENTIFIER, fields=["patient", "issuer_or_endpoint", "value", "status"]),
        patient,
        issuer_or_endpoint,
        value,
    )
    frappe.flags.oc_api_write = True
    try:
        doc = frappe.get_doc(
            {
                "doctype": IDENTIFIER,
                "patient": patient,
                "issuer_or_endpoint": issuer_or_endpoint,
                "namespace": namespace,
                "value": value,
                "status": "active" if decision == core.DECISION_REGISTER else "identity_review",
                "provenance": provenance or f"registered via open_chart.api.v1 by {frappe.session.user}",
            }
        ).insert()
    finally:
        frappe.flags.oc_api_write = False
    return {"name": doc.name, "status": doc.status}


def emit_submission_event(doc, method=None):
    """hooks.py doc_events target: a pointer-only event (FR-008) for
    supported consumers; no clinical content, no derived claims."""
    if frappe is None:
        return
    frappe.publish_realtime(
        "oc_intake_submission_update",
        {"submission": doc.name, "lifecycle_state": doc.lifecycle_state, "patient": doc.patient},
        after_commit=True,
    )
