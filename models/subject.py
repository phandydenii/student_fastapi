from sqlalchemy import Column, Integer, String, ForeignKey
from db.database import Base

class Subject(Base):
    __tablename__ = "subject"
    id = Column(Integer, primary_key=True, index=True)
    name_en = Column(String)
    name_km = Column(String)
    grade_id = Column(Integer)