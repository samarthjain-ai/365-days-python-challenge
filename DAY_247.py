from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1/health")
def api_health():
    return {"status" : "OK"}

@app.get("/api/v1/info")
def api_info():
    return {
    "name": "Git clone",
    "version": "1.0",
    "status": "running"
}

@app.get("/api/v1/version")
def api_version():
    return {"version" : "1.0"}

@app.get("/api/v1/")
def api_welcome():
    return {"message": "Welcome to Git Clone API"}

@app.get("/api/v1/status")
def api_status():
    return {   "service": "Git Clone API",
            "status": "running"}