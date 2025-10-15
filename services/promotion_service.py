from sqlalchemy.orm import Session
from models.promotion import Promotion
from schemas.promotion_schema import PromotionReq


def create(db: Session,req: PromotionReq):
    try:
        data = Promotion(no=req.no,start=req.start,end=req.end)
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
        data = db.query(Promotion).all()
        return data
    except Exception as e:
        db.rollback()
        raise Exception(e)
    finally:
        db.close()