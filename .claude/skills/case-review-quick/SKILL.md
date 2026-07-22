---
name: case-review-quick
description: Fast one-paragraph summary of a single support case. Use when the user asks for a quick case review, a case summary, or a short read on a case by number.
model: haiku
allowed-tools: Bash(curl *)
---

Give a quick review of the support case whose id the user names in their request (e.g. "case 205" → id 205).

1. Fetch it: `curl -s http://localhost:5050/api/cases/<id>`, substituting the case id you identified.
2. In one short paragraph, state the tenant_id, the subject, the priority, and whether it is escalated (say so first if it is).
3. Do not invent tables, tenants, or notes that are not in the fetched JSON. All data is synthetic; never add PHI.
