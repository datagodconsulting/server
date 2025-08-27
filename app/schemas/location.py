from pydantic import BaseModel

class LocationResponse(BaseModel):
    city: str
    state: str
    pincode: str

    class Config:
        orm_mode = True