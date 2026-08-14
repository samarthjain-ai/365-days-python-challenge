from fastapi import FastAPI
from pydantic import  BaseModel

app = FastAPI()

class Student(BaseModel):
    id:int
    name:str
    age:int
    course:str

students = []
@app.post("/student")
def data(student:Student):
    students.append(student)
    return "massage : data resived",student

@app.get("/student_all")
def student_ditails():
    return students

@app.get("/student/{id}")
def one_student(id):
    for student in students:
        if student.id == id :
            return student
    else:
        return "student not found"
        