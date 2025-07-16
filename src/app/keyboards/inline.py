from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_menue = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💰 Продажа", callback_data="sale"),
            InlineKeyboardButton(text="🛒 Покупка", callback_data="buy")
        ],
        [
            InlineKeyboardButton(text="📋 Мои объявления", callback_data="my_ads")
        ],
        [
            InlineKeyboardButton(text="🔍 Поиск по категориям", callback_data="Search_by_category")
        ],
        [
            InlineKeyboardButton(text="🛠 Поддержка", callback_data="Support")
        ],
        [
            InlineKeyboardButton(text="📢 Купит рекламу", callback_data="Buy_advertising")
        ]
    ]
)


admin_main_panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🚀 Рассылка", callback_data="mailing")
        ],
        [
            InlineKeyboardButton(text="📊 Статистика", callback_data="statistics")
        ],
        [
            InlineKeyboardButton(text="🚫 Блокировка/разблокировка", callback_data="blocking/unblocking")
        ],
        [
            InlineKeyboardButton(text="📋 Канал", callback_data="channel_settings")
        ]
    ]
)

quit_to_admin_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_admin_menu")
        ]
    ]
)
