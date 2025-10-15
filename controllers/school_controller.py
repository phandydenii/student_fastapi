from http.client import HTTPException
from typing import List

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.school_schema import SchoolReq, SchoolRes
from services import school_service
from util.response import success

router = APIRouter(prefix="/grades", tags=["Grades"])
@router.post("/", response_model=SchoolRes)
def create(school: SchoolReq, db: Session = Depends(get_db)):
    try:
        data = school_service.create_school(db, school)
        json = jsonable_encoder(data)
        return success(json)
    except Exception as e:
        db.rollback()
        raise HTTPException("Bade request!", 400)
    finally:
        db.commit()
        db.close()

@router.get("/", response_model=List[SchoolRes])
def get(db: Session = Depends(get_db)):
    try:
        data = school_service.get_schools(db)
        json = jsonable_encoder(data)
        return success(json)
    except Exception as e:
        db.rollback()
        raise HTTPException("Bade request!", 400)
    finally:
        db.commit()
        db.close()