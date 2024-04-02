"""
Created on 14.01.2024

@author: neumann
"""

from flask import Flask
import sqlite3
import os


DB_PATH = os.path.join(os.path.dirname(__file__), "..", "database", "db.sqlite")
LOCALHOST = "http://127.0.0.1:5000"

app = Flask(__name__)


@app.route("/")
def index():
    return f"""<h1>Sort Part Finder</h1>
               <a href='/rooms'>Räume</a>"""


@app.route("/rooms")
def getRooms():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT * FROM ROOMS")

    response = """<h1>Sort Part Finder</h1>
                  <ul>"""

    for room in cur.fetchall():
        response += f"""
        <li>
          Id {room[0]} Name
          <a href="../storages/{room[0]}">
            {room[1]}
          </a>
          <a href="../room/{room[0]}">Edit</a>
        </li>"""

    cur.close()
    conn.close()

    response += f"""</ul>
                    <br><br>
                    <a href='..'>Home</a>"""

    return response


@app.route("/room/<roomid>")
def getRoom(roomid):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM ROOMS WHERE ID={roomid}")

    response = "<h1>Sort Part Finder</h1>"

    room = cur.fetchall()[0]

    response += f"<p>Id {room[0]} Name {room[1]}</p>"

    cur.close()
    conn.close()

    response += f"<br><br> <a href='../rooms'>Räume</a>"

    return response


@app.route("/storages/<roomsid>")
def getStorages(roomsid):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM STORAGES WHERE roomsid={roomsid}")

    response = """<h1>Sort Part Finder</h1><ul>"""

    for storage in cur.fetchall():
        response += f"<li>Id {storage[0]} Name {storage[1]}</li>"

    cur.close()
    conn.close()

    response += f"""</ul>
                    <br><br>
                    <a href="../rooms">Räume
                    </a>"""

    return response
