from aiogram.dispatcher.middlewares import BaseMiddleware
from sqlalchemy.ext.asyncio import AsyncSession

from service.repo.repository import SQLAlchemyRepos


class Repository(BaseMiddleware):

    async def on_pre_process_message(self, obj, data, *args):
        session: AsyncSession = data['session']
        data['repo'] = SQLAlchemyRepos(session)

    async def on_process_message(self, obj, data, *args):
        session: AsyncSession = data['session']
        data['repo'] = SQLAlchemyRepos(session)


    async def on_pre_process_callback_query(self, obj, data, *args):
        session: AsyncSession = data['session']
        data['repo'] = SQLAlchemyRepos(session)


    async def on_process_callback_query(self, obj, data, *args):
        session: AsyncSession = data['session']
        data['repo'] = SQLAlchemyRepos(session)
