from sqlalchemy import Column, Integer, String, CHAR, ForeignKey
from Connection.database import Base , engine

class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey("question.id"))
    letter = Column(CHAR(1), nullable=False)  # A, B, C, D
    text = Column(String, nullable=False)