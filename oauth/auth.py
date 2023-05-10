import os
import requests
import json

from urllib.parse import urlencode

from fastapi import FastAPI, Request, Response
from fastapi.responses import RedirectResponse, JSONResponse

from starlette.middleware.sessions import SessionMiddleware

from oauth.ouath_crud import OAuthCrud
import oauth.oauth_jwt as oauth_jwt

from dotenv import load_dotenv
load_dotenv('.env.secret')

auth_app = FastAPI()

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID') or None
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET') or None
REDIRECT_URL = os.getenv('REDIRECT_URL') or None
SECRET_KEY = os.getenv('SECRET_KEY') or None
API_KEY_NAME = os.getenv('API_KEY_NAME') or "access_token"
API_REFRESH_NAME = os.getenv('API_REFRESH_NAME') or "refresh_token"

OAuthServerEndpoint = 'https://accounts.google.com/o/oauth2/v2/auth?'
TokenServerEndpoint = 'https://oauth2.googleapis.com/token'
RequestURI = 'https://www.googleapis.com/oauth2/v2/userinfo'

scopes = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    'openid'
]

auth_app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

@auth_app.route('/login')
async def login(requset: Request):
    scopes_str = ' '.join(scopes)
    query_params = {
        'client_id': GOOGLE_CLIENT_ID,
        'redirect_uri': REDIRECT_URL,
        'response_type': 'code',
        'scope': scopes_str
    }
    auth_uri = OAuthServerEndpoint + urlencode(query_params)
    print(GOOGLE_CLIENT_ID)
    return RedirectResponse(auth_uri)

@auth_app.route('/logout')
async def logout(request: Request):
    response = RedirectResponse("/")
    response.delete_cookie(key=API_KEY_NAME)
    # request.cookies.clear() or could be better used 
    return response

@auth_app.route('/code')
async def call_back_google(request: Request):
    auth_user_code = request.query_params['code']
    auth_params = {
        'client_id': GOOGLE_CLIENT_ID,
        'client_secret': GOOGLE_CLIENT_SECRET,
        'code': auth_user_code,
        'grant_type': 'authorization_code',
        'redirect_uri': REDIRECT_URL
    }
    token_result = requests.post(TokenServerEndpoint, data=auth_params)
    credentials = json.loads(token_result.text)
    headers = {'Authorization': 'Bearer {}'.format(credentials['access_token'])}
    user_info = requests.get(RequestURI, headers=headers)
    
    user_profile = OAuthCrud().set_social_profile(user_info=json.loads(user_info.text))
    jwt_user_token = oauth_jwt.create_token(user_profile.user_id)
    jwt_refresh_token = oauth_jwt.create_refresh_token(user_profile.user_id)
    response = RedirectResponse("/")
    response.set_cookie(key=API_KEY_NAME, value=jwt_user_token)
    response.set_cookie(key=API_REFRESH_NAME, value=jwt_refresh_token)
    return response;

