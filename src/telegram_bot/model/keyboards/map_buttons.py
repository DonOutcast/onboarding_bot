from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

map_buttons = [
    [
        InlineKeyboardButton(callback_data='back', text='<'),
        InlineKeyboardButton(callback_data='info', text='Подробнее'),
        InlineKeyboardButton(callback_data='next', text='>')
    ],
    [
        InlineKeyboardButton(callback_data='back', text='Назад'),
    ]
]

map_keyboard = InlineKeyboardMarkup(inline_keyboard=map_buttons)
