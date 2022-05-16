from sqlalchemy import insert, select, update

from models.language import Language
from models.user import User
from service.repo.base_repo import BaseSQLAlchemyRepo


class UserRepo(BaseSQLAlchemyRepo):
    model = User

    async def add_user(self, user_id: int, name: str, language: int, is_active: bool):
        sql = insert(self.model).values(user_id=user_id, name=name, language_id=language, is_active=is_active).returning('*')
        await self._session.execute(sql)
        await self._session.commit()

    async def get_user(self, user_id: int) -> model:
        sql = select(self.model).where(self.model.user_id == user_id)
        request = await self._session.execute(sql)
        user = request.scalar()
        return user

    async def update_language(self, user_id: int, updated: dict):
        sql = update(self.model).where(self.model.user_id == user_id).values(**updated)
        await self._session.execute(sql)
        await self._session.commit()

    async def get_language(self, user_id: int) -> model:
        sql_lang = select(Language).select_from(Language).filter(Language.id == select(self.model.language_id).filter(self.model.user_id == user_id))
        request = await self._session.execute(sql_lang)
        return request.scalar()