import uvicorn
from fastapi import FastAPI
from crud.crud_user import UserCrud
from crud.crud_url import UrlCrud
from db.database import Database


app = FastAPI()

@app.get("/")
async def root():
    
    result = UrlCrud().delete_url(9)
    
    return result
    
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)