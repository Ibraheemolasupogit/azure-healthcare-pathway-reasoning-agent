"""Explainable pathway reasoning engine for simulated cases."""

from __future__ import annotations

from typing import Any

import pandas as pd

from src.agent.risk_rules import (
    calculate_risk_score,
    determine_risk_level,
    evaluate_risk_factors,
    is_yes,
    normalize_text,
)


def _case_to_dict(case: dict[str, Any] | pd.Series) -> dict[str, Any]:
    if isinstance(case, pd.Series):
        return case.to_dict()
    return dict(case)


def _build_reasoning_explanation(
    case: dict[str, Any], risk_level: str, factors: list[dict[str, Any]]
) -> str:
    pathway_label = str(case["pathway_type"])
    pathway_phrase = (
        pathway_label
        if pathway_label.lower().endswith("pathway")
        else f"{pathway_label} pathway"
    )

    if not factors:
        return (
            f"Case {case['case_id']} is currently assessed as Low risk because no "
            "material operational risk factors were identified in the simulated data."
        )

    factor_details = " ".join(factor["detail"] for factor in factors)
    return (
        f"Case {case['case_id']} is assessed as {risk_level} risk on the "
        f"{pathway_phrase}. {factor_details}"
    )


def _build_recommended_actions(case: dict[str, Any], risk_level: str) -> list[str]:
    actions: list[str] = []

    days_waiting = int(case["days_waiting"])
    target_days = int(case["target_days"])
    risk_flags = normalize_text(case.get("risk_flags", ""))
    diagnostic_status = normalize_text(case["diagnostic_status"])
    treatment_status = normalize_text(case["treatment_status"])
    last_contact_days = int(case["last_contact_days"])

    if days_waiting > target_days:
        actions.append("Review pathway breach position and confirm an owner today.")
    elif target_days - days_waiting <= 2:
        actions.append("Check that the next pathway step is confirmed before target date.")

    if last_contact_days >= 7:
        actions.append("Update patient or pathway contact record and confirm current status.")

    if diagnostic_status in {"pending", "delayed", "not started"}:
        actions.append("Follow up diagnostics and confirm the expected completion date.")

    if treatment_status == "not yet booked":
        actions.append("Confirm treatment booking requirements and identify the booking owner.")

    if is_yes(case["capacity_issue"]):
        actions.append("Escalate capacity constraint to the relevant service manager.")

    if is_yes(case["admin_blocker"]):
        actions.append("Resolve the administrative blocker or route it to the correct team.")

    if normalize_text(case["clinical_priority"]) == "urgent":
        actions.append("Prioritise review because the case is marked urgent.")

    if "delayed appointment" in risk_flags:
        actions.append("Seek an earlier appointment slot or document why delay is unavoidable.")

    if risk_level in {"High", "Critical"}:
        actions.append("Add the case to the operational escalation list for human review.")

    if not actions:
        actions.append("Continue routine pathway monitoring.")

    return list(dict.fromkeys(actions))


def assess_pathway_case(case: dict[str, Any] | pd.Series) -> dict[str, Any]:
    """Assess one simulated pathway case and return explainable risk output."""
    case_data = _case_to_dict(case)
    factors = evaluate_risk_factors(case_data)
    risk_score = calculate_risk_score(factors)
    risk_level = determine_risk_level(risk_score, case_data, factors)

    return {
        "case_id": case_data["case_id"],
        "risk_level": risk_level,
        "risk_score": risk_score,
        "identified_risk_factors": factors,
        "reasoning_explanation": _build_reasoning_explanation(
            case_data, risk_level, factors
        ),
        "recommended_next_actions": _build_recommended_actions(
            case_data, risk_level
        ),
    }
