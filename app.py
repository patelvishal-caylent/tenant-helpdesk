"""Workshop Demo — a small fictional multi-tenant support/ops app.

Built as a workshop lab repo: entirely synthetic data, no external services,
no credentials required. Run with `python app.py` after `python seed.py`.
"""
import os
import sqlite3

from flask import Flask, g, jsonify, render_template

DB_PATH = os.path.join(os.path.dirname(__file__), "workshop_demo.sqlite3")

app = Flask(__name__)


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


@app.route("/")
def dashboard():
    db = get_db()
    tenants = db.execute(
        """SELECT t.*, s.open_case_count, s.order_count
           FROM tenants t LEFT JOIN tenant_stats s ON s.tenant_id = t.tenant_id
           ORDER BY t.tenant_id"""
    ).fetchall()
    return render_template("dashboard.html", tenants=tenants)


@app.route("/tenants/<int:tenant_id>")
def tenant_detail(tenant_id):
    db = get_db()
    tenant = db.execute("SELECT * FROM tenants WHERE tenant_id = ?", (tenant_id,)).fetchone()
    orders = db.execute("SELECT * FROM orders WHERE tenant_id = ? ORDER BY order_id", (tenant_id,)).fetchall()
    cases = db.execute("SELECT * FROM cases WHERE tenant_id = ? ORDER BY case_id", (tenant_id,)).fetchall()
    contacts = db.execute("SELECT * FROM contacts WHERE tenant_id = ?", (tenant_id,)).fetchall()
    return render_template("tenant_detail.html", tenant=tenant, orders=orders, cases=cases, contacts=contacts)


@app.route("/cases")
def case_list():
    db = get_db()
    cases = db.execute(
        """SELECT c.*, t.name AS tenant_name, ct.name AS contact_name
           FROM cases c
           JOIN tenants t ON t.tenant_id = c.tenant_id
           LEFT JOIN contacts ct ON ct.contact_id = c.contact_id
           ORDER BY CASE c.priority WHEN 'escalated' THEN 0 WHEN 'high' THEN 1 WHEN 'normal' THEN 2 ELSE 3 END,
                    c.created_at DESC"""
    ).fetchall()
    return render_template("case_list.html", cases=cases)


@app.route("/cases/<int:case_id>")
def case_detail(case_id):
    db = get_db()
    case = db.execute(
        """SELECT c.*, t.name AS tenant_name, ct.name AS contact_name, ct.email AS contact_email
           FROM cases c
           JOIN tenants t ON t.tenant_id = c.tenant_id
           LEFT JOIN contacts ct ON ct.contact_id = c.contact_id
           WHERE c.case_id = ?""",
        (case_id,),
    ).fetchone()
    notes = db.execute("SELECT * FROM case_notes WHERE case_id = ? ORDER BY created_at", (case_id,)).fetchall()
    return render_template("case_detail.html", case=case, notes=notes)


# --- JSON API, for skills/scripts to query against ---

@app.route("/api/tenants")
def api_tenants():
    db = get_db()
    rows = db.execute("SELECT * FROM tenants").fetchall()
    return jsonify([dict(r) for r in rows])


@app.route("/api/tenants/<int:tenant_id>/orders")
def api_tenant_orders(tenant_id):
    db = get_db()
    rows = db.execute("SELECT * FROM orders WHERE tenant_id = ?", (tenant_id,)).fetchall()
    return jsonify([dict(r) for r in rows])


@app.route("/api/cases")
def api_cases():
    db = get_db()
    rows = db.execute("SELECT * FROM cases").fetchall()
    return jsonify([dict(r) for r in rows])


@app.route("/api/cases/<int:case_id>")
def api_case_detail(case_id):
    db = get_db()
    case = db.execute("SELECT * FROM cases WHERE case_id = ?", (case_id,)).fetchone()
    if case is None:
        return jsonify({"error": "not found"}), 404
    notes = db.execute("SELECT * FROM case_notes WHERE case_id = ?", (case_id,)).fetchall()
    result = dict(case)
    result["notes"] = [dict(n) for n in notes]
    return jsonify(result)


if __name__ == "__main__":
    if not os.path.exists(DB_PATH):
        print("No database found — run `python seed.py` first.")
    app.run(debug=True, port=5050)
