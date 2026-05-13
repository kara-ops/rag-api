from sqlalchemy.orm import Session
from app.models.service import User
from fastapi import HTTPException
from app.security.auth import hash_password,verify_password
from app.security.jwt_handler import create_access_token,decode_access_token


def create_user(email:str, password:str,db:Session):
    email_db = db.query(User).filter(User.email==email).first()
    if email_db:
        raise HTTPException(status_code=400,detail="Email already registered")
    
    hash_pass = hash_password(password)
    user = User(
        email=email,
        hashed_password=hash_pass
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def user_login(email:str, password:str, db:Session):
    email_db = db.query(User).filter(User.email==email).first()
    if not email_db:
        raise HTTPException(status_code=401,detail="Wrong Credentials")
    check_pass = verify_password(password,email_db.hashed_password)
    if not check_pass:
        raise HTTPException(status_code=401,detail="Wrong Credentials")
    
    token = create_access_token({"sub":str(email_db.id)})
    return token
     