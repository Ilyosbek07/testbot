from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, _
from callback_datas import cb_answers2, cb_test, cb_reset2, cb_pagination, cb_delete_all, cb_reset2, cb_answers4, \
    cb_reset4
from data.data import variants


@dp.callback_query_handler(cb_answers2.filter())
async def answer_handler(query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await query.answer()
    async with state.proxy() as data:
        data['answers'][int(callback_data.get('test'))] = callback_data.get('key')
    data = await state.get_data()
    keyboard = types.InlineKeyboardMarkup(row_width=5)
    result = (await state.get_data()).get('result')
    for i in range(21, 31):
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
                            callback_data=cb_answers2.new(test=i, key=variant)
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
                        callback_data=cb_answers2.new(test=i, key=variant)
                    )
                )

    keyboard.add(
        types.InlineKeyboardButton(
            text=_('Oldingi saxifa'),
            callback_data=cb_pagination.new(
                page=1,
                location="next"
            )
        )
    )
    keyboard.add(
        types.InlineKeyboardButton(
            text=_('Keyingi saxifa'),
            callback_data=cb_pagination.new(
                page=4,
                location="next3"
            )
        )
    )
    keyboard.add(
        types.InlineKeyboardButton(text=_("Barchasini o'chirish"), callback_data=cb_delete_all.new(page=3))
    )

    await query.message.edit_reply_markup(reply_markup=keyboard)

@dp.callback_query_handler(cb_answers4.filter())
async def answer_handler(query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await query.answer()
    async with state.proxy() as data:
        data['answers'][int(callback_data.get('test'))] = callback_data.get('key')
    data = await state.get_data()
    keyboard = types.InlineKeyboardMarkup(row_width=5)
    result = (await state.get_data()).get('result')
    for i in range(31, 46):
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
                            callback_data=cb_answers4.new(test=i, key=variant)
                        )
                    )
                    keyboard.insert(
                        types.InlineKeyboardButton(
                            text="🗑",
                            callback_data=cb_reset4.new(test_id=str(i))
                        )
                    )
        else:
            for variant in variants:
                keyboard.insert(
                    types.InlineKeyboardButton(
                        text=variant,
                        callback_data=cb_answers4.new(test=i, key=variant)
                    )
                )

    keyboard.add(
        types.InlineKeyboardButton(
            text=_('Oldingi saxifa'),
            callback_data=cb_pagination.new(
                page=1,
                location="next"
            )
        )
    )
    keyboard.add(
        types.InlineKeyboardButton(
            text=_('Keyingi saxifa'),
            callback_data=cb_pagination.new(
                page=4,
                location="next3"
            )
        )
    )
    keyboard.add(
        types.InlineKeyboardButton(text=_("Barchasini o'chirish"), callback_data=cb_delete_all.new(page=3))
    )

    await query.message.edit_reply_markup(reply_markup=keyboard)