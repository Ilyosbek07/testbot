from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default import test_type
from loader import dp, __, _
from states.states import TestForm


@dp.message_handler(text=__("🧾 Testlar"), state="*")
async def tests(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=True)
    await message.answer(
        text=_("Kerakli punktni tanlang"),
        reply_markup=test_type()
    )
    await TestForm.price.set()
