from aiogram import types
from loader import _


def main_menu(**kwargs) -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text=_("๐งพ Testlar", locale=kwargs.get('locale'))),
        types.KeyboardButton(text=_("๐ค Kabinet", locale=kwargs.get('locale'))),
        types.KeyboardButton(text=_("โน๏ธ Biz haqimizda", locale=kwargs.get('locale'))),
        types.KeyboardButton(text=_("๐ Natijalar tarixi", locale=kwargs.get('locale'))),
        types.KeyboardButton(text=_("๐ Qo\'llanma", locale=kwargs.get('locale'))),
    )

    return keyboard
