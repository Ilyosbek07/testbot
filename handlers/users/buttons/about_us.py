from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from loader import dp, __, _
from aiogram import types


@dp.message_handler(Text(equals=__("ℹ️ Biz haqimizda")), state="*")
async def about_us(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=True)
    await message.answer(
        text=_('DTM bot')
    )
