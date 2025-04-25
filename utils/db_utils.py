import sqlite3

def init_db(db_path='db/criminal_records.db'):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS criminals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        father_name TEXT,
        age INTEGER,
        crime TEXT
    )''')
    conn.commit()
    conn.close()

def add_criminal_record(name, father_name, age, crime, db_path='db/criminal_records.db'):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("INSERT INTO criminals (name, father_name, age, crime) VALUES (?, ?, ?, ?)",
              (name, father_name, age, crime))
    conn.commit()
    criminal_id = c.lastrowid
    conn.close()
    return criminal_id

def get_criminal_by_id(criminal_id, db_path='db/criminal_records.db'):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM criminals WHERE id = ?", (criminal_id,))
    row = c.fetchone()
    conn.close()
    return row
