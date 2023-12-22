from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_buttons = [
    [
        InlineKeyboardButton(text="Экзамены", callback_data="examinations"),
        InlineKeyboardButton(text="Предметы", callback_data="subject_search"),
    ],
    [
        InlineKeyboardButton(text="Расписание", callback_data="schedule"),
        InlineKeyboardButton(text="Подписка", callback_data="payment"),
    ],
]
main_menu = InlineKeyboardMarkup(inline_keyboard=main_buttons)

exam_buttons = [
    [
        InlineKeyboardButton(text="◀️", callback_data="previous"),
        InlineKeyboardButton(text="Изменить", callback_data="edit"),
        InlineKeyboardButton(text="➡️", callback_data="next"),
    ]
]

exam_menu = InlineKeyboardMarkup(inline_keyboard=exam_buttons)
