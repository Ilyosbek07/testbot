from aiogram import types
from aiogram.dispatcher import FSMContext

from callback_datas import cb_subject
from loader import dp, _
from service.repo.language_repo import LanguageRepo
from service.repo.repository import SQLAlchemyRepos
from service.repo.selected_repo import SelectedTestRepo
from service.repo.subject_repo import SubjectRepo
from service.repo.test_repo import TestRepo
from states.states import TestForm


@dp.message_handler(state=TestForm.direction)
async def select_direction(message: types.Message, repo: SQLAlchemyRepos, state: FSMContext):
    price = (await state.get_data()).get('price')
    language = await repo.get_repo(LanguageRepo).get_language_id(language_name=(await state.get_data()).get('language'))
    if price == 0.0:
        data = await repo.get_repo(TestRepo).get_test(direction_name=message.text, price=float(price),
                                                      language=language.id)
        if not data:
            await message.answer(text=_('Siz kiritgan sozlamalar boyicha xali test mavjud emas'))
        else:
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            await repo.get_repo(SelectedTestRepo).add_test_id(test_id=data[0].test_id, user_id=message.from_user.id)
            for item in data:
                keyboard.insert(
                    types.InlineKeyboardButton(
                        text=await repo.get_repo(SubjectRepo).get_subject_name(subject_id=item.subject_id),
                        callback_data=cb_subject.new(
                            subject_id=item.subject_id,
                            test_id=item.test_id,
                            id=item.id
                        )
                    )
                )
            await message.answer(text=_('Kerakli fanlarni tanlang'), reply_markup=types.ReplyKeyboardRemove())
            await message.answer(text=_('Fanlar'), reply_markup=keyboard)
    elif price == "pay":
        await message.answer(
            text=_('To\'lov turini tanlang'),
            reply_markup=types.InlineKeyboardMarkup(
                row_width=2,
                inline_keyboard=[
                    [types.InlineKeyboardButton(text="Click", callback_data="click")],
                    [types.InlineKeyboardButton(text="PayMe", callback_data="payme")],
                ]
            )
        )
        await state.update_data(direction_name=message.text)
        await TestForm.pay.set()
