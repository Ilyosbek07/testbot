import random
from typing import List

from sqlalchemy import select, and_, func

from models.direction import Direction
from models.direction_subjects import DirectionSubjects
from models.test import Tests
from service.repo.base_repo import BaseSQLAlchemyRepo

# <direction> direction id -> <tests_tests> -> test_id -> <directionsubjects> all test_id -> cycle get subjects


class TestRepo(BaseSQLAlchemyRepo):
    model = Tests

    async def get_test(
            self,
            direction_name: str,
            price: float,
            language: str
    ) -> List[DirectionSubjects]:
        sql = select(Direction.id).filter(Direction.direction_name == direction_name)
        r = await self._session.execute(sql)
        subsql = select(self.model.id).filter(and_(self.model.directions_id == r.scalar()), and_(self.model.price == price), and_(self.model.language_id == language)).order_by(func.random())
        req = await self._session.execute(subsql)
        sql_tests = select(DirectionSubjects).filter(DirectionSubjects.test_id == req.scalar())
        request = await self._session.execute(sql_tests)
        return request.scalars().all()

    async def get_pay_test(
            self,
            direction_name: str

    ) -> model:
        sql = select(Direction.id).filter(Direction.direction_name == direction_name)
        r = await self._session.execute(sql)
        subsql = select(self.model).filter(and_(self.model.directions_id == r.scalar()), and_(self.model.price > 0.0)).order_by(func.random())
        req = await self._session.execute(subsql)
        return req.scalar()

    async def get_test_path(self, test_id: int, subject_id: int):
        sql = select(DirectionSubjects).filter(and_(DirectionSubjects.test_id == test_id), and_(DirectionSubjects.subject_id == subject_id))
        request = await self._session.execute(sql)
        return request.scalar()

    # async def get_test(self, price: int, direction_id: int):
    #     sql = select(self.model).filter(and_(self.model.price == float(price)), and_(self.model.directions_id == direction_id))
    #     request = await self._session.execute(sql)
    #     return request.scalars().all()


    # async def get_test_id(self, test_id: int):
    #     sql = select(self.model).where(self.model.id == test_id)
    #     request = await self._session.execute(sql)
    #     return request.scalar()