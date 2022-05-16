from aiogram.dispatcher import FSMContext

from loader import dp, _
from aiogram import types
from callback_datas import cb_pagination, cb_test, cb_answers2, cb_reset, cb_answers, cb_delete_all
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
                                callback_data=cb_answers2.new(test=i, key=variant)
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
                            callback_data=cb_answers2.new(test=i, key=variant)
                        )
                    )
        keyboard.add(
            types.InlineKeyboardButton(
                text=_('Oldingi saxifa'),
                callback_data=cb_pagination.new(
                    page=page,
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
    elif location == "prev":
        for i in range(1, len(result) - 14):
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
    await query.message.edit_reply_markup(reply_markup=keyboard)
