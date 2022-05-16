from sqlalchemy import select

from models.direction import Direction
from service.repo.base_repo import BaseSQLAlchemyRepo


class DirectionRepo(BaseSQLAlchemyRepo):
    model = Direction

    async def get_directions(self):
        sql = select(self.model.direction_name)
        request = await self._session.execute(sql)
        return request.scalars().all()