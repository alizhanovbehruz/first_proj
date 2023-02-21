from aiogram.dispatcher.filters.state import StatesGroup, State

class MurojatState(StatesGroup):
    tingla = State()

class SendState(StatesGroup):
    send_sms = State()