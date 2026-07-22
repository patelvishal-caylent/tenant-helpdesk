---
name: case-review-detailed
description: Thorough, cited review of a single support case including escalation status, every note, and tenant context. Use when the user asks for a detailed, full, or complete case review.
model: sonnet
allowed-tools: Bash(curl *)
---

Produce a detailed review of the support case whose id the user names in their request (e.g. "case 205" → id 205).

1. Fetch it: `curl -s http://localhost:5050/api/cases/<id>`, substituting the case id you identified.
2. Report, each on its own line: tenant_id, priority (flag it if 'escalated'), status, subject.
3. Summarize every note in the notes array, attributing each to its author.
4. Cite the case_id and note_id for each claim. Do not state anything not present in the fetched JSON.
5. All data is synthetic; never introduce real patient or client PHI into the review.
