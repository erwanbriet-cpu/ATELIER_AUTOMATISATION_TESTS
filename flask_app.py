from flask import Flask, render_template
import storage
from tester.runner import execute_full_run
import sqlite3

app = Flask(__name__)

@app.route('/')
def dashboard():
    runs = storage.list_runs()
    # Calcul QoS rapide pour le bonus
    conn = sqlite3.connect('/home/ErwanBRT/data/history.db')
    availability = conn.execute("SELECT AVG(is_success) * 100 FROM runs").fetchone()[0] or 0
    conn.close()
    return render_template('dashboard.html', runs=runs, availability=availability)

@app.route('/run')
def trigger():
    execute_full_run()
    return "OK", 200

# Route Bonus : Healthcheck
@app.route('/health')
def health():
    return {"status": "up"}, 200