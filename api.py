from fastapi import FastAPI

from schemas import BusinessRequest
from business_logic import classify_budget
from database import initialize_database
from database import (initialize_database,save_request,get_all_requests)

app = FastAPI()
initialize_database()

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

@app.get("/requests")
def get_requests():
    requests = get_all_requests()
    return {
        "status": "success",
        "count": len(requests),
        "requests": requests
    }

@app.post("/requests")
def create_request(request: BusinessRequest):

    category = classify_budget(request.budget)
    request_id = save_request(request, category)

    return {
        "status": "success",
        "request_id": request_id,
        "customer": request.name,
        "industry": request.industry,
        "problem": request.problem,
        "location": request.location,
        "budget": request.budget,
        "category": category
    }