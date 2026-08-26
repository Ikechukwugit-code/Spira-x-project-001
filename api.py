from fastapi import FastAPI

from database import initialize_database
from app.api.v1.requests import router as requests_router

app = FastAPI(
    title="SPIRA-X API",
    description="Business request management API",
    version="1.0.0"

)

initialize_database()

app.include_router(requests_router)



