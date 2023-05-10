import os
import jwt

from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
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
if API_SECRET_KEY is None:
    raise BaseException('Missing API_SECRET_KEY env var.')
API_ALGORITM = os.getenv('API_ALGORITM') or 'HS256'
API_ACCESS_TOKEN_EXTIRE_MINUTES = cast_to_numbers('API_ACCESS_TOKEN_EXTIRE_MINUTES') or 15
REFRESH_TOKEN_EXTIRE_MINUTES = 60 * 24 * 30

CREDENTIALS_EXCEPRIONS = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Could not validate credentials',
    headers={'WWW-Authenticate': 'Bearer'}
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='')

def create_access_token(data: dict, expire_delta: timedelta = None):
    to_encode = data.copy()
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encode_jwt = jwt.encode(to_encode, API_SECRET_KEY, algorithm=API_ALGORITM)
    return encode_jwt

def create_token(user_id):
    access_token_expires = timedelta(minutes=API_ACCESS_TOKEN_EXTIRE_MINUTES)
    access_token = create_access_token(data={'sub': user_id}, expire_delta=access_token_expires)
    return access_token

def validation_user_from_db(user_id):
    result = OAuthCrud.get_social_profile(user_id)
    if not result:
        return False
    return True

async def get_current_user(token: str = Depends(oauth2_scheme)):
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
    
async def get_current_user_token(token: str = Depends(oauth2_scheme)):
    current_token = get_current_user(token)
    return current_token
   
def decode_token(token):
    return jwt.decode(token, API_SECRET_KEY, algorithms=[API_ALGORITM])