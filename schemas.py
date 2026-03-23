# schemas.py

from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    branch: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    branch: str

    class Config:
        from_attributes = True