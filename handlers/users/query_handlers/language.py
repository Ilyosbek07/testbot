from aiogram import types

from callback_datas.callback_datas import cb_language
from keyboards.default import main_menu
from loader import dp, _
from service.repo.repository import SQLAlchemyRepos
from service.repo.user_repo import UserRepo


@dp.callback_query_handler(cb_language.filter())
async def language_handler(query: types.CallbackQuery, callback_data: dict, repo: SQLAlchemyRepos):
    language_id = int(callback_data.get('language_id'))
    language_code = callback_data.get('language_code')
    repo = repo.get_repo(UserRepo)
    if await repo.get_user(user_id=query.from_user.id) is None:
        await repo.add_user(
            user_id=query.from_user.id,
            name=query.from_user.full_name,
            language=language_id,
            is_active=True
        )
    else:
        await repo.update_language(user_id=query.from_user.id, updated={'language_id': language_id})
    await query.message.delete()
    await query.message.answer(
        text=_("Asosiy menu", locale=language_code),
        reply_markup=main_menu(locale=language_code)
    )
