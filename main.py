import uvicorn
from fastapi import FastAPI
from models.model_user import User
from db.database import Database
from crud.crud_user import UserCrud

app = FastAPI()

@app.get("/")
async def root():
    
    result = UserCrud().delete_user(7)
    
    return result
    
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)