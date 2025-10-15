from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100))
    full_name = Column(String(100))
    hashed_password = Column(String(500), nullable=False)
    disabled = Column(Boolean, default=False)
