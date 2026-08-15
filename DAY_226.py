from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class StudentInput(BaseModel):
    name: str
    age: int
    course: str

class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str

students = []

next_id = 1


@app.post("/add_student")
def add_student(student: StudentInput):
    global next_id

    new_student = Student(
        id=next_id,
        name=student.name,
        age=student.age,
        course=student.course)

    students.append(new_student)

    next_id += 1

    return {
        "message": "Student added successfully",
        "student": new_student}


@app.get("/show_student")
def show_students():
    return students


@app.get("/student/{id}")
def student_by_id(id: int):
    for student in students:
        if student.id == id:
            return student

    return {"message": "Student not found"}