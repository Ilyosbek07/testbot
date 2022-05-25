from aiogram.dispatcher import FSMContext

from callback_datas import cb_delete_all, cb_test, cb_answers, cb_reset, cb_answers2, cb_pagination, cb_answers4, \
    cb_answers2, cb_answers5, cb_answers6, cb_answers7, cb_reset2, cb_reset2
from data.data import variants
from loader import dp, _
from aiogram import types


@dp.callback_query_handler(cb_delete_all.filter())
async def delete_all(query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    async with state.proxy() as data:
        data['answers'] = {}
    keyboard = types.InlineKeyboardMarkup(row_width=5)
    page = int(callback_data.get('page'))
    if page == 1:
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

        keyboard.add(
            types.InlineKeyboardButton(
                text=_('Keyingi saxifa'),
                callback_data=cb_pagination.new(
                    page=1,
                    location="next"
                )
            )
        )
        keyboard.add(
            types.InlineKeyboardButton(text=_("Barchasini o'chirish"), callback_data=cb_delete_all.new(page=1))
        )
    elif page == 2:
        for i in range(11, 21):
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
    elif page == 3:
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
    elif page == 4:
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
                                callback_data=cb_reset.new(test_id=str(i))
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
                    page=2,
                    location="next2"
                )
            )
        )
        keyboard.add(
            types.InlineKeyboardButton(
                text=_('Keyingi saxifa'),
                callback_data=cb_pagination.new(
                    page=5,
                    location="next4"
                )
            )
        )
        keyboard.add(
            types.InlineKeyboardButton(text=_("Barchasini o'chirish"), callback_data=cb_delete_all.new(page=4))
        )
    elif page == 5:
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
                                callback_data=cb_answers5.new(test=i, key=variant)
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
                            callback_data=cb_answers5.new(test=i, key=variant)
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
            types.InlineKeyboardButton(text=_("Barchasini o'chirish"), callback_data=cb_delete_all.new(page=5))
        )
    elif page == 6:
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
                                callback_data=cb_answers6.new(test=i, key=variant)
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
                            callback_data=cb_answers6.new(test=i, key=variant)
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
            types.InlineKeyboardButton(text=_("Barchasini o'chirish"), callback_data=cb_delete_all.new(page=6))
        )
    elif page == 7:
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
                                callback_data=cb_answers7.new(test=i, key=variant)
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
                            callback_data=cb_answers7.new(test=i, key=variant)
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
            types.InlineKeyboardButton(text=_("Barchasini o'chirish"), callback_data=cb_delete_all.new(page=7))
        )
        keyboard.add(
            types.InlineKeyboardButton(text=_("Natijalarni yuborish"), callback_data="send")
        )
    await query.message.edit_reply_markup(reply_markup=keyboard)
