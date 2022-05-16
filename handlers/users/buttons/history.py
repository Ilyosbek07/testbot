from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from loader import dp, __, _
from service.repo.repository import SQLAlchemyRepos
from service.repo.selected_answer_repo import SelectedAnswerRepo
from service.repo.subject_repo import SubjectRepo


@dp.message_handler(Text(equals=__("🕓 Natijalar tarixi")), state="*")
async def history(message: types.Message, repo: SQLAlchemyRepos, state: FSMContext):
    await state.reset_state(with_data=True)
    data = await repo.get_repo(SelectedAnswerRepo).get_all_answered(user_id=message.from_user.id)
    if not data:
        await message.answer(
            text=_('Siz hali test yechmadingiz')
        )
    else:
        msg = []
        for index, item in enumerate(data):
            s = await repo.get_repo(SubjectRepo).get_subject_name(subject_id=item.subject_id)
            msg.append(
                f"<b>{item.created_at.strftime('%Y.%m.%d %H:%M')}</b>\n"
                f"{index + 1}. {s}: ✅ {item.right_answers} ❌ {item.wrong_answers}\n"
            )
        await message.answer(
            text="".join(msg)
        )
