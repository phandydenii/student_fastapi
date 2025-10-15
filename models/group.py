from sqlalchemy import Column, Integer, String
from db.database import Base

class Group(Base):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    study_time = Column(Integer)