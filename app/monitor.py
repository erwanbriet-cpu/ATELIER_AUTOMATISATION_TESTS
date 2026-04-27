import requests
import time
import sqlite3

def run_test():
    url = "https://dog.ceo/api/breeds/list/all"
    start = time.time()
    
    try:
        # Robustesse : timeout de 5 secondes
        r = requests.get(url, timeout=5)
        latency = (time.time() - start) * 1000
        
        # Validation du contrat (on attend un 200 et du JSON)
        is_success = 1 if (r.status_code == 200 and "message" in r.json()) else 0
        status = r.status_code
    except Exception:
        is_success = 0
        status = 500
        latency = 0

    # Sauvegarde en base
    conn = sqlite3.connect('data/history.db')
    conn.cursor().execute("INSERT INTO runs (status_code, latency_ms, is_success) VALUES (?, ?, ?)",
                          (status, latency, is_success))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    run_test()