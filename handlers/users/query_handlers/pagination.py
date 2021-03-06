from aiogram.dispatcher import FSMContext

from loader import dp, _
from aiogram import types
from callback_datas import cb_pagination, cb_test, cb_answersaa, cb_reset, cb_answers, cb_delete_all, cb_pagination2, \
    cb_resetaa, cb_answersaa, cb_resetaa, cb_answerscc, cb_answersbb, cb_resetbb, cb_resetcc, cb_resetdd, \
    cb_answersdd, cb_resetee, cb_answersee, cb_resetff, cb_answersff
from service.repo.repository import SQLAlchemyRepos


@dp.callback_query_handler(cb_pagination.filter(), state="*")
async def pagination_handler(query: types.CallbackQuery, callback_data: dict, state: FSMContext, repo: SQLAlchemyRepos):
    page = int(callback_data.get('page'))
    location = callback_data.get('location')
    data = await state.get_data()
    keyboard = types.InlineKeyboardMarkup(row_width=5)
    result = (await state.get_data()).get('result')
    variants = ['A', 'B', 'C', 'D']
    if location == "next":
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
                callback_data=cb_pagination2.new(
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

    elif location == "prev1":
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
    elif location == "next2":
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
                                callback_data=cb_answersbb.new(testbb=i, keybb=variant)
                            )
                        )
                        keyboard.insert(
                            types.InlineKeyboardButton(
                                text="🗑",
                                callback_data=cb_resetbb.new(test_idbb=str(i))
                            )
                        )
            else:
                for variant in variants:
                    keyboard.insert(
                        types.InlineKeyboardButton(
                            text=variant,
                            callback_data=cb_answersbb.new(testbb=i, keybb=variant)
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
    elif location == "next3":
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
    elif location == "next4":
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
            types.InlineKeyboardButton(text=_("Barchasini o'chirish"), callback_data=cb_delete_all.new(page=5))
        )
    elif location == "next5":
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
                callback_data=cb_pagination2.new(
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
    elif location == "next6":
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
