from sqlalchemy import Column, Integer
from db.database import Base

class StudentGroup(Base):
    __tablename__ = "student_group"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer)
    group_id = Column(Integer)
    semester_id = Column(Integer)