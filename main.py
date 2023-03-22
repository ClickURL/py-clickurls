import uvicorn
from fastapi import FastAPI, HTTPException
from typing import Union
from crud.crud_user import UserCrud
from crud.crud_url import UrlCrud
from db.database import Database

from schemas import schemas_user, schemas_url

from models.model_user import User
from models.model_url import Url

app = FastAPI()

@app.get("/")
def test():
    try:
        result = UrlCrud().get_url_by_column("short_url", "second_shrt_code")
        return result
    except Exception as e:
        raise e.detail("Get User with URLs ERROR")


# User side router
# ________________________________________________________________

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


# URL side router
# ________________________________________________________________

@app.get("/urls", response_model=list[schemas_url.UrlGet])
def get_all_urls():
    try:
        result = UrlCrud().get_all_urls()
        return result
    except HTTPException as e:
        raise e.detail("Get All URLs ERROR")
    
@app.get("/urls/url_id{id}", response_model=schemas_url.UrlGet)
def get_url_by_id(id: int):
    try:
        result = UrlCrud().get_url_by_id(id)
        return result
    except HTTPException as e:
        raise e.detail("Get URL ERROR")
    
@app.get("/urls/creator{creator_id}", response_model=list[schemas_url.UrlGet])
def get_url_by_creator(creator_id: int):
    try:
        result = UrlCrud().get_url_by_creator(creator_id)
        return result
    except HTTPException as e:
        raise e.detail("Get URL ERROR")
    
@app.post("/urls", response_model=schemas_url.UrlPost)
def create_url(original_url: str, creator_id: int):
    try:
        result = UrlCrud().create_url(original_url, creator_id)
        return result
    except HTTPException as e:
        raise e.detail("POST URL ERROR")
    
@app.put("/urls/{id}", response_model=schemas_url.UrlUpdate)
def update_url_by_id(id: int, new_url: str):
    try:
        result = UrlCrud().update_url(id, new_url)
        return result
    except HTTPException as e:
        raise e.detail("PUT URL ERROR")
    
@app.delete("/urls/{id}", response_model=schemas_url.UrlDelete)
def delete_url_by_id(id: int):
    try:
        result = UrlCrud().delete_url(id)
        return result
    except HTTPException as e:
        raise e.detail("Delete URL ERROR")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)