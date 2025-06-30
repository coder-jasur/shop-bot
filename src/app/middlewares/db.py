from typing import Callable, Any, Awaitable

#import aiosqlite
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from src.app.core.config import Settings


#class DatabaseMiddleware(BaseMiddleware):
#    async def __call__(
#        self,
#        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
#        event: TelegramObject,
#        data: dict[str, Any],
#    ) -> None:
#        settings: Settings = data["settings"]
#        async with aiosqlite.connect(settings.db_name) as conn:
#            data["conn"] = conn
#            await handler(event, data)
