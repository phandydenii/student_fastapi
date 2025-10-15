
from sqlalchemy import Column, Integer, String
from db.database import Base

class School(Base):
    __tablename__ = "school"
    id = Column(Integer, primary_key=True, index=True)
    name_en = Column(String)
    name_km = Column(String)