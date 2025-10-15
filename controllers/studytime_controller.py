from http.client import HTTPException
from typing import List
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.semester_schema import SemesterRes
from schemas.study_time_schema import StudyTimeReq, StudyTimeRes
from services import studytime_service as services
from util.response import success

router = APIRouter(prefix="/study-times", tags=["Study Times"])
@router.post("/", response_model=StudyTimeRes, status_code=201)
def create(req: StudyTimeReq, db: Session = Depends(get_db)):
    try:
        data = services.create(db, req)
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
        data = services.gets(db)
        json = jsonable_encoder(data)
        return success(json)
    except Exception as e:
        db.rollback()
        raise HTTPException("Bade request!", 400)
    finally:
        db.commit()
        db.close()