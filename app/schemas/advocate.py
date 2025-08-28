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
    location: LocationCreate   # ✅ nested location object when creating

class AdvocateRead(AdvocateBase):
    advocate_id: int
    location: LocationOut      # ✅ nested location object when reading
    class Config:
        from_attributes = True
