from sqlalchemy import BigInteger, Column, String, ForeignKey

from models.base import Base


class DirectionSubjects(Base):
    __tablename__ = 'tests_directionsubjects'

    id = Column(BigInteger(), autoincrement=True, nullable=False, primary_key=True)
    file = Column(String(), nullable=False)
    keys = Column(String(), nullable=False)
    subject_id = Column(ForeignKey('Subjects', ondelete="PROTECT"), nullable=False)
    test_id = Column(ForeignKey('Tests', ondelete="PROTECT"), nullable=False)

    def __str__(self):
        return f"{self.id} | {self.file} | {self.subject_id} | {self.test_id}"
