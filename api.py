from fastapi import FastAPI

from schemas import BusinessRequest
from business_logic import classify_budget
from database import initialize_database
from database import (initialize_database,save_request,get_all_requests,get_request_by_id,update_request,delete_request)

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

@app.get("/requests/{request_id}")
def get_request(request_id: int):

    request = get_request_by_id(request_id)
    if request is None:
        return {
            "status": "error",
            "message": "Request not found"
        }
    return {
        "status": "success",
        "request": request
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

@app.put("/requests/{request_id}")
def update_business_request(request_id: int, request: BusinessRequest):
    print("=== UPDATE STARTED ===")
    print("request_id:", request_id)
    print("request data:", request)

    # check if the request exists

    existing = get_request_by_id(request_id)
    if not existing:
        return {
            "status": "error",
            "message": "Request not found"
        }
    # classify the budget

    category = classify_budget(request.budget)
    # update the database ( call the update function)
    updated = update_request(request_id, request, category)

    if updated == 0:
        return {
            "status": "error",
            "message": "Request not found"
        }

    # get the updated data and return it

    updated_request = get_request_by_id(request_id)
    return {
        "status": "success",
        "message": "Request updated successfully",
        "requests": updated_request
    }

@app.delete("/requests/{request_id}")
def delete_business_request(request_id: int):
    deleted = delete_request(request_id)
    if deleted == 0:
        return {
            "status": "error",
            "message": "Request not found"
        }
    return {
        "status": "success",
        "message": "Request deleted successfully",
        "request_id": request_id
    }