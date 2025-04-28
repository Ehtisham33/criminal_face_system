# utils/db_utils.py

import sqlite3
import os

DB_PATH = "db/criminal_records.db"
os.makedirs("db", exist_ok=True)

def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS criminals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            father_name TEXT,
            age INTEGER,
            crime TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_criminal_record(name, father_name, age, crime):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO criminals (name, father_name, age, crime) VALUES (?, ?, ?, ?)",
                   (name, father_name, age, crime))
    criminal_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return criminal_id

def get_criminal_by_id(criminal_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM criminals WHERE id = ?", (criminal_id,))
    result = cursor.fetchone()
    conn.close()
    return result
