from aiogram import Dispatcher, Router, F

from src.app.core.config import Settings
from src.app.handlers.admin.admin_main import admin_main_router


def register_admin_routers(settings: Settings, dp: Dispatcher):
    admin_register_router = Router()

    admin_register_router.message.filter(F.from_user.id.in_(settings.admin_ids))

    admin_register_router.include_router(admin_main_router)

    dp.include_router(admin_register_router)