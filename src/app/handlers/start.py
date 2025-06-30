from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from src.app.keyboards.inline import main_menue

start_router = Router()

@start_router.message(CommandStart())
async def start_handlers(message: Message) -> None:
    print(1)
    await message.answer(
        "✨Привет! Этот бот для "
        "удобного и быстрой публикации "
        "объявлений на канале @ITbarakholka.\n"
        "🚀Рад приветствовать тебя\n"
        f"@{message.from_user.username}",
        reply_markup=main_menue
    )
