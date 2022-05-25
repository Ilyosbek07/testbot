from aiogram import types

from callback_datas import cb_subject
from data.config import DJANGO_ROOT
from keyboards.default import main_menu
from loader import dp
from service.repo.repository import SQLAlchemyRepos
from service.repo.subject_repo import SubjectRepo
from service.repo.test_repo import TestRepo


@dp.callback_query_handler(cb_subject.filter(), state="*")
async def subject_handler(query: types.CallbackQuery, callback_data: dict, repo: SQLAlchemyRepos):
    await query.answer()
    test_id, subject_id, id = int(callback_data.get('test_id')), int(callback_data.get('subject_id')), int(
        callback_data.get('id'))
    data = await repo.get_repo(TestRepo).get_test_path(test_id=test_id, subject_id=subject_id)
    document = types.InputFile(path_or_bytesio=DJANGO_ROOT + data.file, filename=f"{id}.{(data.file.split('.'))[1]}")
    await query.message.answer_document(
        document=document,
        caption="Fan: {subject}\n"
                "Test ID: <code>{id}</code>".format(
            subject=await repo.get_repo(SubjectRepo).get_subject_name(subject_id=data.subject_id),
            id=id
        ),
        reply_markup=main_menu()
    )