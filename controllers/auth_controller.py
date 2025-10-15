from datetime import timedelta
from http.client import HTTPException
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status
from db.database import get_db
from models.user import User
from schemas.user_schema import UserResponse, Token, UserReq
from security import auth
from services import auth_service
from util.response import success

router = APIRouter(prefix="/auths", tags=["User authentication"])
@router.post("/users/", response_model=UserResponse, status_code=201)
def create_user(user: UserReq, db: Session = Depends(get_db)):
    try:
        data = auth_service.create(db, user)
        json = jsonable_encoder(data)
        return success(json)
    except Exception as e:
        db.rollback()
        raise HTTPException(f"Bade request!. {e}", 400)
    finally:
        db.commit()
        db.close()

@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth_service.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            "Incorrect username or password",
            {"WWW-Authenticate": "Bearer"}
        )
    access_token = auth.create_access_token(data={"sub": user.username},
                                            expires_delta=timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": access_token, "token_type": "bearer"}


# @router.get("/users/me", response_model=UserResponse)
# async def read_users_me(current_user: User = Depends(get_current_active_user)):
#     return current_user
