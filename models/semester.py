from sqlalchemy import Column, Integer, DateTime
from db.database import Base

class Semester(Base):
    __tablename__ = "semester"
    id = Column(Integer, primary_key=True, index=True)
    no = Column(Integer, index=True)
    start = Column(DateTime)
    end = Column(DateTime)