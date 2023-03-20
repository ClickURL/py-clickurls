from datetime import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    
    class Config:
        orm_mode = True

class UserGet(UserBase):
    id: int
    created_at: datetime

class UserPost(UserBase):
    pass
        
class UserUpdate(UserGet):
    updated_at: datetime | None = None

class UserDelete(UserUpdate):
    deleted_at: datetime