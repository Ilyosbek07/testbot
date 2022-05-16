from aiogram import types
from loader import _


def directions_keyboard(directions: list) -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for item in directions:
        keyboard.insert(types.KeyboardButton(text=item))
    keyboard.add(
        types.KeyboardButton(text=_('🏠 Asosiy menu'))
    )
    keyboard.add(
        types.KeyboardButton(text=_('◀️ Ortga'))
    )
    return keyboard