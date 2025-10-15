from sqlalchemy.orm import Session
from models.group import Group
from schemas.group_schema import GroupReq


def create(db: Session,req: GroupReq):
    try:
        data = Group(name=req.name,study_time=req.study_time,)
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
        data = db.query(Group).all()
        return data
    except Exception as e:
        db.rollback()
        raise Exception(e)
    finally:
        db.close()