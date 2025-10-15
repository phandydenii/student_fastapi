from http.client import HTTPException
from typing import List
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.student_group_schema import StudentGroupReq, StudentGroupRes
from services import studentgroup_service as services
from util.response import success

router = APIRouter(prefix="/student-groups", tags=["Student Groups"])
@router.post("/", response_model=StudentGroupRes)
def create(req: StudentGroupReq, db: Session = Depends(get_db)):
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

@router.get("/", response_model=List[StudentGroupRes])
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