import asyncpg
from aiogram import Dispatcher

from src.app.core.config import Settings
from src.app.middlewares.settings import SettingsMiddleware
from asyncpg import Pool

from src.app.middlewares.user_requests import MessageUser


def register_middlewares(dp: Dispatcher, _settings: Settings, db_pool: asyncpg.Pool):

    settings_middleware = SettingsMiddleware(_settings)
    dp.message.outer_middleware(settings_middleware)
    dp.callback_query.outer_middleware(settings_middleware)

    message_user = MessageUser(db_pool)
    dp.update.outer_middleware(message_user)
