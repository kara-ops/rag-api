from jose import jwt, JWTError
from datetime import datetime, timedelta
from app.core.config import settings
from fastapi import HTTPException


def create_access_token(data:dict)->str:
    to_encode = data.copy()
    expiry = datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expiry})
    return jwt.encode(to_encode,settings.SECRET_KEY,algorithm=settings.ALGORITHM)

def decode_access_token(token:str)->dict:
    try:
        payload = jwt.decode(token,settings.SECRET_KEY,algorithm=settings.ALGORITHM)
    except JWTError:
        return None
    return payload

