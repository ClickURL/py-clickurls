import uvicorn
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from models.model_user import User
from models.model_url import Url
from schemas import schemas_user, schemas_url
from crud.crud_user import UserCrud
from crud.crud_url import UrlCrud
from crud.crud_view import ViewCrud

hostname = settings.localhost
port = settings.port

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return "Hello World!"


@app.get("/test/")
def test():
    hostname = ViewCrud().get_all_views()
    return {"views": hostname}

# User side router, to interact with the entity User (for testing)
# ________________________________________________________________

@app.get("/users_test", response_model=list[schemas_user.UserGet])
def get_all_users():
    try:
        result = UserCrud().get_all_users()
        return result
    except HTTPException as e:
        raise e.detail("Get All Users ERROR")
    
@app.get("/users_test/{id}", response_model=schemas_user.UserGet)
def get_user_by_id(id: int):
    try:
        result = UserCrud().get_user(id)
        return result
    except HTTPException as e:
        raise e.detail("Get User ERROR")

@app.post("/users_test", response_model=schemas_user.UserPost)
def create_user(user_post):
    try:
        result = UserCrud().create_user(user_post)
        return result
    except HTTPException as e:
        raise e.detail("POST User ERROR")
    
@app.put("/users_test", response_model=schemas_user.UserUpdate)
def update_user_by_id(id: int, new_user_name):
    try:
        result = UserCrud().update_user(id, new_user_name)
        return result
    except HTTPException as e:
        raise e.detail("Update User ERROR")
    
@app.delete("/users_test/{id}", response_model=schemas_user.UserDelete)
def delete_user_by_id(id: int):
    try:
        result = UserCrud().delete_user(id)
        return result
    except HTTPException as e:
        raise e.detail("Delete User ERROR")


# URL side router, to interact with the entity URL (for testing)
# ________________________________________________________________

@app.get("/urls_test", response_model=list[schemas_url.UrlGet])
def get_all_urls():
    try:
        result = UrlCrud().get_all_urls()
        return result
    except HTTPException as e:
        raise e.detail("Get All URLs ERROR")
    
@app.get("/urls_test/url_id{id}", response_model=schemas_url.UrlGet)
def get_url_by_id(id: int):
    try:
        result = UrlCrud().get_url_by_id(id)
        return result
    except HTTPException as e:
        raise e.detail("Get URL ERROR")
    
@app.get("/urls_test/creator{creator_id}", response_model=list[schemas_url.UrlGet])
def get_urls_by_creator(creator_id: int):
    try:
        result = UrlCrud().get_urls_by_creator(creator_id)
        return result
    except HTTPException as e:
        raise e.detail("Get URL ERROR")
    
@app.post("/urls_test", response_model=schemas_url.UrlPost)
def create_url(original_url: str, creator_id: int):
    try:
        result = UrlCrud().create_url(original_url, creator_id)
        return result
    except HTTPException as e:
        raise e.detail("POST URL ERROR")
    
@app.put("/urls_test/{id}", response_model=schemas_url.UrlUpdate)
def update_url_by_id(id: int, new_url: str):
    try:
        result = UrlCrud().update_url(id, new_url)
        return result
    except HTTPException as e:
        raise e.detail("PUT URL ERROR")
    
@app.delete("/urls_test/{id}", response_model=schemas_url.UrlDelete)
def delete_url_by_id(id: int):
    try:
        result = UrlCrud().delete_url(id)
        return result
    except HTTPException as e:
        raise e.detail("Delete URL ERROR")


# URL redirect side router
# ________________________________________________________________

@app.get("/2{short_url}/")
def redirect_to_long_url(short_url: str):
    try:
        result = UrlCrud().get_url_by_column("short_url", short_url)
        redirect_url = result.original_url
        if redirect_url:
            ViewCrud().create_view(result.id)
        return RedirectResponse(redirect_url)
    except HTTPException as e:
        raise e.detail("Redirect to original URL ERROR")

@app.get("/edit/{secret_access_token}", response_model=schemas_url.UrlEditPage)
def edit_url(secret_access_token: str):
    try:
        result = UrlCrud().get_url_by_column("secret_access_token", secret_access_token)
        return result
    except HTTPException as e:
        raise e.detail("EDIT URL ERROR")

@app.get("/api/v1/{secret_access_token}/stats.json")
def get_stats(secret_access_token: str):
    try:
        result = ViewCrud().get_stats_group_by_time(secret_access_token)
        return {"views_stats": result}
    except HTTPException as e:
        raise e.detail("GET stats URL ERROR")

@app.post("/main/")
def create_url(original_url: str, creator_id: int):
    try:
        result = UrlCrud().create_url(original_url, creator_id)
        redirect_url = f"/edit/{result.secret_access_token}"
        return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
    except HTTPException as e:
        raise e.detail("POST URL ERROR")

if __name__ == "__main__":
    uvicorn.run("main:app", host=hostname, port=port, reload=True)
