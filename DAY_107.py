# DAY -107 conncting API+Database

from fastapi import FastAPI
import sqlite3
app=FastAPI()

def get_db():
    conn = sqlite3.connect("notes.db")
    conn.row_factory = sqlite3.Row  # row_factory  - convert data to dic
    return conn

@app.get("/")
def home():
    return {"message":"API +DB working"}

@app.post("/add")
def add_note(note:str):
    conn =get_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO notes (text) VALUES (?)",
    (note,))
    conn.commit()

    conn.close()

    return{"message":"Note added"}


@app.get("/notes")
def get_notes():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM notes")
    data= cursor.fetchall()

    cursor.close
    return {"notes":[dict(row)for row in data]}

@app.get("/not/{id}")
def get_note(id:int):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM notes WHERE id=?",(id,))
    data = cursor.fetchone()

    conn.close()

    if data:
        return dict(data)
    return {"error":"Not found"}

@app.delete("/delete/{id}")
def delete_not(id:int):
    conn= get_db()
    cursor=conn.cursor()

    cursor.execute("DELETE FROM notes WHERE id=?",(id,))
    conn.commit()

    conn.close()
    return {"messsage":"Deleted"}


