import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from src.app.core.config import Settings
from src.app.handlers import register_routers
from src.app.middlewares import register_middlewares

logger = logging.getLogger(__name__)
logging.basicConfig(level="INFO")

async def main():
    settings = Settings()

    bot = Bot(token=settings.bot_token)

    dp = Dispatcher()
    register_middlewares(dp=dp, _settings=settings)
    register_routers(dp)


    await dp.start_polling(bot)



if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.exception("Clouse", e)