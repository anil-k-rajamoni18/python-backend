from pydantic import BaseModel
from typing import Dict, Any

class UserCreate(BaseModel):
    id: int
    data: Dict[str, Any]

class UserResponse(BaseModel):
    id: int
    data: Dict[str, Any]

    class Config:
        from_attributes = True
