from sqlalchemy import Column, Integer, String, ForeignKey, Float
from db.database import Base

class Score(Base):
    __tablename__ = "score"
    id = Column(Integer, primary_key=True, index=True)
    student_group_id = Column(Integer)
    subject_id = Column(Integer)
    month = Column(Integer)
    year = Column(Integer)
    total = Column(Float)