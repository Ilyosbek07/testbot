from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default import language
from loader import dp, __, _
from service.repo.language_repo import LanguageRepo
from service.repo.repository import SQLAlchemyRepos
from states.states import TestForm


@dp.message_handler(text=__("🆓 Bepul testlar"), state=TestForm.price)
async def free_test(message: types.Message, repo: SQLAlchemyRepos, state: FSMContext):
    languages = []
    data = await repo.get_repo(LanguageRepo).get_languages()
    for item in data:
        languages.append(item.language_name)
    await message.answer(
        text=_("Test tilini tanlang"),
        reply_markup=language(languages=languages)
    )
    await state.update_data(price=0.00, languages=languages)
    await TestForm.language.set()
