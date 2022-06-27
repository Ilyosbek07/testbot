from aiogram.dispatcher import FSMContext

from keyboards.default import cabinet_keyboard, main_menu
from keyboards.inline import language
from loader import dp, _, __
from aiogram import types
from aiogram.dispatcher.filters import Text

from service.repo.language_repo import LanguageRepo
from service.repo.repository import SQLAlchemyRepos


@dp.message_handler(Text(equals=__("👤 Kabinet")), state="*")
async def cabinet(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=True)
    await message.answer(
        text=_("Kerakli punktni tanlang"),
        reply_markup=cabinet_keyboard()
    )


@dp.message_handler(Text(equals=__("🌐 Tilni o'zgartirish")))
async def change_lang(message: types.Message, repo: SQLAlchemyRepos):
    data = await repo.get_repo(LanguageRepo).get_languages()
    languages = []
    for item in data:
        languages.append(
            {item.id: [{item.language_name: item.language_code}]}
        )
    await message.answer(
        text=_("Kerakli tilni tanlang"),
        reply_markup=language(languages=languages)
    )
    
    
@dp.message_handler(Text(equals=__("◀️  Ortga")))
async def change_lang(message: types.Message):
    await message.answer(text='Asosiy menu', reply_markup=main_menu())

