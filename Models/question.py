from sqlalchemy import Column, Integer, String
from Connection.database import Base , engine

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)
    category = Column(String, nullable=False)