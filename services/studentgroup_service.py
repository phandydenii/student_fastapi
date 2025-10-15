from typing import List

from sqlalchemy.orm import Session
from models.student_group import StudentGroup
from schemas.student_group_schema import StudentGroupReq, StudentGroupRes


def create(db: Session,req: StudentGroupReq):
    try:
        data = StudentGroup(student_id=req.student_id,group_id=req.group_id,semester_id=req.semester_id)
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
        data = db.query(StudentGroup).all()
        return data
    except Exception as e:
        db.rollback()
        raise Exception(e)
    finally:
        db.close()
