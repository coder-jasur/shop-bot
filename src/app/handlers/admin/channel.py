from pprint import pprint

import asyncpg
from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.app.database.queries.channel import get_channel, add_channel, delete_channel
from src.app.keyboards import inline_keyboard_creator
from src.app.states.admin import AddChannel

channel_router = Router()


@channel_router.callback_query(F.data == "channel_settings")
async def channel_settings(call: CallbackQuery, db_pool: asyncpg.Pool, bot: Bot):

    async with db_pool.acquire() as conn:
        channel = await get_channel(conn)

        if not channel:
            await call.message.edit_text(
                text="вы еще не добавили канал",
                reply_markup=inline_keyboard_creator(["add_channel"], ["➕ Дабавить канал"])
            )
        else:
            await call.message.edit_text(
                text="О канале:\n"
                     f"username: @{channel[0][1]}\n"
                     f"ID {channel[0][0]}\n"
                     f"количество пользователей {await bot.get_chat_member_count(channel[0][0])}",
                reply_markup=inline_keyboard_creator(
                    ["delite_channel", "back_to_admin_menu"],
                    ["🗑 Удалить канал", "🔙Назад"]
                )
            )


@channel_router.callback_query(F.data == "add_channel")
async def add_channel_stup(call: CallbackQuery, state: FSMContext, db_pool: asyncpg.Pool):
    async with db_pool.acquire() as conn:
        channel = await get_channel(conn)
        if not channel:
            await state.set_state(AddChannel.get_channel_id)
            await call.message.edit_text(
                text="отправлять сообщения из канала каторого вы хотите добавить",
            )
        else:
            await call.message.answer(
                text="у вас уже есть канал",
                reply_markup=inline_keyboard_creator(["back_to_admin_menu"], ["🔙Меню"])
            )


@channel_router.message(AddChannel.get_channel_id)
async def add_channel_for_bd(message: Message, db_pool: asyncpg.Pool, state: FSMContext):
    async with db_pool.acquire() as conn:
        try:
            await add_channel(
                conn=conn,
                channel_id=message.forward_from_chat.id,
                channel_name=message.forward_from_chat.username,

            )
            await message.answer(
                "✅ Канал успешно добален",
                reply_markup=inline_keyboard_creator(["back_to_admin_menu"], ["🔙Меню"])
            )
            await state.clear()
        except Exception as e:
            print("ERROR", e)


@channel_router.callback_query(F.data == "delite_channel")
async def delete_channel_question(call: CallbackQuery, db_pool: asyncpg.Pool):
    await call.message.answer(
        text="Вы уверени что хотите удалить канал?",
        reply_markup=inline_keyboard_creator(
            ["delete_channel", "cancel", "back_to_admin_menu"],
            ["✅ Подтвердит", "❌ Отменить", "🔙Назад"]
        )
    )
    async with db_pool.acquire() as conn:
        await delete_channel(conn)


@channel_router.callback_query(F.data == "delete_channel")
async def channel_delete(call: CallbackQuery, db_pool: asyncpg.Pool):
    async with db_pool.acquire() as conn:
        await delete_channel(conn)
        await call.message.edit_text(
            text="✅ Канал успешно удален",
            reply_markup=inline_keyboard_creator(
                ["back_to_admin_menu"],
                ["🔙Назад"]
            )
        )


@channel_router.callback_query(F.data == "cancel")
async def channel_delete(call: CallbackQuery, db_pool: asyncpg.Pool, bot: Bot):
    async with db_pool.acquire() as conn:
        channel = await get_channel(conn)

        await call.message.edit_text(
            text="О канале:\n"
                 f"username: {channel[0][1]}\n"
                 f"ID {channel[0][0]}\n"
                 f"количество пользователей {await bot.get_chat_member_count(channel[0][0])}",
            reply_markup=inline_keyboard_creator(
                ["back_to_admin_menu", "delite_channel"],
                ["🔙Назад", "🗑 Удалить канал"]
            )
        )
