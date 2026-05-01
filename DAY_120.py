from fastapi import  FastAPI
app = FastAPI()
import sqlite3

@app.put("/update/{student_id}")
def update_student(student_id:int,name:str,mark:int,subject:str):
    conn =sqlite3.connect("mark_table.db")
    cursor=conn.cursor()

    cursor.execute("UPDATE student_marks SET name=?,mark=?,subject=? WHERE rowid=?",(name,mark,subject,student_id,))

    return {"message":"update done"}

