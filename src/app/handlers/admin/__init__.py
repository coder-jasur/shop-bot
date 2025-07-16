from aiogram import Dispatcher, Router, F

from src.app.core.config import Settings
from src.app.handlers.admin.admin_main import admin_main_router
from src.app.handlers.admin.broadcast import broadcater_router
from src.app.handlers.admin.channel import channel_router
from src.app.handlers.admin.statistics import statistics_router
from src.app.handlers.admin.user_status import user_status


def register_admin_routers(settings: Settings, dp: Dispatcher):
    admin_register_router = Router()

    admin_register_router.message.filter(F.from_user.id.in_(settings.admin_ids))

    admin_register_router.include_router(admin_main_router)
    admin_register_router.include_router(broadcater_router)
    admin_register_router.include_router(channel_router)
    admin_register_router.include_router(statistics_router)
    admin_register_router.include_router(user_status)

    dp.include_router(admin_register_router)