from pydantic import BaseModel
from typing import Optional

class ClientBase(BaseModel):
    user_id: int
    address: Optional[str] = None

class ClientCreate(ClientBase):
    pass

class ClientRead(ClientBase):
    client_id: int
    class Config:
        from_attributes = True 