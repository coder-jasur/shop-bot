from environs import Env

env = Env()
env.read_env()


class Settings:
    bot_token = env.str("BOT_TOKEN")
    db_name = env.str("DB_NAME")
    superadmin_ids = env.list("ADMIN_IDS", subcast=int)