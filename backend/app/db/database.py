import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent.parent / "assistant.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS logs (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 kind TEXT,
                 input_text TEXT,
                 output_text TEXT,
                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                 )""")
    conn.commit()
    conn.close()

def log(kind, input_text, output_text):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO logs (kind, input_text, output_text) VALUES (?, ?, ?)",
              (kind, input_text, output_text))
    conn.commit()
    conn.close()

# initialize on import
init_db()
