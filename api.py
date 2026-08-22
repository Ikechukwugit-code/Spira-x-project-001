from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "SPIRA-X API is running!",
        "status": "success"

    } 

@app.get("/about")
def about():
    return {
        "project": "SPIRA-X Project 001",
        "version": "0.1",
        "description": "Business Request Engine"
    }