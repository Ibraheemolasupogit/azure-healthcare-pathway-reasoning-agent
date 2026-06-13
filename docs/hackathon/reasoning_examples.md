# Reasoning Examples

These examples use fully synthetic cases from `data/sample/simulated_pathway_cases.csv`. They demonstrate deterministic operational reasoning only; they do not provide clinical diagnosis or medical advice.

## Example 1: Low Risk

### Input Case Summary

- Case: `SIM-0026`
- Pathway type: Urgent care follow-up
- Days waiting: 3 of 7 target days
- Stage: Discharge advice review
- Diagnostics: Not required
- Treatment: Not required
- Clinical priority: Routine

### Risk Level

Low

### Reasoning

The pathway is early in its operational target window and there is no recorded delay, capacity issue, admin blocker, diagnostic dependency, treatment booking dependency, or stale contact history.

### Recommended Action

Continue routine pathway monitoring.

## Example 2: High Risk

### Input Case Summary

- Case: `SIM-0013`
- Pathway type: RTT elective
- Days waiting: 175 of 126 target days
- Stage: Surgical scheduling
- Diagnostics: Completed
- Treatment: Not yet booked
- Clinical priority: Routine

### Risk Level

High

### Reasoning

The case is significantly beyond the elective pathway target. Treatment is not yet booked, recent contact is overdue, and a capacity issue is recorded. These factors indicate operational delay and unclear route to the next pathway step.

### Recommended Action

Confirm ownership for the pathway breach, update contact records, identify treatment booking requirements, and escalate the capacity constraint for human review.

## Example 3: Critical Risk

### Input Case Summary

- Case: `SIM-0009`
- Pathway type: Cancer 62-day
- Days waiting: 75 of 62 target days
- Stage: Awaiting diagnostics
- Diagnostics: Delayed
- Treatment: Not yet booked
- Clinical priority: Urgent

### Risk Level

Critical

### Reasoning

The case is on a time-sensitive cancer pathway, is beyond its target, has delayed diagnostics, has no treatment booking, has a capacity issue, and is marked urgent. This combination creates a critical operational risk requiring immediate human review.

### Recommended Action

Escalate the case to the operational escalation list, follow up diagnostics, confirm the treatment booking owner, and raise the capacity issue with the relevant service manager.
