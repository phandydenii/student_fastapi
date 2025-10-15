from http.client import HTTPException
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.group_schema import GroupRes, GroupReq
from schemas.semester_schema import SemesterRes
from services import group_service
from fastapi.encoders import jsonable_encoder

from util.response import success

router = APIRouter(prefix="/groups", tags=["Groups"])
@router.post("/", response_model=GroupRes)
def create(group: GroupReq, db: Session = Depends(get_db)):
    try:
        data = group_service.create(db, group)
        json = jsonable_encoder(data)
        return success(json)
    except Exception as e:
        db.rollback()
        raise HTTPException("Bade request!", 400)
    finally:
        db.commit()
        db.close()

@router.get("/", response_model=List[SemesterRes])
def get(db: Session = Depends(get_db)):
    try:
        data = group_service.gets(db)
        json = jsonable_encoder(data)
        return success(json)
    except Exception as e:
        db.rollback()
        raise HTTPException("Bade request!", 400)
    finally:
        db.commit()
        db.close()