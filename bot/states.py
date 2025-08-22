from aiogram.fsm.state import State, StatesGroup


class RequestStates(StatesGroup):
    """States for handling user service requests."""

    waiting_for_request = State()
