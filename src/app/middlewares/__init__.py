from aiogram import Dispatcher

from src.app.core.config import Settings
#from src.app.middlewares.db import DatabaseMiddleware
from src.app.middlewares.settings import SettingsMiddleware


def register_middlewares(dp: Dispatcher, _settings: Settings):

    settings_middleware = SettingsMiddleware(_settings)
    dp.message.outer_middleware(settings_middleware)
    dp.callback_query.outer_middleware(settings_middleware)

#    db_middleware = DatabaseMiddleware()
#    dp.message.outer_middleware(db_middleware)
#    dp.callback_query.outer_middleware(db_middleware)