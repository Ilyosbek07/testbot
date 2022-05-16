from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.default import main_menu
from loader import dp, __, _


@dp.message_handler(Text(equals=__("🏠 Asosiy menu")), state="*")
async def home(message: types.Message, state: FSMContext):
    await message.answer(
        text=_("Asosiy menu"),
        reply_markup=main_menu()
    )
    await state.reset_state(with_data=True)
