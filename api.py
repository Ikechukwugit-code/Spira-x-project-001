from fastapi import FastAPI

from schemas import BusinessRequest
from business_logic import classify_budget

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

@app.post("/requests")
def create_request(request: BusinessRequest):

    category = classify_budget(request.budget)

    return {
        "status": "success",
        "customer": request.name,
        "industry": request.industry,
        "problem": request.problem,
        "location": request.location,
        "budget": request.budget,
        "category": category
    }