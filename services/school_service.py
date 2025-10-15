from sqlalchemy.orm import Session
from models.school import School
from schemas.school_schema import SchoolReq


def create_school(db: Session,school: SchoolReq):
    try:
        db_book = School(name_en=school.name_en, name_km=school.name_km)
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book
    except Exception as e:
        db.rollback()
        raise Exception(e)
    finally:
        db.commit()
        db.close()

def get_schools(db: Session):
    try:
        degrees = db.query(School).all()
        return degrees
    except Exception as e:
        db.rollback()
        raise Exception(e)
    finally:
        db.commit()
        db.close()
