"""Populate workshop_demo.sqlite3 with synthetic seed data. Safe to re-run: drops and rebuilds."""
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "workshop_demo.sqlite3")
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")

TENANTS = [
    (1, "Northwind Health Partners", "large", "cluster_type_a"),
    (2, "Blue Ridge Family Care", "medium", "cluster_type_b"),
    (3, "Sunrise Pediatrics Group", "small", "cluster_type_b"),
    (4, "Cascade Orthopedic Associates", "large", "cluster_type_a"),
    (5, "Harbor View Clinic", "small", "cluster_type_c"),
    (6, "Prairie Wind Medical", "medium", "cluster_type_b"),
]

CONTACTS = [
    (1, 1, "Dana Whitfield", "Practice Manager", "d.whitfield@example-tenant.test", 1),
    (2, 2, "Marcus Ellery", "Office Administrator", "m.ellery@example-tenant.test", 1),
    (3, 3, "Priya Nandakumar", "Owner", "p.nandakumar@example-tenant.test", 1),
    (4, 4, "Owen Castellano", "IT Liaison", "o.castellano@example-tenant.test", 1),
    (5, 5, "Renee Aubuchon", "Office Manager", "r.aubuchon@example-tenant.test", 1),
    (6, 6, "Tobias Kirchner", "Practice Manager", "t.kirchner@example-tenant.test", 1),
]

ORDERS = [
    (101, 1, "fulfilled", 458000), (102, 1, "open", 12000), (103, 1, "fulfilled", 87500),
    (104, 2, "fulfilled", 34200), (105, 2, "cancelled", 9900),
    (106, 3, "open", 4500),
    (107, 4, "fulfilled", 612000), (108, 4, "fulfilled", 233000), (109, 4, "open", 18000),
    (110, 5, "fulfilled", 7200),
    (111, 6, "open", 45600), (112, 6, "fulfilled", 91000),
]

CASES = [
    (201, 1, 1, "Two-step login redirect confusing new staff", "resolved", "low"),
    (202, 1, 1, "Appointment slot API returning stale data intermittently", "open", "high"),
    (203, 2, 2, "ODBC connector timing out on bulk export", "awaiting_reply", "normal"),
    (204, 3, 3, "Question about HL7 field mapping for demographics", "open", "normal"),
    (205, 4, 4, "Escalation: billing report totals don't reconcile", "open", "escalated"),
    (206, 5, 5, "How do I reset a locked-out user account", "resolved", "low"),
    (207, 6, 6, "Integration questions re: appointment API auth flow", "open", "normal"),
]

CASE_NOTES = [
    (301, 202, "support-agent-1", "Confirmed intermittent; correlates with cache eviction window. Escalating to platform."),
    (302, 203, "support-agent-2", "Asked tenant for a sample export size to reproduce. Awaiting reply."),
    (303, 205, "support-agent-1", "Numbers point to a rounding difference in the nightly aggregation job, not the report itself."),
]


def main():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    with open(SCHEMA_PATH) as f:
        conn.executescript(f.read())

    conn.executemany("INSERT INTO tenants VALUES (?, ?, ?, ?, datetime('now'))", TENANTS)
    conn.executemany("INSERT INTO contacts VALUES (?, ?, ?, ?, ?, ?)", CONTACTS)
    conn.executemany("INSERT INTO orders VALUES (?, ?, ?, ?, datetime('now'))", ORDERS)
    conn.executemany("INSERT INTO cases VALUES (?, ?, ?, ?, ?, ?, datetime('now'))", CASES)
    conn.executemany("INSERT INTO case_notes VALUES (?, ?, ?, ?, datetime('now'))", CASE_NOTES)

    for (tenant_id,) in conn.execute("SELECT tenant_id FROM tenants").fetchall():
        open_cases = conn.execute(
            "SELECT COUNT(*) FROM cases WHERE tenant_id = ? AND status != 'resolved'", (tenant_id,)
        ).fetchone()[0]
        order_count = conn.execute(
            "SELECT COUNT(*) FROM orders WHERE tenant_id = ?", (tenant_id,)
        ).fetchone()[0]
        conn.execute(
            "INSERT INTO tenant_stats (tenant_id, open_case_count, order_count) VALUES (?, ?, ?)",
            (tenant_id, open_cases, order_count),
        )

    conn.commit()
    conn.close()
    print(f"Seeded {DB_PATH} with {len(TENANTS)} tenants, {len(CASES)} cases, {len(ORDERS)} orders.")


if __name__ == "__main__":
    main()
