from aiogram.dispatcher import FSMContext

from keyboards.default import main_menu
from loader import dp, _
from aiogram import types

from service.repo.repository import SQLAlchemyRepos
from service.repo.selected_answer_repo import SelectedAnswerRepo


@dp.callback_query_handler(text="send")
async def check_test(query: types.CallbackQuery, state: FSMContext, repo: SQLAlchemyRepos):
    right = 0
    wrong = 0
    data = await state.get_data()
    answers = data.get('answers')
    result = data.get('result')
    subject_id = data.get('subject_id')
    new = {}
    answer_signature = {}
    for i in result:
        for key, val in i.items():
            new[key] = val
    for key, var in new.items():
        if key in answers:
            if answers[key] == var:
                answer_signature[key] = "✅"
                right += 1
            else:
                answer_signature[key] = "❌"
                wrong += 1
        else:
            wrong += 1
            answer_signature[key] = "❌"
    msg = []
    for key, answer in answer_signature.items():
        msg.append(
            f"{key}. {answer}"
        )
    await repo.get_repo(SelectedAnswerRepo).add_answer(subject_id=subject_id, user_id=query.from_user.id,
                                                       right_answers=right, wrong_answers=wrong)
    await query.message.delete()
    await query.message.answer(
        text="\n".join(msg) + _("\nTo'g'ri javoblar soni: {right}\nNoto'g'ri javoblar soni: {wrong}").format(
            right=right, wrong=wrong), reply_markup=main_menu())
