from aiogram import types
from loader import _


def test_type() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text=_("💰 Pullik testlar")),
        types.KeyboardButton(text=_("🆓 Bepul testlar")),
        types.KeyboardButton(text=_("🔍 Natijani bilish")),
    )
    keyboard.add(
        types.KeyboardButton(text=_('◀️ Ortga'))
    )

    return keyboard
