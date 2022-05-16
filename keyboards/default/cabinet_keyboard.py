from aiogram import types
from loader import _


def cabinet_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(
        types.KeyboardButton(text=_('🌐 Tilni o\'zgartirish')),
        types.KeyboardButton(text=_('📄 Qo\'llanma')),
    )
    return keyboard
