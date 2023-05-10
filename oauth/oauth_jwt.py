import os
import jwt

from fastapi import HTTPException, status, Depends, Security
from fastapi.security.api_key import APIKeyCookie  #OAuth2PasswordBearer,
from fastapi.openapi.models import APIKey
from datetime import timedelta, datetime

from oauth.ouath_crud import OAuthCrud

from dotenv import load_dotenv

load_dotenv('.env.secret')

def cast_to_numbers(id):
    temp = os.getenv(id)
    if temp is not None:
        try:
            return float(temp)
        except ValueError:
            return None
    return None

API_SECRET_KEY = os.getenv('API_SECRET_KEY') or None
API_REFRESH_KEY = os.getenv('API_REFRESH_KEY') or None
if API_SECRET_KEY is None or API_REFRESH_KEY is None:
    raise BaseException('Missing API_SECRET_KEY or API_REFRESH_KEY env var.')
API_ALGORITM = os.getenv('API_ALGORITM') or 'HS256'
API_KEY_NAME = os.getenv('API_KEY_NAME') or "access_token"
API_ACCESS_TOKEN_EXTIRE_MINUTES = cast_to_numbers('API_ACCESS_TOKEN_EXTIRE_MINUTES') or 60
API_REFRESH_TOKEN_EXTIRE_MINUTES = cast_to_numbers('API_REFRESH_TOKEN_EXTIRE_MINUTES') or 60 * 24 * 7

CREDENTIALS_EXCEPRIONS = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Could not validate credentials',
    headers={'WWW-Authenticate': 'Bearer'}
)

SIGNATURE_EXPIRED_EXCEPRIONS = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Signature has expired',
    headers={'WWW-Authenticate': 'Bearer'}
)

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl='')
api_key_cookie = APIKeyCookie(name=API_KEY_NAME, auto_error=False)

def create_access_token(data: dict, expire_delta: timedelta = None, secret_jwt = API_SECRET_KEY):
    to_encode = data.copy()
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encode_jwt = jwt.encode(to_encode, secret_jwt, algorithm=API_ALGORITM)
    return encode_jwt

def create_token(user_id):
    access_token_expires = timedelta(minutes=API_ACCESS_TOKEN_EXTIRE_MINUTES)
    access_token = create_access_token(data={'sub': user_id}, expire_delta=access_token_expires, secret_jwt=API_SECRET_KEY)
    return access_token

def create_refresh_token(user_id):
    refresh_token_expires = timedelta(minutes=API_REFRESH_TOKEN_EXTIRE_MINUTES)
    refresh_token = create_access_token(data={'sub': user_id}, expire_delta=refresh_token_expires, secret_jwt=API_REFRESH_KEY)
    return refresh_token

def validation_user_from_db(user_id):
    result = OAuthCrud().get_social_profile(user_id)
    if not result:
        return False
    return True

async def get_current_user(token: APIKey = Security(api_key_cookie)):
    try:
        payload = decode_token(token)
        user_id: str = payload.get('sub')
        if user_id is None:
            raise CREDENTIALS_EXCEPRIONS
    except jwt.PyJWKError:
        raise CREDENTIALS_EXCEPRIONS
    
    if not validation_user_from_db(user_id):
        raise CREDENTIALS_EXCEPRIONS
    
    return user_id
   
def decode_token(token):
    try:
        result = jwt.decode(token, API_SECRET_KEY, algorithms=[API_ALGORITM])
        return result
    except jwt.ExpiredSignatureError:
        raise SIGNATURE_EXPIRED_EXCEPRIONS
    
    
# Зробити механізм онволення токену