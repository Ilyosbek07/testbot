from aiogram import types
from loader import _


def main_menu(**kwargs) -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text=_("🧾 Testlar", locale=kwargs.get('locale'))),
        types.KeyboardButton(text=_("👤 Kabinet", locale=kwargs.get('locale'))),
        types.KeyboardButton(text=_("ℹ️ Biz haqimizda", locale=kwargs.get('locale'))),
        types.KeyboardButton(text=_("🕓 Natijalar tarixi", locale=kwargs.get('locale'))),
        types.KeyboardButton(text=_("📄 Qo\'llanma", locale=kwargs.get('locale'))),
    )

    return keyboard
