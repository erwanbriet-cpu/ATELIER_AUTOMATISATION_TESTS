from flask import Flask, render_template_string, render_template, jsonify, request, redirect, url_for, session
from flask import render_template
from flask import json
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)

@app.get("/")
def consignes():
     return render_template('consignes.html')

if __name__ == "__main__":
    # utile en local uniquement
    app.run(host="0.0.0.0", port=5000, debug=True)

    from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

@app.route('/')
def dashboard():
    conn = sqlite3.connect('data/history.db')
    curr = conn.cursor()
    # Récupère les 10 derniers tests
    curr.execute("SELECT * FROM runs ORDER BY timestamp DESC LIMIT 10")
    data = curr.fetchall()
    
    # Calcul de la QoS (Disponibilité moyenne)
    curr.execute("SELECT AVG(is_success) * 100 FROM runs")
    availability = curr.fetchone()[0] or 0
    
    conn.close()

    # Template HTML ultra simple
    html = f"""
    <h1>API Monitoring Dashboard</h1>
    <p>Disponibilité globale : {availability:.2f}%</p>
    <table border="1">
        <tr><th>Date</th><th>Status</th><th>Latence (ms)</th><th>Succès</th></tr>
        {"".join([f"<tr><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]:.0f}</td><td>{row[4]}</td></tr>" for row in data])}
    </table>
    """
    return html
@app.route('/run-my-tests-secret-99')
def trigger_test():
    from app.monitor import run_test
    run_test()
    return "Test effectué et ajouté à SQLite !", 200
