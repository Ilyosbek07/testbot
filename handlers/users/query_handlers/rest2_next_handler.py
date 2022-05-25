from aiogram import types
from aiogram.dispatcher import FSMContext

from callback_datas import cb_reset2, cb_test, cb_answers, cb_pagination, cb_delete_all, cb_answers2, cb_reset4, \
    cb_answers4
from data.data import variants
from loader import dp, _


@dp.callback_query_handler(cb_reset2.filter())
async def reset_test(query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    reset_number = int(callback_data.get('test_id'))
    async with state.proxy() as data:
        data['answers'].pop(reset_number)
    keyboard = types.InlineKeyboardMarkup(row_width=5)
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
                page=2,
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

@dp.callback_query_handler(cb_reset4.filter())
async def reset_test(query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    reset_number = int(callback_data.get('test_id'))
    async with state.proxy() as data:
        data['answers'].pop(reset_number)
    keyboard = types.InlineKeyboardMarkup(row_width=5)
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
                page=2,
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

@dp.callback_query_handler(cb_reset2.filter())
async def reset_test(query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    reset_number = int(callback_data.get('test_id'))
    async with state.proxy() as data:
        data['answers'].pop(reset_number)
    keyboard = types.InlineKeyboardMarkup(row_width=5)
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
                page=2,
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

@dp.callback_query_handler(cb_reset2.filter())
async def reset_test(query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    reset_number = int(callback_data.get('test_id'))
    async with state.proxy() as data:
        data['answers'].pop(reset_number)
    keyboard = types.InlineKeyboardMarkup(row_width=5)
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
                page=2,
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