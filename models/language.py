from sqlalchemy import BigInteger, Column, String

from models.base import Base


class Language(Base):
    __tablename__ = 'tests_language'

    id = Column(BigInteger(), autoincrement=True, nullable=False, primary_key=True)
    language_name = Column(String(length=30), nullable=False)
    language_code = Column(String(length=5), nullable=False)

    def __str__(self):
        return f"{self.id} | {self.language_name} | {self.language_code}"