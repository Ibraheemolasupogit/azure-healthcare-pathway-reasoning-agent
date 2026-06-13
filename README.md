# Azure Healthcare Pathway Reasoning Agent

A local-first Microsoft Agents League hackathon prototype for reasoning over simulated healthcare pathway data. The project explores how an AI-assisted agent could help healthcare teams identify operational risks, explain pathway reasoning, recommend next actions, and produce structured escalation notes.

This repository is intentionally starting with the foundation only: documentation, architecture notes, project structure, and initial dependencies. It does not include real patient data or a production clinical workflow.

## Healthcare Problem Statement

Healthcare teams often manage complex patient pathways across referrals, diagnostics, appointments, specialist reviews, discharge planning, and follow-up actions. Operational risks can emerge when pathway steps are delayed, incomplete, duplicated, or missing clear ownership.

This prototype focuses on simulated pathway records to explore how an agent could:

- Surface operational risk signals early.
- Explain why a pathway may require attention.
- Recommend practical next actions for care coordination teams.
- Generate structured escalation notes suitable for human review.

The goal is to support operational awareness, not to make clinical decisions.

## Target Users

- Healthcare operations teams monitoring pathway progress.
- Care coordination and scheduling teams.
- Service managers reviewing bottlenecks and escalation queues.
- Digital transformation teams evaluating AI-enabled workflow support.
- Hackathon judges reviewing Microsoft AI agent patterns in a healthcare-adjacent scenario.

## Hackathon Alignment

This project is designed for the Microsoft Agents League hackathon as a professional, portfolio-ready prototype that demonstrates:

- Agentic reasoning over structured, simulated healthcare operations data.
- Human-readable explanations of risk identification.
- Responsible AI positioning with clear data privacy boundaries.
- Alignment with Azure AI and Microsoft AI Foundry concepts.
- A practical pathway from local prototype to cloud-hosted agent workflow.

## Microsoft Technology Alignment

The planned implementation is aligned with Microsoft AI Foundry and Azure AI agent patterns:

- **Azure AI Foundry** for agent design, evaluation, deployment planning, and responsible AI workflows.
- **Azure OpenAI Service** for language reasoning, explanation generation, and escalation note drafting.
- **Azure AI Agent Service** as a target pattern for orchestrating reasoning, tool use, and structured outputs.
- **Azure Functions** as a possible lightweight execution layer for pathway analysis tasks.
- **Azure Storage or Azure SQL** as future options for simulated pathway datasets.
- **Application Insights** for future observability, tracing, and evaluation telemetry.
- **Microsoft Teams integration** as a future channel for escalation note delivery.

The initial repository remains local-first so the concept can be developed, reviewed, and demonstrated without cloud dependencies.

## Proposed Architecture

The intended architecture follows a simple local prototype flow:

1. Simulated pathway data is stored under `data/sample/`.
2. Data loading and validation utilities live in `src/data/`.
3. Agent orchestration and reasoning logic live in `src/agent/`.
4. Evaluation checks live in `src/evaluation/`.
5. Reporting and escalation note generation live in `src/reporting/`.
6. Documentation and hackathon materials live in `docs/`.
7. Evidence for demos, screenshots, and evaluation results lives in `evidence/`.

Future Azure deployment can map these local responsibilities to Azure AI Foundry agent assets, Azure-hosted storage, serverless execution, and monitored endpoints.

## Key Features

Planned prototype capabilities include:

- Load simulated healthcare pathway records.
- Detect operational risk indicators such as delays, missing next steps, unclear ownership, or approaching targets.
- Generate explainable reasoning for each flagged pathway.
- Recommend operational next actions.
- Produce structured escalation notes for healthcare teams.
- Evaluate outputs for consistency, safety, and usefulness.
- Keep all demonstrations based on simulated data only.

## Safety And Data Privacy

This project must use simulated data only. Do not add real patient data, protected health information, confidential operational data, or identifiable clinical records.

The prototype is intended for operational reasoning demonstrations and portfolio use. It is not a medical device, clinical decision support system, diagnostic tool, or replacement for professional healthcare judgement. Any future real-world adaptation would require governance, privacy review, clinical safety assessment, security controls, and human oversight.

## Synthetic Dataset

The sample dataset in `data/sample/simulated_pathway_cases.csv` is fully synthetic. It contains fictional operational pathway scenarios only and does not include real patient data, protected health information, or identifiable clinical records.

The dataset is intended to support operational decision support prototyping, such as identifying delayed appointments, missing diagnostics, capacity constraints, admin blockers, and pathways needing human review. The project does not provide clinical diagnosis, clinical prioritization, treatment advice, or medical decision-making.

## Reasoning Workflow

The first reasoning engine is deterministic and rule based. It reads one simulated pathway case, evaluates transparent operational risk factors, calculates an additive risk score, assigns a risk level, and returns a plain-language explanation with recommended next actions.

The current rules consider waiting time against target, recent contact history, diagnostic progress, treatment booking status, capacity constraints, administrative blockers, urgent priority, delayed appointments, and pathway type. No external AI APIs are called in this milestone.

## Escalation Notes

The escalation note generator turns one simulated pathway case and its reasoning output into a structured operational note. Each note includes a case summary, pathway type, risk level, risk score, key risk factors, reasoning summary, recommended next actions, suggested owner or team, urgency wording, and a human review reminder.

Escalation notes are designed to support pathway coordination workflows by making the reasoning output easier to review and act on. They remain deterministic, explainable, and local-first. They are operational decision support only, are not clinical diagnosis, and require human review before action.

## Planned Roadmap

- **Milestone 1:** Repository foundation, architecture notes, and hackathon brief.
- **Milestone 2:** Add simulated pathway dataset and schema documentation.
- **Milestone 3:** Implement local data loader and validation checks.
- **Milestone 4:** Build initial risk scoring and reasoning workflow.
- **Milestone 5:** Generate structured escalation notes.
- **Milestone 6:** Add evaluation examples and safety checks.
- **Milestone 7:** Create a demo workflow aligned with Microsoft AI Foundry patterns.
- **Milestone 8:** Prepare final hackathon evidence, screenshots, and presentation materials.
