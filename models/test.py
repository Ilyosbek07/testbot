from sqlalchemy import BigInteger, Column, String, ForeignKey, DECIMAL
from models.base import Base


class Tests(Base):
    __tablename__ = 'tests_tests'

    id = Column(BigInteger(), autoincrement=True, nullable=False, primary_key=True)
    price = Column(DECIMAL(precision=2, scale=8), nullable=False)
    directions_id = Column(ForeignKey('Direction', ondelete="PROTECT"), nullable=False)
    language_id = Column(ForeignKey('Language', ondelete="PROTECT"), nullable=False)

    def __str__(self):
        return f"{self.id}  | {self.price} | {self.directions_id}"
