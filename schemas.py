from pydantic import BaseModel

class BusinessRequest(BaseModel):
    name: str
    industry: str
    problem: str
    location: str
    budget: int