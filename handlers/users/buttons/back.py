from aiogram.dispatcher.filters import Text

from keyboards.default import main_menu, test_type, language
from loader import dp, __, _
from aiogram import types
from aiogram.dispatcher import FSMContext

from service.repo.language_repo import LanguageRepo
from service.repo.repository import SQLAlchemyRepos
from states import states


@dp.message_handler(Text(equals=__("◀️ Ortga")), state=states.TestForm.price)
async def back(message: types.Message, state: FSMContext):
    await message.answer(
        text=_("Asosiy menu"),
        reply_markup=main_menu()
    )
    await state.reset_state(with_data=True)


@dp.message_handler(Text(equals=__("◀️ Ortga")), state=states.TestForm.language)
async def back(message: types.Message, state: FSMContext):
    await message.answer(
        text=_("Kerakli punktni tanlang"),
        reply_markup=test_type()
    )
    await states.TestForm.previous()


@dp.message_handler(Text(equals=__("◀️ Ortga")), state=states.TestForm.direction)
async def back(message: types.Message, repo: SQLAlchemyRepos, state: FSMContext):
    languages = []
    data = await repo.get_repo(LanguageRepo).get_languages()
    for item in data:
        languages.append(item.language_name)
    await message.answer(
        text=_("Test tilini tanlang"),
        reply_markup=language(languages=languages)
    )
    await states.TestForm.previous()


@dp.message_handler(Text(equals=__("◀️ Ortga")), state=states.CheckResult.test_id)
async def back(message: types.Message, state: FSMContext):
    await message.answer(
        text=_("Kerakli punktni tanlang"),
        reply_markup=test_type()
    )
    await states.TestForm.price.set()
