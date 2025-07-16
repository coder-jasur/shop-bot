from aiogram import Dispatcher, Router
from aiogram.types import CallbackQuery

from src.app.core.config import Settings
from src.app.handlers.admin import register_admin_routers
from src.app.handlers.start import start_router


def register_routers(dp: Dispatcher, settings: Settings):
    main_router = Router()

    register_admin_routers(settings, dp)
    main_router.include_router(start_router)

    dp.include_router(main_router)
