# Demo Walkthrough

This walkthrough is designed for a 3 to 5 minute Microsoft Agents League hackathon demo. The app uses fully synthetic data and runs locally.

## Setup

Run the Streamlit app:

```bash
streamlit run app.py
```

Open the local URL shown in the terminal.

## Demo Flow

### 1. Introduce The Scenario

Explain that healthcare pathway teams need to spot operational risks across referrals, diagnostics, appointments, treatment booking, and follow-up steps.

State the safety boundary clearly: the dataset is fully synthetic, the app is for operational decision support only, and outputs require human review.

### 2. Select A Low Or Routine Case

Use the case selector to choose a lower-risk case such as `SIM-0026`.

Show:

- Pathway case details.
- Low risk level and low risk score.
- Routine monitoring recommendation.

This establishes the baseline behavior.

### 3. Select A High-Risk Case

Choose a case such as `SIM-0017`.

Show:

- Risk level and score.
- Identified risk factors.
- Reasoning explanation.
- Recommended next actions.

Emphasize that the logic is deterministic, transparent, and grounded in the visible case fields.

### 4. Select A Critical Case

Choose a case such as `SIM-0009`.

Show:

- Critical risk level.
- Multiple contributing risk factors.
- Immediate operational review wording.
- Suggested owner or team.

Explain how this supports pathway coordination teams by turning raw pathway status into structured operational reasoning.

### 5. Show The Escalation Note

Open the Escalation Note tab and use the download button.

Highlight:

- Case summary.
- Key risk factors.
- Reasoning summary.
- Recommended next actions.
- Human review reminder.
- Safety statement.

Close by noting that this is a local-first prototype aligned with Microsoft AI Foundry and Azure AI agent patterns, without calling external AI APIs yet.

