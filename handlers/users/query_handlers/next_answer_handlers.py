from data.data import variants
from loader import dp, _
from aiogram import types
from callback_datas import cb_answersaa, cb_test, cb_resetaa, cb_pagination, cb_delete_all
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(cb_answersaa.filter())
async def answer_handler(query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await query.answer()
    async with state.proxy() as data:
        data['answers'][int(callback_data.get('testaa'))] = callback_data.get('keyaa')
    data = await state.get_data()
    keyboard = types.InlineKeyboardMarkup(row_width=5)
    result = (await state.get_data()).get('result')
    for i in range(11, 21):
    # for i in range(16, len(result) + 1):
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
                            callback_data=cb_answersaa.new(testaa=i, keyaa=variant)
                        )
                    )
                    keyboard.insert(
                        types.InlineKeyboardButton(
                            text="🗑",
                            callback_data=cb_resetaa.new(test_idaa=str(i))
                        )
                    )
        else:
            for variant in variants:
                keyboard.insert(
                    types.InlineKeyboardButton(
                        text=variant,
                        callback_data=cb_answersaa.new(testaa=i, keyaa=variant)
                    )
                )
    keyboard.add(
        types.InlineKeyboardButton(
            text=_('Oldingi saxifa'),
            callback_data=cb_pagination.new(
                page=1,
                location="prev1"
            )
        )
    )
    keyboard.add(
        types.InlineKeyboardButton(
            text=_('Keyingi saxifa'),
            callback_data=cb_pagination.new(
                page=3,
                location="next2"
            )
        )
    )
    keyboard.add(
        types.InlineKeyboardButton(text=_("Barchasini o'chirish"), callback_data=cb_delete_all.new(page=2))
    )

    await query.message.edit_reply_markup(reply_markup=keyboard)