import datetime

import asyncpg
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.app.database.queries.users import get_user, add_user
from src.app.ioc_container_dishka.containers import AppContainer
from src.app.keyboards.inline import main_menue

start_router = Router()


@start_router.message(CommandStart())
async def start_handlers(message: Message, db_pool: asyncpg.Pool) -> None:

    async with db_pool.acquire() as conn:
        user = await get_user(
            conn=conn,
            user_id=message.from_user.id
        )
        if not user:
            await add_user(
                conn=conn,
                user_id=message.from_user.id,
                activity_date=str(datetime.date.today()),
                username=message.from_user.username
            )

        await message.answer(
            "✨Привет! Этот бот для "
            "удобного и быстрой публикации "
            "объявлений на канале @ITbarakholka.\n"
            "🚀Рад приветствовать тебя\n"
            f"@{message.from_user.username}",
            reply_markup=main_menue
        )


