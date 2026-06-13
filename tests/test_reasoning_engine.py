import pandas as pd

from src.agent.reasoning_engine import assess_pathway_case


def make_case(**overrides: object) -> dict[str, object]:
    case = {
        "case_id": "SIM-TEST",
        "pathway_type": "RTT elective",
        "referral_date": "2026-06-01",
        "days_waiting": 20,
        "target_days": 126,
        "current_stage": "Waiting list",
        "last_contact_days": 2,
        "diagnostic_status": "Completed",
        "treatment_status": "Planned",
        "risk_flags": "none",
        "capacity_issue": "No",
        "admin_blocker": "No",
        "clinical_priority": "Routine",
        "next_appointment_date": "2026-06-20",
        "notes": "Synthetic case: test record.",
    }
    case.update(overrides)
    return case


def test_low_risk_case() -> None:
    result = assess_pathway_case(make_case())

    assert result["risk_level"] == "Low"
    assert result["risk_score"] <= 2


def test_medium_risk_case() -> None:
    result = assess_pathway_case(
        make_case(
            case_id="SIM-MEDIUM",
            pathway_type="Cancer 2WW",
            days_waiting=10,
            target_days=14,
            diagnostic_status="Pending",
        )
    )

    assert result["risk_level"] == "Medium"
    assert result["risk_score"] > 2


def test_high_risk_case() -> None:
    result = assess_pathway_case(
        make_case(
            case_id="SIM-HIGH",
            days_waiting=134,
            target_days=126,
            last_contact_days=8,
            treatment_status="Not yet booked",
            capacity_issue="Yes",
        )
    )

    assert result["risk_level"] == "High"


def test_critical_risk_case() -> None:
    result = assess_pathway_case(
        make_case(
            case_id="SIM-CRITICAL",
            pathway_type="Cancer 62-day",
            days_waiting=75,
            target_days=62,
            last_contact_days=9,
            diagnostic_status="Delayed",
            treatment_status="Not yet booked",
            capacity_issue="Yes",
            clinical_priority="Urgent",
        )
    )

    assert result["risk_level"] == "Critical"


def test_output_contains_recommended_actions() -> None:
    result = assess_pathway_case(
        make_case(diagnostic_status="Pending", clinical_priority="Urgent")
    )

    assert result["recommended_next_actions"]
    assert any("diagnostics" in action.lower() for action in result["recommended_next_actions"])


def test_output_contains_reasoning_explanation_for_series_input() -> None:
    result = assess_pathway_case(
        pd.Series(make_case(case_id="SIM-SERIES", admin_blocker="Yes"))
    )

    assert result["reasoning_explanation"]
    assert "SIM-SERIES" in result["reasoning_explanation"]
