from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.directions import directions_keyboard
from loader import dp, _
from service.repo.direction_repo import DirectionRepo
from service.repo.repository import SQLAlchemyRepos
from states.states import TestForm


@dp.message_handler(state=TestForm.language)
async def select_handler(message: types.Message, state: FSMContext, repo: SQLAlchemyRepos):
    languages = (await state.get_data()).get('languages')
    languages.append(_('◀️ Ortga'))
    if message.text not in languages:
        await message.answer(
            text=_("Iltimos faqat tugmalar yordamida kiriting")
        )
    else:
        directions = await repo.get_repo(DirectionRepo).get_directions()
        await state.update_data(language=message.text)
        await message.answer(
            text=_("Yo'nalishni tanlang"),
            reply_markup=directions_keyboard(directions=directions)
        )
        await TestForm.direction.set()
