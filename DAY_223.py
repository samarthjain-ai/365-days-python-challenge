from fastapi import FastAPI

app = FastAPI()

from pydantic import BaseModel

class Student(BaseModel):
    name:str
    age:int
    course:str


@app.post("/students")
def data(student:Student):
    
    return("student data have resived",student)


