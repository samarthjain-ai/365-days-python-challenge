from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}

@app.get("/about")
def about():
    return{
        "Name : ":"Samarth jain",
        "Age  : ": "18",
        "Course :": "B.Tech AI",
        "DAY :" : "222"}

@app.get("/skills")
def skills():
    return {
        "skills": [
            "Python",
            "Machine Learning",
            "Generative AI",
            "FastAPI"
        ]
    }