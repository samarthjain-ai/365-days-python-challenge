from fastapi import  FastAPI
app = FastAPI()
import sqlite3



@app.get("/student/{student_id}")
def find_student(student_id :int):
    conn=sqlite3.connect("mark_table.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student_marks WHERE rowid=(?)",(student_id,))
    student = cursor.fetchone()

    if student:
        return {"student":student}
    else:
        return {"message":"student not found"}
    
@app.get("/students")
def show_students():
    conn=sqlite3.connect("mark_table.db")
    cursor = conn.cursor()

    cursor.execute("SELECT rowid, * FROM student_marks")
    students =cursor.fetchall()

    return students

@app.post("/add")
def add_student(name:str,mark:int,subject:str):

    conn=sqlite3.connect("mark_table.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO student_marks VALUES(?,?,?)",(name,mark,subject))
    conn.commit()
    conn.close()
    return {"message":"student_added"}

@app.delete("/delete/{student_id}")
def delete_student(student_id):

    conn=sqlite3.connect("mark_table.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM student_marks WHERE rowid=(?) ",student_id)
    return {"message":"deleted"}