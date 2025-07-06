import asyncpg
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from aiogram import Router, F, Bot
from aiogram.filters import Command

from src.app.ioc_container_dishka.containers import AppContainer
from src.app.keyboards import inline_keyboard_creator
from src.app.keyboards.inline import admin_main_panel
from src.app.states.mailing import Mailing

admin_main_router = Router()


@admin_main_router.message(Command("admin"))
async def amin_main_panel(message: Message):
    await message.answer(
        text="👋 Добро пожаловать в административную панель.",
        reply_markup=admin_main_panel
    )

@admin_main_router.callback_query(F.data == "mailing")
async def get_mailing_message(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(
        text="💬 Введите текст сообщения для рассылки",
        reply_markup=inline_keyboard_creator(["back_to_admin_menu"], ["🔙Назад"])
    )
    await state.set_state(Mailing.mailing_message)

@admin_main_router.message(Mailing.mailing_message)
async def mailing(message: Message, state: FSMContext, db_pool: asyncpg.Pool, container: AppContainer,bot: Bot):
    async with db_pool.acquire() as conn:
        user_dao = container.user_dao(conn=conn)
        users = await user_dao.get_users()
        for i in range(len(users)):
            await bot.send_message(users[0][0], text=message.text)
            await state.clear()






@admin_main_router.callback_query(F.data == "back_to_admin_menu")
async def bact_to_admin_menu(call: CallbackQuery):
    await call.message.edit_text(
        text="👋 Добро пожаловать в административную панель.",
        reply_markup=admin_main_panel
    )





