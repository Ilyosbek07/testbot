from aiogram import types
from callback_datas.callback_datas import cb_language


def language(languages: list) -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    for index, i in enumerate(languages):
        for language_id in i.keys():
            for item in languages[index][language_id]:
                for language_name, language_code in item.items():
                    keyboard.insert(
                        types.InlineKeyboardButton(
                            text=language_name,
                            callback_data=cb_language.new(language_code=language_code, language_id=language_id))
                    )

    return keyboard