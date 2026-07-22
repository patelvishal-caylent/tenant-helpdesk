---
description: Review a support case and produce a grounded, priority-preserving summary.
model: claude-sonnet-5
---
Read the case from GET /api/cases/$0 (the app runs on http://localhost:5050).
Ground every claim in schema.sql and CLAUDE.md. Preserve the case's priority —
if it is escalated, say ESCALATED. Name only tables that exist in schema.sql.
Output a short summary: what the issue is, the root cause per the notes, the
priority, and the status.
