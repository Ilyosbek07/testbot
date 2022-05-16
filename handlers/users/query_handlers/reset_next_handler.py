from aiogram import types
from aiogram.dispatcher import FSMContext

from callback_datas import cb_reset2, cb_test, cb_answers, cb_pagination, cb_delete_all
from data.data import variants
from loader import dp, _


@dp.callback_query_handler(cb_reset2.filter())
async def reset_test(query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    reset_number = int(callback_data.get('test_id'))
    async with state.proxy() as data:
        data['answers'].pop(reset_number)
    keyboard = types.InlineKeyboardMarkup(row_width=5)
    for i in range(16, 31):
        keyboard.add(
            types.InlineKeyboardButton(
                text=str(i),
                callback_data=cb_test.new(number=str(i))
            )
        )
        if i in data['answers'].keys():
            for variant in variants:
                if data['answers'][i] == variant:
                    keyboard.insert(
                        types.InlineKeyboardButton(
                            text="🔘" + variant,
                            callback_data=cb_answers.new(test=i, key=variant)
                        )
                    )
                    keyboard.insert(
                        types.InlineKeyboardButton(
                            text="🗑",
                            callback_data=cb_reset2.new(test_id=str(i))
                        )
                    )
        else:
            for variant in variants:
                keyboard.insert(
                    types.InlineKeyboardButton(
                        text=variant,
                        callback_data=cb_answers.new(test=i, key=variant)
                    )
                )
    keyboard.add(
        types.InlineKeyboardButton(
            text=_('Oldingi saxifa'),
            callback_data=cb_pagination.new(
                page=2,
                location="prev"
            )
        )
    )
    keyboard.add(
        types.InlineKeyboardButton(text=_("Barchasini o'chirish"), callback_data=cb_delete_all.new(page=2))
    )
    keyboard.add(
        types.InlineKeyboardButton(text=_("Natijalarni yuborish"), callback_data="send")
    )
    await query.message.edit_reply_markup(reply_markup=keyboard)
