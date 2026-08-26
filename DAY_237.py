from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# ==================================================
# 1. INPUT MODEL
# ==================================================

class Student(BaseModel):
    name: str
    age: int
    course: str


# ==================================================
# 2. STUDENT MODEL WITH ID
# ==================================================

class Student_id(BaseModel):
    id: int
    name: str
    age: int
    course: str


# ==================================================
# 3. PATCH / UPDATE MODEL
# ==================================================

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    course: Optional[str] = None


# ==================================================
# 4. DATABASE (TEMPORARY LIST)
# ==================================================

students = []

next_id = 1


# ==================================================
# 5. POST → ADD STUDENT
# ==================================================

@app.post("/add_student")
def add_student(student: Student):

    global next_id

    new_student = Student_id(
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


# ==================================================
# 6. GET → SHOW ALL STUDENTS
# ==================================================

@app.get("/show_all_student")
def show_all_students():

    return students


# ==================================================
# 7. GET → SHOW ONE STUDENT
# ==================================================

@app.get("/student/{id}")
def student_by_id(id: int):

    for student in students:

        if student.id == id:
            return student

    return {
        "message": "Student not found"
    }


# ==================================================
# 8. PUT → UPDATE COMPLETE STUDENT
# ==================================================

@app.put("/student/{id}")
def update_student(id: int, student: Student):

    for old_student in students:

        if old_student.id == id:

            old_student.name = student.name
            old_student.age = student.age
            old_student.course = student.course

            return {
                "message": "Student updated successfully",
                "student": old_student
            }

    return {
        "message": "Student not found"
    }


# ==================================================
# 9. DELETE → DELETE STUDENT
# ==================================================

@app.delete("/student/{id}")
def delete_student(id: int):

    for old_student in students:

        if old_student.id == id:

            students.remove(old_student)

            return {
                "message": "Student deleted successfully",
                "student": old_student
            }

    return {
        "message": "Student not found"
    }


# ==================================================
# 10. PATCH → PARTIALLY UPDATE STUDENT
# ==================================================

@app.patch("/student/{id}")
def patch_student(id: int, student: StudentUpdate):

    for old_student in students:

        if old_student.id == id:

            # Update name only if provided
            if student.name is not None:
                old_student.name = student.name

            # Update age only if provided
            if student.age is not None:
                old_student.age = student.age

            # Update course only if provided
            if student.course is not None:
                old_student.course = student.course

            return {
                "message": "Student partially updated successfully",
                "student": old_student
            }

    return {
        "message": "Student not found"
    }