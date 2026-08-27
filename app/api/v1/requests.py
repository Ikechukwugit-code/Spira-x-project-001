from fastapi import APIRouter,status, HTTPException
from schemas import BusinessRequest
from app.repositories.request_repository import update_request, get_by_id
from business_logic import classify_budget
from database import (
    save_request,
    get_all_requests,
    get_request_by_id,
    update_request,
    delete_request
)

router = APIRouter(
    prefix="/api/v1/requests",
    tags=["Requests"]
)

@router.post("",status_code=status.HTTP_201_CREATED)
def create_request(request: BusinessRequest):
    category = classify_budget(request.budget)
    request_id = save_request(
        request,
        category
    )
    return {
        "status": "success",
        "request_id": request_id,
        "customer": request.name,
        "industry": request.industry,
        "problem": request.problem,
        "location":request.location,
        "budget": request.budget,
        "category": category
    }

@router.get("")
def get_request():

    requests = get_all_requests()
    return {
        "status": "success",
        "count": len(requests),
        "requests": requests
    }

@router.get("/requests/{request_id}")
def get_request(request_id: int):

    request = get_request_by_id(request_id)
    if request is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Request not found"
        )
    return {
        "status": "success",
        "request": request
    }

@router.put("/{request_id}")
def update_business_request(
    request_id: int,
    request: BusinessRequest
):

    category = classify_budget(request.budget)
    updated_count = update_request(
        request_id,
        request,
        category
    )

    if updated_count ==0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "Request not found"
        )

    updated_request= get_request_by_id(
        request_id
    )

    return {
        "status": "success",
        "message": "Request updated successfully",
        "request": update_request

    }

@router.delete("/{request_id}")
def delete_business_request(
    request_id: int
):
    deleted = delete_request(request_id)
    if deleted == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Request not found"
        )

    return {
        "status": "success",
        "message": "Request deleted successfully",
        "request_id": request_id
    }

