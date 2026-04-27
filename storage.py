import sqlite3
import os

DB_PATH = '/home/ErwanBRT/data/history.db'

def save_run(status_code, latency, success, metrics_json):
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT INTO runs (status_code, latency_ms, is_success, metrics) VALUES (?, ?, ?, ?)", 
                 (status_code, latency, success, metrics_json))
    conn.commit()
    conn.close()

def list_runs():
    if not os.path.exists(DB_PATH): return []
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute("SELECT * FROM runs ORDER BY timestamp DESC LIMIT 20").fetchall()
    conn.close()
    return rows