from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, _
from callback_datas import cb_answersbb, cb_test, cb_resetbb, cb_pagination, cb_delete_all, cb_resetbb, cb_answerscc, \
    cb_resetcc, cb_resetbb, cb_answersdd, cb_resetdd, cb_answersee, cb_resetee, cb_answersff, cb_resetff
from data.data import variants


@dp.callback_query_handler(cb_answerscc.filter())
async def answer_handler(query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await query.answer()
    async with state.proxy() as data:
        data['answers'][int(callback_data.get('testcc'))] = callback_data.get('keycc')
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
                            callback_data=cb_answerscc.new(testcc=i, keycc=variant)
                        )
                    )
                    keyboard.insert(
                        types.InlineKeyboardButton(
                            text="🗑",
                            callback_data=cb_resetcc.new(test_idcc=str(i))
                        )
                    )
        else:
            for variant in variants:
                keyboard.insert(
                    types.InlineKeyboardButton(
                        text=variant,
                        callback_data=cb_answerscc.new(testcc=i, keycc=variant)
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


@dp.callback_query_handler(cb_answersdd.filter())
async def answer_handler(query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await query.answer()
    async with state.proxy() as data:
        data['answers'][int(callback_data.get('testdd'))] = callback_data.get('keydd')
    data = await state.get_data()
    keyboard = types.InlineKeyboardMarkup(row_width=5)
    result = (await state.get_data()).get('result')
    for i in range(46, 61):
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
                            callback_data=cb_answersdd.new(testdd=i, keydd=variant)
                        )
                    )
                    keyboard.insert(
                        types.InlineKeyboardButton(
                            text="🗑",
                            callback_data=cb_resetdd.new(test_iddd=str(i))
                        )
                    )
        else:
            for variant in variants:
                keyboard.insert(
                    types.InlineKeyboardButton(
                        text=variant,
                        callback_data=cb_answersdd.new(testdd=i, keydd=variant)
                    )
                )

    keyboard.add(
        types.InlineKeyboardButton(
            text=_('Oldingi saxifa'),
            callback_data=cb_pagination.new(
                page=3,
                location="next3"
            )
        )
    )
    keyboard.add(
        types.InlineKeyboardButton(
            text=_('Keyingi saxifa'),
            callback_data=cb_pagination.new(
                page=5,
                location="next5"
            )
        )
    )
    keyboard.add(
        types.InlineKeyboardButton(text=_("Barchasini o'chirish"), callback_data=cb_delete_all.new(page=4))
    )

    await query.message.edit_reply_markup(reply_markup=keyboard)


@dp.callback_query_handler(cb_answersee.filter())
async def answer_handler(query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await query.answer()
    async with state.proxy() as data:
        data['answers'][int(callback_data.get('testee'))] = callback_data.get('keyee')
    data = await state.get_data()
    keyboard = types.InlineKeyboardMarkup(row_width=5)
    result = (await state.get_data()).get('result')
    for i in range(61, 76):
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
                            callback_data=cb_answersee.new(testee=i, keyee=variant)
                        )
                    )
                    keyboard.insert(
                        types.InlineKeyboardButton(
                            text="🗑",
                            callback_data=cb_resetee.new(test_idee=str(i))
                        )
                    )
        else:
            for variant in variants:
                keyboard.insert(
                    types.InlineKeyboardButton(
                        text=variant,
                        callback_data=cb_answersee.new(testee=i, keyee=variant)
                    )
                )

    keyboard.add(
        types.InlineKeyboardButton(
            text=_('Oldingi saxifa'),
            callback_data=cb_pagination.new(
                page=4,
                location="next4"
            )
        )
    )
    keyboard.add(
        types.InlineKeyboardButton(
            text=_('Keyingi saxifa'),
            callback_data=cb_pagination.new(
                page=6,
                location="next6"
            )
        )
    )
    keyboard.add(
        types.InlineKeyboardButton(text=_("Barchasini o'chirish"), callback_data=cb_delete_all.new(page=5))
    )

    await query.message.edit_reply_markup(reply_markup=keyboard)


@dp.callback_query_handler(cb_answersff.filter())
async def answer_handler(query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await query.answer()
    async with state.proxy() as data:
        data['answers'][int(callback_data.get('testff'))] = callback_data.get('keyff')
    data = await state.get_data()
    keyboard = types.InlineKeyboardMarkup(row_width=5)
    result = (await state.get_data()).get('result')
    for i in range(76, 91):
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
                            callback_data=cb_answersff.new(testff=i, keyff=variant)
                        )
                    )
                    keyboard.insert(
                        types.InlineKeyboardButton(
                            text="🗑",
                            callback_data=cb_resetff.new(test_idff=str(i))
                        )
                    )
        else:
            for variant in variants:
                keyboard.insert(
                    types.InlineKeyboardButton(
                        text=variant,
                        callback_data=cb_answersff.new(testff=i, keyff=variant)
                    )
                )

    keyboard.add(
        types.InlineKeyboardButton(
            text=_('Oldingi saxifa'),
            callback_data=cb_pagination.new(
                page=5,
                location="next5"
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
