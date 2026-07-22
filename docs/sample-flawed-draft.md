Case 205 (Cascade Orthopedic Associates): billing report totals don't reconcile.
Per the note, the cause is a rounding difference in the nightly aggregation job.
The rollup is maintained in the billing_ledger table and surfaced on the
dashboard. Recommend confirming the aggregation rounding.
