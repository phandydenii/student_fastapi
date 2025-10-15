from http.client import HTTPException
from io import BytesIO
from typing import List
from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.score_schema import ScoreReq, ScoreRes
from services import score_service as services
from util.response import success
import pandas as pd
router = APIRouter(prefix="/scores", tags=["Scores"])
@router.post("/", response_model=ScoreReq, status_code=201)
def create(req: ScoreReq, db: Session = Depends(get_db)):
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

@router.get("/", response_model=List[ScoreRes])
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

@router.post("/import-csv/")
async def upload_csv_pandas(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(BytesIO(contents))
    # Convert DataFrame to a list of dicts
    data = df.to_dict(orient="records")
    json = jsonable_encoder(data)
    return success(json)