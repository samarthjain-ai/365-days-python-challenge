from fastapi import FastAPI

app = FastAPI()

@app.post("/api/repos")
def check_repo_working():
    print("workig")