from aiogram import types
from loader import _


def language(languages: list) -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    for lang in languages:
        keyboard.insert(types.KeyboardButton(text=lang))
    keyboard.add(
        types.KeyboardButton(text=_('🏠 Asosiy menu'))
    )
    keyboard.add(
        types.KeyboardButton(text=_('◀️ Ortga'))
    )
    return keyboard