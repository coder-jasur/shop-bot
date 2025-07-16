from typing import Callable, Any, Awaitable

import asyncpg
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Update

from src.app.database.queries.users import update_user_activity


class MessageUser(BaseMiddleware):

    def __init__(self, db_pool: asyncpg.Pool):
        self._db_pool = db_pool

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: dict[str, Any]
    ) -> None:
        user_id = None
        if event.message:
            user_id = event.message.from_user.id
        elif event.callback_query:
            user_id = event.callback_query.from_user.id

        data["user_id"] = user_id
        async with self._db_pool.acquire() as conn:
            await update_user_activity(conn, user_id)

        return await handler(event, data)
