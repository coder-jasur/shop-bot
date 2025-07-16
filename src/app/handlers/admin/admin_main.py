import asyncpg
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from aiogram import Router, F, Bot
from aiogram.filters import Command

from src.app.ioc_container_dishka.containers import AppContainer
from src.app.keyboards import inline_keyboard_creator
from src.app.keyboards.inline import admin_main_panel


admin_main_router = Router()


@admin_main_router.message(Command("admin"))
async def amin_main_panel(message: Message):
    await message.answer(
        text="👋 Добро пожаловать в административную панель.",
        reply_markup=admin_main_panel
    )



@admin_main_router.callback_query(F.data == "back_to_admin_menu")
async def bact_to_admin_menu(call: CallbackQuery):
    await call.message.edit_text(
        text="👋 Добро пожаловать в административную панель.",
        reply_markup=admin_main_panel
    )





