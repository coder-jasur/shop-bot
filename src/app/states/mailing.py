
from aiogram.fsm.state import StatesGroup, State


class Mailing(StatesGroup):
    mailing_message = State()