from sqlalchemy import BigInteger, String, Column

from models.base import Base


class Subjects(Base):

    __tablename__ = 'tests_subjects'

    id = Column(BigInteger(), autoincrement=True, nullable=False, primary_key=True)
    subject_name = Column(String(length=60), nullable=False)