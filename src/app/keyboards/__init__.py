from typing import Protocol

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from asyncpg import Connection


def inline_keyboard_creator(callback_data_list: list, button_name_list: list):
    inline_keyboard = InlineKeyboardBuilder()
    for i in range(len(button_name_list)):
        callback_data = callback_data_list[i]
        button_name = button_name_list[i]
        inline_keyboard.row(InlineKeyboardButton(text=button_name, callback_data=callback_data))

    return inline_keyboard.as_markup()


# class ShopRepository:
#
#     def __init__(self, conn: Connection):
#         self._conn = conn
#
#     async def add[T](self) -> None:
#         async with self._conn as conn:
#             return
#
#     async def delete[T](self) -> T | None:
#         async with self._conn as conn:
#             return T
#
#     async def uppdate[T](self) -> T | None:
#         async with self._conn as conn:
#             return T


# class AddShop(Protocol):
#
#     async def add(self) -> None: ...


# class DeleteShop(Protocol):
#
#     async def delete[T](self) -> T | None: ...


# async def on_start(add_shop: AddShop) -> None:
#     await add_shop.add()
#
#
# async def on_delete(delete_shop: DeleteShop) -> None:
#     await delete_shop.delete()
#
#
# async def main() -> None:
#
#     shop_repo = ShopRepository(Connection())
#
#     await on_start(shop_repo)
#     await on_delete(shop_repo)
