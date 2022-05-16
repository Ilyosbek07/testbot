from data.data import variants
from loader import dp, _
from aiogram import types
from callback_datas import cb_answers, cb_test, cb_reset, cb_pagination, cb_delete_all
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(cb_answers.filter())
async def answer_handler(query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await query.answer()
    async with state.proxy() as data:
        data['answers'][int(callback_data.get('test'))] = callback_data.get('key')
    data = await state.get_data()
    keyboard = types.InlineKeyboardMarkup(row_width=5)
    for i in range(1, 11):
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
                            callback_data=cb_reset.new(test_id=str(i))
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

    if len(data.get('result')) == 10:
        keyboard.add(
            types.InlineKeyboardButton(text=_("Barchasini o'chirish"), callback_data=cb_delete_all.new(page=1))
        )
        keyboard.add(
            types.InlineKeyboardButton(text=_("Natijalarni yuborish"), callback_data="send")
        )
    else:
        keyboard.add(
            types.InlineKeyboardButton(
                text=_('Keyingi saxifa'),
                callback_data=cb_pagination.new(
                    page=1,
                    location="next"
                )
            )
        )
    await query.message.edit_reply_markup(reply_markup=keyboard)
