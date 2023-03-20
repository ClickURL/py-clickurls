from pydantic import BaseModel

class UrlBase(BaseModel):
    original_url: str
    
    class Config:
        orm_mode = True