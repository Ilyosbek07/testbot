from sqlalchemy import BigInteger, Column, Integer, DateTime

from models.base import Base


class SelectedAnswer(Base):
    __tablename__ = 'tests_selectedanswers'

    id = Column(BigInteger(), autoincrement=True, nullable=False, primary_key=True)
    user_id = Column(BigInteger(), nullable=False)
    subject_id = Column(BigInteger(), nullable=False)
    right_answers = Column(Integer(), nullable=False)
    wrong_answers = Column(Integer(), nullable=False)
    created_at = Column(DateTime(timezone='Asia/Tashkent'))

    def __str__(self):
        return f"{self.user_id} | {self.subject_id} | {self.right_answer} | {self.wrong_answer}"