from pydantic import BaseModel
from typing import Optional


# ---- Location schema ----
class LocationBase(BaseModel):
    city: str
    state: str
    pincode: str

class LocationCreate(LocationBase):
    pass

class LocationOut(LocationBase):
    location_id: int

    class Config:
        from_attributes = True


# ---- Advocate schema ----
class AdvocateBase(BaseModel):
    user_id: int
    bar_council_id: Optional[str] = None
    specialization: Optional[str] = None
    years_of_experience: Optional[int] = None


class AdvocateCreate(AdvocateBase):
    location_id: int   # ✅ link advocate to location (FK)


class AdvocateRead(AdvocateBase):
    advocate_id: int
    location_id: int   # ✅ include location_id for lookups

    class Config:
        from_attributes = True


class AdvocateOut(BaseModel):
    advocate_id: int
    user_id: int
    bar_council_id: Optional[str] = None
    specialization: Optional[str] = None
    years_of_experience: Optional[int] = None
    location: Optional[LocationOut]   # ✅ nested location object

    class Config:
        from_attributes = True