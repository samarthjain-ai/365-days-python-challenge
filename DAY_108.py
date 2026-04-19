# clear and structure fome 
from fastapi import FastAPI
import sqlite3

app = FastAPI()


# Function to connect database
def get_db():
    conn = sqlite3.connect("notes.db")
    conn.row_factory = sqlite3.Row
    return conn


# Home route
@app.get("/")
def home():
    return {"message": "API + DB working"}


# Add note
@app.post("/add")
def add_note(note: str):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO notes (text) VALUES (?)", (note,))
    conn.commit()

    conn.close()
    return {"message": "Note added"}


# Get all notes
@app.get("/notes")
def get_notes():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM notes")
    data = cursor.fetchall()

    conn.close()
    return {"notes": [dict(row) for row in data]}


# Delete note
@app.delete("/delete/{id}")
def delete_note(id: int):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM notes WHERE id=?", (id,))
    conn.commit()

    conn.close()
    return {"message": "Note deleted"}