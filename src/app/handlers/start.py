import asyncpg
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.app.ioc_container_dishka.containers import AppContainer
from src.app.keyboards.inline import main_menue

start_router = Router()


@start_router.message(CommandStart())
async def start_handlers(message: Message, db_pool: asyncpg.Pool, container: AppContainer) -> None:

    async with db_pool.acquire() as conn:
        user_dao = container.user_dao(conn=conn)
        user = await user_dao.get_user(message.from_user.id)
        if not user:
            await user_dao.add_user(
                _id=message.from_user.id,
                username=message.from_user.username,
            )

        await message.answer(
            "✨Привет! Этот бот для "
            "удобного и быстрой публикации "
            "объявлений на канале @ITbarakholka.\n"
            "🚀Рад приветствовать тебя\n"
            f"@{message.from_user.username}",
            reply_markup=main_menue
        )


