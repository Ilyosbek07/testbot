from pathlib import Path

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.i18n import I18nMiddleware

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
BASE_DIR = Path(__file__).parent
LOCALES_DIR = BASE_DIR / 'locales'
i18n = I18nMiddleware(config.I18N_DOMAIN, LOCALES_DIR, default="uz")
_ = i18n.gettext
__ = i18n.lazy_gettext
