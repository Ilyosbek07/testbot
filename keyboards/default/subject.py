from aiogram import types


def subject(subjects: list) -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    for sub in subjects:
        keyboard.insert(types.KeyboardButton(text=sub))
    return keyboard