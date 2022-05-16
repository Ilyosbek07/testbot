from app import session_fabric
from data import config
from loader import LOCALES_DIR, dp
from .db_session import DbSessionMiddleware
from .language import ACLMiddleware
from .repo import Repository
from .throttling import ThrottlingMiddleware

if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(DbSessionMiddleware(session_pool=session_fabric))
    dp.middleware.setup(Repository())
    dp.middleware.setup(ACLMiddleware(config.I18N_DOMAIN, LOCALES_DIR, default="uz"))

# def setup_middlewares(dp: Dispatcher, sm: sessionmaker):
    # dp.middleware.setup(ThrottlingMiddleware())


