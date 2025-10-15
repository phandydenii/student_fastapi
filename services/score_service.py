from io import BytesIO

from fastapi import UploadFile, File
from sqlalchemy.orm import Session
from models.score import Score
from schemas.score_schema import ScoreReq
import pandas as pd
def create(db: Session, req: ScoreReq):
    try:
        data = Score(
            student_group_id=req.student_group_id,
            subject_id=req.subject_id,
            month=req.month,
            year=req.year,
            total=req.total
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

def gets(db: Session):
    try:
        data = db.query(Score).all()
        return data
    except Exception as e:
        db.rollback()
        raise Exception(e)
    finally:
        db.close()

async def upload_csv_pandas(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(BytesIO(contents))
    # Convert DataFrame to a list of dicts
    data = df.to_dict(orient="records")
    return {"rows": data}