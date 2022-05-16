import datetime
from typing import List

from sqlalchemy import insert, select

from models.selected_answer import SelectedAnswer
from service.repo.base_repo import BaseSQLAlchemyRepo


class SelectedAnswerRepo(BaseSQLAlchemyRepo):
    model = SelectedAnswer

    async def add_answer(self, subject_id: int, user_id: int, right_answers: int, wrong_answers: int):
        print(user_id, right_answers, wrong_answers)
        sql = insert(self.model).values(user_id=user_id, subject_id=subject_id, right_answers=right_answers, wrong_answers=wrong_answers, created_at=datetime.datetime.now()).returning('*')
        await self._session.execute(sql)
        await self._session.commit()

    async def get_answered(self, user_id: int):
        sql = select(SelectedAnswer.subject_id).filter(SelectedAnswer.user_id == user_id)
        request = await self._session.execute(sql)
        return request.scalars().all()

    async def get_all_answered(self, user_id) -> List[model]:
        sql = select(self.model).filter(self.model.user_id == user_id)
        request = await self._session.execute(sql)
        return request.scalars().all()