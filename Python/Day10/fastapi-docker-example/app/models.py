from sqlalchemy import Column, Integer, JSON
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON, nullable=False)
