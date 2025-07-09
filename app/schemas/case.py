from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CaseBase(BaseModel):
    client_id: int
    advocate_id: Optional[int] = None
    case_type: str
    case_status: Optional[str] = 'Open'
    case_description: str

class CaseCreate(CaseBase):
    pass

class CaseRead(CaseBase):
    case_id: int
    created_at: datetime
    updated_at: Optional[datetime]
    class Config:
        from_attributes = True 