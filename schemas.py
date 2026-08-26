from pydantic import BaseModel, Field

class BusinessRequest(BaseModel):
    name: str
    industry: str
    problem: str
    location: str
    budget: int = Field(..., strict=True)
