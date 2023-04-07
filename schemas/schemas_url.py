from uuid import UUID
from datetime import datetime
from pydantic import BaseModel

class UrlBase(BaseModel):
    original_url: str
    
    class Config:
        orm_mode = True
        
class UrlGet(UrlBase):
    id: int
    created_at: datetime
    short_url: str
    secret_access_token: UUID
    
class UrlPost(UrlBase):
    creator_id: int

class UrlUpdate(UrlGet):
    updated_at: datetime

class UrlDelete(UrlGet):
    deleted_at: datetime
    
class UrlEditPage(BaseModel):
    short_url: str
    secret_access_token: UUID
    # secret_access_token_full: str

    class Config:
        orm_mode = True
