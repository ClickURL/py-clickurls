import uvicorn
from fastapi import FastAPI
from models.model_user import User
from db.database import Database

app = FastAPI()

@app.get("/")
async def root():
    
    db = Database()
    result = db.get_user(3)
    result.delete_user()
    user = db.delete_user(result)
    return user
    
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)