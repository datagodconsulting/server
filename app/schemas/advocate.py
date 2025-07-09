from pydantic import BaseModel
from typing import Optional

class AdvocateBase(BaseModel):
    user_id: int
    bar_council_id: Optional[str] = None
    specialization: Optional[str] = None
    years_of_experience: Optional[int] = None
    location: Optional[str] = None

class AdvocateCreate(AdvocateBase):
    pass

class AdvocateRead(AdvocateBase):
    advocate_id: int
    class Config:
        from_attributes = True 