import uvicorn
from fastapi import FastAPI, HTTPException
from typing import Union
from crud.crud_user import UserCrud
from crud.crud_url import UrlCrud
from db.database import Database

from schemas import schemas_user, schemas_url, schemas_user_url

from models.model_user import User
from models.model_url import Url

app = FastAPI()

@app.get("/")
def test():
    try:
        result = Database().get_urls_by_user(3)
        return result
    except Exception as e:
        raise e.detail("Get User with URLs ERROR")

@app.get("/ted", response_model=schemas_user_url.UserUrlBase)
def root():
    try:
    
        result = Database().get_urls_by_user(1)
        user_return = {"name": result[1], "id": result[0], "created_at": result[2], "original_url": result[6]}
        return user_return
    except Exception as e:
        raise e.detail("Get User with URLs ERROR")

@app.get("/users", response_model=list[schemas_user.UserGet])
def get_all_users():
    try:
        result = UserCrud().get_all_users()
        return result
    except HTTPException as e:
        raise e.detail("Get All Users ERROR")
    
@app.get("/users/{id}", response_model=schemas_user.UserGet)
def get_user_by_id(id: int):
    try:
        result = UserCrud().get_user(id)
        return result
    except HTTPException as e:
        raise e.detail("Get User ERROR")

@app.post("/users", response_model=schemas_user.UserPost)
def create_user(user_post):
    try:
        result = UserCrud().create_user(user_post)
        return result
    except HTTPException as e:
        raise e.detail("POST User ERROR")
    
@app.put("/users", response_model=schemas_user.UserUpdate)
def update_user_by_id(id: int, new_user_name):
    try:
        result = UserCrud().update_user(id, new_user_name)
        return result
    except HTTPException as e:
        raise e.detail("Update User ERROR")
    
@app.delete("/users/{id}", response_model=schemas_user.UserDelete)
def delete_user_by_id(id: int):
    try:
        result = UserCrud().delete_user(id)
        return result
    except HTTPException as e:
        raise e.detail("Delete User ERROR")
    
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)