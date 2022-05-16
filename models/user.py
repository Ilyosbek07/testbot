from sqlalchemy import BigInteger, Column, String, Boolean, ForeignKey

from models.base import Base


class User(Base):
    __tablename__ = 'tests_user'

    id = Column(BigInteger(), autoincrement=True, nullable=False, primary_key=True)
    user_id = Column(BigInteger(), primary_key=True, nullable=False)
    name = Column(String(length=100), nullable=False)
    language_id = Column(ForeignKey('Language', ondelete="PROTECT"), nullable=False)
    is_active = Column(Boolean(), nullable=False)

    def __str__(self):
        return f"{self.user_id} | {self.name} | {self.is_active} | {self.language_id}"
