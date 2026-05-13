from app.schemas.user_schema import UserRegister,UserLogin,TokenResponse
from fastapi import APIRouter,Depends
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.services.user import create_user,user_login
from app.models.service import User



router = APIRouter(prefix="/auth")

@router.post("/sign_up")
def user_create(user:UserRegister,db:Session=Depends(get_db)):
    sign_up  = create_user(user.email,user.password,db)
    token = user_login(user.email,user.password,db)
    return {"access_token":token,"token_type":"bearer"}

@router.post("/sign_in")
def login(user:UserLogin,db:Session=Depends(get_db)):
    sign_in = user_login(user.email,user.password,db)
    return {"access_token":sign_in,"token_type":"bearer"}
