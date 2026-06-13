"""Structured escalation note generation for simulated pathway cases."""

from __future__ import annotations

from typing import Any

import pandas as pd

from src.agent.risk_rules import is_yes, normalize_text


SAFETY_STATEMENT = (
    "Operational decision support only. This note is not clinical diagnosis, "
    "does not provide treatment advice, and requires human review before action."
)


def _case_to_dict(case: dict[str, Any] | pd.Series) -> dict[str, Any]:
    if isinstance(case, pd.Series):
        return case.to_dict()
    return dict(case)


def suggest_owner_or_team(case: dict[str, Any], reasoning_output: dict[str, Any]) -> str:
    """Suggest an operational owner based on the active risk pattern."""
    factor_names = {
        normalize_text(factor["name"])
        for factor in reasoning_output.get("identified_risk_factors", [])
    }

    if is_yes(case["admin_blocker"]) or "administrative blocker" in factor_names:
        return "Pathway administration team"
    if (
        normalize_text(case["diagnostic_status"])
        in {"pending", "delayed", "not started"}
        or "diagnostics pending" in factor_names
        or "diagnostics not progressing" in factor_names
    ):
        return "Diagnostics coordination team"
    if (
        normalize_text(case["treatment_status"]) == "not yet booked"
        or "treatment not booked" in factor_names
    ):
        return "Treatment booking team"
    if is_yes(case["capacity_issue"]) or "capacity issue" in factor_names:
        return "Service manager"
    if reasoning_output["risk_level"] in {"High", "Critical"}:
        return "Pathway coordination lead"
    return "Pathway coordination team"


def urgency_wording(risk_level: str) -> str:
    """Return professional urgency wording for the escalation note."""
    urgency_by_level = {
        "Critical": "Immediate operational review required today.",
        "High": "Priority operational review required.",
        "Medium": "Review recommended at the next coordination huddle.",
        "Low": "Routine monitoring recommended.",
    }
    return urgency_by_level.get(risk_level, "Human review recommended.")


def generate_escalation_note(
    case: dict[str, Any] | pd.Series, reasoning_output: dict[str, Any]
) -> dict[str, Any]:
    """Create a structured operational escalation note."""
    case_data = _case_to_dict(case)
    key_risk_factors = [
        factor["name"] for factor in reasoning_output["identified_risk_factors"]
    ]

    return {
        "case_summary": (
            f"Case {case_data['case_id']} is at {case_data['current_stage']} "
            f"after {case_data['days_waiting']} days waiting against a "
            f"{case_data['target_days']}-day target. Next appointment: "
            f"{case_data['next_appointment_date']}."
        ),
        "pathway_type": case_data["pathway_type"],
        "risk_level": reasoning_output["risk_level"],
        "risk_score": reasoning_output["risk_score"],
        "key_risk_factors": key_risk_factors,
        "reasoning_summary": reasoning_output["reasoning_explanation"],
        "recommended_next_actions": reasoning_output["recommended_next_actions"],
        "suggested_owner_or_team": suggest_owner_or_team(case_data, reasoning_output),
        "urgency_wording": urgency_wording(reasoning_output["risk_level"]),
        "human_review_reminder": (
            "A human pathway coordinator or service lead must review this note "
            "before any operational action is taken."
        ),
        "safety_statement": SAFETY_STATEMENT,
    }


def render_escalation_note_markdown(note: dict[str, Any]) -> str:
    """Render a structured escalation note as Markdown."""
    risk_factors = "\n".join(
        f"- {factor}" for factor in note["key_risk_factors"]
    ) or "- No material operational risk factors identified"
    actions = "\n".join(
        f"- {action}" for action in note["recommended_next_actions"]
    )

    return "\n".join(
        [
            "# Structured Escalation Note",
            "",
            f"**Case summary:** {note['case_summary']}",
            f"**Pathway type:** {note['pathway_type']}",
            f"**Risk level:** {note['risk_level']}",
            f"**Risk score:** {note['risk_score']}",
            "",
            "## Key Risk Factors",
            "",
            risk_factors,
            "",
            "## Reasoning Summary",
            "",
            note["reasoning_summary"],
            "",
            "## Recommended Next Actions",
            "",
            actions,
            "",
            "## Suggested Owner Or Team",
            "",
            note["suggested_owner_or_team"],
            "",
            "## Urgency",
            "",
            note["urgency_wording"],
            "",
            "## Human Review Reminder",
            "",
            note["human_review_reminder"],
            "",
            "## Safety Statement",
            "",
            note["safety_statement"],
            "",
        ]
    )
