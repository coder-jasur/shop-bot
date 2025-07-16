import datetime

import asyncpg
from aiogram import Router, F, Bot
from aiogram.enums import ChatMemberStatus
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from src.app.database.queries.channel import get_channel
from src.app.database.queries.users import get_all_users
from src.app.keyboards import inline_keyboard_creator

statistics_router = Router()


@statistics_router.callback_query(F.data == "statistics")
async def get_statistics(call: CallbackQuery, db_pool: asyncpg.Pool, bot: Bot):

    async with db_pool.acquire() as conn:

        all_users = await get_all_users(conn=conn)
        channel = await get_channel(conn)
        activ_user = 0

        for user in all_users:
            chat_member = await bot.get_chat_member(
                chat_id=channel[0][0],
                user_id=user[0]
            )
            if chat_member.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.CREATOR,
                ChatMemberStatus.ADMINISTRATOR]:
                user_time = user[3]

                real_time = datetime.date.today()

                if user_time:
                    user_time_to_date_time_obj = datetime.datetime.strptime(user_time, "%Y-%m-%d").date()
                    time_difference = (user_time_to_date_time_obj - real_time).days
                    if time_difference <= 15:
                        activ_user += 1

        await call.message.edit_text(
            text="Текущая статистика:\n"
                 f"📊 Общее количество пользователей канала: {await bot.get_chat_member_count(channel[0][0])}\n"
                 f"👥 Активные пользователи канала: {activ_user}\n"
                 f"🤖Всего пользователей в боте: {len(all_users)}\n",
            reply_markup=inline_keyboard_creator(["back_to_admin_menu"], ["🔙Меню"])
        )


@statistics_router.message(Command("userss"))
async def get_last_day_statistics(message: Message, db_pool: asyncpg.Pool):
    async with db_pool.acquire() as conn:
        all_user = await get_all_users(conn)

        new_user_in_day = 0

        for user in all_user:
            user_registration_time = user[4]
            user_time_to_date_time_obj = datetime.datetime.strptime(
                str(user_registration_time), "%Y-%m-%d %H:%M:%S.%f"
            ).date()
            time_difference = user_time_to_date_time_obj - datetime.date.today()
            if time_difference.days >= -1:
                new_user_in_day += 1

            print(time_difference.days)
            await message.answer(
                f"Всего пользователей в боте: {len(all_user)}\n"
                f"Новых пользователей за сутки: {new_user_in_day}"
            )
