"""Transparent operational risk rules for simulated pathway cases."""

from __future__ import annotations

from typing import Any


LOW_MAX_SCORE = 2
MEDIUM_MAX_SCORE = 5
HIGH_MAX_SCORE = 8


def normalize_text(value: Any) -> str:
    """Return a lower-case string for simple deterministic comparisons."""
    if value is None:
        return ""
    return str(value).strip().lower()


def is_yes(value: Any) -> bool:
    """Return whether a yes/no field is marked as yes."""
    return normalize_text(value) == "yes"


def evaluate_risk_factors(case: dict[str, Any]) -> list[dict[str, Any]]:
    """Evaluate one simulated pathway case against transparent risk rules."""
    factors: list[dict[str, Any]] = []

    days_waiting = int(case["days_waiting"])
    target_days = int(case["target_days"])
    days_over_target = days_waiting - target_days
    pathway_type = normalize_text(case["pathway_type"])
    risk_flags = normalize_text(case.get("risk_flags", ""))
    diagnostic_status = normalize_text(case["diagnostic_status"])
    treatment_status = normalize_text(case["treatment_status"])
    clinical_priority = normalize_text(case["clinical_priority"])
    last_contact_days = int(case["last_contact_days"])

    if days_over_target > 0:
        score = 4 if days_over_target >= max(7, int(target_days * 0.2)) else 3
        factors.append(
            {
                "name": "Waiting time beyond target",
                "score": score,
                "detail": (
                    f"Case has waited {days_waiting} days against a "
                    f"{target_days}-day target."
                ),
            }
        )
    elif target_days - days_waiting <= 2:
        factors.append(
            {
                "name": "Close to pathway target",
                "score": 1,
                "detail": (
                    f"Case is within {target_days - days_waiting} day(s) "
                    f"of the {target_days}-day target."
                ),
            }
        )

    if last_contact_days >= 10:
        factors.append(
            {
                "name": "No recent contact",
                "score": 2,
                "detail": f"Last recorded contact was {last_contact_days} days ago.",
            }
        )
    elif last_contact_days >= 7:
        factors.append(
            {
                "name": "Contact may need refresh",
                "score": 1,
                "detail": f"Last recorded contact was {last_contact_days} days ago.",
            }
        )

    if diagnostic_status in {"delayed", "not started"}:
        factors.append(
            {
                "name": "Diagnostics not progressing",
                "score": 3,
                "detail": f"Diagnostic status is {case['diagnostic_status']}.",
            }
        )
    elif diagnostic_status == "pending":
        factors.append(
            {
                "name": "Diagnostics pending",
                "score": 2,
                "detail": "Diagnostic result or completion is still pending.",
            }
        )

    if treatment_status == "not yet booked":
        factors.append(
            {
                "name": "Treatment not booked",
                "score": 2,
                "detail": "Treatment is not yet booked where pathway planning is active.",
            }
        )

    if is_yes(case["capacity_issue"]):
        factors.append(
            {
                "name": "Capacity issue",
                "score": 2,
                "detail": "A service capacity constraint is recorded.",
            }
        )

    if is_yes(case["admin_blocker"]):
        factors.append(
            {
                "name": "Administrative blocker",
                "score": 2,
                "detail": "An administrative blocker is preventing pathway progress.",
            }
        )

    if clinical_priority == "urgent":
        factors.append(
            {
                "name": "Urgent clinical priority",
                "score": 2,
                "detail": "The case is marked as urgent priority for operational review.",
            }
        )

    if "delayed appointment" in risk_flags:
        factors.append(
            {
                "name": "Delayed appointment",
                "score": 2,
                "detail": "The recorded risk flags include a delayed appointment.",
            }
        )

    if pathway_type in {"cancer 2ww", "cancer 62-day"}:
        factors.append(
            {
                "name": "Time-sensitive cancer pathway",
                "score": 1,
                "detail": f"{case['pathway_type']} has a time-sensitive operational target.",
            }
        )
    elif pathway_type == "urgent care follow-up" and days_over_target > 0:
        factors.append(
            {
                "name": "Overdue urgent follow-up pathway",
                "score": 1,
                "detail": "Urgent care follow-up is beyond its short operational target.",
            }
        )

    return factors


def calculate_risk_score(factors: list[dict[str, Any]]) -> int:
    """Calculate an additive risk score from evaluated factors."""
    return sum(int(factor["score"]) for factor in factors)


def determine_risk_level(
    risk_score: int, case: dict[str, Any], factors: list[dict[str, Any]]
) -> str:
    """Convert a risk score into a risk level, with one urgent escalation rule."""
    factor_names = {normalize_text(factor["name"]) for factor in factors}
    is_urgent = normalize_text(case["clinical_priority"]) == "urgent"
    is_overdue = int(case["days_waiting"]) > int(case["target_days"])
    has_unresolved_blocker = bool(
        factor_names
        & {
            "diagnostics not progressing",
            "diagnostics pending",
            "treatment not booked",
            "capacity issue",
            "administrative blocker",
            "no recent contact",
            "delayed appointment",
        }
    )

    if is_urgent and is_overdue and has_unresolved_blocker:
        return "Critical"
    if risk_score > HIGH_MAX_SCORE:
        return "Critical"
    if risk_score > MEDIUM_MAX_SCORE:
        return "High"
    if risk_score > LOW_MAX_SCORE:
        return "Medium"
    return "Low"
