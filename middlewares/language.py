from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware

from service.repo.repository import SQLAlchemyRepos
from service.repo.user_repo import UserRepo


class ACLMiddleware(I18nMiddleware):

    async def get_user_locale(self, action, data):
        repo: SQLAlchemyRepos = data[-1]['repo']
        user = types.User.get_current()
        language = await repo.get_repo(UserRepo).get_language(user_id=user.id)
        if language:
            return language.language_code
        else:
            return user.locale