from fastapi import FastAPI

from database import initialize_database
from app.api.v1.requests import router as requests_router
from app.config import ENVIRONMENT, DEBUG

app = FastAPI(
    title="SPIRA-X API",
    description="Business request management API",
    version="1.0.0",
    debug=DEBUG

)

@app.get("/about")
def about():
    return {
        "project": "SPIRA-X Project 001",
        "version": "1.0",
        "environment": ENVIRONMENT,
        "description": "Business Request Engine"
    }

initialize_database()

app.include_router(requests_router)



