from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DocumentBase(BaseModel):
    case_id: int
    uploaded_by_id: int
    file_url: str
    document_type: str

class DocumentCreate(DocumentBase):
    pass

class DocumentRead(DocumentBase):
    document_id: int
    uploaded_at: datetime
    class Config:
        from_attributes = True 