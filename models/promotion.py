
from sqlalchemy import Column, Integer, DateTime
from db.database import Base

class Promotion(Base):
    __tablename__ = "promotion"
    id = Column(Integer, primary_key=True, index=True)
    no = Column(Integer, index=True)
    start = Column(DateTime)
    end = Column(DateTime)