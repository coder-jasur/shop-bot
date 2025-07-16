from aiogram.fsm.state import StatesGroup, State


class BroadcastingManagerSG(StatesGroup):
    get_message = State()
    confirm_broadcasting = State()


class AddChannel(StatesGroup):
    get_channel_id = State()

class GetUserId(StatesGroup):
    get_user_id = State()
    blocked_user = State()
    unblocked_user = State()