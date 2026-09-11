from fastapi import FastAPI

app = FastAPI()

repos = {
    "subh": {
        "my_repo": {"description": "Test repo"}
    }
}

@app.post("/api/repos")
def check_repo_working():
    return {"status": "working"}

@app.get("/repos/{owner}/{repo}")
def repo_owner(owner: str, repo: str):
    if owner in repos:
        if repo in repos[owner]:
            return repos[owner][repo]
        else:
            return {"error": "Repo not found"}
    else:
        return {"error": "Owner not found"}


