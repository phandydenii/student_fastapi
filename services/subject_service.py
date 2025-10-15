from sqlalchemy.orm import Session
from models.subject import Subject
from schemas.subject_schema import SubjectReq


def create(db: Session,req: SubjectReq):
    try:
        data = Subject(name_en=req.name_en,name_km=req.name_km,grade_id=req.grade_id)
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
        data = db.query(Subject).all()
        return data
    except Exception as e:
        db.rollback()
        raise Exception(e)
    finally:
        db.close()