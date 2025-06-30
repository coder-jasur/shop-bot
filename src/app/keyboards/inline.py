from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_menue = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💰 Продажа", callback_data=" "),
            InlineKeyboardButton(text="🛒 Покупка", callback_data=" ")
        ],
        [
            InlineKeyboardButton(text="📋 Мои объявления", callback_data=" ")
        ],
        [
            InlineKeyboardButton(text="🔍 Поиск по категориям", callback_data=" ")
        ],
        [
            InlineKeyboardButton(text="🛠 Поддержка", callback_data=" ")
        ],
        [
            InlineKeyboardButton(text="📢 Купит рекламу", callback_data=" ")
        ]
    ]
)
