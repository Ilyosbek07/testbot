from sqlalchemy import BigInteger, Column, String, ForeignKey, DECIMAL, Integer, Text

from models.base import Base


class Direction(Base):
    __tablename__ = 'tests_direction'

    id = Column(BigInteger(), autoincrement=True, nullable=False, primary_key=True)
    direction_name = Column(String(length=60), nullable=False)

    def __str__(self):
        return f"{self.id} | {self.direction_name}"
