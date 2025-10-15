from http.client import HTTPException
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.degree import DegreeRes, DegreeReq
from services import degree_service
from util.response import success
from fastapi.encoders import jsonable_encoder
router = APIRouter(prefix="/degrees", tags=["Degrees"])
@router.post("/", response_model=DegreeRes)
def create(degree: DegreeReq, db: Session = Depends(get_db)):
    try:
        db_book = degree_service.create_degree(db, degree)
        json = jsonable_encoder(db_book)
        return success(json)
    except Exception as e:
        db.rollback()
        raise HTTPException("Bade request!", 400)
    finally:
        db.commit()
        db.close()
@router.get("/", response_model=List[DegreeRes])
def get(db: Session = Depends(get_db)):
    try:
        degrees = degree_service.get_degrees(db)
        json = jsonable_encoder(degrees)
        return success(json)
    except Exception as e:
        db.rollback()
        raise HTTPException("Bade request!", 400)
    finally:
        db.commit()
        db.close()