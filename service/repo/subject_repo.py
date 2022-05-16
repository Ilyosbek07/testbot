from sqlalchemy import insert, select

from models.subject import Subjects
from service.repo.base_repo import BaseSQLAlchemyRepo


class SubjectRepo(BaseSQLAlchemyRepo):
    model = Subjects

    async def get_subjects(self) -> model:
        sql = select(self.model.subject_name)
        request = await self._session.execute(sql)
        return request.scalars().all()

    async def get_subject_id(self, subject_name: str) -> model:
        sql = select(self.model.id).where(self.model.subject_name == subject_name)
        request = await self._session.execute(sql)
        return request.scalar()

    async def get_subject_name(self, subject_id: str) -> model:
        sql = select(self.model.subject_name).where(self.model.id == subject_id)
        request = await self._session.execute(sql)
        return request.scalar()