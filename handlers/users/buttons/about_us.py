from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from loader import dp, __, _
from aiogram import types


@dp.message_handler(Text(equals=__("ℹ️ Biz haqimizda")), state="*")
async def about_us(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=True)
    text = "Testolog-servis o'quv markazi 15 yilga yaqin tajribaga ega bo'lgan ta'lim dargohi." \
           "-Abiturientlarni test sinovlariga sifatli tayyorlaydi." \
           "Diagno'stik, IQ va Genetik testlarni o'z binosida " \
           "va joylarga borib o'tqazib beradi." \
           "📞97-400-77-33"
    photo = 'AgACAgIAAxkBAAEP4tRiiHNDtbc6I1oiMeqeWIJ7FwLtwwAC4L0xG29YQUjaFFUdber_xQEAAwIAA3MAAyQE'
    await message.answer(text=text)
    # await message.answer_photo(caption=text, photo=photo)

@dp.message_handler(Text(equals=__("📄 Qo\'llanma")), state="*")
async def about_us(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=True)
    await message.answer(
        text="https://telegra.ph/Botdan-foydalanish-boyicha-qollanma-04-21"
    )