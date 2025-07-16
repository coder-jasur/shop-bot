import asyncio
import logging

import asyncpg
from aiogram import Bot, Dispatcher
from aiogram.types import CallbackQuery
from dependency_injector import containers, providers

from src.app.common.get_db_url import construct_postgresql_url
from src.app.core.config import Settings
from src.app.database.tables import create_table
from src.app.handlers import register_routers
from src.app.ioc_container_dishka.containers import AppContainer
from src.app.middlewares import register_middlewares

logger = logging.getLogger(__name__)
logging.basicConfig(level="INFO")


async def main():
    container = AppContainer()

    try:
        await container.init_resources()
        settings = container.config()
        bot = Bot(token=settings.bot_token)
        pool = await container.db_pool()

        await create_table(pool)

        dp = Dispatcher()

        register_middlewares(dp=dp, _settings=settings, db_pool=pool)
        register_routers(dp, settings)

        await dp.start_polling(bot, **{"db_pool": pool, "container": container})
    finally:
        await container.shutdown_resources()




if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.exception("Clouse", e)
