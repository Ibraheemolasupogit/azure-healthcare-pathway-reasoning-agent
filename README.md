# Azure Healthcare Pathway Reasoning Agent

A local-first Microsoft Agents League hackathon prototype for reasoning over simulated healthcare pathway data. The project explores how an AI-assisted agent could help healthcare teams identify operational risks, explain pathway reasoning, recommend next actions, and produce structured escalation notes.

This repository contains a demo-ready local prototype with a synthetic dataset, deterministic reasoning engine, escalation note generator, Streamlit interface, sample outputs, and hackathon documentation. It does not include real patient data or a production clinical workflow.

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
- Intended future alignment with Azure AI and Microsoft AI Foundry concepts.
- A practical pathway from local prototype to cloud-hosted agent workflow.

## Microsoft Technology Alignment

The current prototype is local-first. It is designed for future alignment with Microsoft AI Foundry and Azure AI agent patterns:

- **Microsoft AI Foundry** as a future environment for agent design, evaluation, tracing, and responsible AI workflows.
- **Azure OpenAI Service** as a possible future language reasoning layer, if appropriate.
- **Azure AI Agent Service** as a future target pattern for orchestrating reasoning, tool use, and structured outputs.
- **Azure Functions** as a possible future lightweight execution layer for pathway analysis tasks.
- **Azure Storage or Azure SQL** as future options for simulated or governed pathway datasets.
- **Application Insights** for future observability, tracing, and evaluation telemetry.
- **Microsoft Teams or Microsoft 365 Copilot extension** as optional future channels for escalation workflows.

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

Future Azure deployment could map these local responsibilities to Microsoft AI Foundry agent assets, Azure-hosted storage, serverless execution, and monitored endpoints. No Azure deployment is included in the current prototype.

## Key Features

Planned prototype capabilities include:

- Load simulated healthcare pathway records.
- Detect operational risk indicators such as delays, missing next steps, unclear ownership, or approaching targets.
- Generate explainable reasoning for each flagged pathway.
- Recommend operational next actions.
- Produce structured escalation notes for healthcare teams.
- Evaluate outputs for consistency, safety, and usefulness.
- Keep all demonstrations based on simulated data only.

## Responsible AI And Safety

This project must use simulated data only. Do not add real patient data, protected health information, confidential operational data, or identifiable clinical records.

The prototype is intended for operational decision support demonstrations and portfolio use. It is not a medical device, diagnostic tool, treatment recommendation system, or replacement for professional healthcare judgement.

Current safety boundaries:

- Synthetic data only.
- No real patient data.
- No protected health information.
- No clinical diagnosis.
- Operational decision support only.
- Human review required before action.
- Transparent deterministic reasoning.
- No external AI API calls in the current prototype.

Any future real-world adaptation would require governance, privacy review, clinical safety assessment, security controls, model evaluation, and human oversight.

## Synthetic Dataset

The sample dataset in `data/sample/simulated_pathway_cases.csv` is fully synthetic. It contains fictional operational pathway scenarios only and does not include real patient data, protected health information, or identifiable clinical records.

The dataset is intended to support operational decision support prototyping, such as identifying delayed appointments, missing diagnostics, capacity constraints, admin blockers, and pathways needing human review. The project does not provide clinical diagnosis, clinical prioritization, treatment advice, or medical decision-making.

## Reasoning Workflow

The first reasoning engine is deterministic and rule based. It reads one simulated pathway case, evaluates transparent operational risk factors, calculates an additive risk score, assigns a risk level, and returns a plain-language explanation with recommended next actions.

The current rules consider waiting time against target, recent contact history, diagnostic progress, treatment booking status, capacity constraints, administrative blockers, urgent priority, delayed appointments, and pathway type. No external AI APIs are called in the current prototype.

## Escalation Notes

The escalation note generator turns one simulated pathway case and its reasoning output into a structured operational note. Each note includes a case summary, pathway type, risk level, risk score, key risk factors, reasoning summary, recommended next actions, suggested owner or team, urgency wording, and a human review reminder.

Escalation notes are designed to support pathway coordination workflows by making the reasoning output easier to review and act on. They remain deterministic, explainable, and local-first. They are operational decision support only, are not clinical diagnosis, and require human review before action.

## Streamlit Demo App

The local Streamlit app lets users select a synthetic pathway case, review the case details, run the deterministic reasoning engine, inspect risk factors and recommended actions, and generate a structured escalation note. The note can be downloaded as Markdown for demo evidence or review.

The app does not call external AI APIs and does not deploy any Azure resources.

## Hackathon Documentation

- [Agent architecture](docs/architecture/agent_architecture.md)
- [High-level architecture](docs/architecture/high_level_architecture.md)
- [Submission summary](docs/hackathon/submission_summary.md)
- [Judging alignment](docs/hackathon/judging_alignment.md)
- [Demo walkthrough](docs/hackathon/demo_walkthrough.md)
- [Demo script](docs/hackathon/demo_script.md)
- [Reasoning examples](docs/hackathon/reasoning_examples.md)
- [Evidence README](evidence/README.md)
- [Sample escalation note: SIM-0017](evidence/sample_outputs/escalation_note_SIM-0017.md)
- [Sample escalation note: SIM-0009](evidence/sample_outputs/escalation_note_SIM-0009.md)
- [Sample escalation note: SIM-0027](evidence/sample_outputs/escalation_note_SIM-0027.md)

## Local Development

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Run tests:

```bash
python3 -m pytest
```

Run lint checks:

```bash
python3 -m ruff check .
```

Run the Streamlit app:

```bash
streamlit run app.py
```

## Planned Roadmap

- **Completed:** Repository foundation, synthetic dataset, data loader, validation tests, deterministic reasoning engine, escalation notes, Streamlit demo, sample outputs, and hackathon submission documentation.
- **Next:** Add screenshots and a short demo video.
- **Future:** Add Azure AI Foundry evaluation assets.
- **Future:** Add richer synthetic scenario coverage.
- **Future:** Add optional Microsoft Teams or Microsoft 365 Copilot extension workflow.
- **Future:** Add Azure deployment path after local prototype validation.
