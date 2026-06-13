# Demo Script

This script is designed for a 5-minute demo video.

## 0:00-0:40 Opening Problem Statement

Healthcare pathway teams manage many moving parts: referrals, diagnostics, appointments, treatment booking, capacity constraints, and follow-up. When delays or blockers appear, teams need to understand which pathways need attention, why they are risky, and what action should happen next.

This project explores that operational challenge with a local-first reasoning agent using fully synthetic healthcare pathway data.

## 0:40-1:20 Project Overview

The project is called Azure Healthcare Pathway Reasoning Agent. It is built for the Reasoning Agents track.

The agent loads simulated pathway cases, applies transparent rules, generates a risk score and risk level, explains the reasoning in operational language, recommends next actions, and creates a structured escalation note for human review.

The prototype is deterministic. It does not call external AI APIs and does not use real patient data.

## 1:20-2:20 App Walkthrough

Open the Streamlit app.

Show the case selector in the sidebar and select a routine case first, such as `SIM-0026`. Point out the selected pathway details, risk level, score, and routine monitoring recommendation.

Then select a higher-risk case such as `SIM-0017`. Show the risk assessment panel, the selected case fields, and the tabs for risk factors, reasoning, next actions, and escalation note.

Explain that the app is intentionally simple so judges can inspect the complete reasoning flow.

## 2:20-3:10 Reasoning Explanation

Open the Risk Factors and Reasoning tabs.

Explain that the engine considers waiting time against target, last contact, diagnostic status, treatment booking status, capacity issues, admin blockers, urgent priority, delayed appointments, and pathway type.

Emphasize that every risk factor is visible and deterministic. The app is not making hidden model calls; it is showing a transparent first version of an operational reasoning agent.

## 3:10-4:00 Escalation Note Explanation

Open the Escalation Note tab.

Show the structured note sections:

- Case summary.
- Pathway type.
- Risk level and score.
- Key risk factors.
- Reasoning summary.
- Recommended next actions.
- Suggested owner or team.
- Urgency wording.
- Human review reminder.
- Safety statement.

Use the download button to show that the escalation note can be exported as Markdown.

## 4:00-4:35 Safety And Human Review Statement

State clearly that the project uses simulated data only. It does not contain real patient data, protected health information, or identifiable clinical records.

The output is operational decision support only. It is not clinical diagnosis, not treatment advice, and not a replacement for professional healthcare judgement. Every note requires human review before action.

## 4:35-5:00 Closing Pitch

This prototype shows how a reasoning agent can help pathway teams move from raw operational data to explainable action.

The future direction is to align the workflow with Microsoft AI Foundry for agent evaluation, Azure AI Agent Service for orchestration, and Microsoft 365 Copilot or Teams for escalation workflows.

The project is intentionally local-first today, but the architecture is ready for a responsible Microsoft cloud path later.

