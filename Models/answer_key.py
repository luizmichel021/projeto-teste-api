from sqlalchemy import Column, Integer, CHAR, ForeignKey
from Connection.database import Base , engine

class AnswerKey(Base):
    __tablename__ = "answers_key"

    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey("question.id"), unique=True)
    correct_letter = Column(CHAR(1), nullable=False)  # A, B, C, D
