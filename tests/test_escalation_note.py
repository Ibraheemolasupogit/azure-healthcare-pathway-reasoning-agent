from src.agent.escalation_note import (
    generate_escalation_note,
    render_escalation_note_markdown,
)
from src.agent.reasoning_engine import assess_pathway_case


def make_case(**overrides: object) -> dict[str, object]:
    case = {
        "case_id": "SIM-NOTE",
        "pathway_type": "RTT elective",
        "referral_date": "2026-01-10",
        "days_waiting": 154,
        "target_days": 126,
        "current_stage": "Outpatient follow-up",
        "last_contact_days": 4,
        "diagnostic_status": "Completed",
        "treatment_status": "Planned",
        "risk_flags": "long wait",
        "capacity_issue": "No",
        "admin_blocker": "No",
        "clinical_priority": "Routine",
        "next_appointment_date": "2026-06-21",
        "notes": "Synthetic case: test escalation note record.",
    }
    case.update(overrides)
    return case


def test_note_generation_for_high_risk_case() -> None:
    case = make_case(
        case_id="SIM-HIGH-NOTE",
        treatment_status="Not yet booked",
        capacity_issue="Yes",
    )
    reasoning = assess_pathway_case(case)
    note = generate_escalation_note(case, reasoning)

    assert note["risk_level"] == "High"
    assert note["risk_score"] == reasoning["risk_score"]
    assert note["suggested_owner_or_team"]


def test_note_generation_for_critical_risk_case() -> None:
    case = make_case(
        case_id="SIM-CRITICAL-NOTE",
        pathway_type="Cancer 62-day",
        days_waiting=75,
        target_days=62,
        diagnostic_status="Delayed",
        treatment_status="Not yet booked",
        capacity_issue="Yes",
        clinical_priority="Urgent",
    )
    reasoning = assess_pathway_case(case)
    note = generate_escalation_note(case, reasoning)

    assert note["risk_level"] == "Critical"
    assert "Immediate operational review" in note["urgency_wording"]


def test_note_includes_recommended_actions() -> None:
    case = make_case(diagnostic_status="Pending")
    reasoning = assess_pathway_case(case)
    note = generate_escalation_note(case, reasoning)

    assert note["recommended_next_actions"]
    assert any("diagnostics" in action.lower() for action in note["recommended_next_actions"])


def test_note_includes_human_review_wording() -> None:
    case = make_case()
    reasoning = assess_pathway_case(case)
    note = generate_escalation_note(case, reasoning)
    rendered_note = render_escalation_note_markdown(note)

    assert "requires human review" in note["safety_statement"].lower()
    assert "must review this note" in note["human_review_reminder"].lower()
    assert "Human Review Reminder" in rendered_note


def test_note_does_not_include_real_patient_identifiers() -> None:
    case = make_case()
    reasoning = assess_pathway_case(case)
    note = generate_escalation_note(case, reasoning)
    rendered_note = render_escalation_note_markdown(note).lower()

    disallowed_identifier_terms = [
        "nhs number",
        "date of birth",
        "dob",
        "patient name",
        "address",
        "postcode",
    ]

    assert not any(term in rendered_note for term in disallowed_identifier_terms)
