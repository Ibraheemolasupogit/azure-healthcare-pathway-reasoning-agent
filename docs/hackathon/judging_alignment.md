# Judging Alignment

## Project

Azure Healthcare Pathway Reasoning Agent

## Track

Reasoning Agents

## Accuracy & Relevance

The project focuses on a realistic healthcare operations problem: identifying pathway cases that may need coordination attention because of delays, missing diagnostics, admin blockers, capacity issues, stale contact, or unbooked treatment steps.

Accuracy is supported by:

- A fully synthetic dataset with explicit pathway fields.
- A validation layer that checks required columns and unique case IDs.
- Deterministic risk rules that are visible in code.
- Tests covering data loading, reasoning levels, recommended actions, and escalation note generation.

The current prototype is relevant to operational pathway coordination only. It does not claim clinical diagnosis, clinical prioritization, or treatment advice.

## Reasoning & Multi-Step Thinking

The reasoning workflow evaluates multiple structured signals for each case:

- Waiting time compared with target days.
- Recent contact history.
- Diagnostic status.
- Treatment booking status.
- Capacity issues.
- Administrative blockers.
- Urgent priority.
- Delayed appointment flags.
- Pathway type.

The agent combines these signals into an explainable risk score, assigns a risk level, lists the contributing risk factors, writes a plain-language reasoning summary, recommends next actions, and creates a structured escalation note.

This demonstrates multi-step reasoning while remaining transparent and inspectable.

## Creativity & Originality

The project applies reasoning-agent patterns to a practical healthcare operations scenario. Instead of generating generic chatbot responses, it turns pathway status data into operationally useful outputs:

- Risk assessment.
- Explanation.
- Recommended action.
- Suggested owner or team.
- Escalation note.
- Markdown export for review.

The concept is designed to be local-first today while mapping naturally to future Microsoft AI Foundry, Azure AI Agent Service, and Microsoft 365 Copilot workflows.

## User Experience & Presentation

The Streamlit demo is intentionally simple and judge-friendly:

- Select a synthetic case ID.
- Inspect the raw pathway details.
- Review the risk level and risk score.
- See the exact risk factors.
- Read the reasoning explanation.
- Review recommended next actions.
- Generate and download a structured escalation note.

The documentation includes a demo walkthrough, five-minute video script, submission summary, architecture diagrams, reasoning examples, and sample escalation notes.

## Reliability & Safety

The current prototype is deterministic and testable:

- No external AI API calls.
- No live Azure deployment.
- No real patient data.
- No Microsoft 365 Copilot integration implemented.
- No hidden model reasoning.
- Automated tests validate the core loader, reasoning engine, and escalation notes.

Responsible AI and safety boundaries are stated throughout the repository:

- Synthetic data only.
- No protected health information.
- Operational decision support only.
- Not clinical diagnosis.
- Not treatment advice.
- Human review required before action.
- Transparent rule-based reasoning.

## Community Vote / Demo Appeal

The demo is designed to be easy to understand in a short judging window. It shows a clear before-and-after transformation:

1. Start with a raw synthetic pathway case.
2. Apply transparent reasoning.
3. Surface operational risk.
4. Recommend next actions.
5. Produce a professional escalation note.

This creates a concrete story for viewers: the agent helps pathway teams move from fragmented operational data to explainable, review-ready action.

