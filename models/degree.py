from sqlalchemy import Column, Integer, String
from db.database import Base

class Degree(Base):
    __tablename__ = "degree"
    id = Column(Integer, primary_key=True, index=True)
    name_en = Column(String)
    name_km = Column(String)