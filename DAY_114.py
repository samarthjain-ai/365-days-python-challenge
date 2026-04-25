from fastapi import FastAPI,Path
app = FastAPI()

students={
    1:{
        "name":"subh",
        "age":18, 
    }
}

@app.get("/")
def index():
    return { "Name": "First API"}

@app.get("/get-student/{student_id}")
def get_student(student_id:int=Path(...,description ="The id of the student",gt=0,it=3)):
    return students[student_id]




