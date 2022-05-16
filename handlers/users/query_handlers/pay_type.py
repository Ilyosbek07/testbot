from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType

from data.config import CLICK, PAYME
from keyboards.default import main_menu
from loader import dp, _, bot
from aiogram import types

from service.repo.repository import SQLAlchemyRepos
from service.repo.test_repo import TestRepo
from states.states import TestForm


@dp.callback_query_handler(text="click", state=TestForm.pay)
async def pay_type(query: types.CallbackQuery, repo: SQLAlchemyRepos, state: FSMContext):
    data = await state.get_data()
    data = await repo.get_repo(TestRepo).get_pay_test(direction_name=data.get('direction_name'))
    await query.message.delete()
    if not data:
        await query.message.answer(text=_('Siz kiritgan sozlamalar boyicha xali test mavjud emas'))
    else:
        price_test = [
            types.LabeledPrice(label='Test', amount=int(f"{int(data.price)}00"))
        ]
        await query.message.answer(
            text=_("Asosiy menu"),
            reply_markup=main_menu()
        )
        await bot.send_invoice(
            chat_id=query.message.chat.id,
            title="Test",
            description="Test description",
            provider_token=CLICK,
            currency='uzs',
            prices=price_test,
            start_parameter='example',
            payload='some_invoice'
        )
        await state.reset_state(with_data=True)


@dp.callback_query_handler(text="payme", state=TestForm.pay)
async def pay_type(query: types.CallbackQuery, repo: SQLAlchemyRepos, state: FSMContext):
    data = await state.get_data()
    data = await repo.get_repo(TestRepo).get_pay_test(direction_name=data.get('direction_name'))
    await query.message.delete()
    if not data:
        await query.message.answer(text=_('Siz kiritgan sozlamalar boyicha xali test mavjud emas'))
    else:
        price_test = [
            types.LabeledPrice(label='Test', amount=int(f"{int(data.price)}00"))
        ]
        await query.message.answer(
            text=_("Asosiy menu"),
            reply_markup=main_menu()
        )
        await bot.send_invoice(
            chat_id=query.message.chat.id,
            title="Test",
            description="Test description",
            provider_token=PAYME,
            currency='uzs',
            prices=price_test,
            start_parameter='example',
            payload='some_invoice'
        )
        await state.reset_state(with_data=True)


@dp.pre_checkout_query_handler(lambda q: True)
async def checkout_process(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print(message)
    await bot.send_message(
        message.chat.id,
        'Success'
    )
