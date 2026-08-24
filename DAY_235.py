from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name :str
    age :int
    course : str 

class Student_id(BaseModel):
    name:str
    age:int
    course : str
    id:int

students =[]
next_id=1

@app.post("/add_student")
def add_student(student:Student):
    global next_id

    new_student=Student_id(
        id=next_id,
        name=student.name,
        age =student.age,
        course=student.course
        )
    students.append(new_student)
    next_id+=1

    return {
        "Message " : "Succesfuly added the new student ",
        "Student " : new_student
        }

@app.get("/show_all_student")
def show_all_students():
    return students

@app.get("/student/{id}")
def student_bt_id(id:int):
    for student in students:
        if student.id==id:
            return student
    else:
        return "Student not found"

@app.delete("/student/{id}")
def delete_student(id:int):

    for old_student in students:
        if old_student.id ==id:
            students.remove(old_student)
            return {
                "message": "Student delete successfully",
                "student": old_student
            }

    return {"message": "Student not found"}
