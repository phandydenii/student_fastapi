from sqlalchemy import Column, Integer, String
from db.database import Base

class StudyTime(Base):
    __tablename__ = "study_time"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)