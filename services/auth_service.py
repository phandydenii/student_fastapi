from fastapi import FastAPI, Depends, HTTPException, status
from jose import JWTError
from passlib.context import CryptContext
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

from schemas.user_schema import UserReq
from security import auth
from models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt_sha256"], deprecated="auto")


def create(db: Session,req: UserReq) -> User:
    try:
        hashed_password = pwd_context.hash(req.password)
        print(hashed_password)
        data = User(
            username=req.username,
            email=req.email,
            hashed_password=hashed_password[:70],
            full_name=req.full_name,
            disabled=req.disabled,
        )
        db.add(data)
        db.commit()
        db.refresh(data)
        return data
    except Exception as e:
        db.rollback()
        raise Exception(e)
    finally:
        db.close()

def get_user_by_username(db: Session, username: str):
    try:
        data = db.query(User).filter(User.username == username).one()
        return data
    except NoResultFound:
        raise HTTPException(status_code=404, detail="User not found")
    except MultipleResultsFound:
        raise HTTPException(status_code=400, detail="Multiple users found")
    except NoResultFound:
        raise HTTPException(status_code=404, detail="User not found")


def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)

    if not user:
        return False
    if not auth.verify_password(password, user.hashed_password):
        return False
    return user


async def get_current_user(db: Session, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = auth.jwt.decode(token, auth.SECRET_KEY, algorithms=[auth.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user_by_username(db, username=username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

