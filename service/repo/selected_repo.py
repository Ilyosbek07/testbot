from sqlalchemy import insert, select

from models.selected_test import SelectedTest
from service.repo.base_repo import BaseSQLAlchemyRepo


class SelectedTestRepo(BaseSQLAlchemyRepo):
    model = SelectedTest

    async def check_test_id(self, user_id: int):
        sql = select(self.model.user_id).filter(self.model.user_id == user_id)
        request = await self._session.execute(sql)
        return request.scalar()

    async def add_test_id(self, test_id: int, user_id: int):
        sql = insert(self.model).values(user_id=user_id, test_id=test_id).returning('*')
        await self._session.execute(sql)
        await self._session.commit()

    async def get_test_id(self, user_id: int):
        sql = select(self.model.test_id).filter(self.model.user_id == user_id)
        request = await self._session.execute(sql)
        return request.scalar()

    async def delete_test_id(self, test_id: int, user_id: int):
        pass