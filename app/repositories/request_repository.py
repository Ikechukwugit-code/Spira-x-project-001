from schemas import BusinessRequest
from database import (
    save_request,
    get_all_requests,
    get_request_by_id,
    update_request,
    delete_request
)

def create(request: BusinessRequest, category: str):
    return save_request(request,category)

def get_all():
    return get_all_requests()

def get_by_id(request_id: int):
    return get_request_by_id(request_id)

def update(
        request_id: int,
        request: BusinessRequest,
        category: str
):
    return update_request(
        request_id,
        request,
        category
    )

def delete(request_id: int):
    return delete_request(request_id)