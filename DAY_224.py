from fastapi import FastAPI
from pydantic import  BaseModel

app = FastAPI()

class Student(BaseModel):
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