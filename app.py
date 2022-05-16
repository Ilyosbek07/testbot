from aiogram import executor
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from loader import dp
import middlewares, handlers
from utils.misc.req_func import make_connection_string
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


engine = create_async_engine(
    make_connection_string(), future=True, echo=False, pool_size=30, max_overflow=30
)

session_fabric = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

