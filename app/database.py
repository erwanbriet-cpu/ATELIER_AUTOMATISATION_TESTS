import sqlite3

def init_db():
    conn = sqlite3.connect('data/history.db')
    c = conn.cursor()
    # On stocke : date, code HTTP, latence et succès (0 ou 1)
    c.execute('''CREATE TABLE IF NOT EXISTS runs 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, 
                  status_code INTEGER, 
                  latency_ms REAL, 
                  is_success INTEGER)''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()