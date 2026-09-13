from fastapi import FastAPI
from pydantic import BaseModel, field_validator
from enum import Enum

from DAY_248 import validate_repository_name


class Visibility(Enum):
    private = "private"
    public = "public"


class RepositoryCreate(BaseModel):
    name: str
    description: str
    visibility: Visibility

    @field_validator("name")
    @classmethod
    def check_name(cls, value):
        return validate_repository_name(value)


app = FastAPI()


@app.post("/repo")
def repo_create(repo: RepositoryCreate):
    return {
        "message": "Repository created",
        "data": repo
    }