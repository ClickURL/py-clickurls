import uvicorn
import logging
from typing import Annotated, Optional
from fastapi import FastAPI, HTTPException, Request, Response, Cookie, status, Depends
from fastapi.responses import RedirectResponse, HTMLResponse, FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder

from fastapi.openapi.models import APIKey


from config import settings
from schemas import schemas_user, schemas_url
from crud.crud_user import UserCrud
from crud.crud_url import UrlCrud
from crud.crud_view import ViewCrud

from oauth.auth import auth_app
from oauth.oauth_jwt import get_current_user

hostname = settings.localhost
port = settings.port

app = FastAPI()


app.mount('/auth', auth_app)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"detail": (exc.errors())[0]["msg"]})
    )

logger = logging.getLogger(__name__)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/py-clickurl", StaticFiles(directory="./frontend/", html = True), name="static")
templates = Jinja2Templates(directory = "./frontend/public")

@app.exception_handler(404)
async def http_exception_handler(request: Request, exc: HTTPException):
    return RedirectResponse("/error/404")

@app.get("/error/404")
def not_found(request: Request):
    return templates.TemplateResponse("not_found.html", {"request": request})

@app.get("/favicon.ico")
def favicon():
    return FileResponse("favicon.ico")

@app.get("/")
def main(request: Request):
    return templates.TemplateResponse("create_url.html", {"request": request})

@app.get("/hello_world")
def root(user_id: APIKey = Depends(get_current_user)):
    try:
        if user_id is None:
            message = "User not logined"
        message = f'user id {user_id}'
        return {"message": message}
    except HTTPException as e:
        raise e.detail("JWT token ERROR")
    

@app.get("/api/edit/{secret_access_token}", response_model=schemas_url.UrlEditPage)
def edit_url(secret_access_token: str):
    try:
        result = UrlCrud().get_url_by_token(secret_access_token)
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

@app.post("/api/create_url", response_model=schemas_url.UrlEditPage)
def create_url(input: schemas_url.UrlPost):
    try:
        result = UrlCrud().create_url(input.original_url, input.creator_id)
        return result
    except HTTPException as e:
        logger.error("POST ERROR")
        raise e

@app.get("/edit/{secret_access_token}", response_class=HTMLResponse)
def edit(secret_access_token: str, request: Request):
    return templates.TemplateResponse("edit_url.html", {"request": request}, headers={'secret_access_token': secret_access_token})

@app.get("/{short_url}")
def redirect_to_long_url(short_url: str):
    try:
        result = UrlCrud().get_url_by_short(short_url)
        redirect_url = result.original_url
        ViewCrud().create_view(result.id)
        return RedirectResponse(redirect_url)
    except HTTPException as e:
        logger.error("Redirect to original URL ERROR")
        raise e

# User side router, to interact with the entity User (for testing)
# ________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________

@app.get("/users_test/test", response_model=list[schemas_user.UserGet])
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
def create_user():
    try:
        result = UserCrud().create_user()
        return result
    except HTTPException as e:
        raise e.detail("POST User ERROR")
    
@app.put("/users_test", response_model=schemas_user.UserUpdate)
def update_user_by_id(id: int):
    try:
        result = UserCrud().update_user(id)
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

@app.get("/urls_test/test", response_model=list[schemas_url.UrlGet])
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
def delete_url_by_id(id: int, secret_access_token: str):
    try:
        result = UrlCrud().delete_url(id, secret_access_token)
        return result
    except HTTPException as e:
        raise e.detail("Delete URL ERROR")

if __name__ == "__main__":
    uvicorn.run("main:app", host=hostname, port=port, reload=True)
