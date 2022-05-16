from sqlalchemy import select

from models.language import Language
from service.repo.base_repo import BaseSQLAlchemyRepo


class LanguageRepo(BaseSQLAlchemyRepo):
    model = Language

    async def get_languages(self) -> model:
        sql = select(self.model)
        request = await self._session.execute(sql)
        return request.scalars().all()

    async def get_language_id(self, language_name: str) -> model:
        sql = select(self.model).filter(self.model.language_name == language_name)
        request = await self._session.execute(sql)
        return request.scalar()