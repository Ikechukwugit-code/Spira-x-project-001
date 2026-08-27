from app.repositories.request_repository import (
    create,
    get_all,
    get_by_id,
    update,
    delete
)

from schemas import BusinessRequest
from business_logic import classify_budget

def create_business_request(request: BusinessRequest):
    category = classify_budget(request.budget)
    request_id = create(
        request,
        category
    )
    return {
        "id": request_id,
        "name": request.name,
        "industry": request.industry,
        "problem": request.problem,
        "loacation": request.location,
        "budget": request.budget,
        "category": category
    }

def list_business_requests():
    return get_all()

def get_business_request(request_id: int):
    return get_by_id(request_id)

def update_business_request(request_id: int, request: BusinessRequest):
    category = classify_budget(request.budget)
    updated = update(
        request_id,
        request,
        category
    )

    if updated == 0:
        return None
    return get_by_id(request_id)

def delete_business_request(request_id: int):
    return delete(request_id)