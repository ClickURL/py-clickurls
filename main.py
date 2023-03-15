import uvicorn
from fastapi import FastAPI
import db.dbinit as db

app = FastAPI()

@app.get("/")
async def root():
    return ("py-clicks Hello World")
    
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)