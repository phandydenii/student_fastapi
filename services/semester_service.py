from sqlalchemy.orm import Session
from models.semester import Semester
from schemas.semester_schema import SemesterReq


def create(db: Session,req: SemesterReq):
    try:
        data = Semester(no=req.no,start=req.start,end=req.end)
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
        data = db.query(Semester).all()
        return data
    except Exception as e:
        db.rollback()
        raise Exception(e)
    finally:
        db.close()