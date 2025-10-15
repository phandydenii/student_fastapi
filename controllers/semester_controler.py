from http.client import HTTPException
from typing import List
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.semester_schema import SemesterRes,SemesterReq
from services import semester_service as services
from util.response import success

router = APIRouter(prefix="/semesters", tags=["Semesters"])
@router.post("/", response_model=SemesterRes)
def create(semester: SemesterReq, db: Session = Depends(get_db)):
    try:
        data = services.create(db, semester)
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