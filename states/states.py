from aiogram.dispatcher.filters.state import StatesGroup, State


class TestForm(StatesGroup):
    price = State()
    language = State()
    direction = State()
    pay = State()


class CheckResult(StatesGroup):
    test_type = State()
    test_id = State()

