from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# menu_buttons = [
#     [
#         InlineKeyboardButton(callback_data='Study', text='Обучение'),
#         InlineKeyboardButton(callback_data='company', text='О нас')
#     ],
#     [
#         InlineKeyboardButton(callback_data='faq', text='Задать вопрос'),
#         InlineKeyboardButton(callback_data='map', text='Карта')
#     ],
#     [
#         InlineKeyboardButton(callback_data='employees', text='Сотрудники'),
#         InlineKeyboardButton(callback_data='unknown', text='не знаю')
#     ]
# ]

# menu_keyboard = InlineKeyboardMarkup(inline_keyboard=menu_buttons)

menu_buttons = [
    [
        KeyboardButton(text='Обучение'),
        KeyboardButton(text='Карта')
    ],
    [
        KeyboardButton(text='О нас'),
        KeyboardButton(text='Наши сотрудники')
    ],
    [
        KeyboardButton(text='Задать вопрос'),
        KeyboardButton(text='О себе')
    ],
    [KeyboardButton(text='Админка')]

]

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=menu_buttons, resize_keyboard=True)
