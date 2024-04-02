"""
Created on 03.01.2024

@author: neumann
"""

import os
import sqlite3

if __name__ == "__main__":
    db_path = os.path.join(os.path.dirname(__file__), "..", "database", "db.sqlite")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("SELECT * FROM ROOMS")

    for room in cur.fetchall():
        print(room)

    cur.close()
    conn.close()
