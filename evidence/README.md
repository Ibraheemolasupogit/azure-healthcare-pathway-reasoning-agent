# Evidence

This folder contains sample outputs and demo evidence for the Azure Healthcare Pathway Reasoning Agent.

## Included Evidence Files

The current evidence set includes generated Markdown escalation notes:

- `sample_outputs/escalation_note_SIM-0017.md`
- `sample_outputs/escalation_note_SIM-0009.md`
- `sample_outputs/escalation_note_SIM-0027.md`

These files were generated from fully synthetic pathway cases and show the structure of the escalation note output used in the Streamlit demo.

## How Sample Escalation Notes Support The Demo

The sample notes help judges and reviewers inspect the project output without running the app first. Each note includes:

- Case summary.
- Pathway type.
- Risk level.
- Risk score.
- Key risk factors.
- Reasoning summary.
- Recommended next actions.
- Suggested owner or team.
- Urgency wording.
- Human review reminder.
- Safety statement.

The notes demonstrate how the agent converts structured synthetic pathway data into operationally useful, human-reviewable output.

## Screenshots

Screenshots can be added later under:

```text
evidence/screenshots/
```

Suggested screenshots:

- Streamlit case selector.
- Risk assessment panel.
- Risk factors tab.
- Reasoning tab.
- Escalation note tab.
- Markdown download result.

## How To Inspect Outputs

Judges or reviewers can open the Markdown files directly in this repository or run the Streamlit demo:

```bash
streamlit run app.py
```

Then select the matching synthetic case IDs and compare the app output with the sample notes.

## Safety Note

All evidence files use simulated data only. They do not include real patient data, protected health information, real NHS integration, live Azure deployment, or live Microsoft 365 Copilot integration.

