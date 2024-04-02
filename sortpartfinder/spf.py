"""
Created on 03.01.2024

@author: neumann
"""
import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect("..\database\db.sqlite")
    cur = conn.cursor()

    cur.execute("SELECT * FROM ROOMS")

    for room in cur.fetchall():
        print(room)

    cur.close()
    conn.close()
