from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Data received from the user
class StudentInput(BaseModel):
    name: str
    age: int
    course: str


# Complete student stored by our API
class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str


students = []

next_id = 1


# ---------------- POST ----------------
# Add a new student
@app.post("/add_student")
def add_student(student: StudentInput):
    global next_id

    new_student = Student(
        id=next_id,
        name=student.name,
        age=student.age,
        course=student.course
    )

    students.append(new_student)

    next_id += 1

    return {
        "message": "Student added successfully",
        "student": new_student
    }


# ---------------- GET ALL ----------------
# Show all students
@app.get("/show_student")
def show_students():
    return students


# ---------------- GET ONE ----------------
# Find one student using ID
@app.get("/student/{id}")
def student_by_id(id: int):

    for student in students:
        if student.id == id:
            return student

    return {"message": "Student not found"}


# ---------------- PUT ----------------
# Update one student using ID
@app.put("/student/{id}")
def update_student(id: int, student: StudentInput):

    for existing_student in students:

        if existing_student.id == id:

            existing_student.name = student.name
            existing_student.age = student.age
            existing_student.course = student.course

            return {
                "message": "Student updated successfully",
                "student": existing_student
            }

    return {"message": "Student not found"}