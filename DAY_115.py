import sqlite3
from  fastapi import FastAPI

conn = sqlite3.connect("student.db")
cursor=conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS students (
               id INTEGER PRIMARY KEY,
               name TEXT,
               age INTEGER 
           
           )
            """)


app = FastAPI()

@app.get("/")
def get_start():
    return {"message":"Student API working"}


@app.post("/add")
def add_student(name:str,age:int):
    conn = sqlite3.connect("student.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO students (name,age) VALUES (?,?)",(name,age))

    conn.commit()
    conn.close()

    return {"message":"Student added"}

@app.get("/students")
def show_details():
    conn = sqlite3.connect("student.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM students ")
    students =cursor.fetchall()

    return {"Students details  ":students}