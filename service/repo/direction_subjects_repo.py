from sqlalchemy import select, and_, func

from models.direction_subjects import DirectionSubjects
from models.test import Tests
from service.repo.base_repo import BaseSQLAlchemyRepo


class DirectionSubjectsRepo(BaseSQLAlchemyRepo):
    model = DirectionSubjects

    async def get_results(self, test_id: int, test_type):
        if test_type == "pay":
            sql = select(self.model).filter(self.model.test_id == select(Tests.id).filter(and_(Tests.id == test_id), and_(Tests.price > 0.0)))
        else:
            sql = select(self.model).filter(self.model.id == test_id)
        request = await self._session.execute(sql)
        return request.scalar()

    async def get_test_by_id(self, test_id: int):
        sql = select(self.model).filter(self.model.test_id == test_id)
        request = await self._session.execute(sql)
        return request.scalars().all()