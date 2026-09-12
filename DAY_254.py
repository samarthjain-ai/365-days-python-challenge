from fastapi import FastAPI
from pydantic import BaseModel

class RepositoryCreate(BaseModel):
    name: str
    description: str
    visibility: str

app = FastAPI()


@app.post("/repo")
def repo_create(repo: RepositoryCreate):
    return {"message": "Repository created", "data": repo}

@app.get("/repo/show")
def show(repo: RepositoryCreate):
    return repo
