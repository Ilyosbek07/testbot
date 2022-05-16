from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import main_menu
from keyboards.inline import language
from loader import dp, _
from service.repo.language_repo import LanguageRepo
from service.repo.repository import SQLAlchemyRepos
from service.repo.user_repo import UserRepo


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext, repo: SQLAlchemyRepos):
    await state.reset_state()
    user = repo.get_repo(UserRepo)
    if await user.get_user(user_id=message.from_user.id) is None:
        data = await repo.get_repo(LanguageRepo).get_languages()
        languages = []
        for item in data:
            languages.append(
                {item.id: [{item.language_name: item.language_code}]}
            )
        await message.answer(
            text=_("Assalomu Alaykum, xush kelibsiz!"),
            reply_markup=language(languages=languages)
        )
    else:
        await message.answer(
            text=_("Asosiy menu"),
            reply_markup=main_menu()
        )
