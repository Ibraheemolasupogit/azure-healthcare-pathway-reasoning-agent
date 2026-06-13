"""Streamlit demo for the healthcare pathway reasoning agent."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from src.agent.escalation_note import (
    generate_escalation_note,
    render_escalation_note_markdown,
)
from src.agent.reasoning_engine import assess_pathway_case
from src.data.load_cases import load_cases


@st.cache_data
def load_demo_cases() -> pd.DataFrame:
    """Load simulated cases for the Streamlit demo."""
    return load_cases()


def display_case_details(case: pd.Series) -> None:
    """Render selected case details."""
    st.subheader("Selected Pathway Case")
    st.dataframe(
        case.to_frame(name="value"),
        use_container_width=True,
    )


def display_risk_factors(factors: list[dict[str, object]]) -> None:
    """Render risk factors in a compact table."""
    if not factors:
        st.info("No material operational risk factors identified.")
        return

    st.dataframe(
        pd.DataFrame(factors)[["name", "score", "detail"]],
        use_container_width=True,
        hide_index=True,
    )


def display_recommended_actions(actions: list[str]) -> None:
    """Render recommended next actions."""
    for action in actions:
        st.markdown(f"- {action}")


def main() -> None:
    st.set_page_config(
        page_title="Healthcare Pathway Reasoning Agent",
        layout="wide",
    )

    st.title("Healthcare Pathway Reasoning Agent")
    st.caption(
        "Local-first demo using fully synthetic pathway data. "
        "Operational decision support only; not clinical diagnosis."
    )

    cases = load_demo_cases()
    case_ids = cases["case_id"].tolist()

    selected_case_id = st.sidebar.selectbox(
        "Select a synthetic case",
        case_ids,
        index=0,
    )
    selected_case = cases.loc[cases["case_id"] == selected_case_id].iloc[0]

    reasoning_output = assess_pathway_case(selected_case)
    escalation_note = generate_escalation_note(selected_case, reasoning_output)
    escalation_note_markdown = render_escalation_note_markdown(escalation_note)

    st.sidebar.markdown("### Safety Boundary")
    st.sidebar.info(
        "This prototype uses simulated data only. Outputs require human review "
        "and must not be used for clinical diagnosis or treatment decisions."
    )

    summary_col, detail_col = st.columns([1, 2])

    with summary_col:
        st.subheader("Risk Assessment")
        st.metric("Risk Level", reasoning_output["risk_level"])
        st.metric("Risk Score", reasoning_output["risk_score"])
        st.write(f"**Suggested owner:** {escalation_note['suggested_owner_or_team']}")
        st.write(f"**Urgency:** {escalation_note['urgency_wording']}")
        st.download_button(
            label="Download Escalation Note",
            data=escalation_note_markdown,
            file_name=f"escalation_note_{selected_case_id}.md",
            mime="text/markdown",
        )

    with detail_col:
        display_case_details(selected_case)

    tab_factors, tab_reasoning, tab_actions, tab_note = st.tabs(
        [
            "Risk Factors",
            "Reasoning",
            "Next Actions",
            "Escalation Note",
        ]
    )

    with tab_factors:
        display_risk_factors(reasoning_output["identified_risk_factors"])

    with tab_reasoning:
        st.subheader("Reasoning Explanation")
        st.write(reasoning_output["reasoning_explanation"])

    with tab_actions:
        st.subheader("Recommended Next Actions")
        display_recommended_actions(reasoning_output["recommended_next_actions"])

    with tab_note:
        st.subheader("Structured Escalation Note")
        st.markdown(escalation_note_markdown)


if __name__ == "__main__":
    main()
