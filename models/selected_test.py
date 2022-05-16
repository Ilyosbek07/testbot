from sqlalchemy import BigInteger, Column, String, Boolean, ForeignKey

from models.base import Base


class SelectedTest(Base):
    __tablename__ = 'tests_selectedtest'

    id = Column(BigInteger(), autoincrement=True, nullable=False, primary_key=True)
    user_id = Column(BigInteger(), nullable=False)
    test_id = Column(BigInteger(), nullable=True)

    def __str__(self):
        return f"{self.user_id} | {self.test_id}"