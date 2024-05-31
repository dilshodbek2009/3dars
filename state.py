from aiogram.dispatcher.filters.state import State, StatesGroup


class AddUserState(StatesGroup):
    title = State()
    text = State()
    price = State()
    country = State()
    photo = State()

