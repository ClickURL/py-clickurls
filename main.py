import uvicorn
from fastapi import FastAPI
from crud.crud_user import UserCrud
from db.database import Database
from datetime import datetime

app = FastAPI()

@app.get("/")
async def root():
    
    result = Database().create_user("Borus")
    
    return result
    
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)