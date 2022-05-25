from aiogram.dispatcher import FSMContext

from data.data import variants
from loader import dp, _
from aiogram import types
from callback_datas import cb_reset, cb_test, cb_answers, cb_pagination, cb_delete_all


@dp.callback_query_handler(cb_reset.filter())
async def reset_test(query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    reset_number = int(callback_data.get('test_id'))
    async with state.proxy() as data:
        print(data['answers'])
        data['answers'].pop(reset_number)
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
    if len(data.get('result')) == 90:
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

    await query.message.edit_reply_markup(reply_markup=keyboard)