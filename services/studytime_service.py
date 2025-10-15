from sqlalchemy.orm import Session
from models.study_time import StudyTime
from schemas.study_time_schema import StudyTimeReq


def create(db: Session,req: StudyTimeReq):
    try:
        data = StudyTime(name=req.name)
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
        data = db.query(StudyTime).all()
        return data
    except Exception as e:
        db.rollback()
        raise Exception(e)
    finally:
        db.close()