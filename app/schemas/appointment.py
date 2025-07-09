from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AppointmentBase(BaseModel):
    client_id: int
    advocate_id: int
    appointment_datetime: datetime
    meeting_link: Optional[str] = None
    status: Optional[str] = 'Scheduled'
    notes: Optional[str] = None

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentRead(AppointmentBase):
    appointment_id: int
    class Config:
        from_attributes = True 