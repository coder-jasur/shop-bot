import asyncpg
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.app.database.queries.users import get_user, update_user_status
from src.app.keyboards import inline_keyboard_creator
from src.app.states.admin import GetUserId

user_status = Router()


@user_status.callback_query(F.data == "blocking/unblocking")
async def get_user_id(call: CallbackQuery, state: FSMContext):
    await state.set_state(GetUserId.get_user_id)
    await call.message.edit_text(
        text="👤Введите id пользователя которого хотите заблокировать/разблокировать",
        reply_markup=inline_keyboard_creator(["back_to_admin_menu"], ["🔙Назад"])
    )


@user_status.message(GetUserId.get_user_id)
async def update_user_id(message: Message, db_pool: asyncpg.Pool, state: FSMContext):
    await state.clear()

    async with db_pool.acquire() as conn:
        user = await get_user(
            conn=conn,
            user_id=int(message.text)
        )
        if user[2] == "unblocked":

            await message.answer(
                text=f"👤 Вы выбрали пользователя с ID: {message.text}. Выберите действие:",
                reply_markup=inline_keyboard_creator(
                    [f"bloced_user_{message.text}", "back_to_admin_menu"],
                    ["❌ Заблокировать", "🔙Назад"]
                )
            )

        elif user[2] == "blocked":
            await message.answer(
                text=f"👤 Вы выбрали пользователя с ID: {message.text}. Выберите действие:",
                reply_markup=inline_keyboard_creator(
                    [f"unbloced_user_{message.text}", "back_to_admin_menu"],
                    ["🔓 Разблокировать", "🔙Назад"]
                )
            )



@user_status.callback_query(F.data.startswith("unbloced_user_") | F.data.startswith("bloced_user_"))
async def block_adn_unblock_user_status(call: CallbackQuery, db_pool: asyncpg.Pool):
    await call.answer()
    data = call.data.split("_")
    user_id = data[2]
    b_u = data[0]

    async with db_pool.acquire() as conn:
        if b_u == "unbloced":
            await update_user_status(
                conn=conn,
                user_id=int(user_id),
                new_status="unblocked"
            )
            await call.message.edit_text(
                text=f"✅ Пользователь с ID: {user_id} успешно разблокирован. Теперь он снова имеет доступ к боту.",
                reply_markup=inline_keyboard_creator(["back_to_admin_menu"], ["🔙Меню"])
            )
        elif b_u == "bloced":
            await update_user_status(
                conn=conn,
                user_id=int(user_id),
                new_status="blocked"
            )
            await call.message.edit_text(
                text=f"🚫 Пользователь с ID: {user_id} заблокирован. Он больше не сможет использовать бота.",
                reply_markup=inline_keyboard_creator(["back_to_admin_menu"], ["🔙Меню"])
            )



