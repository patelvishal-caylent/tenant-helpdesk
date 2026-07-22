# Requirement — escalated-case review summary

Produce a short review summary for an escalated support case, suitable for handing
to the account owner. The summary MUST:

1. Name only tables that exist in the system (see schema.sql). No invented tables.
2. Preserve and clearly flag the case's priority. Escalated cases must be marked ESCALATED.
3. Ground every claim in the case notes and the schema. No unsupported root causes.
4. Screen for PHI: no raw contact emails or personal identifiers beyond what the summary needs.
5. Not be written to outbound/ until it has been reviewed AND a human has approved it.
