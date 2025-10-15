from sqlalchemy.orm import Session
from models.degree import Degree
from schemas.degree import DegreeReq

def create_degree(db: Session,degree: DegreeReq):
    try:
        db_book = Degree(name_en=degree.name_en, name_km=degree.name_km)
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book
    except Exception as e:
        db.rollback()
        raise Exception(e)
    finally:
        db.close()
def get_degrees(db: Session):
    try:
        degrees = db.query(Degree).all()
        return degrees
    except Exception as e:
        db.rollback()
        raise Exception(e)
    finally:
        db.close()