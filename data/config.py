from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
CLICK = env.str("CLICK")
PAYME = env.str("PAYME")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
I18N_DOMAIN = env.str("I18N_DOMAIN")
POSTGRES_HOST = env.str("POSTGRES_HOST")
POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD")
POSTGRES_USER = env.str("POSTGRES_USER")
POSTGRES_DB = env.str("POSTGRES_DB")
POSTGRES_PORT = env.str("POSTGRES_PORT")
POSTGRES_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
DJANGO_ROOT = "backend/panel/"