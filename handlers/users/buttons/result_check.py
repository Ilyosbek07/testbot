from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from callback_datas import cb_answers, cb_test, cb_pagination, cb_delete_all
from data.config import DJANGO_ROOT
from data.data import digit_error, variants
from keyboards.default import test_type_check
from loader import dp, __, _
from service.repo.direction_subjects_repo import DirectionSubjectsRepo
from service.repo.repository import SQLAlchemyRepos
from states.states import CheckResult
from utils.misc.req_func import get_excel_data


@dp.message_handler(Text(equals=__("🔍 Natijani bilish")), state="*")
async def check_result(message: types.Message):
    await message.answer(
        text='Test turini tanlang',
        reply_markup=test_type_check()
    )
    await CheckResult.test_type.set()


@dp.message_handler(state=CheckResult.test_type)
async def test_typer(message: types.Message, state: FSMContext):
    test_type = message.text
    if test_type not in [_("💰 Pullik testlar"), _("🆓 Bepul testlar")]:
        await message.answer(
            text=_("Iltimos faqat tugmalar yordamida kiriting")
        )
    else:
        print('Else')
        if test_type == _("💰 Pullik testlar"):
            await state.update_data(test_type="pay")
        elif test_type == _("🆓 Bepul testlar"):
            await state.update_data(test_type=0)
        await message.answer(
            text=_('Kitob raqamini kiriting'),
            reply_markup=types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True,
                                                   keyboard=[[types.KeyboardButton(text=_("◀️ Ortga"))]])
        )
        await CheckResult.test_id.set()


@dp.message_handler(state=CheckResult.test_id)
async def get_test_id(message: types.Message, repo: SQLAlchemyRepos, state: FSMContext):
    test_id = message.text
    if not test_id.isdigit():
        await message.answer(
            text=digit_error
        )
    else:
        s = await state.get_data()
        data = await repo.get_repo(DirectionSubjectsRepo).get_results(test_id=int(test_id),
                                                                      test_type=s.get('test_type'))
        if data is None:
            await message.answer(text=_('Siz kiritgan sozlamalar boyicha xali test mavjud emas'))
        else:
            result = await get_excel_data(file_path=DJANGO_ROOT + data.keys)
            await state.update_data(subject_id=data.subject_id)
            keyboard = types.InlineKeyboardMarkup(row_width=5)
            for i in range(1, 11):
                keyboard.insert(
                    types.InlineKeyboardButton(
                        text=str(i),
                        callback_data=cb_test.new(number=str(i))
                    )
                )
                for variant in variants:
                    keyboard.insert(
                        types.InlineKeyboardButton(
                            text=variant,
                            callback_data=cb_answers.new(test=i, key=variant)
                        )
                    )
            if len(result) == 90:
                keyboard.add(types.InlineKeyboardButton(text=_("Keyingi saxifa"),
                                                        callback_data=cb_pagination.new(page=1, location="next")))
            keyboard.add(
                types.InlineKeyboardButton(text=_("Barchasini o'chirish"), callback_data=cb_delete_all.new(page=1))
            )
            await message.answer(
                text=_('Quyidagi testlarga javob berib, "Natijalarni yuborish" tugmasini bosing'
                       '( "/back" bekor qilish )'),
                reply_markup=keyboard
            )
            await state.reset_state(with_data=False)
            await state.update_data(result=result, answers={})