from datetime import datetime
from pydantic import BaseModel

class UrlBase(BaseModel):
    original_url: str
    
    class Config:
        orm_mode = True
        
class UrlGet(UrlBase):
    id: int
    created_at: datetime
    
class UrlPost(UrlBase):
    pass

class UrlUpdate(UrlGet):
    updated_at: datetime

class UrlDelete(UrlUpdate):
    deleted_at: datetime